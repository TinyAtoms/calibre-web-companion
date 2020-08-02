
1. clone repo
2. pip install -r requirements.txt
3. install gunicorn and nginx
4. move this nginx.conf to /etc/nginx
5. make whatever user nginx runs as (in this case, massiveatoms) the owner of calibredir
6. give execute permissions to parent of calibredir
7. cd to repo, run `gunicorn CalibreWebCompanion.wsgi`
8. start nginx `sudo systemctl restart nginx`

Slight issues with this atm:
1. server_name in nginx.conf needs to be changed
2. User needs to be edited in nginx.conf, now it's just my user acc. This affectd step 4-6
3. where to do ssl?


Suggestions: 
1. We might want to use sockets instead of ip/port?
2. logging
3. autostart gunicorn/nginx
4. some extra instrumentation for gunicorn https://docs.gunicorn.org/en/latest/deploy.html