#!/usr/bin/env python
# encoding: utf-8

"""
ldap_webmgr
"""

import bottle
import ldap_
import config

#app = bottle.Bottle()

@bottle.get('/')
def home(alert=False, alert_type=None, alert_title=None, alert_message=None):
    """@todo: Docstring for home.
    :returns: @todo

    """
    return bottle.template(
        'home', project=config.PROJECT,
        alert=alert,
        alert_type=alert_type,
        alert_title=alert_title,
        alert_message=alert_message,
        users=list_users(),
    )

def list_users(row=5):
    """@todo: Docstring for list_users.

    :row: @todo
    :returns: @todo

    """
    ldap_.init()
    result = ldap_.list_user()
    ldap_.close()
    users, i = [], 0
    while i <= row:
        if len(result) == 0:
            break
        dn, attrs = result.pop() 
        users.append(dict(rdn=dn.split(',')[0], dn=dn))
        i += 1
    return users

@bottle.get('/_static/<filepath:path>')
def get_static(filepath):
    """Return static file.
    """
    return bottle.static_file(filepath, root='./static/')

@bottle.post('/')
def password():
    """@todo: Docstring for password.
    :returns: @todo

    """
    form = bottle.request.forms
    ldap_.init()
    result = ldap_.edit_password(
        form.get('inputUsername'),
        form.get('inputOldPassword'),
        form.get('inputNewPassword'),
    )
    ldap_.close()
    if result:
        return home(
            alert=True,
            alert_type='alert-success',
            alert_title='Well done!',
            alert_message='Update password success.',
        )
    else:
        return home(
            alert=True,
            alert_type='alert-danger',
            alert_title='Oh snap!',
            alert_message='Fail to update password.',
        )

if __name__ == '__main__':
    bottle.run(
         host=config.BIND_HOST, port=config.BIND_PORT, debug=True, reloader=True)
else:
    application = bottle.default_app()

