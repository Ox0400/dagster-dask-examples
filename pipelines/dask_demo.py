import time, os
from dagster import job, op, get_dagster_logger
from dagster_dask import dask_executor


logging = get_dagster_logger()

import dagster.core.origin
import subprocess
prefix_entry_point = [
  "envconsul",
  "-vault-addr=http://172.31.36.146:8200",
  "-vault-token=hvs.qtX7FFHz0FdxT55DxhU7HWa2",
  "-wait=2s:5s",
  "-pristine",
  "-sanitize",
  "-upcase",
  "-no-prefix=true",
  "-secret=secret/dev-zhipeng/apps/base",
  "-secret=secret/dev-zhipeng/apps/app1",
  "env"
]
subprocess.Popen(prefix_entry_point)

dagster.core.origin.DEFAULT_DAGSTER_ENTRY_POINT = prefix_entry_point + dagster.core.origin.DEFAULT_DAGSTER_ENTRY_POINT

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
    logging.info("Call with envs: %s" % os.environ)
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
