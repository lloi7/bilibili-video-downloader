import sys
import gzip
from urllib import request
import requests

Url =  "http://cn-sdbz-cu-v-06.acgvideo.com/upgcxcode/90/53/48775390/48775390-1-32.flv?expires=1533293100&platform=pc&ssig=iJNRosb9MI02IjCU8p3DIA&oi=3752278975&nfa=ZGlYLwTu0dW3o1gJGPmYTQ==&dynamic=1&hfa=2035758489&hfb=Yjk5ZmZjM2M1YzY4ZjAwYTMzMTIzYmIyNWY4ODJkNWI=&trid=26724c599b4344b8afcee0441a69e633&nfc=1" 
download_Headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
	"Referer":"https://www.bilibili.com/video/av28216827/?spm_id_from=333.334.chief_recommend.22",
	"Origin":"https://www.bilibili.com"
}

Headers = {
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#	"Accept-Encoding":"utf-8",
	"Accept-Language":"zh-CN,zh;q=0.9"
}

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python bilibili-VD.py <av number>")
	else:
		try:
			av = int(sys.argv[1])
		except:
			print("Usage: python bilibili-VD.py <av number>")
	pageUrl = "https://www.bilibili.com/video/av%d/" % (av)
	pageReq = request.Request(pageUrl, headers=Headers)
	doc = request.urlopen(pageReq).read()
	try:  
		htmlStr = gzip.decompress(doc).decode("utf-8")  
	except:  
		htmlStr = doc.decode("utf-8")
	videoUrl = htmlStr[htmlStr.find('"url":')+len('"url":')+1:]
	videoUrl = videoUrl[:videoUrl.find('"')]
	#print(videoUrl)
	print("Start to download, please wait!")
	videoReq = request.Request(videoUrl, headers=download_Headers)
	video = request.urlopen(videoReq).read()
	with open("av%d.flv"%(av), "wb") as fp:
		fp.write(video)
	print("Finish!")
	
	