from pyspark.sql import SparkSession, DataFrame #from pandas import DataFrame
from pyspark.sql.types import *
from pyspark.sql.functions import regexp_replace, col
from config import configuration


#Entrypoint


def spark_session(app_name) -> SparkSession:
    '''Create a spark session
        - assign an app to it
        - configure the session with the necessary jars
    '''
    spark = SparkSession.builder.appName(app_name)\
    .config("spark.jars.packages",
            "org.apache.hadoop:hadoop-aws:3.3.1,com.amazonaws:aws-java-sdk:1.11.469")\
    .config("spark.hadoop.fs.s3a.impl", 
            "org.apache.hadoop.fs.s3a.S3AFileSystem")\
    .config("spark.hadoop.fs.s3a.access.key", configuration.get("AWS_ACCESS_KEY_ID"))\
    .config("spark.hadoop.fs.s3a.secret.key", configuration.get("AWS_SECRET_ACCESS_KEY"))\
    .config("spark.hadoop.fs.s3a.aws.credentials.provider","org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")\
    .config("spark.hadoop.fs.s3a.committer.name", "partitioned")\
    .config("spark.hadoop.fs.s3a.committer.magic.enabled", "true")\
    .config("spark.hadoop.fs.s3a.committer.magic.path", f"s3a://{configuration.get('AWS_BUCKET_NAME')}/staging/")\
    .getOrCreate()
    
    #Log level
    spark.sparkContext.setLogLevel('WARN')
    
    return spark

def regex_col_clean(df: DataFrame, column_to_clean, char_to_remove, replace_with, output_dtype):
    cleaned_df = df.withColumn(column_to_clean, regexp_replace(col(column_to_clean), char_to_remove, replace_with).cast(output_dtype))
    return cleaned_df
    
def write_to_s3(df: DataFrame, output_loc):
    return (df.coalesce(1).write.format('csv').save(f"s3a://{configuration.get('AWS_BUCKET_NAME')}/{output_loc}"))
    


    

df = spark_session('S3DataProcessor').read.format('csv').option("header", "true").load(f"s3a://{configuration.get('AWS_BUCKET_NAME')}/*.csv")
cleaned_df = regex_col_clean(df, 'price', '£', '', 'float')
write_to_s3(cleaned_df, 'output/composite-output.csv')
cleaned_df.show()

