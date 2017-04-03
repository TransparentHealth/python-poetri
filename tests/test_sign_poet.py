#!/usr/bin/env python
import unittest, os
from poetri.sign_poet import sign_poet

#This key is for testing and the CN is "transparenthealth.org"
test_private_key = """
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQComk77MDN73N/w
FphyPbL0uc0jzKvSI8qK/TGvDx+9ygPFzYq6RdsgNE5cOHdtXk6/ukaMt7ssmvRU
zyqKtx4033MssEvDlmYIrE1dvquiPg2CSIMxCsyny7191rLPN3iANC3a/39OBOg+
pBev6S+k9hQcV00j0oxfC9Aof8aT1f9P+l6gu3n3y9OTDcrz3hSv4dONDOxnKWiD
JG26Myuvap0+AP84Qa2WwNWJR0mwXAR5q9RuCG3IoIWuBUTKIDbe79Favy7R15Fc
B7atsd7KSnpyhSwwWp85OcMpQPSiUNCTNHgLl9WqdZxD1LFCR2WkUbMDtYZx1Yw+
vP0qE+3ZAgMBAAECggEAS566IetijAFq5zIbOdH2e9EB8zaPMfcfluss54lvAR6k
RomD2TwPpggPxUkGN6V+yHtxvReC+eSeBZPNTt4GzEwUSkzgDl9ccDNnl843CNOw
F2kSfmKLnA7DdLdhB5OnlkjQ8FJ79LA6wi2y+hEqb2B3cKavUIvUraSMvj1hAVjV
hu0Dh6RvpMwDKRk5R74EEbBRfV4kX6qNjOaGFw9siwtp5qSY17eSbBCsBOMQHe9U
t1nG5Fu/ChgOpUOjCsKtGPgl7H/6BfZjtLiP7xaoxRySfSbnpyu+Sxqofwa8mnjE
qdQTONkR7GztnaL/+2LHeLrCyDtklwptzeNuVKf6AQKBgQDQX3M/mfh1tCe9pZVi
+APDRVGw1ofsUQXOAHmY9eEwmIjmkV2HCHue3zwehzeLcmEeeI1Ozxi0JBsCsb+l
vb4m9AvEJkz6BaUCclqD6lcfcgiQbtSEsdQTS35aZSu8Woa0OGt4zDrSLB4jLrPR
EFdpA2FxcZMoNqbHMbF0B+9TYQKBgQDPI8krEwZT+mG0PCEIFiBFv5jMvOXd8qZE
Rq1iDVfI3iHta5fs7D0KzQVQqSFqCEQjPfC+dNAZL0SWHewNdf523TTZK4vOkaIB
PQEh568xk9EvV6/8QInO+4ljAM9/Kcze08SL0wj2aqa+iuys/6k1Ociz8xoEeEK0
4kEhbDileQKBgDYGiXsUELdz3lntdK4UX+VhM60F8nfzCe4/cUeXeKuA4P3m8rjw
Gh03A/9mT6B4J3YfC4RDbcRHGDm6nFX8vDCdVe+lfo/UptPbklxhhfVBO7c3BSLi
eHoIONp3IL/VONfBSRwo15dmmOnGUhkCg6dWmQ0wxVbH1LYQzFGpPQQBAoGAYoSA
r03zGonhYlme1DvByaqgv++v3GoGDj8XQ6VY9R5BQKyFq5eISNTODFkEnWulDKXv
FIZ2WyQSGNvOY3CVQG9hLVD6w5qcVL5xBXEt8AR/32ZzOyRu5tTXuRCvn6l/2RMb
Te1nO9vpxoJIotdN4RTEkmGzJCEWiPV7SKwyHPECgYEAwCdBX0pzpgAFbcX44FG8
Wo1b7C6y2vnAzm/MazBcDm9MH8X1oXdqRjKpY7kHXFYHB/fAxsUVCyOP82JVl5mq
yld/v0Z19nKV1e+rQz8DhdJtyUOOQ1szetHHvprDSK3KulBcojznIDgrRHqxSJcc
j1DFK16BeYLj88PTTKLtheE=
-----END PRIVATE KEY-----"""


class TestSigning(unittest.TestCase):

    def test_sign_poet_happy(self):
        result = sign_poet({"sub":"someapp.foo.com"}, test_private_key, "tranparenthealth.org", 3600)

        """Test the POET JWT signing by ensuring exactly two periods in output."""
        self.assertEqual(result.count('.'), 2)



if __name__ == '__main__':
    unittest.main()
