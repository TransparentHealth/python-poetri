#!/usr/bin/env python
from jwkest.jwk import RSAKey
import json
import sys
from collections import OrderedDict

__author__ = 'Alan Viars @aviars'


def gen_public(private_key_jwk):
    rsak = RSAKey(**private_key_jwk)
    return(rsak.serialize())


# Command line app.
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage:")
        print("generate_public_jwk.py [JWK_KEYPAIR_FILE_PATH]")
        print("generate_public_jwk.py my.jwk")
        sys.exit(1)
    my_jwk_file = sys.argv[1]
    my_jwk_fh = open(my_jwk_file)

    try:
        k = my_jwk_fh.read()
        my_jwk = json.loads(k, object_pairs_hook=OrderedDict)
    except ValueError:
        print("Error parsing the JWK.", str(sys.exc_info()))
        exit(1)

    result = gen_public(my_jwk)
    my_jwk_fh.close()
    print(json.dumps(result, indent=4))
