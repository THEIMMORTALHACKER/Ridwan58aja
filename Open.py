#!/usr/bin/python2
ASCII character '\xe2
see http://python.org/dev/peps/pep-0263/ for details

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

def next():
	os.system('bash')
