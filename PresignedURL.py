import boto3
import os
from datetime import datetime


import requests

foldername = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
s3= boto3.client('s3')
file_name1=foldername+'/'+'report.html'
file_name2=foldername+'/'+'log.html'
bucket_name = "occ-ui-automation-results"
directory_name = foldername #it's name of your folders
url = s3.generate_presigned_url('put_object', Params={'Bucket':bucket_name,'Key':file_name1,'ACL': 'public-read'}, ExpiresIn= 3600, HttpMethod='PUT')
urllog = s3.generate_presigned_url('put_object', Params={'Bucket':bucket_name,'Key':file_name2,'ACL': 'public-read'}, ExpiresIn= 3600, HttpMethod='PUT')
print(url)
file = os.path.abspath("report.html")
file1 = os.path.abspath("log.html")
files = {foldername: open(file, 'r', encoding='utf-8')}
files1 = {foldername: open(file1, 'r', encoding='utf-8')}
headers = {
    'x-amz-acl': 'public-read'
}
response = requests.put(url, files=files,headers=headers)
print(response.text)
print(response.status_code)
response = requests.put(urllog, files=files1,headers=headers)
print(response.text)
print(response.status_code)
Sysadmin_ReportUrl= f'https://{bucket_name}.s3.us-west-2.amazonaws.com/{foldername}/report.html'
print(Sysadmin_ReportUrl)
Sysadmin_logUrl= f'https://{bucket_name}.s3.us-west-2.amazonaws.com/{foldername}/log.html'
print(Sysadmin_logUrl)
