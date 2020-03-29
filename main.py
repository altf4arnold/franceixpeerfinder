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
        print("Error - request timeout !")
        toreturn = {}
    return toreturn

def confchecker():
    """
    here to tell if the user did put garbage in his config file
    """
    no_error = True
    if config.location != "PAR" and config.location != "MRS":
        print(config.location + " in config is garbage")
        no_error = False
    if type(config.asusage) != bool:
        print("asusage in config must be a boolean")
        no_error = False
    if type(config.asn) != int:
        print(str(config.asn) + " in config is garbage")
        no_error = False
    if config.asn > 4294967295 or config.asn < 1:
        print(str(config.asn) + " is not a valid ASN")
        no_error = False
    if bool(config.asn > 64495 and config.asn < 131072) or bool(config.asn > 399260 and config.asn <= 4294967295):
        print(str(config.asn) + " is a private ASN")
        no_error = False
    return no_error


def main():
    if confchecker() is False:
        return 0
    print(jsonparsser(config.location))


if __name__ == '__main__':
	main()
