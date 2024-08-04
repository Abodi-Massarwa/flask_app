# from flask_app import app
# import gspread
# from flask import render_template , request, redirect,url_for
# from functools import partial
# import fairpyx as fp
# algorithms = [
#     {"name": "Per-Category Round-Robin", "route": "algorithm1", "description": """this is the Algorithm 1 from the paper
#      per category round-robin is an allocation algorithm which guarantees EF1 (envy-freeness up to 1 good) allocation
#     under settings in which agent-capacities are equal across all agents,
#     no capacity-inequalities are allowed since this algorithm doesnt provie a cycle-prevention mechanism
#     TLDR: same partition, same capacities, may have different valuations across agents  -> EF1 allocation"""},
#     {"name": "Capped Round-Robin", "route": "algorithm2", "description": """this is Algorithm 2 CRR (capped round-robin) algorithm TLDR: single category , may have differnt capacities
#     capped in CRR stands for capped capacity for each agent unlke RR , maye have different valuations -> F-EF1 (
#     feasible envy-freeness up to 1 good) allocation"""},
#     {"name": "Back&Forth RR(Round-Robin)", "route": "algorithm3", "description": """this is Algorithm 3 back and forth capped round-robin algorithm (2 categories,may have different capacities,may have different valuations)
#         in which we simply
#         1)call capped_round_robin(arg1 ,.... argk,item_categories=<first category>)
#         2) reverse(order)
#         3)call capped_round_robin(arg1 ,.... argk,item_categories=<second category>)
#         -> F-EF1 (feasible envy-freeness up to 1 good) allocation"""},
#     {"name": "Per-Category CRR(Capped-Round-Robin)", "route": "algorithm4", "description": """ this is Algorithm 4 deals with (Different Capacities, Identical Valuations), suitable for any number of categories
#     CRR (per-category capped round-robin) algorithm
#     TLDR: multiple categories , may have different capacities , but have identical valuations -> F-EF1 (feasible envy-freeness up to 1 good) allocation"""},
#     {"name": "Iterated Priority Matching", "route": "algorithm5", "description": """this is Algorithm 5  deals with (partition Matroids with Binary Valuations, may have different capacities)
#     loops as much as maximum capacity in per each category , each iteration we build :
#     1) agent-item graph (bidirectional graph)
#     2) envy graph
#     3) topological sort the order based on the envy graph (always a-cyclic under such settings,proven in papers)
#     4) compute priority matching based on it we allocate the items among the agents
#     we do this each loop , and in case there remains item in that category we arbitrarily give it to random agent
# """},
# ]

# account = gspread.service_account('/home/abodi-massarwa/website_final_project/secret_files/credentials.json')

# # Function to get data from Google Sheet by URL
# def get_sheet_data_by_url(sheet_url):
#     sheet = account.open_by_url(sheet_url).sheet1
#     data = sheet.get_all_records()
#     return data

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/algorithm1', methods=['GET', 'POST'])
# def algorithm1():
#     if request.method == 'POST':
#         data = get_sheet_data_by_url('https://docs.google.com/spreadsheets/d/1fs_FeivOv-LXOQ89OIug1PVZw1X3LqE7Dul0t8JsaDw/edit?gid=0#gid=0')
#         # Process your data here
#         return "Algorithm 1 data processed successfully!"
#     return render_template('algorithm.html', algorithm_name='Algorithm 1', sheet_url='https://docs.google.com/spreadsheets/d/1fs_FeivOv-LXOQ89OIug1PVZw1X3LqE7Dul0t8JsaDw/edit?gid=0#gid=0')

# @app.route('/algorithm2', methods=['GET', 'POST'])
# def algorithm2():
#     if request.method == 'POST':
#         data = get_sheet_data_by_url('https://docs.google.com/spreadsheets/d/1fs_FeivOv-LXOQ89OIug1PVZw1X3LqE7Dul0t8JsaDw/edit?gid=0#gid=0')
#         # Process your data here
#         return "Algorithm 2 data processed successfully!"
#     return render_template('algorithm.html', algorithm_name='Algorithm 2', sheet_url='https://docs.google.com/spreadsheets/d/1fs_FeivOv-LXOQ89OIug1PVZw1X3LqE7Dul0t8JsaDw/edit?gid=0#gid=0')

# @app.route('/algorithm3', methods=['GET', 'POST'])
# def algorithm3():
#     if request.method == 'POST':
#         data = get_sheet_data_by_url('https://docs.google.com/spreadsheets/d/1fs_FeivOv-LXOQ89OIug1PVZw1X3LqE7Dul0t8JsaDw/edit?gid=0#gid=0')
#         # Process your data here
#         return "Algorithm 3 data processed successfully!"
#     return render_template('algorithm.html', algorithm_name='Algorithm 3', sheet_url='https://docs.google.com/spreadsheets/d/1fs_FeivOv-LXOQ89OIug1PVZw1X3LqE7Dul0t8JsaDw/edit?gid=0#gid=0')

