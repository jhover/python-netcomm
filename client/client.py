#!/bin/env python
#
# About SubjectAltName
# https://github.com/shazow/urllib3/issues/523
import logging
import requests
import urllib3

logging.captureWarnings(True)

NCHOME = '/home/jhover/git/certify/misc/ssca/intermediate/'
USER = "JohnHover"     
USERCERT = "%s/certs/%s.cert.pem" % (NCHOME, USER)
USERKEY = "%s/private/%s.keynopw.pem" % (NCHOME, USER)
CHAIN = "%s/certs/ca-chain.cert.pem" % (NCHOME)

TESTURLS = [ 'http://cloudy.rhic.bnl.gov:20333/',
             'http://cloudy.rhic.bnl.gov:20333/generate/',
             'http://cloudy.rhic.bnl.gov:20333/generate/?length=12',
             'https://cloudy.rhic.bnl.gov:20334/',
             'https://cloudy.rhic.bnl.gov:20334/generate/',
             'https://cloudy.rhic.bnl.gov:20334/generate/?length=12',            
            ]

TESTKEY='testkey'
TESTDOC='''{"uchicago_rcc" : {
            "base" : {
                "distribution" : "redhat",
                "release" : "6.7",
                "architecture" : "x86_64"}
                }
            }'''

APITEST = 'https://cloudy.rhic.bnl.gov:20334/webservice'

for tu in TESTURLS:
    print ("Testing URL: %s" % tu)
    try:
        r = requests.get(tu, verify=CHAIN)
        print(r.text)
        print(r.status_code)    
    except requests.exceptions.ConnectionError, ce:
        print('Connection failure. %s' % ce)
    
    
tu = '%s' % APITEST    
r = requests.put(tu, verify=CHAIN, params={'key' : TESTKEY, 'doc' : TESTDOC})
print(r.text)
print(r.status_code)
