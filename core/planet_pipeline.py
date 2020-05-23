import boto3


class PlanetPipeline:
    def __init__(self):
        pass

    def put_payload(self):
        s3_resource = boto3.resource('s3')
        buckets = s3_resource.Bucket('interview-pipeline2.upside-services.com')
        for my_bucket_object in buckets.objects.all():
            print(my_bucket_object)
        pass

    def get_result(self, name: str):
        pass
