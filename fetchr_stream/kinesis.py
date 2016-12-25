from stream_utils import as_json_of, get_uuid
from botocore.exceptions import ClientError

import boto3
import json
import logging
import traceback

logger = logging.getLogger(__name__)

def _is_success_put_response(_put_response):

    if "ResponseMetadata" in _put_response and \
        "HTTPStatusCode" in _put_response["ResponseMetadata"] and \
            _put_response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return True

    return False

def push_to_erp_stream(stream_name, access_key_id, secret_access_key, payload_key, payload, region="ap-southeast-1"):
    if not isinstance(payload_key, basestring):
        return False, "Payload key should be a string"

    json_payload = as_json_of(payload)
    try:
        _kinesis = boto3.client("kinesis", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key, region_name=region)
        _stream_payload = { "key": payload_key, "payload": payload }
        _put_response = _kinesis.put_record(StreamName=stream_name, Data=json.dumps(_stream_payload), PartitionKey=get_uuid())
        return _is_success_put_response(_put_response), _put_response
    except ClientError:
        logger.exception("Kinesis push exception")
        return False, "Error while pushing to kinesis"
