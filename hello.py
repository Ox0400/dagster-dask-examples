import time
from dagster import job, op, get_dagster_logger

logging = get_dagster_logger()


@op
def get_name(context):
    name = context.op_config.get('name')
    name1 = context.op_config.get('name1')
    logging.info('name is:%s' % name)
    return name

@op
def helloa(name):
    logging.info("Hello-a, {name}!".format(name=name))
    time.sleep(1)

@op
def hellob(name):
    logging.info("Hello-b, {name}!".format(name=name))
    time.sleep(1)

@job
def hello_dagster():
    start = time.time()
    name = get_name()
    helloa(name)
    hellob(name)
    logging.info('Total time: %s' % (time.time() - start))


if __name__ == "__main__":
    result = hello_dagster.execute_in_process()
