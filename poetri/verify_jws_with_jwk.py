#!/usr/bin/env python
import sys
import json
from collections import OrderedDict
from jwkest.jws import JWS
from jwkest.jwk import RSAKey, DeSerializationNotPossible
from jwkest import BadSignature

__author__ = 'Alan Viars @aviars'


def verify_poet(my_jws, my_jwk_dict):

    # load the Signed JWT (JWS)
    my_jws = my_jws.rstrip().lstrip()
    signed_token = JWS(my_jws)

    # load the JWK
    rsak = RSAKey(**my_jwk_dict)
    try:
        vt = signed_token.verify_compact(signed_token.msg, keys=[rsak])
        retval = vt
    except BadSignature:
        retval = {"error": "The signature did not match"}
    except:
        retval = {"error": str(sys.exc_info())}
    return retval

# command line app.
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage:")
        print("verify_jws_with_jwk.py [JWT_FILE_PATH] [JWK_PUBLIC_FILE_PATH]")
        print("Example: verify_jws_with_jwk.py my.jwt  public.jwk")
        sys.exit(1)

    my_jwt_file = sys.argv[1]
    my_jwk_file = sys.argv[2]
    jwt_fh = open(my_jwt_file)
    jwk_fh = open(my_jwk_file)

    # Ensure JWK is a JSON object
    try:
        k = jwk_fh.read()
        my_jwk_dict = json.loads(k, object_pairs_hook=OrderedDict)
    except ValueError:
        print("Error parsing the JWK.", str(sys.exc_info()))
        exit(1)

    result = verify_poet(jwt_fh.read(), my_jwk_dict)
    result = json.dumps(result, indent=4)
    jwt_fh.close()
    jwk_fh.close()
    print(result)
