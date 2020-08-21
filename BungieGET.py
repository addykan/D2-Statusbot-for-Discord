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

#%%
#First step: Figure out how to allow user to authorize the app to access Bungie data