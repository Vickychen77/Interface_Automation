# coding=utf-8

import requests,os,sys
from simplejson import JSONDecodeError

from .mac import *


class MACRequests():

    def __init__(self):
        self.timestamp=get_timestamp()
        self.nonce=get_nonce()
        self.sn=get_sn()
        self.signature=get_signature()
        self.base_url="http://mac.meizu.com"

    def get(self,url,payload=None):
        mac_url=self.base_url+url
        newpayload= {'sn': self.sn, 'nonce': self.nonce, 'timestamp': self.timestamp, 'signature': self.signature}

        if payload is not None:
            for key ,value in payload.items():
                newpayload[key]=value
        r =requests.get(mac_url,params=newpayload)

        try:
            result=r.json()
        except:
            result=r.text
        return result

    def post(self,url,data=None):
        mac_url=self.base_url+url
        mac_post_url=mac_url++ "?signature=" + self.signature + "&nonce=" + self.nonce + "&sn=" + self.sn + "&timestamp=" + self.timestamp
        r=requests.post(mac_post_url,data=data)

        try:
            result=r.json()
        except:
            result=r.text
        return result
