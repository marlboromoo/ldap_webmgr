# LDAPWebMgr

A simple management tool for LDAP server.
```
   __   ___  ___   ___ _      __    __   __  ___        
  / /  / _ \/ _ | / _ \ | /| / /__ / /  /  |/  /__ _____
 / /__/ // / __ |/ ___/ |/ |/ / -_) _ \/ /|_/ / _ `/ __/
/____/____/_/ |_/_/   |__/|__/\__/_.__/_/  /_/\_, /_/   
                                             /___/      
```

## Requirments 
 - Python
 - [Bottle] [1]
 - [Python-LDAP] [2]
 - [uWSGI] [3] (option)
 - [nginx] [4] (option)
                                                                                
## Install

### Build-in server
```
sudo su -
cd /var/www/
git clone https://github.com/marlboromoo/ldap_webmgr.git
cd ldap_webmgr
pip install bottle python-ldap
python ./web.py
```

### Nginx + uWSGI
```
#. ubuntu 12.04
sudo su -
apt-get install uwsgi uwsgi-plugin-python nginx 
pip install bottle python-ldap
cd /var/www/
git clone https://github.com/marlboromoo/ldap_webmgr.git
cd ldap_webmgr 
#. uWSGI config
cp doc/uwsgi.xml /etc/uwsgi/apps-available/ldap_webmgr.xml
ln -s  /etc/uwsgi/apps-available/ldap_webmgr.xml /etc/uwsgi/apps-enabled/
/etc/init.d/uwsgi restart
#. nginx config
cp doc/nginx.conf /etc/nginx/sites-available/ldap_webmgr
ln -s /etc/nginx/sites-available/ldap_webmgr /etc/nginx/sites-enabled/
/etc/init.d/nginx restart
```

## Upgrade
```
cd /var/www/ldap_webmgr
git pull
/etc/init.d/uwsgi restart
```
## TODO
 - ...

## Author                                                                       
Timothy.Lee a.k.a MarlboroMoo.                                                  
                                                                                
## License                                                                      
Released under the [MIT License] [4].                                           
                                                                                
  [1]: http://bottlepy.org "Bottle"
  [2]: http://www.python-ldap.org/ "Python-LDAP"
  [3]: http://projects.unbit.it/uwsgi/ "uWSGI"
  [4]: http://nginx.org/ "Nginx"
  [4]: http://opensource.org/licenses/MIT "MIT License"

