poetri - Pre OAuth Entity Trust Reference Implementation
========================================================


JSON Web Token (JWT) is an open, industry standard (RFC 7519) method for representing 
claims securely between two parties.

Pre-OAuth Entity Trust (POET) is a specific JWT designed to facilitate claims about consumer-facing
health applications. https://github.com/hhsidealab/poet 

This is a reference implementation for signing and verifying POET JWTs in Python2 and Python3.

It contains both libraries and command line utilities.

To install on Ubuntu Linux first install the prerequisites:

    sudo apt-get install python-dev

(The above instruction will differ for iOS, Redhat, Windows, etc.)

To install poetri type:


    git clone https://github.com/TransparentHealth/python-poetri.git
    pip install ./python-poetri
    
    
Command Line Tools
==================

With these tools you can see POET in action and operate as an endorsing body.
Note there are a lot of way to generate keys and work with JWTs. You could use
other tools or roll your own. These methods are provided as a convenience.

Minting a NewKeypair
---------------------

`generate_jwk_keypair.py` mints a new public and private keypair in JWT format.  This file is used to sign JWTs (a.k.a. JWSs).
The only positional command line argument is the key id `kid`. Its output is to standard out `stdout`.


    >generate_jwk_keypair.py example.com

...outputs:


        {"d": "IcyWRDjh5yc8ZCRfgFf11Ia1SJ8b70Sr3AXKtKJ5qQjfkCRw2zJmUl5B-RQaPTGph1x1gxtW3Mgy5ZHfcshBkYpYBJvBPSvaTlCoioSrbdP-BNioYzgHeYoKNwdJf4HTTY1L8VlYojKD2mBZeEC8J18PRjKn75p-DPu-4-q3yOt5cyFsjwogPgxnTAQWMhn1GUYapTw5IxyhrL32vUrCX4GSlwYLiWWVtJn8J-ETrjZIA5qiAOnvB1o6slPd8_QbAbzDhXzdAGa2fK4PDga3Atc6T4I9mGW-gFfcyC4TXfHvz3fWPGjBlehauWofq7PdjDKc2osxFMvcxBMc7ZCKkQ", "alg": "RS256", "p": "41Q3O2oqQ_PdbLOoJ4DKv0xkJInHuqnlYUieXBHfxHghUAN2MlAEm_4sAYI4mSBUCijO7vczSgNePyYmiQZ7wFLImpM1qQQJ1UFPPGXWZOo3-Ytizr02AmLj-L97AQ5PWMMoI__vSBn9oLX63zP_sNs9JPNFjQDCcaMadmq24rU", "n": "zJvhj-TnXGQoL0_GmkJDKxjfNa_-EeQrtzT8anA8DRzpFi5G1lEY2OblKzpkMsp7FP-AG6O6w94hViPHKywJ4SmbnklBDO_cTB49pr0H9QOjUxBAOMMaML-Id5f3dWn06yhgcmLj8bJ8r9ebkA-d0jOEl_PZRdC-3Ugeo2PUYwWsxEwAOCv1eyajee6R-kEqNS7yQ-EdwqtB-BhG736g_iIni1f56ydVuDPWACnoH_Szvsa7dqSRU5-nIQkOaf1G1K8WIifaK7K1-qMULK2DB96ZoE-a3bkT-TexzEahEakvpNbrZuFDw3zkmnZOW9Qd1kiSoCmNCXJoBsQywtFxrw", "kty": "RSA", "kid": "example.com", "use": "sig", "e": "AQAB", "q": "5moZ-njQkowMIEzW_L-8tvm9_S2RyaUZMLiQrYsnBwi5VPBu19dEOwXZdua3SjEAwfHYEvnW9ghjB93JNl2Lq7stoTK26-8-xwK21aWA-LeV82VDgfSjofjs7WcnMjJsqwHZxpeiV0EG73qegBc9n9HZIWkqSYdFFuGn6jPvzVM"}
    
...or even better, redirect the output to a new file:

        
        >generate_jwk_keypair.py example.com > keypair.jwk

Key your private key safe!



Creating a Public Key from the Keypair:
---------------------------------------

`generate_public_jwk.py` create a public only JWK.  This is the public key that is hosted at https://[iss]/.well-known/poet.jwk
and is used to verify signatures on JWTs (a.k.a. JWKs).  Its only positional argument is the keypair file.
It outputs the public JWK to standard out `stdout`

    generate_public_jwk.py keypair.jwk
    >{
    "alg": "RS256",
    "kty": "RSA",
    "kid": "example.com",
    "e": "AQAB",
    "n": "zJvhj-TnXGQoL0_GmkJDKxjfNa_-EeQrtzT8anA8DRzpFi5G1lEY2OblKzpkMsp7FP-AG6O6w94hViPHKywJ4SmbnklBDO_cTB49pr0H9QOjUxBAOMMaML-Id5f3dWn06yhgcmLj8bJ8r9ebkA-d0jOEl_PZRdC-3Ugeo2PUYwWsxEwAOCv1eyajee6R-kEqNS7yQ-EdwqtB-BhG736g_iIni1f56ydVuDPWACnoH_Szvsa7dqSRU5-nIQkOaf1G1K8WIifaK7K1-qMULK2DB96ZoE-a3bkT-TexzEahEakvpNbrZuFDw3zkmnZOW9Qd1kiSoCmNCXJoBsQywtFxrw",
    "use": "sig"
    }


...or redirect it to a file..
 
 
    > generate_public_jwk.py keypair.jwk > poet.jwk


Signing a JWT:
--------------

