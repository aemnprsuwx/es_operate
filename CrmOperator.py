#-*-coding:utf-8-*-
import time
import OaDataSystem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class CrmOperator:
	__index = ""
	__doc = ""
	__accessLog = ""
	__warningLog = ""
	__errorLog = ""
	__fileName = ""
	__fileType = ""

	def __init__(self, index, doc):
		self.__initParams(index, doc)

	# 初始化系统参数
	def __initParams(self, index, doc):
		self.__index = index
		self.__doc = doc
		# 获得日志路径
		self.__accessLog = OaDataSystem.Core.logAddress + "/run/" + str(index) + "/" 
		self.__errorLog = OaDataSystem.Core.logAddress + "/error/" + str(index) + "/"
		self.__warningLog = OaDataSystem.Core.logAddress + "/warning/"+ str(index) + "/" 
		# 获得系统时间和日志文件名
		todayStr = time.localtime(int(time.time()))
		todayData = time.strftime('%Y-%m-%d', todayStr)
		self.__fileName = str(todayData)
		self.__fileType = ".log"

	# 系统脚本运算数据
	def timeCaculate(self, functionName):
		beginTime = int(time.time())
		message = functionName()
		endTime = int(time.time())
		executeTime = endTime - beginTime
		message = str(message) + ", execute " + str(executeTime) + "s." 
		writeLog = OaDataSystem.UseCrmFile.UseFile(self.__accessLog, self.__fileName, self.__fileType, "utf-8")
		writeLog.writeDataInFile(message)
		return executeTime

	def logOperator(self, logStatus, content):
                todayStr = time.localtime(int(time.time()))
                todayData = time.strftime('%Y-%m-%d', todayStr)
                self.__fileName = str(todayData)
		if logStatus == OaDataSystem.Core.status['error']['code']:
			writeLog = OaDataSystem.UseCrmFile.UseFile(self.__errorLog, self.__fileName, self.__fileType, "utf-8")
			writeLog.writeDataInFile(content)
		elif logStatus == OaDataSystem.Core.status['warning']['code']:
			writeLog = OaDataSystem.UseCrmFile.UseFile(self.__warningLog, self.__fileName, self.__fileType, "utf-8")
			writeLog.writeDataInFile(content)
		else:
			writeLog = OaDataSystem.UseCrmFile.UseFile(self.__accessLog, self.__fileName, self.__fileType, "utf-8")
			writeLog.writeDataInFile(content)
