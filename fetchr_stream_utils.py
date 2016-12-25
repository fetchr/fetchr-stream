import json
import uuid

from exceptions import Exception

class NotAJSONError(Exception):
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = args[0]

        super(NotAJSONError, self).__init__(self.message)

def as_json_of(payload):
    try:
        json_payload = json.dumps(payload)
    except:
        raise NotAJSONError("Unable to convert the payload as json - {}".format(payload))

    return json_payload

def get_uuid():
    return uuid.uuid4().get_hex()

