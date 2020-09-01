# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:47:07 2020

@author: addyk
"""

'''
This code is used to pull data from Bungie's servers about what any player is doing in D2

The expectation is to input a player ID (from Bungie) and to receive information in JSON(?) format about what said player is doing at the moment

Primary API info page for the Bungie API: https://bungie-net.github.io/multi/index.html
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
'''
This imports a few key variables used to authorize the script's access to the API: Mainly the API key (absolutely required), 
but also the client secret and client id (both may be unnecessary)
Script is not required, it's easy enough to just initialize the APIkey variable manually'
'''
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
#This is on hold until I figure out how to implement OAuth2
'''
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
'''
#%%
#Get Destiny Manifest (so as to crash the computer)
manifest = requests.get(f'{Rootpath}/Destiny2/Manifest/', headers = auth)
objman = json.loads(manifest.text)
print(objman)
#%%
'''
Get game status of player
Modules: 
Accumulate all necessary player info (character ID, member ID, membership type, etc)
Then use this info to get current status from Bungie
'''
#Begin by searching player name
auth = {'X-API-Key' : APIkey}
params = {'q' : 'Addykan'}
playersearch = requests.get(f'{Rootpath}/User/SearchUsers', headers = auth, params = params)

print(playersearch.text)
print('\n')
results = json.loads(playersearch.text)
membershipId = results['Response'][0]['membershipId']
print(membershipId)
#This gives us the membershipId parameter
membershipType = input('Enter the platform for the player: \n 1 for Xbox \n 2 for Playstation \n 3 for Steam \n 4 for Blizzard (deprecated) \n 5 for Stadia \n')
#This gives us membershipType - might be interesting to figure out how to set a default type if an account only has 1 active type linked
memdataurl = f'{Rootpath}/User/GetMembershipsById/{membershipId}/{membershipType}/'
memdatajson = requests.get(memdataurl, headers = auth)
memdata = json.loads(memdatajson.text)
print(memdata)
print(results)
destinyMembershipId = membershipId
#Final piece of activity history: Need to figure out how to get characterId
#%%
#Now that we have all parameters, we need to figure out what the player is doing in-game
activityhistoryurl = f'{Rootpath}/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/Activities/'










