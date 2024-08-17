from flask_app.instance_generator_forms import Algorithm1GeneratorForm,Algorithm2GeneratorForm,Algorithm3GeneratorForm,Algorithm4GeneratorForm,Algorithm5GeneratorForm
import fairpyx.algorithms.heterogeneous_matroid_constraints_algorithms
import fairpyx.algorithms.heterogeneous_matroid_constraints_algorithms
import fairpyx.algorithms.heterogeneous_matroid_constraints_algorithms
from flask import session
from flask_app import app
import gspread
from flask import render_template, request, redirect, url_for
from functools import partial
from fairpyx.algorithms.heterogeneous_matroid_constraints_algorithms import per_category_round_robin,capped_round_robin,two_categories_capped_round_robin,per_category_capped_round_robin,iterated_priority_matching
from fairpyx.algorithms.heterogeneous_matroid_constraints_algorithms import *
from fairpyx.utils.test_heterogeneous_matroid_constraints_algorithms_utils import random_instance
#from .forms import InputForm 
from fairpyx.allocations import AllocationBuilder, Instance
import ast
from flask_app.forms import Algorithm1Form, Algorithm2Form , Algorithm3Form, Algorithm4Form, Algorithm5Form
# Define your algorithms


algorithms = [
    {"name": "Per-Category Round-Robin", "route": "algorithm1", "description": """this is the Algorithm 1 from the paper<br>
     per category round-robin is an allocation algorithm which guarantees EF1 (envy-freeness up to 1 good) allocation
    under settings in which agent-capacities are equal across all agents,<br>
    no capacity-inequalities are allowed since this algorithm doesnt provie a cycle-prevention mechanism<br>
    TLDR: same partition, same capacities, may have different valuations across agents  -> EF1 allocation"""},
    {"name": "Capped Round-Robin", "route": "algorithm2", "description": """this is Algorithm 2 CRR (capped round-robin) algorithm <br>TLDR: single category , may have differnt capacities
    capped in CRR stands for capped capacity for each agent unlke RR , maye have different valuations -> F-EF1 (
    feasible envy-freeness up to 1 good) allocation"""},
    {"name": "Back&Forth RR(Round-Robin)", "route": "algorithm3", "description": """this is Algorithm 3 back and forth capped round-robin algorithm<br> (2 categories,may have different capacities,may have different valuations)
        in which we simply<br>
        1)call capped_round_robin(arg1 ,.... argk,item_categories=<first category>)<br>
        2) reverse(order)<br>
        3)call capped_round_robin(arg1 ,.... argk,item_categories=<second category>)<br>
        -> F-EF1 (feasible envy-freeness up to 1 good) allocation"""},
    {"name": "Per-Category CRR(Capped-Round-Robin)", "route": "algorithm4", "description": """ this is Algorithm 4 deals with (Different Capacities, Identical Valuations),<br> suitable for any number of categories
    CRR (per-category capped round-robin) algorithm<br>
    TLDR: multiple categories , may have different capacities , but have identical valuations -> F-EF1 (feasible envy-freeness up to 1 good) allocation"""},
    {"name": "Iterated Priority Matching", "route": "algorithm5", "description": """this is Algorithm 5  deals with (partition Matroids with Binary Valuations, may have different capacities)<br>
    loops as much as maximum capacity in per each category , each iteration we build :<br>
    1) agent-item graph (bidirectional graph)<br>
    2) envy graph<br>
    3) topological sort the order based on the envy graph (always a-cyclic under such settings,proven in papers)<br>
    4) compute priority matching based on it we allocate the items among the agents<br>
    we do this each loop , and in case there remains item in that category we arbitrarily give it to random agent
"""},
]

# Existing routes for algorithms
@app.route('/')
def index():
    return render_template('index.html', algorithms=algorithms)

@app.route('/<algorithm_route>')
def algorithm_page(algorithm_route):
    algorithm = next((alg for alg in algorithms if alg["route"] == algorithm_route), None)
    if algorithm:
        return render_template('algorithm.html', algorithm=algorithm)
    else:
        return "Algorithm not found", 404

