#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import json
from os.path import dirname, abspath

import requests
from BeautifulSoup import BeautifulSoup

reload( sys )
sys.setdefaultencoding('utf-8')
PREFIX = dirname(abspath(__file__))

class Spider(object):
    '''To scrape all topic from http://huati.weibo.com/.'''
    def __init__(self):
        pass

    def send_request(self,i=1,retry=-1):
        '''To send a request.

        Use the url which http://huati.weibo.com/ transmit json data.'''
        retry = retry + 1
        url = ''.join([
            'http://huati.weibo.com/aj_topiclist/big?ctg1=99&ctg2=0&prov=0&sort=time&p=',
            str(i)])
        response = requests.get(url,headers={'X-Requested-With':'XMLHttpRequest'})
        self.parse_response(i,retry,response)

    def parse_response(self,i,retry,response):
        '''Parse the response to to get titile,url,description.

        Use BeautifulSoup to parse the response.'''
        if response.status_code != requests.codes.ok and retry < 3:
            self.send_request(i,retry)
        html = json.loads(response.content)['data']['html']
        soup = BeautifulSoup(''.join(html))
        title = soup.findAll('a',{'class':'name'})
        desc = soup.findAll('p',{'class':'info W_textc'})
        with open('%s/data.txt' % PREFIX,'a') as file:
            count = 0
            for a,b in zip(title,desc):
                count = count + 1
                file.write(''.join(['topic: ',str((i-1)*20+count)])+'\n'
                           +''.join(['url: ','http://huati.weibo.com',a['href']])+'\n'
                           +''.join(['title: ',a.string])+'\n'
                           +''.join(['des: ',b.string])+'\n'
                           +'\n')
        if soup.findAll(text='下一页'):
            i = i + 1
            self.send_request(i)

if __name__ == '__main__':
    spider = Spider()
    spider.send_request()
