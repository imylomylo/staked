#!/usr/bin/env python2
import os
import json

script_dir = os.getcwd()
with open(script_dir + '/assetchains.json') as file:
    assetchains = json.load(file)

for chain in assetchains:
    print(chain['ac_name'])
