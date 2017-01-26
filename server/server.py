#!/bin/env python
import cherrypy
import random
import string
import logging

# Possibly required in /etc/services?
# vc3-http        20333/tcp
# vc3-https       20334/tcp
#
# Thanks: http://www.zacwitte.com/using-ssl-https-with-cherrypy-3-2-0-example
#
# SSL broken in CherryPy > 3.2.3 
# Download srpm from https://www.rpmfind.net/linux/RPM/centos/7.2.1511/x86_64/Packages/python-cherrypy-3.2.2-4.el7.noarch.html
# Rebuild for Fedora 24. 
#
#
class InfoService(object):
    @cherrypy.expose
    def index(self):
        return "Hello World"
    
    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))
    
if __name__ == '__main__':
    
    NCHOME = '/home/jhover/git/certify/misc/ssca/intermediate/'
    HOST = 'cloudy.rhic.bnl.gov'    
    CERT = "%s/certs/%s.cert.pem" % (NCHOME, HOST)
    KEY = "%s/private/%s.keynopw.pem" % (NCHOME, HOST)
    CHAIN = "%s/certs/ca-chain.cert.pem" % (NCHOME)


    print('cert is %s' % CERT)
    print('key is %s' % KEY)
    print('chain is %s' % CHAIN)    

    
    cherrypy.tree.mount(InfoService())
    cherrypy.server.unsubscribe()

    server1 = cherrypy._cpserver.Server()
    server1.socket_port=20334
    server1._socket_host='0.0.0.0'
    server1.thread_pool=30
    server1.ssl_module = 'builtin'
    #server1.ssl_module = 'pyopenssl'
    server1.ssl_certificate = CERT
    server1.ssl_private_key = KEY
    server1.ssl_certificate_chain = CHAIN
    server1.subscribe()

    server2 = cherrypy._cpserver.Server()
    server2.socket_port=20333
    server2._socket_host="0.0.0.0"
    server2.thread_pool=30
    server2.subscribe()

    cherrypy.engine.start()
    cherrypy.engine.block()   
    
    
    
    
    
    #cherrypy.quickstart(InfoService())
