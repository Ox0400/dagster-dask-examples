from dagster import job, get_dagster_logger, op
from dagster_docker import docker_executor

logging = get_dagster_logger()

@op
def get_name():
    return 'name: docker'

@job(executor_def=docker_executor)
def docker_job():
    name = get_name()
    logging.info('run docker ....')
    logging.info('r: %s' % name)

"""
execution:
  config:
    container_kwargs:
      entrypoint: null
      stdin_open: true
      tty: true
      working_dir: /app/codes
    env_vars:
    - POSTGRESQL_URI
    - DAGSTER_HOME
    image: 0x0400/dagster-code
"""

