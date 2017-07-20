#!/usr/bin/env python
import sys
import json
from jwkest.jws import JWS, NoSuitableSigningKeys
from jwkest.jwt import JWT
from jwkest.jwk import RSAKey, DeSerializationNotPossible
from jwkest import BadSignature
import requests

__author__ = 'Alan Viars @aviars'


def verify_poet_via_url(my_jws):

    # load the Signed JWT (JWS)
    my_jws = my_jws.rstrip().lstrip()
    signed_token = JWS(my_jws)

    # create aplain old JWT so we can fish out the 'iss'
    t = JWT()
    unpacked = t.unpack(token=my_jws)
    payload = unpacked.payload()
    if "iss" not in payload:
        print("Missing 'iss' claim in the JWS payload.")
        exit(1)
    else:
        iss = payload['iss']

    # Fetch the public key from iss

    url = "https://%s/.well-known/poet.jwk" % (iss)
    r = requests.get(url)

    if r.status_code != 200:
        print("The key could not be fetched.")
        exit(1)

    # load the JWK into an RSA Key structure
    rsak = RSAKey(**r.json())
    try:
        vt = signed_token.verify_compact(signed_token.msg, keys=[rsak])
        retval = vt
    except BadSignature:
        retval = {"error": "The signature did not match"}
    except NoSuitableSigningKeys:
        retval = {"error": str(sys.exc_info()[1])}
    except DeSerializationNotPossible:
        retval = {"error": str(sys.exc_info()[1])}
    except:
        retval = {"error": str(sys.exc_info())}
    return retval

# command line app.
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage:")
        print("verify_jws_with_jwk_url.py [JWT_FILE_PATH]")
        print("Example: verify_jws_with_jwk_url.py my.jwt")
        sys.exit(1)

    my_jwt_file = sys.argv[1]
    jwt_fh = open(my_jwt_file)

    result = verify_poet_via_url(jwt_fh.read())
    result = json.dumps(result, indent=4)
    jwt_fh.close()
    print(result)
