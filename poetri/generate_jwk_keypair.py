#!/usr/bin/env python
from Crypto.PublicKey import RSA
from jwkest.jwk import RSAKey
import json
import sys

__author__ = 'Alan Viars @aviars'


def gen_jwk_keypair(kid):
    # Mint a new RSA key
    _rsakey = RSA.generate(2048)
    # Wrap it in a JWK class
    _rsajwk = RSAKey(kid=kid, use="sig", alg="RS256", key=_rsakey)
    return json.dumps(_rsajwk.serialize(private=True))

# Command line app.
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage:")
        print("generate_poet_keypair.py [KID]")
        print("generate_poet_keypair.py example.com")
        sys.exit(1)
    kid = sys.argv[1]
    result = gen_jwk_keypair(kid=kid)
    print(result)
