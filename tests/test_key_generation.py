#!/usr/bin/env python
import unittest
import json
from poetri.generate_jwk_keypair import gen_jwk_keypair
from poetri.generate_public_jwk import gen_public

__author__ = 'Alan Viars @aviars'


class TestJWKGeneration(unittest.TestCase):

    def setUp(self):
        self.mykey = "example.com"

    def test_generate_jwk_keypair(self):

        result = gen_jwk_keypair(self.mykey)

        d = json.loads(result)
        keys = ['kty', 'd', 'e', 'use', 'kid', 'alg', 'n', 'q', 'p']

        """Assert expected keys are in output"""
        for j in d:
            self.assertIn(j, keys)

        self.assertEqual(d['kty'], 'RSA')
        self.assertEqual(d['use'], 'sig')
        self.assertEqual(d['alg'], 'RS256')
        self.assertEqual(d['kid'], self.mykey)

    def test_gen_public(self):
        keypair = gen_jwk_keypair(self.mykey)
        result = gen_public(json.loads(keypair))
        keys = ['kty', 'e', 'use', 'kid', 'alg', 'n', 'q', 'p']
        """Assert expected keys are in output"""
        for j in result:
            self.assertIn(j, keys)

        self.assertNotIn('d', result.keys())
        self.assertEqual(result['kty'], 'RSA')
        self.assertEqual(result['use'], 'sig')
        self.assertEqual(result['alg'], 'RS256')
        self.assertEqual(result['kid'], self.mykey)


if __name__ == '__main__':
    unittest.main()
