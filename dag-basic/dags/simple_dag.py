from airflow import DAG
from airflow.operators import bash
from datetime import datetime

default_args = {
  'owner': 'dery'
}

with DAG(
  default_args=default_args,
  dag_id="test.dag",
  tags=["playground"],
  schedule_interval="* * * * *",
  start_date=datetime(2022, 3, 30, 13),
  catchup=True,
) as dag:

  t1 = bash.BashOperator(
    task_id="test.dag.t1",
    bash_command="sleep 5"
  )

  t2 = bash.BashOperator(
    task_id="test.dag.t2",
    bash_command="sleep 2"
  )

  t1 >> t2
