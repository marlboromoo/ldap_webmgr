#!/usr/bin/env python
# encoding: utf-8

"""
ldap_webmgr
"""

import ldap
import config

ldap_obj = None

def get_user(rdn):
    """@todo: Docstring for get_user.

    :user: @todo
    :returns: @todo

    """
    try:
        return ldap_obj.search_s(make_user_dn(rdn), ldap.SCOPE_BASE)
    except ldap.NO_SUCH_OBJECT:
        return None

def has_user(user, getrdn=False):
    """@todo: Docstring for has_user.

    :user: @todo
    :returns: @todo

    """
    attrs=['uid', 'cn']
    for attr in attrs:
        rdn = "%s=%s" % (attr, user)
        if get_user(rdn):
            return rdn if getrdn else True
    return None if getrdn else False

def list_user():
    """@todo: Docstring for list_user.
    :returns: @todo

    """
    try:
        return ldap_obj.search_s(config.LDAP_USER, ldap.SCOPE_ONELEVEL)
    except Exception: 
        return None


def make_user_dn(rdn):
    """@todo: Docstring for make_user_dn.

    :rdn: @todo
    :returns: @todo

    """
    return "%s,%s" % (rdn, config.LDAP_USER)

def edit_password(user, oldpwd, newpwd):
    """@todo: Docstring for edit_password.

    :user: @todo
    :oldpwd: @todo
    :newpwd: @todo
    :returns: @todo

    """
    rdn = has_user(user, getrdn=True)
    if rdn:
        dn = make_user_dn(rdn)
        try:
            ldap_obj.passwd_s(dn, oldpwd, newpwd)
            return True
        except ldap.UNWILLING_TO_PERFORM, e:
            del(e)
            #print e
            return False
    return False

def test():
    """@todo: Docstring for test.
    :returns: @todo

    """
    def _assert_equal(result, value):
        print result
        assert result == value
    r = has_user('spam', True); _assert_equal(r, 'cn=spam')
    r = has_user('foo', True); _assert_equal(r, 'uid=foo')
    r = has_user('bar'); _assert_equal(r, False)
    r = edit_password('spam', '1qaz2wsx', '12345678'); _assert_equal(r, True)
    r = edit_password('spam', '12345678', '1qaz2wsx'); _assert_equal(r, True)
    r = edit_password('foo', '12345678', '1qaz2wsx'); _assert_equal(r, False)
    #. list user
    users = list_user()
    for user in users:
        print type(user)
        print user

def init():
    """@todo: Docstring for init.
    :returns: @todo

    """
    global ldap_obj
    try:
        ldap_obj = ldap.open(config.LDAP_HOST)
        ldap_obj.simple_bind_s(config.LDAP_ADMIN, config.LDAP_PWD)
    except Exception, e:
        raise e

def close():
    """@todo: Docstring for close.
    :returns: @todo

    """
    global ldap_obj
    try:
        ldap_obj.unbind_s()
        ldap_obj = None
    except Exception, e:
        raise e

def main():
    init()
    test()
    close()

if __name__ == '__main__':
    main()