# @app.route('/algorithm4', methods=['GET', 'POST'])
# def algorithm4():
#     if request.method == 'POST':
#         data = get_sheet_data_by_url('https://docs.google.com/spreadsheets/d/1fs_FeivOv-LXOQ89OIug1PVZw1X3LqE7Dul0t8JsaDw/edit?gid=0#gid=0')
#         # Process your data here
#         return "Algorithm 4 data processed successfully!"
#     return render_template('algorithm.html', algorithm_name='Algorithm 4', sheet_url='https://docs.google.com/spreadsheets/d/1fs_FeivOv-LXOQ89OIug1PVZw1X3LqE7Dul0t8JsaDw/edit?gid=0#gid=0')

# @app.route('/algorithm5', methods=['GET', 'POST'])
# def algorithm5():
#     if request.method == 'POST':
#         data = get_sheet_data_by_url('https://docs.google.com/spreadsheets/d/1fs_FeivOv-LXOQ89OIug1PVZw1X3LqE7Dul0t8JsaDw/edit?gid=0#gid=0')
#         # Process your data here
#         return "Algorithm 5 data processed successfully!"
#     return render_template('algorithm.html', algorithm_name='Algorithm 5', sheet_url='https://docs.google.com/spreadsheets/d/1fs_FeivOv-LXOQ89OIug1PVZw1X3LqE7Dul0t8JsaDw/edit?gid=0#gid=0')

# @app.route('/form/<route>')
# def form(route):
#     algorithm = next((algo for algo in algorithms if algo["route"] == route), None)
#     if algorithm:
#         return render_template('form.html', algorithm=algorithm)
#     return redirect(url_for('index'))

# @app.route('/process_form/<route>', methods=['POST'])
# def process_form(route):
#     input_data = request.form.get('input_data')
#     processed_data = input_data.upper()  # Example processing
#     return f"Processed Data: {processed_data}"

# @app.route('/spreadsheet_options/<route>')
# def spreadsheet_options(route):
#     algorithm = next((algo for algo in algorithms if algo["route"] == route), None)
#     if algorithm:
#         return render_template('spreadsheet_options.html', algorithm=algorithm)
#     return redirect(url_for('index'))

# @app.route('/process_spreadsheet/<route>', methods=['POST'])
# def process_spreadsheet(route):
#     algorithm = next((algo for algo in algorithms if algo["route"] == route), None)
#     if algorithm:
#         column_name = "YourColumnName"  # Replace with the actual column name you want to fetch
#         column_data = get_column_data(algorithm['sheet_url'], column_name)
#         return f"Data from column '{column_name}' processed successfully: {column_data}"
#     return redirect(url_for('index'))
# def algorithm_template(name, description):
#     return render_template('algorithm.html', title=name, description=description)

# def get_sheet_data_by_url(sheet_url):
#     sheet = account.open_by_url(sheet_url).sheet1
#     data = sheet.get_all_records()
#     return data

# def get_column_data(sheet_url, column_name):
#     data = get_sheet_data_by_url(sheet_url)
#     column_data = [row[column_name] for row in data if column_name in row]
#     return column_data
# # for algorithm in algorithms:
# #     app.add_url_rule(f'/{algorithm["route"]}', 
# #                      endpoint=algorithm["route"], 
# #                      view_func=partial(algorithm_template, algorithm["name"], algorithm["description"]))

from flask import session
from flask_app import app
import gspread
from flask import render_template, request, redirect, url_for
from functools import partial
from fairpyx.algorithms.heterogeneous_matroid_constraints_algorithms import per_category_round_robin,capped_round_robin,two_categories_capped_round_robin,per_category_capped_round_robin,iterated_priority_matching
#from .forms import InputForm 
from fairpyx.allocations import AllocationBuilder, Instance
import ast
from flask_app.forms import Algorithm1Form, Algorithm2Form , Algorithm3Form, Algorithm4Form, Algorithm5Form
# Define your algorithms


