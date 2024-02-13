#!/usr/bin/env python
"""Offlineimap helper script"""

from subprocess import check_output
from os import getenv, path
import json

JSON_FILE = "credentials.json"
if getenv("XDG_DATA_HOME") and path.exists(getenv("XDG_DATA_HOME") + "/" + "offlineimap"):
    JSON_PATH = getenv("XDG_DATA_HOME") + "/" + "offlineimap"
else:
    JSON_PATH = getenv("HOME") + "/" + ".local/share/offlineimap"


f = open(JSON_PATH + "/" + JSON_FILE)
creds_data = json.load(f)

def get_credentials(name, query):
    for item in creds_data["accounts"]:
        if item["name"] == name:
            if query == "host":
                return item["host"]
            elif query == "port":
                return item["port"]
            elif query == "user":
                return item["user"]
            elif query == "passeval":
                return item["passeval"]
