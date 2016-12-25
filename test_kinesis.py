from fetchr.kinesis import push_to_erp_stream
from fetchr.stream_utils import NotAJSONError
from moto import mock_kinesis

import pytest
import sure
import boto3

@mock_kinesis
def test_invalid_payload_key():
    is_success, message = push_to_erp_stream("Sample", "some-access-key", "secret-access-key", 1234, "1234")
    assert is_success == False

@mock_kinesis
def test_invalid_payload():
    with pytest.raises(NotAJSONError):
        push_to_erp_stream("Sample", "some-access-key", "secret-access-key", "1234", set([1,2,3]))

@mock_kinesis
def test_invalid_streamname():
    is_success, message = push_to_erp_stream("sample", "some-access-key", "secret-access-key", "1234", {"a":123,"b":456})
    assert is_success == False


@mock_kinesis
def test_valid_streampush():
    _kinesis = boto3.client("kinesis", region_name="ap-southeast-1")
    _kinesis.create_stream(StreamName="sample-stream", ShardCount=2)
    is_success, message = push_to_erp_stream("sample-stream", "some-access-key", "secret-access-key", "1234", {"a":123,"b":456})
    assert is_success == True