algorithms = [
    {"name": "Per-Category Round-Robin", "route": "algorithm1", "description": """this is the Algorithm 1 from the paper
     per category round-robin is an allocation algorithm which guarantees EF1 (envy-freeness up to 1 good) allocation
    under settings in which agent-capacities are equal across all agents,
    no capacity-inequalities are allowed since this algorithm doesnt provie a cycle-prevention mechanism
    TLDR: same partition, same capacities, may have different valuations across agents  -> EF1 allocation"""},
    {"name": "Capped Round-Robin", "route": "algorithm2", "description": """this is Algorithm 2 CRR (capped round-robin) algorithm TLDR: single category , may have differnt capacities
    capped in CRR stands for capped capacity for each agent unlke RR , maye have different valuations -> F-EF1 (
    feasible envy-freeness up to 1 good) allocation"""},
    {"name": "Back&Forth RR(Round-Robin)", "route": "algorithm3", "description": """this is Algorithm 3 back and forth capped round-robin algorithm (2 categories,may have different capacities,may have different valuations)
        in which we simply
        1)call capped_round_robin(arg1 ,.... argk,item_categories=<first category>)
        2) reverse(order)
        3)call capped_round_robin(arg1 ,.... argk,item_categories=<second category>)
        -> F-EF1 (feasible envy-freeness up to 1 good) allocation"""},
    {"name": "Per-Category CRR(Capped-Round-Robin)", "route": "algorithm4", "description": """ this is Algorithm 4 deals with (Different Capacities, Identical Valuations), suitable for any number of categories
    CRR (per-category capped round-robin) algorithm
    TLDR: multiple categories , may have different capacities , but have identical valuations -> F-EF1 (feasible envy-freeness up to 1 good) allocation"""},
    {"name": "Iterated Priority Matching", "route": "algorithm5", "description": """this is Algorithm 5  deals with (partition Matroids with Binary Valuations, may have different capacities)
    loops as much as maximum capacity in per each category , each iteration we build :
    1) agent-item graph (bidirectional graph)
    2) envy graph
    3) topological sort the order based on the envy graph (always a-cyclic under such settings,proven in papers)
    4) compute priority matching based on it we allocate the items among the agents
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
    form = None
    form=session['form_data']
    #print(f'process_data page form is -> {form} and its type is _>{type(form)}')
    if algorithm == 'algorithm1':
            item_categories = ast.literal_eval(form['item_categories'])
            item_capacities = ast.literal_eval(form['item_capacities'])
            category_capacities = ast.literal_eval(form['category_capacities'])
            item_valuations = ast.literal_eval(form['item_valuations'])
            initial_agent_order = ast.literal_eval(form['initial_agent_order'])
            alloc=AllocationBuilder(Instance(item_capacities=item_capacities, valuations=item_valuations))
            per_category_round_robin(item_categories=item_categories, agent_category_capacities=category_capacities, initial_agent_order=initial_agent_order, alloc=alloc)
            #print(f'algorithm 1 allocation result is {result}')
            return render_template('result.html', result=alloc.bundles)
    elif algorithm == 'algorithm2':
            item_categories = ast.literal_eval(form['item_categories'])
            item_capacities = ast.literal_eval(form['item_capacities'])
            category_capacities = ast.literal_eval(form['category_capacities'])
            item_valuations = ast.literal_eval(form['item_valuations'])
            initial_agent_order = ast.literal_eval(form['initial_agent_order'])
            target_category = ast.literal_eval(form['target_category'])
            print(f"TARGET CATEGORY IS->{form['target_category']}")
            alloc=AllocationBuilder(Instance(item_capacities=item_capacities, valuations=item_valuations))
            result = capped_round_robin(item_categories=item_categories, agent_category_capacities=category_capacities, initial_agent_order=initial_agent_order, alloc=alloc,target_category=target_category)
            return render_template('result.html', result=alloc.bundles)
    elif algorithm == 'algorithm3':
            item_categories = ast.literal_eval(form['item_categories'])
            item_capacities = ast.literal_eval(form['item_capacities'])
            category_capacities = ast.literal_eval(form['category_capacities'])
            item_valuations = ast.literal_eval(form['item_valuations'])
            initial_agent_order = ast.literal_eval(form['initial_agent_order'])
            target_category_pair = ast.literal_eval(form['target_category_pair'])
            alloc=AllocationBuilder(Instance(item_capacities=item_capacities, valuations=item_valuations))
            result = two_categories_capped_round_robin(item_categories=item_categories, agent_category_capacities=category_capacities, initial_agent_order=initial_agent_order, alloc=alloc,target_category_pair=target_category_pair)
            return render_template('result.html', result=alloc.bundles)
    elif algorithm == 'algorithm4':
            item_categories = ast.literal_eval(form['item_categories'])
            item_capacities = ast.literal_eval(form['item_capacities'])
            category_capacities = ast.literal_eval(form['category_capacities'])
            item_valuations = ast.literal_eval(form['item_valuations'])
            initial_agent_order = ast.literal_eval(form['initial_agent_order'])
            alloc=AllocationBuilder(Instance(item_capacities=item_capacities, valuations=item_valuations))
            result = per_category_capped_round_robin(item_categories=item_categories, agent_category_capacities=category_capacities, initial_agent_order=initial_agent_order, alloc=alloc)
            return render_template('result.html', result=alloc.bundles)
    elif algorithm == 'algorithm5':
            item_categories = ast.literal_eval(form['item_categories'])
            item_capacities = ast.literal_eval(form['item_capacities'])
            category_capacities = ast.literal_eval(form['category_capacities'])
            item_valuations = ast.literal_eval(form['item_valuations'])
            alloc=AllocationBuilder(Instance(item_capacities=item_capacities, valuations=item_valuations))
            result = iterated_priority_matching(item_categories=item_categories, agent_category_capacities=category_capacities, alloc=alloc)
            return render_template('result.html', result=alloc.bundles)

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

# @app.route('/process_data')
# def process_data():
#     # Logic to process data
#     return "Data processed successfully"
