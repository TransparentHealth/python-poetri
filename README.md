poetri - Pre OAuth Entity Trust Reference Implementation
========================================================


JSON Web Tokens (JWTs) are an open, industry standard RFC 7519 method for representing 
claims securely between two parties.

Pre-OAuth Entity Trust (POET) is a specific JWT designed to facilitate claims about consumer-facing health applications. https://github.com/hhsidealab/poet 

This is a reference implemenation for signing and verifing POET JWTs in Python2 and Python3.

It contains both libraries and command line utilities.

To install on Ubuntu Linux first install the prerequisites:


    sudo apt-get install libssl-dev

(The above instruction will differ for iOS, Redhat, Windows, etc.)

To install poetri type:


    git clone https://github.com/TransparentHealth/python-poetri.git
    python python-poetri/setup.py install

The command line tools are  `verify_poet.py` and `sign_poet.py`. Just type their name for usage info.

The following section illustrates how to use the API for signing JWTs and verifing their information.


    Python 3.5.1 (default, Dec 26 2015, 18:11:22) 
    [GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    
Import the sign_poet method


    >>> from poetri.sign_poet import sign_poet


A private key ready for signing...   
  
   
    >>> test_private_key = """
    ... -----BEGIN PRIVATE KEY-----
    ... MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQComk77MDN73N/w
    ... FphyPbL0uc0jzKvSI8qK/TGvDx+9ygPFzYq6RdsgNE5cOHdtXk6/ukaMt7ssmvRU
    ... zyqKtx4033MssEvDlmYIrE1dvquiPg2CSIMxCsyny7191rLPN3iANC3a/39OBOg+
    ... pBev6S+k9hQcV00j0oxfC9Aof8aT1f9P+l6gu3n3y9OTDcrz3hSv4dONDOxnKWiD
    ... JG26Myuvap0+AP84Qa2WwNWJR0mwXAR5q9RuCG3IoIWuBUTKIDbe79Favy7R15Fc
    ... B7atsd7KSnpyhSwwWp85OcMpQPSiUNCTNHgLl9WqdZxD1LFCR2WkUbMDtYZx1Yw+
    ... vP0qE+3ZAgMBAAECggEAS566IetijAFq5zIbOdH2e9EB8zaPMfcfluss54lvAR6k
    ... RomD2TwPpggPxUkGN6V+yHtxvReC+eSeBZPNTt4GzEwUSkzgDl9ccDNnl843CNOw
    ... F2kSfmKLnA7DdLdhB5OnlkjQ8FJ79LA6wi2y+hEqb2B3cKavUIvUraSMvj1hAVjV
    ... hu0Dh6RvpMwDKRk5R74EEbBRfV4kX6qNjOaGFw9siwtp5qSY17eSbBCsBOMQHe9U
    ... t1nG5Fu/ChgOpUOjCsKtGPgl7H/6BfZjtLiP7xaoxRySfSbnpyu+Sxqofwa8mnjE
    ... qdQTONkR7GztnaL/+2LHeLrCyDtklwptzeNuVKf6AQKBgQDQX3M/mfh1tCe9pZVi
    ... +APDRVGw1ofsUQXOAHmY9eEwmIjmkV2HCHue3zwehzeLcmEeeI1Ozxi0JBsCsb+l
    ... vb4m9AvEJkz6BaUCclqD6lcfcgiQbtSEsdQTS35aZSu8Woa0OGt4zDrSLB4jLrPR
    ... EFdpA2FxcZMoNqbHMbF0B+9TYQKBgQDPI8krEwZT+mG0PCEIFiBFv5jMvOXd8qZE
    ... Rq1iDVfI3iHta5fs7D0KzQVQqSFqCEQjPfC+dNAZL0SWHewNdf523TTZK4vOkaIB
    ... PQEh568xk9EvV6/8QInO+4ljAM9/Kcze08SL0wj2aqa+iuys/6k1Ociz8xoEeEK0
    ... 4kEhbDileQKBgDYGiXsUELdz3lntdK4UX+VhM60F8nfzCe4/cUeXeKuA4P3m8rjw
    ... Gh03A/9mT6B4J3YfC4RDbcRHGDm6nFX8vDCdVe+lfo/UptPbklxhhfVBO7c3BSLi
    ... eHoIONp3IL/VONfBSRwo15dmmOnGUhkCg6dWmQ0wxVbH1LYQzFGpPQQBAoGAYoSA
    ... r03zGonhYlme1DvByaqgv++v3GoGDj8XQ6VY9R5BQKyFq5eISNTODFkEnWulDKXv
    ... FIZ2WyQSGNvOY3CVQG9hLVD6w5qcVL5xBXEt8AR/32ZzOyRu5tTXuRCvn6l/2RMb
    ... Te1nO9vpxoJIotdN4RTEkmGzJCEWiPV7SKwyHPECgYEAwCdBX0pzpgAFbcX44FG8
    ... Wo1b7C6y2vnAzm/MazBcDm9MH8X1oXdqRjKpY7kHXFYHB/fAxsUVCyOP82JVl5mq
    ... yld/v0Z19nKV1e+rQz8DhdJtyUOOQ1szetHHvprDSK3KulBcojznIDgrRHqxSJcc
    ... j1DFK16BeYLj88PTTKLtheE=
    ... -----END PRIVATE KEY-----"""
    
    
    
Sign the payload and build the JWT. The issuer is transparenthealth.org 
    
    
    >>> sign_poet({"sub":"someapp.foo.com"}, test_private_key, "tranparenthealth.org", 3600)

The result of sign_poet is just a string contining the JWT.


    'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE0ODcyNjA1NzEsImV4cCI6MTQ4NzI2NDE3MSwiaXNzIjoidHJhbnBhcmVudGhlYWx0aC5vcmciLCJzdWIiOiJzb21lYXBwLmZvby5jb20ifQ.aoAgaYruGDOvaMp1tzC3GRcS6GU0bnkoM9tcMthSRrTN6yfLxozbXASkgbveNnrGkBoXCwZNNySetTIrjX8hnFAzNVmWlHBwieUykoYCRwLrD5gBe5Fpa0fy1XO3YqqQbGY29eb8ix-gvH0cM0crWCAGnAu56AhqJcqAjd2VgHdrgS5ipEE-gfvoSLISWFOeWt54kclPsHh7WSYMm0WnuntGRHcQnHSSany_96M8t4LlGMhpPO3nJo_0G2r6e634aggYxB9aGs4ErrFG4GhFWZieve3Kia9R6ihzZCIgc0mNUOMD5xl44vDiTU9eZFA8DGknZ1ohGlaXKWHtSgh3FA'
        

Now let's verify the signature on the JWT. Let's import the library


        >>> from poetri.verify_poet import verify_poet


A public key to verify the signature.
        

        >>> test_public_key = """
        ... -----BEGIN CERTIFICATE-----
        ... MIIEozCCA4ugAwIBAgICAU4wDQYJKoZIhvcNAQELBQAwcTELMAkGA1UEBhMCVVMx
        ... CzAJBgNVBAgMAk5DMQ8wDQYDVQQHDAZEdXJoYW0xEjAQBgNVBAoMCVZpZGVudGl0
        ... eTEUMBIGA1UEAwwLZXhhbXBsZS5vcmcxGjAYBgkqhkiG9w0BCQEWC2V4YW1wbGUu
        ... b3JnMB4XDTE2MDUwMjE0NTczNVoXDTE4MDUwMjE0NTczNVowgYwxCzAJBgNVBAYT
        ... AlVTMQswCQYDVQQIDAJOQzEPMA0GA1UEBwwGRHVyaGFtMRkwFwYDVQQKDBBTb21l
        ... IHNpZ25pbmcgb3JnMR4wHAYDVQQDDBV0cmFuc3BhcmVudGhlYWx0aC5vcmcxJDAi
        ... BgkqhkiG9w0BCQEWFXRyYW5zcGFyZW50aGVhbHRoLm9yZzCCASIwDQYJKoZIhvcN
        ... AQEBBQADggEPADCCAQoCggEBAKiaTvswM3vc3/AWmHI9svS5zSPMq9Ijyor9Ma8P
        ... H73KA8XNirpF2yA0Tlw4d21eTr+6Roy3uyya9FTPKoq3HjTfcyywS8OWZgisTV2+
        ... q6I+DYJIgzEKzKfLvX3Wss83eIA0Ldr/f04E6D6kF6/pL6T2FBxXTSPSjF8L0Ch/
        ... xpPV/0/6XqC7effL05MNyvPeFK/h040M7GcpaIMkbbozK69qnT4A/zhBrZbA1YlH
        ... SbBcBHmr1G4Ibcigha4FRMogNt7v0Vq/LtHXkVwHtq2x3spKenKFLDBanzk5wylA
        ... 9KJQ0JM0eAuX1ap1nEPUsUJHZaRRswO1hnHVjD68/SoT7dkCAwEAAaOCAScwggEj
        ... MAkGA1UdEwQCMAAwIAYDVR0RBBkwF4IVdHJhbnNwYXJlbnRoZWFsdGgub3JnMB0G
        ... A1UdDgQWBBS5pG89q+k0QWti8nbH46RghZNPYjAfBgNVHSMEGDAWgBSXucht5NOZ
        ... 8X/6PdQlCtDYZHHwdjALBgNVHQ8EBAMCBaAwXwYDVR0fBFgwVjAwoC6gLIYqaHR0
        ... cDovL2NhLmRpcmVjdGNhLm9yZy9jcmwvZXhhbXBsZS5vcmcuY3JsMCKgIKAehhxo
        ... dHRwOi8vbXlvdGhlcmZmLmNvbS9jcmwuY3JsMEYGCCsGAQUFBwEBBDowODA2Bggr
        ... BgEFBQcwAoYqaHR0cDovL2NhLmRpcmVjdGNhLm9yZy9haWEvZXhhbXBsZS5vcmcu
        ... ZGVyMA0GCSqGSIb3DQEBCwUAA4IBAQB5AIGpYWvA8CJ/ipMu2f0DEYlgj+sECzpU
        ... U/KYYZZ/Ra/6ffFo2BFfhozztPAv5PXCeNk0vV8loE3KbgNjw/FBAk27t+gyysTC
        ... en4ZDNgi8lt2X9mzULX4qdPIOfP96S0JVXcClcdNJ2FwSDuuUwXpgfkf1nlNYB8n
        ... jd0QMN4v73uZkouFYhN+YWxyqASD/9AOVULUZbYAIf2Rv1L7TSnYJZwZ3vjC002p
        ... gJDEwf1x7ojkmlMaLHJd0rSB7vO7jbTuvkaz6oWnoNRERLHaqf4YqX8pQbvHcX1T
        ... y1AaA1AqLNz7WJgwfjMPciyGofFDRJT/Cp0Jyf8VvYq55a0Y+tBg
        ... -----END CERTIFICATE-----
        ... """
        
        
   A JWT to verify
        
        
        >>> encoded_jwt ="""eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ0cmFuc3BhcmVudGhlYWx0aC5vcmciLCJpYXQiOjE0NjIyOTM3OTAsImhlbGxvIjoid29ybGQiLCJleHAiOjE0OTM4Mjk3OTB9.kPGNV5R0G5PQPB9aCW6hTHZPMKsRcc-YmJqj9oCibdKtPM5cofSivSXX0waa1CQUU8VoPdQTOyry7ShldsWURN8ZNpXHBMXnamUiR1Phvjw93_awsbZCjAh4pK29gexNRX5oHjQ15kDv4Xd6bY2BA9pzueTN1jLnK1P2s3SDu-DtMhXcIUz-5_H_vq6VbaL6DAMeOePxEUevnGIIhkCtQdktUfTep55k7f8ujCDa52k-x8cEktXZmuACogyth-SeCd_I9GXrhYTN13jGqI02jAk8XiP8nzFMaT-bCkTWcFUzh8i3s0G0OLyVw07I6YC7yRJXMmNSEdPo30wM7EeB3Q
        ... """
   
   
   Verify the POET JWTs signature
   
   
        >>> verify_poet(encoded_jwt, test_public_key) 
        {'hello': 'world', 'exp': 1493829790, 'iss': 'transparenthealth.org', 'iat': 1462293790}
        >>> 


If verified, the payload is returned.  (Keep in mind the payload is accesible without signature verification using standard JWT libraries.)

