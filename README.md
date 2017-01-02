Fetchr Stream
===================


**Fetchr Stream** is an attempt to have a wrapper library to synchronously push data to data streams. Initial version supports only kinesis and json payload.

----------


How to use
-------------

```python
    from fetchr_stream.kinesis import push_to_stream
    
    status, message = push_to_stream("stream_name", "aws-access-key", "aws-secret-access-key", "payload-key", "json_serializable_payload")
```
