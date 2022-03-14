import os, requests, re, urllib.parse, sys
from time import *
from random import *
from datetime import *
import shutil,base64
from urllib.parse import *
from requests import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from time import *
from random import *
from string import *
from datetime import datetime
import time

os.system("clear")
ss = requests.session()
ck = "PHPSESSID=tnobhjv0al4p524e0tsn2jco24; _ga=GA1.1.425027146.1646794415; bitmedia_fid=eyJmaWQiOiI0ZjAwOWQ0YjkwYzEyZTkyOGFkYTYwYzQzOWI4NjUwYyIsImZpZG5vdWEiOiIxZWJjMWIwMjQ3ZDM4N2NlODRhODk4NGYyZDEzM2UzZiJ9; clever-last-tracker-53577=1; SesHashKey=4xwc2s1t94025ivy; SesToken=ses_id%3D87864%26ses_key%3D4xwc2s1t94025ivy; AccExist=87864; uuid=Pbdcf7de5-ebcc-4ecc-8873-696a9e5f7b3b; _ga_7Z81E54NN3=GS1.1.1647244763.9.0.1647244763.0; clever-counter-53577=0-1"
apisolve = "https://api-secure.solvemedia.com/papi/_challenge.js?k=5TuPjHOPoHvCPuSfsUohIl19kOkG2877;f=_ACPuzzleUtil.callbacks[0];l=en;t=img;s=standard;c=js,h5c,h5ct,svg,h5v,v/h264,v/ogg,v/webm,h5a,a/mp3,a/ogg,ua/chrome,ua/chrome99,os/nt,os/nt10.0,fwv/BluWwA.pniz56,jslib/jquery,htmlplus;am=DJtRuImRhZ0KwMAEiZGFnQ;ca=ajax;ts=1647243941;ct=1647244761;th=white;r=0.5129875125613557"
use = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
os.system("clear")
head = {
"user-agent":use,
"cookie":ck,
}
a = ss.get("https://earnbitmoon.club/",headers=head).text
tk = a.split('class="text-success">')[1].split('<')[0]
print("Tên Tài Khoản:",tk)
print("-"*40)
while True:
	try:
		head = {
"user-agent":use,
"cookie":ck,
}
		a = ss.get("https://earnbitmoon.club/",headers=head).text
		token = a.split("var token = '")[1].split("'")[0]
		if "You can claim again" in a:
			for z in range(300,-1,-1):
				print("Đợi",z,"giây",end=" \r")
				sleep(1)
		cap = {"Host": "api-secure.solvemedia.com","user-agent":use}
		tach = ss.get(apisolve,headers=head).text
		c = tach.split('"chid"     : "')[1].split('"')[0]
		img = ss.get("http://api.solvemedia.com/papi/media?c="+c+";w=300;h=150;fg=000000;bg=f8f8f8",headers=head,stream=True)
		if img.status_code==200:
			img.raw.decode_content=True
			with open("capt.jpg","wb") as f:
				shutil.copyfileobj(img.raw,f)
		head={
	"User-Agent":use,
	"content-type": "application/json",
	}
		with open("capt.jpg","rb") as i:
			img_read = i.read()
			img_en = base64.b64encode(img_read)
			img_en = img_en.decode("utf-8")
		data = {"requests":[{"image":{"content":img_en},"features":[{"type":"TEXT_DETECTION"}]}]}
		v = requests.post("https://vision.googleapis.com/v1/images:annotate?key=AIzaSyC3y-Em42htSB8UEZPqptJ78rlvL58_h6Y",json=data,headers=head)
		rs = v.json()["responses"][0]["textAnnotations"][0]["description"].replace("\n","_")
		rs = rs.split('Enter the following:_')[1].split('_Your Answer')[0].replace('_',' ')
		print("xong")
  sleep(1)
		head = {
"user-agent":use,
"cookie":ck,
}
		data = {
		"a":"getFaucet",
		"token":token,
		"captcha":"0",
		"challenge":c,
		"response":rs,
		}
		nhan = ss.post("https://earnbitmoon.club/system/ajax.php",data=data,headers=head).text
		if "your lucky number was" in nhan:
			head = {
"user-agent":use,
"cookie":ck,
}
	except:
		pass
	
