import json

import boto3

from helpers.parsers import get_json_from_s3_obj
from helpers.waiter import wait_until
from models.file_model import FileModel


class PlanetPipeline:
    BUCKET_BASE_PATH = 'interview-pipeline2.upside-services.com'
    INPUT_PATH = 'input'
    RESPONSE_PATH = 'response/sbx_user1051'

    def __init__(self):
        self.s3_resource = boto3.resource('s3')
        self.bucket = self.s3_resource.Bucket(self.BUCKET_BASE_PATH)

    def put_payload(self, file_name: str, payload_obj):
        file_path = f'{self.INPUT_PATH}/{file_name}'
        s3_object = self.bucket.Object(key=file_path)
        s3_object.put(Body=json.dumps(payload_obj))

    def get_result_model(self, file_name: str):
        file_s3_obj = self._find_latest_file_obj(file_name)

        return FileModel(file_s3_obj)

    def get_result_json(self, file_name: str):
        file_s3_obj = self._find_latest_file_obj(file_name)
        json_content = get_json_from_s3_obj(file_s3_obj)

        return json_content

    def delete_all_files(self):
        self._delete_files_from_folders([self.INPUT_PATH, self.RESPONSE_PATH])

    def print_all_from_bucket(self):
        for my_bucket_object in self.bucket.objects.all():
            print(my_bucket_object)

    def _delete_files_from_folders(self, prefix_of_folders: [str]):
        for p in prefix_of_folders:
            for key in self.bucket.objects.filter(Prefix=p):
                key.delete()
                print(f'"{key.key}" deleted')

    def _find_latest_file_obj(self, file_name: str):
        file_path = f'{self.RESPONSE_PATH}/{file_name}-result-'

        s3_search_predicate = lambda: list(self.bucket.objects.filter(Prefix=file_path))
        obj_list = wait_until(predicate=s3_search_predicate, error_msg=f'File "{file_name}" was not found.')
        latest_file_obj = obj_list[-1]

        return latest_file_obj