@app.route('/form_page/<algorithm>', methods=['GET', 'POST'])
def form_page(algorithm):
    form = None
    if algorithm == 'algorithm1':
        print('algorithm 1 chosen')
        form = Algorithm1Form()
    elif algorithm == 'algorithm2':
        print('algorithm 2 chosen')
        form = Algorithm2Form()
    elif algorithm == 'algorithm3':
        form = Algorithm3Form()
    elif algorithm == 'algorithm4':
        form = Algorithm4Form()
    elif algorithm == 'algorithm5':
        form = Algorithm5Form()

    if request.method == 'POST':
        if form.validate_on_submit():
            print('validated')
            session['form_data']={field.name:field.data for field in form}
            print(session['form_data'])
            return redirect(url_for(f'process_data', algorithm=algorithm,form=form))
            
        else:
            print(f'form validation failed with errors: {form.errors}')

    return render_template(f'{algorithm}_form_page.html', form=form, algorithm=algorithm)

@app.route('/process_data/<algorithm>')
def process_data(algorithm):
    images_data = []
    
    def store_visualization(img_base64):# used to get us the images from fairpyx !
        images_data.append(img_base64)

    form = None
    form=session['form_data']
    #print(f'process_data page form is -> {form} and its type is _>{type(form)}')
    log_stream=fairpyx.algorithms.heterogeneous_matroid_constraints_algorithms.helper_configure_logger()
    if algorithm == 'algorithm1':
            item_categories = ast.literal_eval(form['item_categories'])
            item_capacities = ast.literal_eval(form['item_capacities'])
            category_capacities = ast.literal_eval(form['category_capacities'])
            item_valuations = ast.literal_eval(form['item_valuations'])
            initial_agent_order = ast.literal_eval(form['initial_agent_order'])
            alloc=AllocationBuilder(Instance(item_capacities=item_capacities, valuations=item_valuations))
            per_category_round_robin(item_categories=item_categories, agent_category_capacities=category_capacities, initial_agent_order=initial_agent_order, alloc=alloc,callback=store_visualization)
            #print(f'algorithm 1 allocation result is {result}')
            print(f'images data -> {images_data}')
            logs=helper_get_logs(log_stream)
            return render_template('result.html', result=alloc.bundles,images_data=images_data,logs=logs.splitlines())
    elif algorithm == 'algorithm2':
            item_categories = ast.literal_eval(form['item_categories'])
            item_capacities = ast.literal_eval(form['item_capacities'])
            category_capacities = ast.literal_eval(form['category_capacities'])
            item_valuations = ast.literal_eval(form['item_valuations'])
            initial_agent_order = ast.literal_eval(form['initial_agent_order'])
            target_category = ast.literal_eval(form['target_category'])
            print(f"TARGET CATEGORY IS->{form['target_category']}")
            alloc=AllocationBuilder(Instance(item_capacities=item_capacities, valuations=item_valuations))
            capped_round_robin(item_categories=item_categories, agent_category_capacities=category_capacities, initial_agent_order=initial_agent_order, alloc=alloc,target_category=target_category)
            logs=helper_get_logs(log_stream)
            return render_template('result.html', result=alloc.bundles,images_data=images_data,logs=logs.splitlines())
    elif algorithm == 'algorithm3':
            item_categories = ast.literal_eval(form['item_categories'])
            item_capacities = ast.literal_eval(form['item_capacities'])
            category_capacities = ast.literal_eval(form['category_capacities'])
            item_valuations = ast.literal_eval(form['item_valuations'])
            initial_agent_order = ast.literal_eval(form['initial_agent_order'])
            target_category_pair = ast.literal_eval(form['target_category_pair'])
            alloc=AllocationBuilder(Instance(item_capacities=item_capacities, valuations=item_valuations))
            two_categories_capped_round_robin(item_categories=item_categories, agent_category_capacities=category_capacities, initial_agent_order=initial_agent_order, alloc=alloc,target_category_pair=target_category_pair)
            logs=helper_get_logs(log_stream)
            return render_template('result.html', result=alloc.bundles,images_data=images_data,logs=logs.splitlines())
    elif algorithm == 'algorithm4':
            item_categories = ast.literal_eval(form['item_categories'])
            item_capacities = ast.literal_eval(form['item_capacities'])
            category_capacities = ast.literal_eval(form['category_capacities'])
            item_valuations = ast.literal_eval(form['item_valuations'])
            initial_agent_order = ast.literal_eval(form['initial_agent_order'])
            alloc=AllocationBuilder(Instance(item_capacities=item_capacities, valuations=item_valuations))
            per_category_capped_round_robin(item_categories=item_categories, agent_category_capacities=category_capacities, initial_agent_order=initial_agent_order, alloc=alloc)
            logs=helper_get_logs(log_stream)
            return render_template('result.html', result=alloc.bundles,images_data=images_data,logs=logs.splitlines())
    elif algorithm == 'algorithm5':
            item_categories = ast.literal_eval(form['item_categories'])
            item_capacities = ast.literal_eval(form['item_capacities'])
            category_capacities = ast.literal_eval(form['category_capacities'])
            item_valuations = ast.literal_eval(form['item_valuations'])
            print(f'Algorithm5 input: \n item_categories ->{item_categories} ,\n item_capacities->{item_capacities},\n category_capacities -> {category_capacities},\n item_valuations ->{item_valuations}\n **************************************************')
            alloc=AllocationBuilder(Instance(item_capacities=item_capacities, valuations=item_valuations))
            iterated_priority_matching(item_categories=item_categories, agent_category_capacities=category_capacities, alloc=alloc,callback=store_visualization)
            print(f'images data -> {images_data}')
            logs=helper_get_logs(log_stream)
            return render_template('result.html', result=alloc.bundles,images_data=images_data,logs=logs.splitlines())

    errors = form.errors if form else {}
    return render_template(f'{algorithm}_form_page.html', form=form, errors=errors, algorithm=algorithm)



