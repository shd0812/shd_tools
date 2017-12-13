#coding:utf-8
import logging
import readconfig
import os
import threading
import time

rc =readconfig.ReadConfig()
#print rc.getOther('logpath')
resultPath = rc.getOther('logpath')
class Clog():
	def __init__(self):
		logPaths = os.path.join(resultPath, (time.strftime('%Y%m%d', time.localtime())))
		if os.path.exists(logPaths) is False:
			os.makedirs(logPaths)
		
		LOG_PATH = os.path.join(logPaths,'dd.log')
		self.logger = logging.getLogger()
		#创建一个handler,用于写入日志文件
		fileHandler = logging.FileHandler(LOG_PATH)
		
		#创建一个handler，用于输出到控制台
		#ch = logging.StreamHandler()
		
		#日志输出
		fmt = '\n' + '%(asctime)s - %(filename)s:%(lineno)s	 - %(message)s'
		formatter = logging.Formatter(fmt)
		fileHandler.setFormatter(formatter)
		#ch.setFormatter(formatter)
		#把logger 添加handler
		self.logger.addHandler(fileHandler)
		#self.logger.addHandler(ch)
		#默认的级别是logging.NOTSET, 表示处理所有的日志消息
		self.logger.setLevel(logging.INFO)
		

	def build_case(self,casename):
		casename = " --------------------  " +casename+"   --------------------"
		self.logger.info(casename)
	def collect_error(self,casename):
		
		casename = " --------------------  " +str(casename)+"   --------------------"
		self.logger.error(casename)	

	def DebugMessage(self, msg):
		self.logger.debug(msg) 
		pass
	def write_result(self, result):

		report_path = os.path.join(resultPath, "report.txt")
		flogging = open(report_path, "a")
		try:
			flogging.write(result+"\n")
		finally:
			flogging.close()
		pass
# oc = Clog()
if __name__ == '__main__':
	oc = Clog()
	oc.build_case(u'22222')
	oc.collect_error(u'3333')
	oc.write_result('ok')
	
