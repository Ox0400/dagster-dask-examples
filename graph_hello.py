from dagster import GraphDefinition, op

@op
def return_one():
    return 1

@op
def add_one(num):
    return num + 1

@op
def get_name(context):
    name = context.op_config.get('name', 'Guest')
    logging.info('name is:%s' % name)
    return name

@op
def helloa(name):
    logging.info("Hello, {name}!".format(name=name))
@op
def hellob(name):
    logging.info("Hello, {name}!".format(name=name))

graph_def = GraphDefinition(
    name='basic',
    node_defs=[return_one, add_one, get_name, helloa, hellob],
    dependencies={
        'add_one': {'num': DependencyDefinition('return_one')}
    },
)
