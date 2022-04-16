import time
from dagster import job, op, get_dagster_logger
from dagster_dask import dask_executor


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
    time.sleep(5)
    return '%s-a' % name

@op
def hellob(name):
    logging.info("Hello-b, {name}!".format(name=name))
    time.sleep(5)
    return '%s-b' % name

@op
def merge_result(x, y):
    logging.info("Merging, x;%s, y:%s" % (x, y))
    time.sleep(2)


@job(executor_def=dask_executor)
def dask_test():

    start = time.time()
    name = get_name()
    x = helloa(name)
    y = hellob(name)
    merge_result(x,y)
    #merge_result(helloa(name), hellob(name))

if __name__ == "__main__":
    result = dask_test.execute_in_process()
"""
execution:
  config:
    cluster:
      existing:
        address: tcp://ip-172-31-36-146:8786
ops:
  get_name:
    config:
      name: hello

"""

