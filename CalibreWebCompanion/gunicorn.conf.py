import multiprocessing

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
preload_app = True # By preloading an application you can save some RAM resources as well as speed up server boot times
keepalive = 5
# daemon = True # Detaches the server from the controlling terminal and enters the background. disabled for now
# logging
errorlog = "/home/massiveatoms/Desktop/logs/gunicorn.log"
loglevel = "warning"


# debug settings which need to be commented out in prod
# reload=True
# reload_engine = "inotify"


# I only went till the section https://docs.gunicorn.org/en/latest/settings.html#logging there are more settings
# some of them might be useful