@app.route('/future_feature')
def future_feature():
    return render_template('future_feature.html')



# New route for options page
@app.route('/options_page')
def options_page():
    return render_template('options_page.html')

@app.route('/spreadsheet')
def spreadsheet():
    # Logic to display the spreadsheet
    return render_template('spreadsheet.html')

from flask_app.forms import Algorithm1Form

@app.route('/generate_instance/<algorithm>', methods=['GET', 'POST'])
def generate_instance(algorithm):
    form = None

    if algorithm == 'algorithm1':
        form = Algorithm1GeneratorForm()
    elif algorithm == 'algorithm2':
        form = Algorithm2GeneratorForm()
    elif algorithm == 'algorithm3':
        form = Algorithm3GeneratorForm()
    elif algorithm == 'algorithm4':
        form = Algorithm4GeneratorForm()
    elif algorithm == 'algorithm5':
        form = Algorithm5GeneratorForm()

    if form and request.method == 'POST' and form.validate_on_submit():
        # Store the form data in session
        session['form_data'] = {field.name: field.data for field in form}
        print(session['form_data'])
        # Redirect to the result page
        return redirect(url_for('result_page', algorithm=algorithm))

    if form:
        return render_template(f'{algorithm}_generate_instance.html', algorithm=algorithm, form=form)

    return "Algorithm not found", 404

