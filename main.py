import json
import os

import colorama
import requests
from colorama import Fore, Back, Style
from proxy_checker import ProxyChecker


def notification(what, text):
    if what == 'error':
        print(Back.RED + Fore.BLACK + ' ' + text + ' ' + Style.RESET_ALL)
    if what == 'warning':
        print(Back.YELLOW + Fore.BLACK + ' ' + text + ' ' + Style.RESET_ALL)
    if what == 'notice':
        print(Back.CYAN + Fore.BLACK + ' ' + text + ' ' + Style.RESET_ALL)
    if what == 'success':
        print(Back.LIGHTGREEN_EX + Fore.BLACK + ' ' + text + ' ' + Style.RESET_ALL)
    if what == 'settings':
        print(Back.MAGENTA + Fore.BLACK + ' ' + text + ' ' + Style.RESET_ALL)


def downloadPage(url):
    try:
        r = requests.get(url, proxies=settings['proxies'], timeout=settings['timeout'])
        return r
    except requests.exceptions.RequestException as err:
        raise err


def checkProxy(proxy):
    pc = checker.check_proxy(proxy)
    if pc:
        print('Connected to proxy')
    else:
        notification('error', 'Can\'t connect to proxy')


def getProductList(website):
    if website == 'footLockerUS':
        pageSource = downloadPage('https://www.footlocker.com/category/mens/shoes.html')
    else:
        notification('warning', 'Website \'' + website + '\' not implemented!')


def editSettings():
    if os.path.exists('settings.json'):
        with open("settings.json") as json_file:
            key = input("What setting would you like to configure?")
            try:
                data = json.load(json_file)
                if key not in data:
                    return notification('error', 'That setting doesnt exist!')
                value = input("What setting would you like to configure?")
                data[key] = value
                json.dump(data, open("settings.json", "w"), indent=4)
                json_file.close()
                notification('success', 'Successfully changed ' + key + ' to ' + value)
            except NameError or InterruptedError or ValueError or TypeError:
                notification('error', 'An error has occurred, ensure you are using the correct types and values!')


def loadSettings():
    if os.path.exists('settings.json'):
        with open('settings.json') as json_file:
            try:
                notification('success', 'Loaded settings file')
                return json.load(json_file)
            except ValueError:
                notification('error', 'Invalid settings file!')
                exit()
    else:
        notification('error', 'Can\'t find settings file!')
        exit()


def viewSettings():
    if os.path.exists('settings.json'):
        try:
            settingsFile = open("settings.json")
            settingsOverview = json.load(settingsFile)
            notification('settings', str(settingsOverview))
            settingsFile.close()
        except ValueError:
            notification('error', 'An error has occurred while displaying settings!')
            exit()
    else:
        notification('error', 'Can\'t find settings file!')
        exit()


colorama.init()
settings = loadSettings()
checker = ProxyChecker()
