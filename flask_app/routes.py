from flask_app import app
from flask import render_template
from functools import partial
import fairpyx as fp
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

@app.route('/')
def index():
    return render_template('index.html', title='Home Page')

def algorithm_template(name, description):
    return render_template('algorithm.html', title=name, description=description)

for algorithm in algorithms:
    app.add_url_rule(f'/{algorithm["route"]}', 
                     endpoint=algorithm["route"], 
                     view_func=partial(algorithm_template, algorithm["name"], algorithm["description"]))