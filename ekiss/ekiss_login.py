#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import random
import sys
from datetime import datetime
import time

header = {
        'Referer' : 'http://ekiss.huvitz.com/',
        'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0)'
}

agent_list = [
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0)',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
]

LOGIN_INFO = {
    'txtId': '050031',
    'txtPwd': 'ekissc8c8',
    'btnLogin.x' : '62',
    'btnLogin.y' : '21' ,
    'ddlLang' : 'ko'
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    # select agent
    header['User-Agent'] = agent_list[random.randrange(0,5)]

    first_page = s.get('http://ekiss.huvitz.com/', headers=header)
    html = first_page.text
    soup = bs(html, 'html.parser')

    # extract hidden input fields 
    v = soup.find('input', {'name': '__VIEWSTATE'}) 
    LOGIN_INFO['__VIEWSTATE'] = v['value']
    v = soup.find('input', {'name': '__VIEWSTATEGENERATOR'}) 
    LOGIN_INFO['__VIEWSTATEGENERATOR'] = v['value']
    v = soup.find('input', {'name': '__EVENTVALIDATION'}) 
    LOGIN_INFO['__EVENTVALIDATION'] = v['value']

    LOGIN_INFO['btnLogin.x'] = random.randrange(20, 130)
    LOGIN_INFO['btnLogin.y'] = random.randrange(10, 70)




    # check date
    now = datetime.now()
    print('*', now)

    if now.weekday() == 5 or now.weekday() == 6:
        print('weekend')
        raise Exception('Weekend. Do not login !!!!!')

    # check time
    if now.hour > 9 and now.hour < 18:
        print('working hours')
        raise Exception('Working hours !!!!!')


    # dbg halt
    #print("dbg halt")
    #sys.exit(0)


    # try login
    #print(header)
    #print(LOGIN_INFO)
    print("Login ekiss...")
    login_req = s.post('http://ekiss.huvitz.com/login.aspx', headers=header,data=LOGIN_INFO)
    #print(login_req.status_code)
    # 200 means success

    if login_req.status_code != 200:
        print("login error:", login_req.status_code)
        print(html)
        raise Exception('LOGIN ERROR. Check the code !!!!!')

    print("OK")
    
    # main page
    page = s.get('http://ekiss.huvitz.com/main.aspx')
    #soup = bs(page.text, 'html.parser') 
    #print(soup)

    # sleep 
    sleep_sec = random.randrange(0, 60 * 10)
    print("Sleep", sleep_sec, "second(s)...")
    time.sleep(sleep_sec)



    header['Referer'] = 'http://ekiss.huvitz.com/main.aspx'

    if now.hour < 9:
        # go to work page
        print("Open go to work page...")
        page = s.get('http://ekiss.huvitz.com/board/work_In.aspx', header=header)
    elif now.hour >= 18:
        # leave work page
        print("Open leave work page...")
        page = s.get('http://ekiss.huvitz.com/board/work_Out.aspx', headers=header)

    if page.status_code != 200:
        print("work page error:", page.status_code)
        print(page.text)
        raise Exception('work page ERROR. Check the code !!!!!')

    print("Completed.")

    # log out
    #logout_req = s.get('http://ekiss.huvitz.com/logout.aspx', headers=header)
    #soup = bs(logout_req.text, 'html.parser')
    #print(soup)
