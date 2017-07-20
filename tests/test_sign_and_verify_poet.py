#!/usr/bin/env python
import unittest
import json
import os
from poetri.sign_poet_jwk import sign_poet
from poetri.verify_jws_with_jwk import verify_poet
from collections import OrderedDict

__author__ = 'Alan Viars @aviars'


class TestSignAndVerify(unittest.TestCase):

    def setUp(self):

        # Get the kid/issuer
        self.issuer = "example.com"

        # load a sample payload
        payload_fp = os.path.join(os.path.dirname(__file__), "payload.json")
        payload_fh = open(payload_fp)
        payload = payload_fh.read()
        self.payload = json.loads(payload, object_pairs_hook=OrderedDict)
        payload_fh.close()

        # load a sample keypair
        keypair_fp = os.path.join(os.path.dirname(__file__), "keypair.jwk")
        keypair_fh = open(keypair_fp)
        keypair = keypair_fh.read()
        self.keypair = json.loads(keypair, object_pairs_hook=OrderedDict)
        keypair_fh.close()

        # load a sample public key
        pubkey_fp = os.path.join(os.path.dirname(__file__), "poet.jwk")
        pubkey_fh = open(pubkey_fp)
        pubkey = pubkey_fh.read()
        self.pubkey = json.loads(pubkey, object_pairs_hook=OrderedDict)
        pubkey_fh.close()

        # A public key that doesn't match its private counterpart.
        self.bad_n = "X0vZedyiaeg_tqAcGeVzdpd_DO5QtBHpsRvDX6SKDwOytfsLZUIfR5Q"\
                     "gpz49kLCEDIjGAdg3iQ81leo2zrX5RfZ6q1n5pFpbU7VLX3ylKZ7Sug"\
                     "-ujuiNd7xmVnvdwiKyupnEnG_6XXwJDaoyMT9xXgiR4BKS3pHCoIPO0"\
                     "ktIi2BHGB1Nqb2YqKoCaeMmuZvW6EIA04_wb6wTLIXcf8jh8bt4pJ0C"\
                     "WMLqJqr524p0rEhYGl5P3BsnBDr19vM-i-_dNjAoaUT1Bc6wN_a1wFe"\
                     "baEL1C2Aia1EeF3oMAfsa_aTLA2x8NlWrjwwPyGIOsrxjmjJ6oLqvUC"\
                     "dcg1Nod9YaY9"

    def test_signing(self):

        self.signed_jws = sign_poet(self.payload,
                                    self.keypair,
                                    self.issuer)
        """Test the POET JWT signing by ensuring
           exactly two periods in output."""
        self.assertEqual(self.signed_jws.count('.'), 2)

    def test_signature_verification_good_pubkey(self):
        self.signed_jws = sign_poet(self.payload,
                                    self.keypair,
                                    self.issuer)
        self.verified_payload = verify_poet(self.signed_jws, self.pubkey)
        self.assertNotIn("error", self.verified_payload.keys())

    def test_signature_verification_good_pubkey_bad_kid(self):
        self.signed_jws = sign_poet(self.payload, self.keypair, self.issuer)
        self.pubkey['kid'] = self.pubkey['kid'] + "foo"
        self.verified_payload = verify_poet(self.signed_jws, self.pubkey)
        self.assertIn("error", self.verified_payload.keys())

    def test_signature_verification_bad_pubkey_good_kid(self):
        self.signed_jws = sign_poet(self.payload,
                                    self.keypair,
                                    self.issuer)
        # A non matching public key - modified value for n.
        self.pubkey['n'] = self.bad_n
        self.verified_payload = verify_poet(self.signed_jws, self.pubkey)
        self.assertIn("error", self.verified_payload.keys())

if __name__ == '__main__':
    unittest.main()
