import requests
from bs4 import BeautifulSoup
from lxml import etree
firstz=input('请输入第一章的url:')
fipth=input('下载目录:')
ct=0
def cnm(url):
	res=requests.get(url)
	content = BeautifulSoup(res.text, "html.parser")
	html=etree.HTML(res.text)
	zjmc=html.xpath('/html/body/div[1]/div[4]/div/div/div[2]/h1/text()')
	fi=open(fipth+'/'+zjmc[0]+'-'+str(ct)+'.txt','a+')
	print(zjmc)
	xsnr=content.find_all('p',attrs={'class':'content_detail'})
	fi.write(zjmc[0])
	for i in xsnr:
		print(i.string)
		fi.write(i.string)
		
	a='https://www.xswang.la'+html.xpath('/html/body/div[1]/div[4]/div/div/div[4]/a[4]/@href')[0]
	print(a)
	fi.close()
	return [a,zjmc[0]]

next=cnm(firstz)
print('\"'+next[1]+'\"已爬取完毕'+'enter爬取下一章')
input()
ct+=1
while True:
	next=cnm(next[0])
	print('\"'+next[1]+'\"已爬取完毕'+'enter爬取下一章')
	input()
	ct+=1
