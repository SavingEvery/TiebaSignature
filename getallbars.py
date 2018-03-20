# -*- coding:utf-8 -*-

'''
Created on 20171122
@author:wyl QQ635864540

Python 2.7
'''

import urllib
import urllib2
import re
import time


class GetAllBars:
	def __init__(self):
		self.mainurl = ''
		self.url = 'http://tieba.baidu.com/f/like/mylike?&pn={}'
		self.compiler = re.compile(r'title="([^\s]*?)">', re.IGNORECASE)
		
	def FindAllBars(self):
		cookie = ''
		with open('cookie.txt', 'r') as f:
			cookie = f.read()
			f.close()
		if cookie == '':
			print '\'cookie.txt\' file may not exist, create it and write your cookie in it. Then retry.'
			time.sleep(10)
			return
		result = []
		page = 1
		while True:
			url = 'http://tieba.baidu.com/f/like/mylike?&pn={}'
			url = url.format(page)
			headers = {
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
				'Accept-Language':'zh-CN,zh;q=0.8',
				'Cache-Control':'max-age=0',
				'Cookie':'%s',
				'Host':'tieba.baidu.com',
				'Proxy-Connection':'keep-alive',
				'Upgrade-Insecure-Requests':'1',
				'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
				}
			headers['Cookie'] = headers['Cookie'] % cookie
			try:
				request = urllib2.Request(url=url, headers = headers)
				response = urllib2.urlopen(request)
				html = response.read()
				#print html
				findres=self.compiler.findall(html)
				if len(findres) is 0:
					response.close()
					break
				result = result + findres
			except Exception as e:
				print 'FindAllBars exception:', str(e)
			page = page + 1
			response.close()
			time.sleep(2)
		return result
		
if __name__=='__main__':
	gb=GetAllBars()
	result = gb.FindAllBars()
	print ''
	print len(result)
	for res in result:
		print res