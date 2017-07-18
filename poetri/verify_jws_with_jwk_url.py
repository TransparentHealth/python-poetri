#!/usr/bin/env python
import sys
import json
from collections import OrderedDict
from jwkest.jws import JWS
from jwkest.jwk import RSAKey
from jwkest import BadSignature
import requests


def verify_poet_via_url(my_jws, issuer, secure=True):

    # Fetch the public key
    
    if secure: 
        url = "https://%s/.well-known/poet.jwk" % (issuer)
    else:
        url = "http://%s/.well-known/poet.jwk" % (issuer)
    
    r = requests.get(url)
    
    if r.status_code != 200:
        print("The key could not be fetched.")
        exit(1)

    # load the Signed JWT (JWS)
    my_jws = my_jws.rstrip().lstrip()
    signed_token = JWS(my_jws)

    # load the JWK into an RSA Key structure
    rsak = RSAKey(**r.json())
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
        print("verify_jws_with_jwk_url.py [JWT_FILE_PATH] [JWK_ISSUER]")
        print("Example: verify_jws_with_jwk_url.py my.jwt  example.com")
        sys.exit(1)

    my_jwt_file = sys.argv[1]
    issuer = sys.argv[2]
    jwt_fh = open(my_jwt_file)

    result = verify_poet_via_url(jwt_fh.read(), issuer, secure=False)
    result = json.dumps(result, indent=4)
    jwt_fh.close()
    print(result)