You'll need to add necessary information an claims into JSON document that represent your desired payload in your JWT.
You will supply the private key for signing.  The utility sets the `iat` (issued at), `exp` (expiration) and `iss` (issuer) based on the
system clock and your input. It has 3 required command line arguments; `payload`, `keypair`, and `issuer`. `expiation`
is optional and defaults to 31536000 (one year from now.)


    >sign_poet_jwk.py ../tests/payload.json keypair.jwk  example.com  315360
    eyJhbGciOiJSUzI1NiIsImtpZCI6ImV4YW1wbGUuY29tIiwidHlwIjoiSldUIn0.eyJ0b2tlbl9lbmRwb2ludF9hdXRoX21ldGhvZCI6ImNsaWVudF9zZWNyZXRfYmFzaWMiLCJpc3MiOiJleGFtcGxlLmNvbSIsImNsaWVudF91cmkiOiJodHRwczovL2FwcHMtZHN0dTIuc21hcnRoZWFsdGhpdC5vcmcvY2FyZGlhYy1yaXNrLyIsImluaXRpYXRlX2xvZ2luX3VyaSI6Imh0dHBzOi8vYXBwcy1kc3R1Mi5zbWFydGhlYWx0aGl0Lm9yZy9jYXJkaWFjLXJpc2svbGF1bmNoLmh0bWwiLCJzb2Z0d2FyZV9pZCI6IjROUkIxLTBYWkFCWkk5RTYtNVNNM1IiLCJyZWRpcmVjdF91cmlzIjpbImh0dHBzOi8vYXBwcy1kc3R1Mi5zbWFydGhlYWx0aGl0Lm9yZy9jYXJkaWFjLXJpc2svIl0sImdyYW50X3R5cGVzIjpbImF1dGhvcml6YXRpb25fY29kZSJdLCJjbGllbnRfbmFtZSI6IkNhcmRpYWMgUmlzayBBcHAiLCJleHAiOjE1NjM2NTY3NTcsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgcGF0aWVudC8qLnJlYWQiLCJpYXQiOjE1MDA1ODQ3NTcsImxvZ29fdXJpIjoiaHR0cHM6Ly9nYWxsZXJ5LnNtYXJ0aGVhbHRoaXQub3JnL2ltZy9hcHBzLzY2LnBuZyJ9.GVRUGPLo_jpq3_yBBJmNmxNb6Wk9ZLhGxjRcynP7VAgQ_QlECLlR8fQWDhtwU0e33Ev0MlGKF1OB-xh5Kc3JBkX2qrtUotA1H-MsNmxhhmL1fXg4fV1R2wa6hcqcSjM1zP1iNhzLIPbbsXtq27qDivN6D5pJzrkFIOdvg1lgvmeZxttYndqpn3SUEsdwBLxi66-OWyiPeFdigAfJAtf8EyHk0picgkJZrjK0Zoa3H-Wvwa88fWYGTeFxBpjET7G2nGXdcRNKVgQ-0SDJoasJSM5uoqbJAO7A1h0zpNdFpRY9pjtem4FnN_6LLpZp8b0J0PFXaXqOAxeyU7UFTNiqOw
    
...redirect it to a file...


    >sign_poet_jwk.py ../tests/payload.json keypair.jwk  example.com  315360 > 4NRB1-0XZABZI9E6-5SM3R.jws
    

Now `4NRB1-0XZABZI9E6-5SM3R.jws` hold the endorsement that you can distribute.

Verifying a JWT
--------------
`verify_jws_with_jwk.py`  verifies the signature on a JWS using the public key.
It has two positional arguments; the `jws` and the public `jwk` and if the JWS
signature is verified, then it outputs the JWK's payload to standard out `stdout`.


    >verify_jws_with_jwk.py ./4NRB1-0XZABZI9E6-5SM3R.jws poet.jwk
    {
    "scope": "openid profile patient/*.read",
    "initiate_login_uri": "https://apps-dstu2.smarthealthit.org/cardiac-risk/launch.html",
    "exp": 1563657181,
    "iss": "example.com",
    "software_id": "4NRB1-0XZABZI9E6-5SM3R",
    "token_endpoint_auth_method": "client_secret_basic",
    "client_name": "Cardiac Risk App",
    "logo_uri": "https://gallery.smarthealthit.org/img/apps/66.png",
    "client_uri": "https://apps-dstu2.smarthealthit.org/cardiac-risk/",
    "redirect_uris": [
        "https://apps-dstu2.smarthealthit.org/cardiac-risk/"
    ],
    "iat": 1500585181,
    "grant_types": [
        "authorization_code"
    ]
    }
    
If the key doesn't match, then you'll get an error instead of the payload.

Hey where did you get that public key used in the last step?  How do you know it's really from `example.com`?
You don't unless you fetch it from `example.com` to prove its provenance.  Let's give that a shot.


`verify_jws_with_jwk_url.py` attempts to get the public key from the well-known URL in the POET specification.
It has one required, positional argument, the `jws` and outputs the payload to stdout if the key is found and the signature matches.
An error is returned if not. The well-known URL is derived from the `iss` field in the payload and the details of the POET specification.     
    

    >verify_jws_with_jwk_url.py 4NRB1-0XZABZI9E6-5SM3R.jws
    The key could not be fetched

That's exactly what we would expect to happen.  For this command to run as expected, I would need to place and make public the file `poet.jwk` at
https://example.com/.well-known/poet.jwk.  Since I do not have control over that domain or its website, I cannot impersonate example.com's signature.


Python Library
==============

All of the above functionality is accessible directly in Python as a module.  More documentation is on the way.  For now, the best source of information and
examples can be found in the tests.

