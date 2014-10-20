#!/usr/bin/python
# -*- coding: UTF-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
import json
import requests

class Instapush(object):
    def __init__(self, user_token):
        self.user_token = user_token
        self._headers = {}

    @property
    def headers(self):
        if not self._headers:
            self._headers = {'Content-Type': 'application/json',
                            'x-instapush-token': self.user_token}
        return self._headers

    def add_app(self, title):
        payload = {'title': title}
        ret = requests.post('http://api.instapush.im/v1/apps/add',
                            headers=self.headers,
                            data=json.dumps(payload)).json()
        return ret

    def list_app(self):
        ret= requests.get('http://api.instapush.im/v1/apps/list',
                         headers=self.headers).json()
        return ret


class App(object):
    def __init__(self, appid, secret):
        self.appid = appid
        self.secret = secret
        self._headers = {}


    @property
    def headers(self):
        if not self._headers:
            self._headers = {'Content-Type': 'application/json',
                            'x-instapush-appid': self.appid,
                            'x-instapush-appsecret': self.secret}
        return self._headers

    def add_event(self, event_name, trackers, message):
        payload = {'title': event_name,
                   'trackers': trackers,
                   'message': message}
        ret = requests.post('http://api.instapush.im/v1/events/add',
                            headers=self.headers,
                            data=json.dumps(payload)).json()
        return ret


    def list_event(self):
        ret = requests.get('http://api.instapush.im/v1/events/list',
                           headers=self.headers).json()
        return ret

    def notify(self, event_name, trackers):
        payload = {'event': event_name, 'trackers': trackers}
        ret = requests.post('http://api.instapush.im/v1/post',
                            headers=self.headers,
                            data=json.dumps(payload)).json()
        return ret

