#!/usr/bin/python
# -*- coding: utf-8 -*-
#PhoneInfog
#Phonenumber Information gathering
#=====================================
#-==] Aunthor : David Apriyanto [BLANK]
#-==] Team : sixtysix-Team
#-==] Date : 03 September 2019
#-==] Github : https://github.com/sixtysix-Team
#-==] YouTube : hack 606
#=====================================

#module
import requests
import os
import sys
import urllib
import json

#color
k = '\033[93m'
u = '\033[95m'
n  = '\033[94m'
m = '\033[91m'
h = '\033[92m'
p = '\033[00m'

os.system ('clear')

#banner

print n+"__________.__                         .___        _____       "
print n+"\______   \  |__   ____   ____   ____ |   | _____/ ____\____  "
print n+" |     ___/  |  \ /  _ \ /    \_/ __ \|   |/    \   __\/  _ \ "
print k+" |    |   |   Y  (  <_> )   |  \  ___/|   |   |  \  | (  <_> )"
print k+" |____|   |___|  /\____/|___|  /\___  >___|___|  /__|  \____/ "
print k+"               \/            \/     \/         \/             "
print k+"https://github.com/sixtysix-Team"
print

#input number
number = raw_input(m+"["+k+"#"+m+"]"  +h+"phone number : ")
print
#data
key = "9810ba5ae4fe74c2930842025d11bc58"
url = "http://apilayer.net/api/validate?access_key=" + key + "&number=" + number + "&country_code=&format=1"
output = requests.get(url)
result = output.text
js = json.loads(result)
#running
country_code = js['country_code']
country_name = js['country_name']
location = js['location']
carrier = js['carrier']
line_type = js['line_type']

print m+"["+k+"#"+m+"]"  +h+"phonenumber information gathering"  +m+"["+k+"#"+m+"]"
print
print k+"["+m+"+"+k+"]"  +h+"Information Output"
print k+"--------------------------------------"
print k+" ~" +h+"Phone number: " +str(number)
print k+" ~" +h+"Country: " +str(country_code)
print k+" ~" +h+"Country Name: " +str(country_name)
print k+" ~" +h+"Location: " +str(location)
print k+" ~" +h+"Carrier: " +str(carrier)
print k+" ~" +h+"Device: " +str(line_type)