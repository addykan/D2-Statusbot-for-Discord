# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:47:07 2020

@author: addyk
"""

'''
This code is used to pull data from Bungie's servers about what any player is doing in D2

The expectation is to input a player ID (from Bungie) and to receive information in JSON(?) format about what said player is doing at the moment
'''
import requests
import requests_oauthlib
import json
import os
import base64
from requests.auth import *
os.chdir("D:\General\Github\API-info")
from APIauthcodes import *
bungieauth()
from APIauthcodes import *
os.chdir("D:\General\Github\D2-Statusbot-for-Discord")
Rootpath = 'https://www.bungie.net/Platform'
Authpath = 'https://www.bungie.net/en/oauth/authorize'
Tokenpath = 'https://www.bungie.net/platform/app/oauth/token'
#%%
#First step: Verify application's authentication

auth = {'X-API-Key' : APIkey}
params = {'q' : 'Addykan'}
test = requests.get(f'{Rootpath}/User/SearchUsers', headers = auth, params = params)

print(test.text)
print('\n')
results = json.loads(test.text)
print(results)
#Succes!
#%%
#Step 2: Authenticate users

import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

state = get_random_string(9)
params = {'response_type' : 'code', 'client_id' : client_id, 'state' : state}
authorization = requests.get(f'https://www.bungie.net/en/oauth/authorize', params = params)

print(authorization.url)
#%%
#Redirect URL includes a code to be used in next step
#Next Step: Get token from Bungie
authcode = base64.b64encode()
params = {'grant_type' : 'authorization_code' , 'code' : authcode, 'client_id' : client_id, 'client_secret' : client_secret}
tokenget = requests.post(Tokenpath, headers = params)

print(tokenget.url)
print(tokenget.status_code)
print('\n \n \n Text: \n')
print(tokenget.text)
