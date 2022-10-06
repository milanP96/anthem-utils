# import boto3
import os
import json
import requests

class AnthemEnv:

    def __init__(self):
        pass
#         s3_client = boto3.resource(
#             service_name='s3',
#             region_name=os.getenv('AWS_S3_REGION_NAME'),
#             aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
#             aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
#         )
#
#         env_key = os.getenv('ENV_KEY')
#
#         env_obj = s3_client.Object('anthem-envs', env_key)
#         body = env_obj.get()['Body'].read().decode('utf-8')
#
#         env_json = json.loads(body)
#
#         self._values = env_json
#
#     def get(self, key):
#         return self._values.get(key, None)
