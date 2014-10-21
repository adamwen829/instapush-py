Instapush-py
============

a Python wrapper for the Instapaper API.

#Installation
```Shell
pip install instapush
```

#Usage
```Python
from instapush import Instapush, App

insta = Instapush(user_token='xxxxxxx')

insta.list_app()             #List all apps

insta.add_app(title='title') #Create a app named title

app = App(appid='xxxx', secret='xxxx')

app.list_event()             #List all event

app.add_event(event_name='xxx', trackers=['email'],
              message='{email} is on.')

app.notify(event_name='xxx', trackers={'email': 'test@test.com'})
```

#TODO:
add unittest and travis service
