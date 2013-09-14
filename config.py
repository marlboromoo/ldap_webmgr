#!/usr/bin/env python
# encoding: utf-8

"""
ldap_webmgr
"""

PROJECT='LDAP WebMgr'

#. bottle
BIND_HOST='127.0.1.1'
BIND_PORT=8080

#. ldap 
LDAP_HOST = '10.10.5.30'
LDAP_BASE = 'dc=ldap,dc=lab'
LDAP_USER = 'ou=Users,%s' % (LDAP_BASE)
LDAP_ADMIN = 'cn=admin,%s' % (LDAP_BASE)
LDAP_PWD = '1qaz2wsx'
