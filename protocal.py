import json


def encode_message(message_type, data):
    return json.dumps({"type": message_type, "data": data}).encode('utf-8')


def decode_message(message):
    return json.loads(message.decode('utf-8'))
