poetri
======

A reference implementation of POET https://github.com/hhsidealab/poet 
in Python2 and Python3.

The library signs and verifies POET JWTs.  The libraries double as 
command line tools with near-identical functionality.


To install the prerequisites on Ubuntu:


    sudo apt-get install libssl-dev

The above will varry for iOS, Redhat, etc.

To install type:


    git clone https://github.com/TransparentHealth/python-poetri.git
    python python-poetri/setup.py install

Now try out the command line tools `verify_poet.py` and `sign_poet.py`. Just type their name for usage info.

If you want a payload or header file as a sample then try `sample_payload_poet.py info`.

Stay tuned for more....

