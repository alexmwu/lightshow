import logging
import boto3
from datetime import datetime
from random import *
from botocore.exceptions import ClientError
import json

# Initialized DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tableName = "UserPrefs"

iot = boto3.client('iot-data', region_name='us-east-1')

# initialize the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_user_prefs(event, context):
    global dynamodb
    global tableName
    global topic

    logger.info("Fetching user prefs")
    logger.info(event)
    userId = event["user"]
    table = dynamodb.Table(tableName)

    try:
        response = table.get_item(
            Key={
                'userId': userId
            }
        )
    except ClientError as e:
        logger.error(e.response['Error']['Message'])
        return
    else:
        item = response
        logger.info("GetItem succeeded:")

    userPrefs = item['Item']['preferencesBlob']
    publish_prefs_to_topic(userPrefs)
    return userPrefs

def publish_prefs_to_topic(userPrefs):
    global iot
    response = iot.publish(
        topic='play',
        qos=0,
        payload=json.dumps(userPrefs))
    logger.info('publish response')
    logger.info(response)

