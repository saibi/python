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
    print(now)

    if now.weekday() == 5 or now.weekday() == 6:
        raise Exception('Weekend. Do not login !!!!!')

    # check time
    if now.hour > 9 or now.hour < 18:
        print("working hours")
        #raise Exception('Working hours !!!!!')

    if now.hour < 9:
        print("go to work")
    elif now.hour > 18:
        print("leave work")
    
    # sleep 
    #sleep_sec = random.randrange(0, 60 * 10)
    #print("Sleep", sleep_sec, "second(s)...")
    #time.sleep(sleep_sec)


    sys.exit(0)


    # try login
    print(header)
    print(LOGIN_INFO)
    login_req = s.post('http://ekiss.huvitz.com/login.aspx', headers=header,data=LOGIN_INFO)
    print(login_req.status_code)
    # 200 means success

    if login_req.status_code != 200:
        print(html)
        raise Exception('LOGIN ERROR. Check the code !!!!!')
    
    # main page
    main_page = s.get('http://ekiss.huvitz.com/main.aspx')
    soup = bs(main_page.text, 'html.parser') 
    print(soup)


    if now.hour < 9:
        print("go to work")
        # go to work page
        #gotowork_page = s.get('http://ekiss.huvitz.com/board/work_In.aspx')
    elif now.hour > 18:
        print("leave work")
        # leave work page
        #leavework_page = s.get('http://ekiss.huvitz.com/board/work_Out.aspx')


    # log out
    #logout_req = s.get('http://ekiss.huvitz.com/logout.aspx', headers=header)
    #soup = bs(logout_req.text, 'html.parser')
    #print(soup)
