#!/usr/bin/env python
from jwkest.jws import JWS
from jwkest.jwk import RSAKey
import json
import sys
import time
from collections import OrderedDict

__author__ = 'Alan Viars @aviars'


def sign_poet(payload, private_key_jwk, issuer, expires=63072000):

    # Set the headers
    headers = OrderedDict()
    headers["typ"] = "JWT"
    headers["alg"] = "RS256"

    # Add/overwrite payload
    payload["iss"] = issuer
    payload["iat"] = int(time.time())

    # Set to expire (two years is default)
    payload["exp"] = payload["iat"] + expires
    rsak = RSAKey(**private_key_jwk)
    my_jws = JWS(payload, alg="RS256", typ="JWT")
    return(my_jws.sign_compact([rsak]))

# Command line app.
if __name__ == "__main__":

    if len(sys.argv) not in (4, 5):
        print("Usage:")
        print(
            "sign_poet_jwk.py [PAYLOAD_JSON_FILE] [JWK_KEYPAIR_FILE_PATH] [ISSUER] [SECONDS_UNTIL_EXPIRY]")
        print("Example: sign_poet_jwk.py mypayload.json my-certificate.pem example.org 31536000")
        print("Note: 31536000 is one year from now.")
        sys.exit(1)

    my_payload_file = sys.argv[1]
    my_jwk_file = sys.argv[2]
    issuer = sys.argv[3]
    if sys.argv == 5:
        expires = sys.argv[4]
    else:
        expires = 63072000
    my_payload_fh = open(my_payload_file)
    my_jwk_fh = open(my_jwk_file)

    # convert json to dict
    try:
        p = my_payload_fh.read()
        my_payload = json.loads(p, object_pairs_hook=OrderedDict)
    except ValueError:
        result = ["Error parsing the JSON Payload", str(sys.exc_info())]
    try:
        k = my_jwk_fh.read()
        my_jwk = json.loads(k, object_pairs_hook=OrderedDict)
    except ValueError:
        result = ["Error parsing the JWK.", str(sys.exc_info())]

    result = sign_poet(my_payload, my_jwk, issuer, expires)

    my_payload_fh.close()
    my_jwk_fh.close()

    print(result)
