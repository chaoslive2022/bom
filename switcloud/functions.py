import json
import base64

def attempt_json_deserialize(data, expect_type=None):
    try:
        data = json.loads(data)
    except (TypeError, json.decoder.JSONDecodeError): pass

    if expect_type is not None and not isinstance(data, expect_type):
        raise ValueError(f"Got {type(data)} but expected {expect_type}.")

    return data

def get_credentials(client_id, secret):
    """Example for oauth2 client credential computing""" 
    
    #client_id = "hAMq7bi1HXIKUvMe7Se8wMRyKXC7rXKucp2v3Z9C"
    #secret = "35NwiIHeDd05XGQYgk73NgsCnDnKZN9vMyZPzmpTYuVnBII4ZP5RBgCeFGY62PVuRtm6fU1zMjbfrMe0MAw30AuMe57DI0nnlaflx2SzgyEl9BHagw73WTe0C1smV4Oh"
    credential = "{0}:{1}".format(client_id, secret)
    
    return base64.b64encode(credential.encode("utf-8"))

