import pytest
from fetchr.stream_utils import as_json_of, NotAJSONError

def test_valid_string_json_payload():
    _payload = "addf"
    _json_payload = as_json_of(_payload)
    assert '\"'+_payload+'\"' == _json_payload

def test_valid_dict_payload():
    _payload = {'a': '123', 'b':123}
    _json_payload = as_json_of(_payload)
    assert isinstance(_json_payload, basestring)


def test_valid_int_payload():
    _payload = 123
    _json_payload = as_json_of(123)
    assert isinstance(_json_payload, basestring)


def test_invalid_json_object():
    _payload = set([1,2])
    with pytest.raises(NotAJSONError):
        as_json_of(_payload)
