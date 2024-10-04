import os
import sys
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.jdsports_pipeline import sac_to_s3


default_args = {
    'owner': 'Biokpor Solomon',
    'start_date': datetime(2024, 9, 27)
}



dag = DAG(
    dag_id='etl_sac_pipeline',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['sac', 'etl', 'pipeline']
    
    )
    
#extraction from jd sport
extract = BashOperator(
    task_id='sac_extraction',
    bash_command='cd /opt/airflow/fastfashion && scrapy crawl sac',
    dag=dag
    )

    

upload = PythonOperator(
    task_id = 'sac_to_s3',
    python_callable=sac_to_s3,
    dag=dag
    )

delete = BashOperator(
    task_id = 'delete_sac',
    bash_command = 'cd /opt/airflow/fastfashion && rm -rf sacraw.csv',
    dag=dag
    )
    


extract >> upload >> delete