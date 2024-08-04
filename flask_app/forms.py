from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from fairpyx.algorithms.heterogeneous_matroid_constraints_algorithms import *
import ast
DEFAULT_AGENT_ITEM_CATEGORIES="{'category_1':['item_1'],'category_2':['item_2']}"
DEFAULT_AGENT_ITEM_VALUATIONS="{'agent_1':{'item_1':10,'item_2':1},'agent_2':{'item_1':5,'item_2':2}}"
DEFAULT_AGENT_CATEGORY_CAPACITIES="{'agent_1':{'category_1':5,'category_2':1},'agent_2':{'category_1':1,'category_2':0}}"
DEFAULT_IDENTICAL_AGENT_ITEM_VALUATIONS="{'agent_1':{'item_1':10,'item_2':1},'agent_2':{'item_1':10,'item_2':1}}"
DEFAULT_IDENTICAL_AGENT_CATEGORY_CAPACITIES="{'agent_1':{'category_1':5,'category_2':1},'agent_2':{'category_1':5,'category_2':1}}"
DEFAULT_ITEM_CAPACITIES="{'item_1':2,'item_2':5}"
DEFAULT_INITIAL_AGENT_ORDER="['agent_1','agent_2']"
DEFAULT_BINARY_AGENT_ITEM_VALUATIONS="{'agent_1':{'item_1':0,'item_2':1},'agent_2':{'item_1':1,'item_2':0}}"
DEFAULT_TARGET_CATEGORY="'category_1'"
DEFAULT_TARGET_CATEGORY_PAIR="('category_1','category_2')"
#print(ast.literal_eval(DEFAULT_TARGET_CATEGORY),type(ast.literal_eval(DEFAULT_TARGET_CATEGORY)))

# Custom validators
def validate_using_algorithm(validation_function):
    def _validate(form:FlaskForm, field):
        is_valid, error_message = validation_function(form,field.data)
        if not is_valid:
            raise ValidationError(error_message)
    return _validate

# Placeholder for your algorithm's validation functions
def validate_item_categories(form,data):
    # Replace with actual validation logic
    try:
        data = ast.literal_eval(data)
        print(type(data))
        helper_validate_item_categories(data)
    except Exception as e :
        print(f'exception in {data} -> {e}')
        return False , str(e)+"\n Enter something like {'category_1':['item_1'],'category_2':['item_2']}"
    return True, ""

def validate_item_capacities(form,data): # validate that they look like {item:5.....} dict[str,int]
    try:
        data = ast.literal_eval(data)
        print(type(data))
        helper_validate_item_capacities(data)
    except Exception as e :
        #print(f'exception in {data} -> {e}')
        return False , str(e)+"\n Enter something like {'item_1':2,'item_2':5}"
    return True, ""

def validate_identical_agent_category_capacities(form,data):
    try:
        data = ast.literal_eval(data)
        print(type(data))
        helper_validate_capacities(data,is_identical=True)
    except Exception as e:
        return False ,  str(e)+"\n Enter something like {'agent_1':{'category_1':5,'category_2':1},'agent_2':{'category_1':5,'category_2':1}}"
    return True, ""

def validate_agent_category_capacities(form,data):
    try:
        data = ast.literal_eval(data)
        print(type(data))
        helper_validate_capacities(data)
    except Exception as e:
        return False ,  str(e)+"\n Enter something like {'agent_1':{'category_1':5,'category_2':1},'agent_2':{'category_1':1,'category_2':0}}"
    return True, ""

def validate_agent_item_valuations(form,data):
    
    try:
        data = ast.literal_eval(data)
        print(type(data))
        helper_validate_valuations(data)
    except  Exception as e:
        return False , str(e)+"\n Enter something like {'agent_1':{'item_1':10,'item_2':1},'agent_2':{'item_1':5,'item_2':2}}"
    return True, ""

def validate_identical_agent_item_valuations(form,data):
    
    try:
        data = ast.literal_eval(data)
        print(type(data))
        helper_validate_valuations(data,is_identical=True)
    except  Exception as e:
        return False , str(e)+"\n Enter something like {'agent_1':{'item_1':10,'item_2':1},'agent_2':{'item_1':10,'item_2':1}}"
    return True, ""

