#!/usr/bin/env python
import unittest, os, json
from poetri.verify_poet import verify_poet


test_public_key = """
-----BEGIN CERTIFICATE-----
MIIEozCCA4ugAwIBAgICAU4wDQYJKoZIhvcNAQELBQAwcTELMAkGA1UEBhMCVVMx
CzAJBgNVBAgMAk5DMQ8wDQYDVQQHDAZEdXJoYW0xEjAQBgNVBAoMCVZpZGVudGl0
eTEUMBIGA1UEAwwLZXhhbXBsZS5vcmcxGjAYBgkqhkiG9w0BCQEWC2V4YW1wbGUu
b3JnMB4XDTE2MDUwMjE0NTczNVoXDTE4MDUwMjE0NTczNVowgYwxCzAJBgNVBAYT
AlVTMQswCQYDVQQIDAJOQzEPMA0GA1UEBwwGRHVyaGFtMRkwFwYDVQQKDBBTb21l
IHNpZ25pbmcgb3JnMR4wHAYDVQQDDBV0cmFuc3BhcmVudGhlYWx0aC5vcmcxJDAi
BgkqhkiG9w0BCQEWFXRyYW5zcGFyZW50aGVhbHRoLm9yZzCCASIwDQYJKoZIhvcN
AQEBBQADggEPADCCAQoCggEBAKiaTvswM3vc3/AWmHI9svS5zSPMq9Ijyor9Ma8P
H73KA8XNirpF2yA0Tlw4d21eTr+6Roy3uyya9FTPKoq3HjTfcyywS8OWZgisTV2+
q6I+DYJIgzEKzKfLvX3Wss83eIA0Ldr/f04E6D6kF6/pL6T2FBxXTSPSjF8L0Ch/
xpPV/0/6XqC7effL05MNyvPeFK/h040M7GcpaIMkbbozK69qnT4A/zhBrZbA1YlH
SbBcBHmr1G4Ibcigha4FRMogNt7v0Vq/LtHXkVwHtq2x3spKenKFLDBanzk5wylA
9KJQ0JM0eAuX1ap1nEPUsUJHZaRRswO1hnHVjD68/SoT7dkCAwEAAaOCAScwggEj
MAkGA1UdEwQCMAAwIAYDVR0RBBkwF4IVdHJhbnNwYXJlbnRoZWFsdGgub3JnMB0G
A1UdDgQWBBS5pG89q+k0QWti8nbH46RghZNPYjAfBgNVHSMEGDAWgBSXucht5NOZ
8X/6PdQlCtDYZHHwdjALBgNVHQ8EBAMCBaAwXwYDVR0fBFgwVjAwoC6gLIYqaHR0
cDovL2NhLmRpcmVjdGNhLm9yZy9jcmwvZXhhbXBsZS5vcmcuY3JsMCKgIKAehhxo
dHRwOi8vbXlvdGhlcmZmLmNvbS9jcmwuY3JsMEYGCCsGAQUFBwEBBDowODA2Bggr
BgEFBQcwAoYqaHR0cDovL2NhLmRpcmVjdGNhLm9yZy9haWEvZXhhbXBsZS5vcmcu
ZGVyMA0GCSqGSIb3DQEBCwUAA4IBAQB5AIGpYWvA8CJ/ipMu2f0DEYlgj+sECzpU
U/KYYZZ/Ra/6ffFo2BFfhozztPAv5PXCeNk0vV8loE3KbgNjw/FBAk27t+gyysTC
en4ZDNgi8lt2X9mzULX4qdPIOfP96S0JVXcClcdNJ2FwSDuuUwXpgfkf1nlNYB8n
jd0QMN4v73uZkouFYhN+YWxyqASD/9AOVULUZbYAIf2Rv1L7TSnYJZwZ3vjC002p
gJDEwf1x7ojkmlMaLHJd0rSB7vO7jbTuvkaz6oWnoNRERLHaqf4YqX8pQbvHcX1T
y1AaA1AqLNz7WJgwfjMPciyGofFDRJT/Cp0Jyf8VvYq55a0Y+tBg
-----END CERTIFICATE-----
"""


encoded_jwt ="""eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ0cmFuc3BhcmVudGhlYWx0aC5vcmciLCJpYXQiOjE0NjIyOTM3OTAsImhlbGxvIjoid29ybGQiLCJleHAiOjE0OTM4Mjk3OTB9.kPGNV5R0G5PQPB9aCW6hTHZPMKsRcc-YmJqj9oCibdKtPM5cofSivSXX0waa1CQUU8VoPdQTOyry7ShldsWURN8ZNpXHBMXnamUiR1Phvjw93_awsbZCjAh4pK29gexNRX5oHjQ15kDv4Xd6bY2BA9pzueTN1jLnK1P2s3SDu-DtMhXcIUz-5_H_vq6VbaL6DAMeOePxEUevnGIIhkCtQdktUfTep55k7f8ujCDa52k-x8cEktXZmuACogyth-SeCd_I9GXrhYTN13jGqI02jAk8XiP8nzFMaT-bCkTWcFUzh8i3s0G0OLyVw07I6YC7yRJXMmNSEdPo30wM7EeB3Q
"""



class TestVerifyPoet(unittest.TestCase):

    def test_verify_poet_happy(self):
        """Verify the JWT signature""" 
        payload = verify_poet(encoded_jwt, test_public_key)        
        self.assertEqual(type(payload), type({}))
        self.assertIn('iss', payload.keys())
        self.assertEqual(payload['iss'], 'transparenthealth.org')
        self.assertIn('iat', payload.keys())
        self.assertIn('exp', payload.keys())

if __name__ == '__main__':
    unittest.main()
