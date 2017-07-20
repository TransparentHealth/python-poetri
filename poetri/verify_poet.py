#!/usr/bin/env python
__author__ = 'Alan Viars @aviars'
import jwt
import sys
from cryptography.x509 import load_pem_x509_certificate, OID_COMMON_NAME
from cryptography.hazmat.backends import default_backend
from collections import OrderedDict

def verify_poet(jws, public_key_string):
    python_version = sys.version_info.major
    #print("jws:", jws)
    #print("Public_key_string:", public_key_string)
    jws = jws.rstrip().lstrip()
    
    #print(sys.version_info)

    certBytes = list(public_key_string.encode())
    
    if python_version == 3:    
        certBytes = bytes(certBytes)
    
    certificate = load_pem_x509_certificate(certBytes, default_backend())
    publicKey = certificate.public_key()
    
    cn = certificate.subject.get_attributes_for_oid(OID_COMMON_NAME)[0].value
    try:
        payload = jwt.decode(jws, publicKey, algorithms=['RS256'])
    except jwt.exceptions.ExpiredSignatureError:
        payload = """{"error":"EXPIRED"}"""
    
    if payload.get('iss', ''):
        if payload['iss']!=cn:
            payload = """{"error":"The CN (Common Name) in the public certificate did not match the iss (Issuer) in the JWT payload."}"""    
    else:
        payload = """{"error":"iss (Issuer) was not found in the payload."}"""
    return payload

#command line app.
if __name__ == "__main__":

    if len(sys.argv)!=3:
        print("Usage:")
        print("verify_poet.py [ENCODED_JWT_FILE] [PUBLIC_CERT_FILE]")
        print("Example: verify_poet.py my.jwt my_public_cert.pem")
        sys.exit(1)
    
    jwt_path = sys.argv[1]
    public_key_path = sys.argv[2]
    
    jwt_fh = open(jwt_path)
    public_key_fh = open(public_key_path)
    jws = jwt_fh.read()
    payload = verify_poet(jws, public_key_fh.read())

    print(payload)

    public_key_fh.close()
    jwt_fh.close()
