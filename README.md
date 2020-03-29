# FranceIX Peerfinder :
This program was developped to analyse the member list of the FranceIX IXP
and comparing it with the IRR of the ASN of your choice and the FranceIX route
servers. So that it can output a list of persons to contact for peering.

To run it :
```
virtualenv ve3 -p python3
source ve3/bin/activate
pip install -r requirements.txt
python main.py
```
All settings that should be editted by the users are located in config.py.
