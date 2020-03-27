# Coded : AkasakaID
# 27/03/2020

import requests,time,os,re
r = requests.Session()
from bs4 import BeautifulSoup as bs
def tunggu(t):
	while t:
		wd='Tengga salebetipun '+str(t)+" detik "
		print(wd,end='\r',flush=True)
		time.sleep(1)
		t -= 1
merah = '\x1b[1;31m'
hijau = '\x1b[1;32m'
kuning = '\x1b[1;33m'
biru = '\x1b[1;34m'
magenta = '\x1b[1;35m'
cyan = '\x1b[1;36m'
putih = '\x1b[1;37m'
def bn():
	if os.name == 'nt':os.system('cls')
	else:os.system('clear')
	print(f"""{putih}
	    _   __                  _ ______           __  
	   / | / /___ _____  ____  (_)_  __/______  __/ /__
	  /  |/ / __ `/ __ \/ __ \/ / / / / ___/ / / / //_/
	 / /|  / /_/ / /_/ / /_/ / / / / / /  / /_/ / ,<   
	/_/ |_/\__, /\____/ .___/_/ /_/ /_/   \__,_/_/|_|  
	      /____/     /_/                               

	{hijau}Dipunngasta dening {putih}NgopiTruk
	{cyan}Matur sembah nuwun dhateng sedaya member NgopiTruk
	{kuning}Dolanan litecoin-free {putih}
	""")
user = input("Mlebetaken username: ")
pw = input("Mlebetaken password: ")
bn()
dashboard = 'http://litecoin-free.com/Dashboard'
ua = 'Mozilla/5.0 (Linux; Android 7.1.2; G011A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
try:
	aa = r.post('http://litecoin-free.com/login',headers={'user-agent':ua},data={"username": user,"password": pw,"login_btn": "Sign In"})
	a = r.get(dashboard,headers={'user-agent':ua}).text
	b = bs(a,'html.parser')
	if not b.find('strong'):
		print(f'{merah}Mboten saget mlebet')
		exit()
	else:
		bb = b.findAll("div",attrs={"class":'stat-text'})
		print(f"{hijau}Sugeng Rawuh{putih}"+b.find('strong').text.replace("Welcome",""))
		print(f"{hijau}Saldo panjenengan{putih}:",bb[0].text.strip(),"LTC")
		print(" ")
		while True:
			r.get('http://litecoin-free.com/earn/money-1',headers={'user-agent':ua})
			r.get('http://litecoin-free.com/balance/balance-1.php',headers={'user-agent':ua})
			a = r.get(dashboard,headers={'user-agent':ua}).text
			b = bs(a,'html.parser')
			bb = b.findAll("div",attrs={"class":'stat-text'})
			print(f"{hijau}Saldo panjenengan{putih}:",bb[0].text.strip(),"LTC")
			tunggu(30)
except KeyboardInterrupt:
	print("Metu soko program..!!")
	exit()
except Exception as e:
	print("Error",e)
	exit()