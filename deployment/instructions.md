
1. clone repo
2. pip install -r requirements.txt
3. install gunicorn and nginx
4. move this nginx.conf to /etc/nginx (as of now, it's not working)
5. make whatever user nginx runs as (in this case, massiveatoms) the owner of calibredir
6. give execute permissions to parent of calibredir

Slight issues with this atm:
1. allowed host in settings.json needs to have the ip/host/thing it will be used, as does line 47 from nginx.conf
2. User might need to be edited in nginx.conf, now it's just my user acc. This affectd step 4-6


Suggestions: 
1. We might want to use sockets instead of ip/port?
2. logging
3. autostart gunicorn/nginx