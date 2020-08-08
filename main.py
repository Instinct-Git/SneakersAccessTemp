import colorama, requests, json, os
from colorama import Fore, Back, Style
from proxy_checker import ProxyChecker


def notif(what, text):
	if what == 'error':
		print(Back.RED + Fore.WHITE + ' ' + text + ' ' + Style.RESET_ALL)
	if what == 'warning':
		print(Back.YELLOW + Fore.BLACK + ' ' + text + ' ' + Style.RESET_ALL)
	if what == 'notice':
		print(Back.AQUA + Fore.BLACK + ' ' + text + ' ' + Style.RESET_ALL)
	if what == 'success':
		print(Back.GREEN + Fore.BLACK + ' ' + text + ' ' + Style.RESET_ALL)

def downloadPage(url):
	try:
		r = requests.get(url, proxies=settings['proxies'], timeout=settings['timeout'])
		return r
	except requests.exceptions.RequestException as err:
		raise err

#TODO: check if sites block the proxy
def checkProxy(proxy):
	pc = checker.check_proxy(proxy)
	
	if pc != False:
		print('Connected to proxy')
	else:
		notif('error', 'Can\'t connect to proxy')

def getProductList(website):
	if website == 'footLockerUS':
		pageSource = downloadPage('https://www.footlocker.com/category/mens/shoes.html')
		#...
	else:
		notif('warning', 'Website \'' + website + '\' not implemented!')

def loadSettings():
	if os.path.exists('settings.json'):
		with open('settings.json') as json_file:
			try:
				notif('success', 'Loaded settings file')
				return json.load(json_file)
			except ValueError:
				notif('error', 'Invalid settings file!')
				exit()
	else:
		notif('error', 'Can\'t find settings file!')
		exit()

colorama.init()
checker = ProxyChecker()
settings = loadSettings()
