import json


def get_json_from_s3_obj(file_s3_obj):
    file_content = file_s3_obj.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    print(json_content)

    return json_content


def get_json_val_or_none(obj, key):
    return obj[key] if key in obj else None


def extract_date_time_from_str(date_time_str: str):
    return date_time_str.split('result-')[-1]
