from etls.jdsports_etl import use_pandas
from etls.helpers import S3Helper
from utils.constants import AWS_BUCKET_NAME

def jdsports_pipeline():
    df = use_pandas('/opt/airflow/fastfashion/jdsportraw.csv')
    write_to = '/opt/airflow/fastfashion/jdsport.csv'
    df.to_csv(write_to, index=False)
    

def jdsport_to_s3():
    write_from = '/opt/airflow/fastfashion/jdsportraw.csv'
    bucket = AWS_BUCKET_NAME
    S3Helper().upload_to_s3(write_from, bucket, 'jdsportraw.csv')



def kickgame_to_s3():
    write_from = '/opt/airflow/fastfashion/kickgameraw.csv'
    bucket = AWS_BUCKET_NAME
    S3Helper().upload_to_s3(write_from, bucket, 'kickgameraw.csv')

def sac_to_s3():
    write_from = '/opt/airflow/fastfashion/sacraw.csv'
    bucket = AWS_BUCKET_NAME
    S3Helper().upload_to_s3(write_from, bucket, 'sacraw.csv')
    