"""
Program written by Arnold Dechamps?
MAR/2020 during confinement
"""

import os
import json
import config
from urllib import request


def jsonparsser(location):
    """
    go get the data, make the first parssing and return the data
    """
    try:
        toreturn = json.load(request.urlopen\
		("https://www.franceix.net/api/members/list/json?location={}"\
        .format(location)))
    except:
        toreturn = 'Error'
    return toreturn




def main():
    print(jsonparsser(config.location))


if __name__ == '__main__':
	main()
