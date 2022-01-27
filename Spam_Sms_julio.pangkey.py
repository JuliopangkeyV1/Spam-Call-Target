import requests
import time,os,sys


# clear
os.system('clear')
# logo
print ('==============><><><><><><><>================')
print ('[+] Creator : JULIO PANGKEY')
print ('[+] Yotube : KZ.TUTORIAL')
print ('[+] website : bit.ly/facebookprofilejuliophp')
print ('[+] whatsaap :  085757051840')
print ('==============><><><><><><><>================')
print ('')
print ('==============><><><><><><><>================')
print ('[•] order git vip termux ')
print ('[•] untuk lebih lanjut hububgi no !!!')
print ('[•] 085757051840')
print ('[•] kalo mau order hubungi admin !!!')
print ('______________________________________________')
print ('==============><><><><><><><>================|')
print ('|---------------------------------------------')
print ('|')
print ('|')
print ('|________________________________________________')
print ('[>>>>>>>>••WELCOM.TO.TERMUX.JULIOCYBER••<<<<<<<<<<|')
print ('-------------------------------------------------')
print ('|')
print ('|')
print ('|_______________________________')
print ('[+] Nomor di awali denggan 8xxx |')
print ('_-------------------------------')
print ('')

# Run nomor
nomor = input('[+] Nomor si ngentod masukin : ')
req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
if 'terkirim' in req:
     print ('\n[✓] =====SPAM BERHASIL TERKIRIM KE TARGET TOD====[✓]')
else:
     print ('\n[X) =====GAGAL TERKIRIM KURANG BERKAH KALI TOD===[X]')
