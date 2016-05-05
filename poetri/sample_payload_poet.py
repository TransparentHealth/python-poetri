#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

"""
pypoetri
FILE: sample_payload_poet
Created: 5/4/16 8:58 AM


"""
__author__ = 'Mark Scrimshire:@ekivemark'

import sys, json, time

from collections import OrderedDict

def sample_payload_poet(mode="info"):
    """ create a skeleton jwt based on poet

     https://github.com/HHSIDEALab/poet

     Header

    {
    "alg": "RS256",
    "typ": "JWT"
    }

    Payload

    {
    "iss": "nate-trust.org",
    "iat": 1455031265,
    "exp": 1549639265,
    "aud": "apps-dstu2.smarthealthit.org",
    "sub": "jrocket@apps-dstu2.smarthealthit.org",
    "certification_uid": "9292010131",
       "contacts" : [
          "info@smartplatforms.org",
          "https://gallery.smarthealthit.org"
       ],
      "client_name" : "Cardiac Risk App",
      "client_uri": "https://apps-dstu2.smarthealthit.org/cardiac-risk/",
       "logo_uri" : "https://gallery.smarthealthit.org/img/apps/66.png",
       "initiate_login_uri" : "https://apps-dstu2.smarthealthit.org/cardiac-risk/launch.html",
       "redirect_uris" : [
          "https://apps-dstu2.smarthealthit.org/cardiac-risk/"
       ],
       "scope" : "openid profile patient/*.read",
       "token_endpoint_auth_method" : "none",
       "grant_types" : [ "authorization_code" ]
        }
    Signature

    HMACSHA256(
      base64UrlEncode(header) + "." +
      base64UrlEncode(payload),

    ) secret base64 encoded


     """

    my_mode = mode
    output = ""
    expires = 63072000

    if my_mode.lower() == "info":
        info = "\n#jwt Info===========================\n"
        info += "A signed jwt (pronounced 'jot' contains 2 parts:\n"
        info += "1. Header\n"
        info += "2. Payload file\n"
        info += "These are shown below. You can cut and paste the sections to create\n"
        info += "your own payload file.\n"

        output += info

    if my_mode.lower() in ['info', 'both', 'header']:
        header = OrderedDict()

        header['alg'] = "RS256"
        header["typ"] = "JWT"

        if my_mode.lower() in ['info', 'both']:
            output += "\n#jwt Header Settings================\n"
        output += json.dumps(header, indent=4)

        if my_mode.lower() in ['info', 'both']:
            output += "\n\n#===================================\n"

    if my_mode.lower() in ['info', 'both', 'payload']:
        payload = OrderedDict()

        payload['iss'] = "trust-issuer.org"
        payload['iat'] = int(time.time())
        # Set to expire (two years is default)
        payload["exp"] = payload["iat"] + expires
        payload["aud"] = "app.example.com",
        payload["sub"] = "your_admin_email@example.com",
        payload["certification_uid"] = "Unique_Id_Number",
        payload["contacts"] = [
                                  "info@example.com",
                                  "https://help.app.example.com"
                              ],
        payload["client_name"] = "example app name",
        payload["client_uri"] = "https://apps.example.com/example_url/",
        payload["logo_uri"] = "https://apps.example.com/img/logo.png",
        payload["initiate_login_uri"] = "https://apps.example.com/example_app/launch.html",
        payload["redirect_uris"] = [
                                       "https://apps.example.com/example_app/"
                                   ],
        payload["scope"] = "openid profile patient/*.read",
        payload["token_endpoint_auth_method"] = "none",
        payload["grant_types"] = ["authorization_code"]

        if my_mode.lower() in ['info', 'both']:
            output += "\n#jwt Payload Settings===============\n"

        output += json.dumps(payload, indent=4)

        if my_mode.lower() in ['info', 'both']:
            output += "\n#iat = time now. \n"
            output += "#exp = expire time after iat (two years is default).\n"

            output += "\n\n#===================================\n"



    return output

#Command line app.
if __name__ == "__main__":


    if len(sys.argv) < 2:
        print("Usage: sample_payload_poet.py header|payload|both|info")
        print("Example: sample_payload_poet.py info")

        sys.exit(1)

    my_mode                 = sys.argv[1]

    output = ""
    expires = 63072000

    if my_mode.lower() == "info":

        info =  "\n#jwt Info===========================\n"
        info += "A signed jwt (pronounced 'jot' contains 2 parts:\n"
        info += "1. Header\n"
        info += "2. Payload file\n"
        info += "These are shown below. You can cut and paste the sections to create\n"
        info += "your own payload file.\n"

        output += info

    if my_mode.lower() in ['info', 'both', 'header']:
        header = OrderedDict()

        header['alg'] = "RS256"
        header["typ"] = "JWT"

        if my_mode.lower() in ['info', 'both']:
            output += "\n#jwt Header Settings================\n"
        output += json.dumps(header, indent=4)

        if my_mode.lower() in ['info', 'both']:
            output += "\n\n#===================================\n"

    if my_mode.lower() in ['info', 'both', 'payload']:
        payload = OrderedDict()

        payload['iss'] = "trust-issuer.org"
        payload['iat'] = int(time.time())
        # Set to expire (two years is default)
        payload["exp"] = payload["iat"] + expires
        payload["aud"] =  "app.example.com",
        payload["sub"] = "your_admin_email@example.com",
        payload["certification_uid"] = "Unique_Id_Number",
        payload["contacts"] = [
                        "info@example.com",
                        "https://help.app.example.com"
                    ],
        payload["client_name"] = "example app name",
        payload["client_uri"] = "https://apps.example.com/example_url/",
        payload["logo_uri"] = "https://apps.example.com/img/logo.png",
        payload["initiate_login_uri"] = "https://apps.example.com/example_app/launch.html",
        payload["redirect_uris"] = [
                         "https://apps.example.com/example_app/"
                     ],
        payload["scope"] = "openid profile patient/*.read",
        payload["token_endpoint_auth_method"] = "none",
        payload["grant_types"] = ["authorization_code"]

        if my_mode.lower() in ['info', 'both']:

            output += "\n#jwt Payload Settings===============\n"

        output += json.dumps(payload, indent=4)

        if my_mode.lower() in ['info', 'both']:

            output += "\n#iat = time now. \n"
            output += "#exp = expire time after iat (two years is default).\n"

            output += "\n\n#===================================\n"

    print(output)

