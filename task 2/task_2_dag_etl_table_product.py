from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
default_args = {
    'owner': 'Kitabisa.com',
    'email': ['suryatriatmaja87@gmail.com']
}
dag = DAG(
    dag_id='dag_table_product',
    default_args=default_args,
    description='This is dag for table product',
    start_date=datetime(2022, 3, 4),
    schedule_interval=@once
)

task_1 = BashOperator(
    task_id='task_1',
    bash_command='python3 /home/kitabisa/etl_table_product.py',
    dag=dag,
)
task_1