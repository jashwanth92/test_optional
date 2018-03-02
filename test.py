import boto3
from flask import Flask,request
import boto3
import subprocess
import json
import config
from botocore.exceptions import ClientError



def keys():
    account = './qpair.sh'
    account_output = subprocess.check_output([account])
    account_result = json.loads(account_output)

    for key,value in account_result.iteritems():

        if key == 'Credentials':
           keys = value

           for key,value in keys.iteritems():
                if key == 'SecretAccessKey':
                   seckey = value

                if key == 'AccessKeyId':
                   acekey = value

                if key == 'SessionToken':
                   session_token = value
    print seckey
    return seckey,acekey,session_token


keys()
