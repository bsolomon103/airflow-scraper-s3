{"filter":false,"title":"sac_dag.py","tooltip":"/dags/sac_dag.py","undoManager":{"mark":38,"position":38,"stack":[[{"start":{"row":0,"column":0},"end":{"row":82,"column":61},"action":"insert","lines":["import os","import sys","from datetime import datetime","from airflow import DAG","from airflow.operators.bash import BashOperator","from airflow.operators.python import PythonOperator","sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))","","from pipelines.jdsports_pipeline import jdsports_pipeline, jdsport_to_s3, kickgame_to_s3","","","default_args = {","    'owner': 'Biokpor Solomon',","    'start_date': datetime(2024, 9, 27)","}","","","","dag = DAG(","    dag_id='etl_jd_pipeline',","    default_args=default_args,","    schedule_interval='@daily',","    catchup=False,","    tags=['jdsport', 'etl', 'pipeline']","    ","    )","    ","#extraction from jd sport","extract = BashOperator(","    task_id='jdsport_extraction',","    bash_command='cd /opt/airflow/fastfashion && scrapy crawl jdsport -o jdsportraw.csv',","    dag=dag","    )","","","process = PythonOperator(","    task_id='jdsport_pandas',","    python_callable=jdsports_pipeline,","","    )","    ","","upload = PythonOperator(","    task_id = 'jdsport_to_s3',","    python_callable=jdsport_to_s3,","    dag=dag","    )","","delete = BashOperator(","    task_id = 'delete_jdsport',","    bash_command = 'cd /opt/airflow/fastfashion && rm -rf jdsportraw.csv',","    dag=dag","    )","    ","","#extraction from kickgame sport","extract2 = BashOperator(","    task_id='kickgame_extraction',","    bash_command='cd /opt/airflow/fastfashion && scrapy crawl kickgame -o kickgameraw.csv',","    dag=dag","    )","","","process2 = PythonOperator(","    task_id='kickgame_pandas',","    python_callable=jdsports_pipeline,","","    )","    ","","upload2 = PythonOperator(","    task_id = 'kickgame_to_s3',","    python_callable=kickgame_to_s3,","    dag=dag","    )","","delete2 = BashOperator(","    task_id = 'delete_kickgame',","    bash_command = 'cd /opt/airflow/fastfashion && rm -rf kickgameraw.csv',","    dag=dag","    )","","extract >> upload >> delete >> extract2 >> upload2 >> delete2"],"id":1}],[{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"remove","lines":["d"],"id":2},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"remove","lines":["j"]}],[{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["s"],"id":3},{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"insert","lines":["a"]},{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["c"]}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"remove","lines":["y"],"id":4},{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"remove","lines":["l"]},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"remove","lines":["i"]},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"remove","lines":["a"]},{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"remove","lines":["d"]}],[{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["y"],"id":5},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["e"]},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["a"]},{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"insert","lines":["r"]},{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["l"]},{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["y"]}],[{"start":{"row":23,"column":17},"end":{"row":23,"column":18},"action":"remove","lines":["t"],"id":6},{"start":{"row":23,"column":16},"end":{"row":23,"column":17},"action":"remove","lines":["r"]},{"start":{"row":23,"column":15},"end":{"row":23,"column":16},"action":"remove","lines":["o"]},{"start":{"row":23,"column":14},"end":{"row":23,"column":15},"action":"remove","lines":["p"]},{"start":{"row":23,"column":13},"end":{"row":23,"column":14},"action":"remove","lines":["s"]},{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"remove","lines":["d"]},{"start":{"row":23,"column":11},"end":{"row":23,"column":12},"action":"remove","lines":["j"]}],[{"start":{"row":23,"column":11},"end":{"row":23,"column":12},"action":"insert","lines":["s"],"id":7},{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"insert","lines":["c"]}],[{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"remove","lines":["c"],"id":8}],[{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"insert","lines":["a"],"id":9},{"start":{"row":23,"column":13},"end":{"row":23,"column":14},"action":"insert","lines":["c"]}],[{"start":{"row":35,"column":0},"end":{"row":39,"column":5},"action":"remove","lines":["process = PythonOperator(","    task_id='jdsport_pandas',","    python_callable=jdsports_pipeline,","","    )"],"id":10}],[{"start":{"row":34,"column":0},"end":{"row":35,"column":0},"action":"remove","lines":["",""],"id":11},{"start":{"row":33,"column":0},"end":{"row":34,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":49,"column":0},"end":{"row":73,"column":11},"action":"remove","lines":["#extraction from kickgame sport","extract2 = BashOperator(","    task_id='kickgame_extraction',","    bash_command='cd /opt/airflow/fastfashion && scrapy crawl kickgame -o kickgameraw.csv',","    dag=dag","    )","","","process2 = PythonOperator(","    task_id='kickgame_pandas',","    python_callable=jdsports_pipeline,","","    )","    ","","upload2 = PythonOperator(","    task_id = 'kickgame_to_s3',","    python_callable=kickgame_to_s3,","    dag=dag","    )","","delete2 = BashOperator(","    task_id = 'delete_kickgame',","    bash_command = 'cd /opt/airflow/fastfashion && rm -rf kickgameraw.csv',","    dag=dag"],"id":12}],[{"start":{"row":50,"column":4},"end":{"row":50,"column":5},"action":"remove","lines":[")"],"id":13},{"start":{"row":50,"column":0},"end":{"row":50,"column":4},"action":"remove","lines":["    "]},{"start":{"row":49,"column":0},"end":{"row":50,"column":0},"action":"remove","lines":["",""]},{"start":{"row":48,"column":0},"end":{"row":49,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":8,"column":88},"end":{"row":8,"column":89},"action":"insert","lines":[","],"id":14}],[{"start":{"row":8,"column":89},"end":{"row":8,"column":90},"action":"insert","lines":[" "],"id":15},{"start":{"row":8,"column":90},"end":{"row":8,"column":91},"action":"insert","lines":["s"]},{"start":{"row":8,"column":91},"end":{"row":8,"column":92},"action":"insert","lines":["a"]}],[{"start":{"row":8,"column":90},"end":{"row":8,"column":92},"action":"remove","lines":["sa"],"id":16},{"start":{"row":8,"column":90},"end":{"row":8,"column":101},"action":"insert","lines":["sac_to_s3()"]}],[{"start":{"row":8,"column":99},"end":{"row":8,"column":101},"action":"remove","lines":["()"],"id":17}],[{"start":{"row":30,"column":79},"end":{"row":30,"column":80},"action":"remove","lines":["t"],"id":18},{"start":{"row":30,"column":78},"end":{"row":30,"column":79},"action":"remove","lines":["r"]},{"start":{"row":30,"column":77},"end":{"row":30,"column":78},"action":"remove","lines":["o"]},{"start":{"row":30,"column":76},"end":{"row":30,"column":77},"action":"remove","lines":["p"]},{"start":{"row":30,"column":75},"end":{"row":30,"column":76},"action":"remove","lines":["s"]},{"start":{"row":30,"column":74},"end":{"row":30,"column":75},"action":"remove","lines":["d"]},{"start":{"row":30,"column":73},"end":{"row":30,"column":74},"action":"remove","lines":["j"]}],[{"start":{"row":30,"column":79},"end":{"row":30,"column":80},"action":"remove","lines":["v"],"id":19},{"start":{"row":30,"column":78},"end":{"row":30,"column":79},"action":"remove","lines":["s"]},{"start":{"row":30,"column":77},"end":{"row":30,"column":78},"action":"remove","lines":["c"]},{"start":{"row":30,"column":76},"end":{"row":30,"column":77},"action":"remove","lines":["."]},{"start":{"row":30,"column":75},"end":{"row":30,"column":76},"action":"remove","lines":["w"]},{"start":{"row":30,"column":74},"end":{"row":30,"column":75},"action":"remove","lines":["a"]},{"start":{"row":30,"column":73},"end":{"row":30,"column":74},"action":"remove","lines":["r"]},{"start":{"row":30,"column":72},"end":{"row":30,"column":73},"action":"remove","lines":[" "]},{"start":{"row":30,"column":71},"end":{"row":30,"column":72},"action":"remove","lines":["o"]},{"start":{"row":30,"column":70},"end":{"row":30,"column":71},"action":"remove","lines":["-"]},{"start":{"row":30,"column":69},"end":{"row":30,"column":70},"action":"remove","lines":[" "]}],[{"start":{"row":30,"column":68},"end":{"row":30,"column":69},"action":"remove","lines":["t"],"id":20},{"start":{"row":30,"column":67},"end":{"row":30,"column":68},"action":"remove","lines":["r"]},{"start":{"row":30,"column":66},"end":{"row":30,"column":67},"action":"remove","lines":["o"]},{"start":{"row":30,"column":65},"end":{"row":30,"column":66},"action":"remove","lines":["p"]},{"start":{"row":30,"column":64},"end":{"row":30,"column":65},"action":"remove","lines":["s"]},{"start":{"row":30,"column":63},"end":{"row":30,"column":64},"action":"remove","lines":["d"]},{"start":{"row":30,"column":62},"end":{"row":30,"column":63},"action":"remove","lines":["j"]}],[{"start":{"row":30,"column":62},"end":{"row":30,"column":63},"action":"insert","lines":["s"],"id":21},{"start":{"row":30,"column":63},"end":{"row":30,"column":64},"action":"insert","lines":["a"]},{"start":{"row":30,"column":64},"end":{"row":30,"column":65},"action":"insert","lines":["c"]}],[{"start":{"row":37,"column":21},"end":{"row":37,"column":22},"action":"remove","lines":["t"],"id":22},{"start":{"row":37,"column":20},"end":{"row":37,"column":21},"action":"remove","lines":["r"]},{"start":{"row":37,"column":19},"end":{"row":37,"column":20},"action":"remove","lines":["o"]},{"start":{"row":37,"column":18},"end":{"row":37,"column":19},"action":"remove","lines":["p"]},{"start":{"row":37,"column":17},"end":{"row":37,"column":18},"action":"remove","lines":["s"]},{"start":{"row":37,"column":16},"end":{"row":37,"column":17},"action":"remove","lines":["d"]},{"start":{"row":37,"column":15},"end":{"row":37,"column":16},"action":"remove","lines":["j"]}],[{"start":{"row":37,"column":15},"end":{"row":37,"column":16},"action":"insert","lines":["s"],"id":23},{"start":{"row":37,"column":16},"end":{"row":37,"column":17},"action":"insert","lines":["a"]},{"start":{"row":37,"column":17},"end":{"row":37,"column":18},"action":"insert","lines":["c"]}],[{"start":{"row":38,"column":32},"end":{"row":38,"column":33},"action":"remove","lines":["3"],"id":24},{"start":{"row":38,"column":31},"end":{"row":38,"column":32},"action":"remove","lines":["s"]},{"start":{"row":38,"column":30},"end":{"row":38,"column":31},"action":"remove","lines":["_"]},{"start":{"row":38,"column":29},"end":{"row":38,"column":30},"action":"remove","lines":["o"]},{"start":{"row":38,"column":28},"end":{"row":38,"column":29},"action":"remove","lines":["t"]},{"start":{"row":38,"column":27},"end":{"row":38,"column":28},"action":"remove","lines":["_"]},{"start":{"row":38,"column":26},"end":{"row":38,"column":27},"action":"remove","lines":["t"]},{"start":{"row":38,"column":25},"end":{"row":38,"column":26},"action":"remove","lines":["r"]},{"start":{"row":38,"column":24},"end":{"row":38,"column":25},"action":"remove","lines":["o"]},{"start":{"row":38,"column":23},"end":{"row":38,"column":24},"action":"remove","lines":["p"]},{"start":{"row":38,"column":22},"end":{"row":38,"column":23},"action":"remove","lines":["s"]},{"start":{"row":38,"column":21},"end":{"row":38,"column":22},"action":"remove","lines":["d"]},{"start":{"row":38,"column":20},"end":{"row":38,"column":21},"action":"remove","lines":["j"]}],[{"start":{"row":38,"column":20},"end":{"row":38,"column":21},"action":"insert","lines":["s"],"id":25},{"start":{"row":38,"column":21},"end":{"row":38,"column":22},"action":"insert","lines":["a"]},{"start":{"row":38,"column":22},"end":{"row":38,"column":23},"action":"insert","lines":["c"]}],[{"start":{"row":38,"column":20},"end":{"row":38,"column":23},"action":"remove","lines":["sac"],"id":26},{"start":{"row":38,"column":20},"end":{"row":38,"column":31},"action":"insert","lines":["sac_to_s3()"]}],[{"start":{"row":38,"column":29},"end":{"row":38,"column":31},"action":"remove","lines":["()"],"id":27}],[{"start":{"row":43,"column":28},"end":{"row":43,"column":29},"action":"remove","lines":["t"],"id":28},{"start":{"row":43,"column":27},"end":{"row":43,"column":28},"action":"remove","lines":["r"]},{"start":{"row":43,"column":26},"end":{"row":43,"column":27},"action":"remove","lines":["o"]},{"start":{"row":43,"column":25},"end":{"row":43,"column":26},"action":"remove","lines":["p"]},{"start":{"row":43,"column":24},"end":{"row":43,"column":25},"action":"remove","lines":["s"]},{"start":{"row":43,"column":23},"end":{"row":43,"column":24},"action":"remove","lines":["d"]},{"start":{"row":43,"column":22},"end":{"row":43,"column":23},"action":"remove","lines":["j"]}],[{"start":{"row":43,"column":22},"end":{"row":43,"column":23},"action":"insert","lines":["s"],"id":29},{"start":{"row":43,"column":23},"end":{"row":43,"column":24},"action":"insert","lines":["a"]},{"start":{"row":43,"column":24},"end":{"row":43,"column":25},"action":"insert","lines":["c"]}],[{"start":{"row":44,"column":64},"end":{"row":44,"column":65},"action":"remove","lines":["t"],"id":30},{"start":{"row":44,"column":63},"end":{"row":44,"column":64},"action":"remove","lines":["r"]},{"start":{"row":44,"column":62},"end":{"row":44,"column":63},"action":"remove","lines":["o"]},{"start":{"row":44,"column":61},"end":{"row":44,"column":62},"action":"remove","lines":["p"]},{"start":{"row":44,"column":60},"end":{"row":44,"column":61},"action":"remove","lines":["s"]},{"start":{"row":44,"column":59},"end":{"row":44,"column":60},"action":"remove","lines":["d"]},{"start":{"row":44,"column":58},"end":{"row":44,"column":59},"action":"remove","lines":["j"]}],[{"start":{"row":44,"column":58},"end":{"row":44,"column":59},"action":"insert","lines":["s"],"id":31},{"start":{"row":44,"column":59},"end":{"row":44,"column":60},"action":"insert","lines":["a"]},{"start":{"row":44,"column":60},"end":{"row":44,"column":61},"action":"insert","lines":["c"]}],[{"start":{"row":50,"column":28},"end":{"row":50,"column":61},"action":"remove","lines":[">> extract2 >> upload2 >> delete2"],"id":32},{"start":{"row":50,"column":27},"end":{"row":50,"column":28},"action":"remove","lines":[" "]}],[{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"remove","lines":["t"],"id":33},{"start":{"row":29,"column":18},"end":{"row":29,"column":19},"action":"remove","lines":["r"]},{"start":{"row":29,"column":17},"end":{"row":29,"column":18},"action":"remove","lines":["o"]},{"start":{"row":29,"column":16},"end":{"row":29,"column":17},"action":"remove","lines":["p"]},{"start":{"row":29,"column":15},"end":{"row":29,"column":16},"action":"remove","lines":["s"]}],[{"start":{"row":29,"column":14},"end":{"row":29,"column":15},"action":"remove","lines":["d"],"id":34},{"start":{"row":29,"column":13},"end":{"row":29,"column":14},"action":"remove","lines":["j"]}],[{"start":{"row":29,"column":13},"end":{"row":29,"column":14},"action":"insert","lines":["s"],"id":35},{"start":{"row":29,"column":14},"end":{"row":29,"column":15},"action":"insert","lines":["a"]},{"start":{"row":29,"column":15},"end":{"row":29,"column":16},"action":"insert","lines":["c"]}],[{"start":{"row":21,"column":24},"end":{"row":21,"column":30},"action":"remove","lines":["yearly"],"id":36},{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"remove","lines":["@"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":24},"action":"remove","lines":["''"]}],[{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["N"],"id":37},{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"insert","lines":["o"]},{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["n"]},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":41},"end":{"row":8,"column":89},"action":"remove","lines":["dsports_pipeline, jdsport_to_s3, kickgame_to_s3,"],"id":38},{"start":{"row":8,"column":40},"end":{"row":8,"column":41},"action":"remove","lines":["j"]}],[{"start":{"row":8,"column":40},"end":{"row":8,"column":41},"action":"remove","lines":[" "],"id":39}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":40},"end":{"row":8,"column":40},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":133,"mode":"ace/mode/python"}},"timestamp":1727880013965,"hash":"6ccffc87ed1a42deadfad66428318ed34421485e"}