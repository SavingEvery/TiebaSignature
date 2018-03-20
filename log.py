# -*- coding:utf-8 -*-

'''
Created on 20171122
@author:wyl QQ635864540

Python 2.7
'''
__author__ = 'wyl QQ635864540'

class ClsLog:
	def __init__(self):
		self.logfile = 'log.txt'
		
	def WriteToLog(self, loginfo):
		with open(self.logfile, 'a') as f:
			f.write(loginfo)
			f.close()
			
if __name__=='__main__':
	cls = ClsLog()
	cls.WriteToLog('test' + '\n')
	cls.WriteToLog('test' + '\n')
	cls.WriteToLog('test' + '\n')
	cls.WriteToLog('test' + '\n')