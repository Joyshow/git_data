from bs4 import BeautifulSoup
import requests
import re
import time

urls="https://www.jianyu360.cn/list/stype/ZBGG_ZB.html"
#urls="https://www.kugou.com/yy/rank/home/1-8888.html?from=rank"


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

def get_info(url):
	wb_data = requests.get(url,headers=headers)
	soup = BeautifulSoup(wb_data.text,'lxml')
	tittles = soup.select('#allnews > div.lucene > ul > li > div > div.luce-left > div > a')
	#tops = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num')
	#songname = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
	#rankWrap > div.pc_temp_songlist > ul > li:nth-child(4) > span.pc_temp_num
	#address = soup.select()
	return tittles

	#return songname
	
#rankWrap > div.pc_temp_songlist > ul > li:nth-child(1) > span.pc_temp_num > strong
for titles in get_info(urls):
	titles=str(titles)
	bi=re.findall('>.+<',titles)
	ti=re.findall('dataid=\".+3D\"',titles)
	bi=str(bi)
	ti=str(ti)
	bi=bi[3:-3]
	ti=ti[10:-3]
	p={bi:ti}
	print(p)
	#print(ti)
	#print(titles.get_text())
	
#rankWrap > div.pc_temp_songlist > ul > li:nth-child(1) > a