def validate_binary_agent_item_valuations(form,data):
    
    try:
        data = ast.literal_eval(data)
        print(type(data))
        helper_validate_valuations(data,is_binary=True)
    except  Exception as e:
        return False , str(e)+"\n Enter something like {'agent_1':{'item_1':0,'item_2':1},'agent_2':{'item_1':1,'item_2':0}}"
    return True, ""

def validate_initial_agent_order(form,data):
    try:
        data = ast.literal_eval(data)
        helper_validate_duplicate(data)
    except  Exception as e:
        return False , str(e)+"\n Enter something like ['agent_1','agent_2']"
    return True, ""

def validate_target_category(form,data):
    try:
        target_category=ast.literal_eval(data)
        item_categories=ast.literal_eval(form.item_categories.data)
        if target_category not in item_categories:
            raise ValueError(f"Target category mistyped or not found: {target_category}")
    except  Exception as e:
        return False , str(e)
    return True, ""

def validate_target_category_pair(form,data):
    try:
        target_category_pair=ast.literal_eval(data)
        item_categories=ast.literal_eval(form.item_categories.data)
        if not all(item in item_categories for item in target_category_pair):
            raise ValueError(
            f"Not all elements of the tuple {target_category_pair} are in the categories list {list(item_categories.keys())}.")
    except  Exception as e:
        return False , str(e)
    return True, ""
 
 
def helper_validate_item_capacities(variable):
    if not isinstance(variable, dict):
        raise TypeError(f"Expected a dictionary, but got {type(variable).__name__}")
    for key, value in variable.items():
        if not isinstance(key, str):
            raise TypeError(f"Expected key to be of type 'str', but got key '{key}' of type {type(key).__name__}")
        if not isinstance(value, int):
            raise TypeError(f"Expected value to be of type 'int', but got value '{value}' of type {type(value).__name__}")


class Algorithm1Form(FlaskForm):
    item_categories = StringField('Item Categories', validators=[DataRequired(),validate_using_algorithm(validate_item_categories)],default=DEFAULT_AGENT_ITEM_CATEGORIES)
    item_capacities = StringField('Item Capacities', validators=[DataRequired(),validate_using_algorithm(validate_item_capacities)],default=DEFAULT_ITEM_CAPACITIES)
    category_capacities = StringField('Category Capacities', validators=[DataRequired(),validate_using_algorithm(validate_identical_agent_category_capacities)],default=DEFAULT_IDENTICAL_AGENT_CATEGORY_CAPACITIES)
    item_valuations = StringField('Item Valuations', validators=[DataRequired(),validate_using_algorithm(validate_agent_item_valuations)],default=DEFAULT_AGENT_ITEM_VALUATIONS)
    initial_agent_order = StringField('Initial Agent Order', validators=[DataRequired(),validate_using_algorithm(validate_initial_agent_order)],default=DEFAULT_INITIAL_AGENT_ORDER)
    submit = SubmitField('Submit')


class Algorithm2Form(FlaskForm):
    item_categories = StringField('Item Categories', validators=[DataRequired(),validate_using_algorithm(validate_item_categories)],default=DEFAULT_AGENT_ITEM_CATEGORIES)
    item_capacities = StringField('Item Capacities', validators=[DataRequired(),validate_using_algorithm(validate_item_capacities)],default=DEFAULT_ITEM_CAPACITIES)
    category_capacities = StringField('Category Capacities', validators=[DataRequired(),validate_using_algorithm(validate_agent_category_capacities)],default=DEFAULT_AGENT_CATEGORY_CAPACITIES)
    item_valuations = StringField('Item Valuations', validators=[DataRequired(),validate_using_algorithm(validate_agent_item_valuations)],default=DEFAULT_AGENT_ITEM_VALUATIONS)
    initial_agent_order = StringField('Initial Agent Order', validators=[DataRequired(),validate_using_algorithm(validate_initial_agent_order)],default=DEFAULT_INITIAL_AGENT_ORDER)
    target_category = StringField('Target Category', validators=[DataRequired(),validate_using_algorithm(validate_target_category)],default=DEFAULT_TARGET_CATEGORY)
    #target_category_pair = StringField('Target Category Pair', validators=[DataRequired()])
    submit = SubmitField('Submit')


