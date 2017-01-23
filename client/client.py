#!/bin/env python

import requests
import urllib3
urllib3.disable_warnings()

NCHOME = '/home/jhover/'
UHOME = '/home/jhover'
HOST = 'cloudy.rhic.bnl.gov'    
CERT = "%s/etc/%s/hostcert.pem" % (NCHOME, HOST)
KEY = "%s/etc/%s/hostkey.pem" % (NCHOME, HOST)
CHAIN = "%s/etc/%s/cacert.pem" % (NCHOME, HOST)
USERCERT = "%s/.globus/usercert.pem" % UHOME
USERKEY = "%s/.globus/userkeynopw.pem" % UHOME

TESTURLS = [ 'https://cloudy.rhic.bnl.gov:20334/',
             'https://cloudy.rhic.bnl.gov:20334/generate/',
             'http://cloudy.rhic.bnl.gov:20333/',
             'http://cloudy.rhic.bnl.gov:20333/generate/'            
            ]

for tu in TESTURLS:
    print ("Testing URL: %s" % tu)
    try:
        #r = requests.get('http://cloudy.rhic.bnl.gov:20333/generate')
        #r = requests.get(tu, verify=CHAIN)
        r = requests.get(tu, verify=False)
        print(r.text)
        print(r.status_code)
    
    
    except requests.exceptions.ConnectionError, ce:
        print('Connection failure. %s' % ce)
    

