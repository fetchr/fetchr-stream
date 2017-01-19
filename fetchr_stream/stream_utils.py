import json
import uuid
import netifaces
from datetime import datetime

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


def get_current_time_as_string():
    return datetime.now().strftime("%Y-%m-%d %M:%H:%S")

def get_ips():
    interfaces = filter(lambda ifs: ifs != 'lo', netifaces.interfaces())
    proto = netifaces.AF_INET
    ips = [netifaces.ifaddresses(interface) for interface in interfaces]
    inet_addrs = [addr[proto] for addr in ips if proto in addr]