@app.route('/result_page/<algorithm>')
def result_page(algorithm):
    form_data = session.get('form_data', {})
    images_data = []
    instance = agent_category_capacities = categories = initial_agent_order = target_category = target_category_pair = None
    def store_visualization(img_base64):# used to get us the images from fairpyx !
        images_data.append(img_base64)
    log_stream=fairpyx.algorithms.heterogeneous_matroid_constraints_algorithms.helper_configure_logger()
    if algorithm=='algorithm1':
        instance, agent_category_capacities, categories, initial_agent_order = random_instance(equal_capacities=True,
                                                                                           category_count=ast.literal_eval(form_data['num_categories']),
                                                                                           num_of_agents=ast.literal_eval(form_data['num_agents']),
                                                                                           num_of_items=ast.literal_eval(form_data['num_items']),
                                                                                           item_capacity_bounds=(1, 1),
                                                                                           random_seed_num=0)
        alloc = divide(algorithm=per_category_round_robin, instance=instance,
                   item_categories=categories, agent_category_capacities=agent_category_capacities,
                   initial_agent_order=initial_agent_order,callback=store_visualization)
        logs=helper_get_logs(log_stream)
    elif algorithm == 'algorithm2':
        target_category=f"category{ast.literal_eval(form_data['target_category'])}"
        instance, agent_category_capacities, categories, initial_agent_order = random_instance(equal_capacities=False,
                                                                                           category_count=ast.literal_eval(form_data['num_categories']),
                                                                                           num_of_agents=ast.literal_eval(form_data['num_agents']),
                                                                                           num_of_items=ast.literal_eval(form_data['num_items']),
                                                                                           item_capacity_bounds=(1, 1),
                                                                                           random_seed_num=0)
        print(f'CRR target category is ->{form_data["target_category"]}')
        alloc = divide(algorithm=capped_round_robin, instance=instance,
                   item_categories=categories, agent_category_capacities=agent_category_capacities,
                   initial_agent_order=initial_agent_order,target_category=f'c{ast.literal_eval(form_data["target_category"])}')
        logs=helper_get_logs(log_stream)
    elif algorithm == 'algorithm3':
        target_category_pair=(f"category{ast.literal_eval(form_data['target_category1'])}",f"category{ast.literal_eval(form_data['target_category2'])}")
        instance, agent_category_capacities, categories, initial_agent_order = random_instance(equal_capacities=False,
                                                                                           category_count=ast.literal_eval(form_data['num_categories']),
                                                                                           num_of_agents=ast.literal_eval(form_data['num_agents']),
                                                                                           num_of_items=ast.literal_eval(form_data['num_items']),
                                                                                           item_capacity_bounds=(1, 1),
                                                                                           random_seed_num=0)
        alloc = divide(algorithm=two_categories_capped_round_robin, instance=instance,
                   item_categories=categories, agent_category_capacities=agent_category_capacities,
                   initial_agent_order=initial_agent_order,target_category_pair=(f'c{ast.literal_eval(form_data["target_category1"])}',f'c{ast.literal_eval(form_data["target_category2"])}'))
        logs=helper_get_logs(log_stream)
    elif algorithm=='algorithm4':
        instance, agent_category_capacities, categories, initial_agent_order = random_instance(equal_valuations=True,
                                                                                           category_count=ast.literal_eval(form_data['num_categories']),
                                                                                           num_of_agents=ast.literal_eval(form_data['num_agents']),
                                                                                           num_of_items=ast.literal_eval(form_data['num_items']),
                                                                                           item_capacity_bounds=(1, 1),
                                                                                           random_seed_num=0)
        alloc = divide(algorithm=per_category_capped_round_robin, instance=instance,
                   item_categories=categories, agent_category_capacities=agent_category_capacities,
                   initial_agent_order=initial_agent_order,callback=store_visualization)
        logs=helper_get_logs(log_stream)
    elif algorithm=='algorithm5':
        instance, agent_category_capacities, categories, initial_agent_order = random_instance(binary_valuations=True,
                                                                                           category_count=ast.literal_eval(form_data['num_categories']),
                                                                                           num_of_agents=ast.literal_eval(form_data['num_agents']),
                                                                                           num_of_items=ast.literal_eval(form_data['num_items']),
                                                                                           item_capacity_bounds=(1, 1),
                                                                                           random_seed_num=0)
        alloc = divide(algorithm=iterated_priority_matching, instance=instance,
                   item_categories=categories, agent_category_capacities=agent_category_capacities,
                   callback=store_visualization)
        logs=helper_get_logs(log_stream)
    else:
        return "Algorithm not found", 404 
    # Render the result page and pass the form data
    return render_template(
        'result_generator.html',
        result=alloc,
        images_data=images_data,
        logs=logs.splitlines(),
        instance=instance,
        agent_category_capacities=agent_category_capacities,
        categories=categories,
        initial_agent_order=initial_agent_order,
        target_category=target_category,
        target_category_pair=target_category_pair,
        algorithm=algorithm
    )