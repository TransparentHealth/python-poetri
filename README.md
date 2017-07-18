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

The command line tools are  `sign_poet_jwk.py`, `verify_poet_jwk.py`, `verify_jws_with_jwk.py`
and `verify_jws_with_jwk_url`. Just type their name for usage info.


More help is on the way......