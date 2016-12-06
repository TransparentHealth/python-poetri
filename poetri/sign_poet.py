#!/usr/bin/env python
import jwt
import json, sys, time
from cryptography.hazmat.backends import default_backend
from collections import OrderedDict

def sign_poet(payload, private_key_string, issuer, expires=63072000):
    
    
    #Set the headers
    headers= OrderedDict()
    headers["typ"]="JWT"
    headers["alg"]="RS256"
    
    # Add/overwrite payload
    payload["iss"] = issuer
    payload["iat"] = int(time.time())
    
    
    #Set to expire (two years is default)
    payload["exp"] = payload["iat"] + expires
    jwt_encoded = jwt.encode(payload, private_key_string, algorithm='RS256', headers=headers)
    # Adding a decode in the return. Otherwise returns b'bytestring
    return jwt_encoded.decode('utf-8')

#Command line app.
if __name__ == "__main__":


    if len(sys.argv) not in (4,5):
        print("Usage:")
        print("sign_poet.py [PAYLOAD_JSON_FILE] [SIGNING_PRIVATE_PEM_CERTIFICATE_FILE] [ISSUER] [SECONDS_UNTIL_EXPIRY]")
        print("Example: sign_poet.py mypayload.json my-certificate.pem example.org 31536000")
        print("Note: 31536000 is one year from now.")
        sys.exit(1)

    my_payload_file         = sys.argv[1]
    my_private_key_file     = sys.argv[2]
    issuer                  = sys.argv[3]
    if sys.argv==5:
        expires             = sys.argv[4]
    else:
        expires = 63072000
    my_payload_fh = open(my_payload_file)
    my_private_key_fh = open(my_private_key_file)
        
    #convert json to dict
    try:
        j = my_payload_fh.read()
    
        
        my_payload = json.loads(j, object_pairs_hook=OrderedDict)
        if type(my_payload) ==type({}):
            result = sign_poet(my_payload, my_private_key_fh.read(), issuer, expires)
        else:
            result = "JSON was not an object {}"
    except ValueError:
        result = ["Error parsing JSON", str(sys.exc_info())]
        
    
    my_payload_fh.close()        
    my_private_key_fh.close()
    
    print(result)
