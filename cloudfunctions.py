import boto3

def put_file_to_server(name_of_file: str):
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://tochkateststorage.storage.yandexcloud.net',
        aws_access_key_id = "YCAJEA8dSV5_-ldxhVO_MRtv5",
        aws_secret_access_key = "YCOlMQlCHt98u4V_53yVFTujzV5fsHAGD_LyVLvD"
    )

    s3.upload_file(name_of_file, 'tochkateststorage', name_of_file)

# # Получить список объектов в бакете
# for key in s3.list_objects(Bucket='bucket-name')['Contents']:
#     print(key['Key'])
#
# # Удалить несколько объектов
# forDeletion = [{'Key':'object_name'}, {'Key':'script/py_script.py'}]
# response = s3.delete_objects(Bucket='bucket-name', Delete={'Objects': forDeletion})
#
# # Получить объект
# get_object_response = s3.get_object(Bucket='bucket-name',Key='py_script.py')
# print(get_object_response['Body'].read())
