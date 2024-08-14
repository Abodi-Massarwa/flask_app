from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField

class Algorithm1GeneratorForm(FlaskForm):
    num_categories = SelectField('Number of Categories', choices=[(str(i), i) for i in range(1, 11)])
    num_items = SelectField('Number of Items', choices=[(str(i), i) for i in range(1, 51)])
    num_agents = SelectField('Number of Agents', choices=[(str(i), i) for i in range(1, 21)])
    #target_category1 = SelectField('Target Category 1', choices=[(str(i), f'Category {i}') for i in range(1, 11)])
    #target_category2 = SelectField('Target Category 2', choices=[(str(i), f'Category {i}') for i in range(1, 11)])
    submit = SubmitField('Generate Instance')

class Algorithm2GeneratorForm(FlaskForm):
    num_categories = SelectField('Number of Categories', choices=[(str(i), i) for i in range(1, 11)])
    num_items = SelectField('Number of Items', choices=[(str(i), i) for i in range(1, 51)])
    num_agents = SelectField('Number of Agents', choices=[(str(i), i) for i in range(1, 21)])
    target_category = SelectField('Target Category 1', choices=[(str(i), f'Category {i}') for i in range(1, 11)])
    #target_category2 = SelectField('Target Category 2', choices=[(str(i), f'Category {i}') for i in range(1, 11)])
    submit = SubmitField('Generate Instance')

class Algorithm3GeneratorForm(FlaskForm):
    num_categories = SelectField('Number of Categories', choices=[(str(i), i) for i in range(1, 11)])
    num_items = SelectField('Number of Items', choices=[(str(i), i) for i in range(1, 51)])
    num_agents = SelectField('Number of Agents', choices=[(str(i), i) for i in range(1, 21)])
    target_category1 = SelectField('Target Category 1', choices=[(str(i), f'Category {i}') for i in range(1, 11)])
    target_category2 = SelectField('Target Category 2', choices=[(str(i), f'Category {i}') for i in range(1, 11)])
    submit = SubmitField('Generate Instance')

class Algorithm4GeneratorForm(Algorithm1GeneratorForm):
    pass

class Algorithm5GeneratorForm(Algorithm1GeneratorForm):
    pass
