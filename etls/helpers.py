import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_BUCKET_NAME, AWS_REGION

class S3Connection:
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
    
    def connect(self):
        try:
            s3 = s3fs.S3FileSystem(anon=False, key=self.key, secret=self.secret)
            return s3
        except Exception as e:
            print(e)

class S3Helper(S3Connection):
    def __init__(self):
        super().__init__(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
        
    def create_bucket_if_not_exist(self, s3: s3fs.S3FileSystem, bucket: str):
        try:
            if not s3.exists(bucket):
                s3.mkdir(bucket)
                return 'Bucket Created'
            else:
                return 'Bucket already exists'
        except Exception as e:
            return {'Exception': e}
        
   
    def upload_to_s3(self, file_path:str, bucket: str, file_name: str):
        s3 = self.connect()
        #Check if bucket exists
        status = self.create_bucket_if_not_exist(s3, bucket)
        if 'Exception' not in status:
            try:
                s3.put(file_path, f"{bucket}/{file_name}")
                print(f'File uploaded to S3 bucket {bucket}')
            except Exception as e:
                print(e)
    