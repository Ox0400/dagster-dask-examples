import time
from dagster import RunRequest, ScheduleDefinition, job, op, repository, sensor

@op
def x1():
    time.sleep(5)
    pass


@op
def x2():
    time.sleep(5)
    pass


@job
def job1():
    x1()
    x2()

@job
def job2():
    x1()
    x2()


@repository
def my_repository():
    return [
        job1,
        job2,
    ]


"""
execution:
  config:
    multiprocess:
      max_concurrent: 3

"""