class Algorithm3Form(FlaskForm):
    item_categories = StringField('Item Categories', validators=[DataRequired(),validate_using_algorithm(validate_item_categories)],default=DEFAULT_AGENT_ITEM_CATEGORIES)
    item_capacities = StringField('Item Capacities', validators=[DataRequired(),validate_using_algorithm(validate_item_capacities)],default=DEFAULT_ITEM_CAPACITIES)
    category_capacities = StringField('Category Capacities', validators=[DataRequired(),validate_using_algorithm(validate_agent_category_capacities)],default=DEFAULT_AGENT_CATEGORY_CAPACITIES)
    item_valuations = StringField('Item Valuations', validators=[DataRequired(),validate_using_algorithm(validate_agent_item_valuations)],default=DEFAULT_AGENT_ITEM_VALUATIONS)
    initial_agent_order = StringField('Initial Agent Order', validators=[DataRequired(),validate_using_algorithm(validate_initial_agent_order)],default=DEFAULT_INITIAL_AGENT_ORDER)
    target_category_pair = StringField('Target Category Pair', validators=[DataRequired(),validate_using_algorithm(validate_target_category_pair)],default=DEFAULT_TARGET_CATEGORY_PAIR)
    submit = SubmitField('Submit')

class Algorithm4Form(FlaskForm):
    item_categories = StringField('Item Categories', validators=[DataRequired(),validate_using_algorithm(validate_item_categories)],default=DEFAULT_AGENT_ITEM_CATEGORIES)
    item_capacities = StringField('Item Capacities', validators=[DataRequired(),validate_using_algorithm(validate_item_capacities)],default=DEFAULT_ITEM_CAPACITIES)
    category_capacities = StringField('Category Capacities', validators=[DataRequired(),validate_using_algorithm(validate_agent_category_capacities)],default=DEFAULT_AGENT_CATEGORY_CAPACITIES)
    item_valuations = StringField('Item Valuations', validators=[DataRequired(),validate_using_algorithm(validate_agent_item_valuations)],default=DEFAULT_IDENTICAL_AGENT_ITEM_VALUATIONS)
    initial_agent_order = StringField('Initial Agent Order', validators=[DataRequired(),validate_using_algorithm(validate_initial_agent_order)],default=DEFAULT_INITIAL_AGENT_ORDER)
    submit = SubmitField('Submit')


class Algorithm5Form(FlaskForm):
    item_categories = StringField('Item Categories', validators=[DataRequired(),validate_using_algorithm(validate_item_categories)],default=DEFAULT_AGENT_ITEM_CATEGORIES)
    item_capacities = StringField('Item Capacities', validators=[DataRequired(),validate_using_algorithm(validate_item_capacities)],default=DEFAULT_ITEM_CAPACITIES)
    category_capacities = StringField('Category Capacities', validators=[DataRequired(),validate_using_algorithm(validate_agent_category_capacities)],default=DEFAULT_AGENT_CATEGORY_CAPACITIES)
    item_valuations = StringField('Item Valuations', validators=[DataRequired(),validate_using_algorithm(validate_agent_item_valuations)],default=DEFAULT_BINARY_AGENT_ITEM_VALUATIONS)
    submit = SubmitField('Submit')
    
    submit = SubmitField('Submit')
        
# Define similar forms for Algorithm3Form, Algorithm4Form, Algorithm5Form as needed
"""
Submit Your Data
Item Categories
{'category_1':['item_1'],'category_2':['item_2']}
Item Capacities
{'item_1':2,'item_2':5}
Category Capacities
{'agent_1':{'category_1':5,'category_2':1},'agent_2':{'category_1':1,'category_2':0}}
[malformed node or string on line 1: <ast.Name object at 0x7f6dedfde230> Enter something like {agent_1:{category_1:5,category_2:1},agent_2:{category_1:1,category_2:0}}]
Item Valuations
{'agent_1':{'item_1':10,'item_2':1},'agent_2':{'item_1':10,'item_2':1}}
[malformed node or string on line 1: <ast.Name object at 0x7f6dedfde3b0> Enter something like {agent_1:{item_1:10,item_2:1},agent_2:{item_1:10,item_2:1}}]
Initial Agent Order
['agent_1','agent_2']
[malformed node or string on line 1: <ast.Name object at 0x7f6dedfde3b0> Enter something like [agent_1,agent_2]]
        """