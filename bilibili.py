import sys
import gzip
from urllib import request
import requests

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

def get_name(url):
	url = url[:url.find("?")]
	url = url[len(url)-url[::-1].find("."):]
	return url

if __name__ == "__main__":
	if len(sys.argv) != 2:
		#print("Usage: python bilibili-VD.py <av number>")
		av = int(input("please input the av number you want to download!"))
	else:
		try:
			av = int(sys.argv[1])
		except:
			print("Usage: python bilibili.py <av number>")
	pageUrl = "https://www.bilibili.com/video/av%d/" % (av)
	pageReq = request.Request(pageUrl, headers=Headers)
	doc = request.urlopen(pageReq).read()
	try:  
		htmlStr = gzip.decompress(doc).decode("utf-8")  
	except:  
		htmlStr = doc.decode("utf-8")
	videoUrl = htmlStr[htmlStr.find('"url":')+len('"url":')+1:]
	videoUrl = videoUrl[:videoUrl.find('"')]
	type = get_name(videoUrl)
	#print(videoUrl)
	print("Start to download, please wait!")
	videoReq = request.Request(videoUrl, headers=download_Headers)
	video = request.urlopen(videoReq).read()
	with open("av%d.%s"%(av, type), "wb") as fp:
		fp.write(video)
	print("Finish!")
	
	