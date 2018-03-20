# -*- coding:utf-8 -*-

'''
Created on 20171122
@author:wyl QQ635864540

Python 2.7
'''

import re
import urllib2
import urllib
import time
import getallbars

import log

class TieBaLoginCls:
	def __init__(self, bars):
		self.url = 'http://tieba.baidu.com/sign/add'
		self.bars=bars
		self.sleeptime = 0
		self.logcls = log.ClsLog()

	def BarLogin(self):
		cookie = ''
		with open('cookie.txt', 'r') as f:
			cookie = f.read()
			f.close()
		if cookie == '':
			print '\'cookie.txt\' file may not exist, create it and write your cookie in it. Then retry.'
			time.sleep(10)
			return
		curdate = time.strftime('%Y-%m-%d')
		self.logcls.WriteToLog(curdate + '\n')
		for bar in self.bars:
			print bar
			bar =bar.decode('gbk').encode('utf-8')
			data = {
				'ie':'utf-8',
				'kw':bar,
				'tbs':'fd0f4225389cc40f1511449126'
				}
			headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
				'Accept-Language':'zh-CN,zh;q=0.8',
				'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
				'Cookie':'%s',
				'Host':'tieba.baidu.com',
				'Origin':'http://tieba.baidu.com',
				'Proxy-Connection':'keep-alive',
				'Referer':'http://tieba.baidu.com/f?kw=%s&fr=index&fp=0&ie=utf-8',
				'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
				'X-Requested-With':'XMLHttpRequest'
				}
			headers['Referer'] = headers['Referer'] % bar
			headers['Cookie'] = headers['Cookie'] % cookie
			try:
				request = urllib2.Request(url = self.url, data=urllib.urlencode(data), headers = headers)
				response = urllib2.urlopen(request)
				html = response.read()
				response.close()
				if html.find('errmsg') != -1:
					errindex = html.find('errmsg')
					msgindex = html.find('",', errindex)
					msgstr = html[errindex+9:msgindex]
					print 'errmsg:',msgstr
					if msgstr=='success':
						self.logcls.WriteToLog(bar + ' 吧自动签到成功\n')
				else:
					errorindex = html.find('error')
					errorendindex = html.find('",', errorindex)
					errorstr = html[errorindex + 8:errorendindex]
					print 'error:',errorstr
					if errorstr == 'need vcode':
						print 'You should input verify code by yourself.'
						print headers['Referer'].decode('utf-8').encode('gbk')
						i = raw_input()
						continue
			except Exception as e:
				print 'BarLogin exception:', str(e)
			if self.sleeptime != 0:
				print 'wait for',self.sleeptime,'seconds'
				time.sleep(self.sleeptime)
		
		
if __name__=='__main__':
	gb = getallbars.GetAllBars()
	bars = gb.FindAllBars()
	tl = TieBaLoginCls(bars)
	tl.BarLogin()