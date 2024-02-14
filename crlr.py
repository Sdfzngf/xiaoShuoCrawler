import requests
from bs4 import BeautifulSoup
from lxml import etree
import sys
import getopt

wqd=False
firstz=''
fipth=''
ct=0

def wt(next):
	print('\"',next[1],'\"已爬取完毕','enter爬取下一章\n','q退出')
	if input()=='q':
		sys.exit(0)

def cnm(url):

	res=requests.get(url)
	content = BeautifulSoup(res.text, "html.parser")
	html=etree.HTML(res.text)
	zjmc=html.xpath('/html/body/div[1]/div[4]/div/div/div[2]/h1/text()')
	fi=open(fipth+'/'+str(ct)+'_'+zjmc[0]+'.txt','a+')
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

def stt():
	global firstz,fipth,wqd,ct
	if not wqd:
		firstz=input('请输入第一章的url:')
		fipth=input('下载目录:')
	next=cnm(firstz)
	wt(next)
	ct+=1
	while True:
		next=cnm(next[0])
		wt(next)
		ct+=1

if __name__=="__main__":
	#print("main")
	try:
		opts,args=getopt.getopt(sys.argv[1:],'u:p:')
	#	print('try')
	except getopt.GetoptError:
	#	print('except')
		stt()
		sys.exit(0)
	if len(sys.argv) > 1:
		wqd=True
	#	print('wqd',wqd)
		for opt,arg in opts:
			if opt in ['-u']:
				firstz=arg
			elif opt in ['-p']:
				fipth=arg
	stt()
	sys.exit(0)
