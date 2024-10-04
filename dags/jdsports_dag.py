import os
import sys
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.jdsports_pipeline import jdsports_pipeline, jdsport_to_s3, kickgame_to_s3


default_args = {
    'owner': 'Biokpor Solomon',
    'start_date': datetime(2024, 9, 27)
}



dag = DAG(
    dag_id='etl_jd_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['jdsport', 'etl', 'pipeline']
    
    )
    
#extraction from jd sport
extract = BashOperator(
    task_id='jdsport_extraction',
    bash_command='cd /opt/airflow/fastfashion && scrapy crawl jdsport -o jdsportraw.csv',
    dag=dag
    )


process = PythonOperator(
    task_id='jdsport_pandas',
    python_callable=jdsports_pipeline,

    )
    

upload = PythonOperator(
    task_id = 'jdsport_to_s3',
    python_callable=jdsport_to_s3,
    dag=dag
    )

delete = BashOperator(
    task_id = 'delete_jdsport',
    bash_command = 'cd /opt/airflow/fastfashion && rm -rf jdsportraw.csv',
    dag=dag
    )
    

#extraction from kickgame sport
extract2 = BashOperator(
    task_id='kickgame_extraction',
    bash_command='cd /opt/airflow/fastfashion && scrapy crawl kickgame -o kickgameraw.csv',
    dag=dag
    )


process2 = PythonOperator(
    task_id='kickgame_pandas',
    python_callable=jdsports_pipeline,

    )
    

upload2 = PythonOperator(
    task_id = 'kickgame_to_s3',
    python_callable=kickgame_to_s3,
    dag=dag
    )

delete2 = BashOperator(
    task_id = 'delete_kickgame',
    bash_command = 'cd /opt/airflow/fastfashion && rm -rf kickgameraw.csv',
    dag=dag
    )

extract >> upload >> delete >> extract2 >> upload2 >> delete2