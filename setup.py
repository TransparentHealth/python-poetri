import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name="poetri",
      version="0.0.4",
      description="Pre-OAuth Entity Trust Reference Implementation",
      long_description="""Command line tools and libraries for signing and verifying JWTs according to https://github.com/TransparentHealth/poet.""",
      author="Alan Viars",
      author_email="sales@videntity.com",
      url="https://github.com/transparenthealth/python-poetri",
      download_url="https://github.com/transparenthealth/python-poetri/tarball/master",
      install_requires=['pyjwkest', 'requests', ],
      packages= ['poetri', 'tests'],
      scripts=['poetri/verify_jws_with_jwk.py',
               'poetri/verify_jws_with_jwk_url.py',
               'poetri/sign_poet_jwk.py',
               'poetri/generate_jwk_keypair.py',
               'poetri/generate_public_jwk.py'
               ]
      )

