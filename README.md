# requirements
Django 3.0

# how to use:
EDIT `./CalibreWebCompanion/settings.json.bak`  
Remove the `.bak` from `db.sqlite3.bak` and `settings.json.bak`  
`./CalibreWebCompanion`     
run `./manage.py runserver`    

# Profiling

To do profiling, you have to create some dummy users  
Unbakify a file `./loadtesting/dummyusers.json.bak`  and fill in the credentials for the dummy users  

While django is running, open another shell and cd to `./loadtesting` and run `./bench.py`
To have a more interactive session, 
comment out 
```
run-time = 2m
headless = true
``` 
in `locust.conf`, and then run `./bench.py`
You can then go to [http://localhost:8089/](http://localhost:8089/) to see live graphs, tweak the number of users and more.

this is in development mode. don't actually use it or release it like this. The debug info it shows is spicy.  
# Features

- [x] Books
- [x] navbar with tags, series, authors, etc
- [x] Search
- [x] authentication 
- [x] Cache 
- [x]  Profiling with logging


# TODO
- [ ] cache with vary headers
- [ ] localisation
- [ ] Beautifying template
- [ ]  Setup email functionality

- [ ]  deploy


 