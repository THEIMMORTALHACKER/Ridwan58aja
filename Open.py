#!/usr/bin/python2
# coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
	

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
		
		
logo = """  \x1b[1;93m______   \x1b[1;92m_______  \x1b[1;94m______    \x1b[1;91m___   _\n \x1b[1;93m|      | \x1b[1;92m|   _   |\x1b[1;94m|    _ |  \x1b[1;91m|   | | |\n \x1b[1;93m|  _    |\x1b[1;92m|  |_|  |\x1b[1;94m|   | ||  \x1b[1;91m|   |_| |\n \x1b[1;93m| | |   |\x1b[1;92m|       |\x1b[1;94m|   |_||_ \x1b[1;91m|      _|\n \x1b[1;93m| |_|   |\x1b[1;92m|       |\x1b[1;94m|    __  |\x1b[1;91m|     |_ \n \x1b[1;93m|       |\x1b[1;92m|   _   |\x1b[1;94m|   |  | |\x1b[1;91m|    _  |\n \x1b[1;93m|______| \x1b[1;92m|__| |__|\x1b[1;94m|___|  |_|\x1b[1;91m|___| |_| \x1b[1;96mFB\n\n \x1b[1;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n ✫╬─ \x1b[1;92mReCode \x1b[1;91m: \x1b[1;93mRidwan58                  \x1b[1;95m─╬✫\n ✫╬─ \x1b[1;92mFB    \x1b[1;92m \x1b[1;91m: \x1b[1;96mFacebook.com/Ridwankechil     \x1b[1;95m─╬✫\n ✫╬─ \x1b[1;92mGitHub \x1b[1;91m: \x1b[1;94mGithub.com/RidwanKechil     \x1b[1;95m─╬✫\n ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

def siapa():
	os.system('clear')
	nama = raw_input("\033[1;97mSiapa nama kamu ? \033[1;91m: \033[1;92m")
	if nama =="":
		print"\033[1;96m[!] \033[1;91mIsi yang benar"
		time.sleep(1)
		siapa()
	else:
		os.system('clear')
		jalan("\033[1;97mSelamat datang \033[1;92m" +nama+ "\n\033[1;97mTerimakasih telah menggunakan tools ini !!")
		time.sleep(1)
		loginSC()
		
		
def loginSC():
	os.system('clear')
	print"\033[1;97mSilahkan login SC nya dulu bosque\n"
	username = raw_input("\033[1;96m[*] \033[1;97mUsername \033[1;91m: \033[1;92m")
	password = raw_input("\033[1;96m[*] \033[1;97mPassword \033[1;91m: \033[1;92m")
	if username =="Ridwan" and password =="Kechil":
		print"\033[1;96m[✓] \033[1;92mLogin success"
		time.sleep(1)
		login()
	else:
		print"\033[1;96m[!] \033[1;91mSalah!!"
		time.sleep(1)
                LoginSC()

def login():
	os.system('bash')
