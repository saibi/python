#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import random
import sys
from datetime import datetime
import time


def read_date_file():
    try:
        f = open("/tmp/date.txt", 'r')
    except FileNotFoundError:
        return []

    lines = f.readlines()
    f.close()

    return lines


def conv_line_to_date(line):
        return datetime.strptime(line.rstrip('\n').split(" ")[0], "%Y/%m/%d").date()

def read_date():
    item_list = []
    try:
        f = open("/tmp/date.txt", 'r')
    except FileNotFoundError:
        return item_list

    while True:
        line = f.readline()
        if not line:
            break;

        line = line.rstrip('\n')
        print(line)
        conv = line.split(" ")
        print(conv)

        line_date = datetime.strptime(conv[0], "%Y/%m/%d").date()
        print(line_date)

        item_list.append({ 'date' : line_date, 'line' : line })

    f.close()

    return item_list


list = read_date()

print(list)

all = read_date_file()

print(conv_line_to_date(all[1]))


print("DBG halt")
sys.exit(0)




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
    agent = agent_list[random.randrange(0,5)]
    header['User-Agent'] = agent

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

    # dump header & login info
    #print(header)
    #print(LOGIN_INFO)

    # check date
    now = datetime.now()
    print('*', now, agent)

    if now.weekday() == 5 or now.weekday() == 6:
        print('weekend')
        raise Exception('Weekend. Do not login !!!!!')

    # check time
    if now.hour > 9 and now.hour < 18:
        print('working hours')
        raise Exception('Working hours !!!!!')




    # try login
    print("Login ekiss...")
    login_req = s.post('http://ekiss.huvitz.com/login.aspx', headers=header,data=LOGIN_INFO)
    # login_req.status_code 200 means success
    
    if login_req.status_code != 200:
        print("login error:", login_req.status_code)
        print(html)
        raise Exception('LOGIN ERROR. Check the code !!!!!')

    
    # main page
    page = s.get('http://ekiss.huvitz.com/main.aspx')
    soup = bs(page.text, 'html.parser') 

    result = soup.find('a', { 'class' : 'btn_logout' } )
    if result == None:
        # need mobile msg auth
        print("NEED MOBILE MSG AUTH")
        print(page.text)
        raise Exception('NEED MOBILE MSG AUTH')

    print("OK")

    # need random sleep 
    sleep_sec = random.randrange(0, 60 * 10)
    print("Sleep", sleep_sec, "second(s)...")
    time.sleep(sleep_sec)

    page = None
    header['Referer'] = 'http://ekiss.huvitz.com/main.aspx'
    if now.hour < 9: 
        print("Open checkin page...")
        result = soup.find('a', { 'id' : 'btnWorkIn' } )
        if result != None and str(result).find('btn_attendance_off') < 0:
            # checkin
            page = s.get('http://ekiss.huvitz.com/board/work_In.aspx', headers=header)
        else:
            print("already checked in.")
    elif now.hour >= 18:
        print("Open checkout page...")
        result = soup.find('a', { 'id' : 'btnWorkOut' } )
        if result != None and str(result).find('btn_attendance_off') < 0:
            # checkout
            page = s.get('http://ekiss.huvitz.com/board/work_Out.aspx', headers=header)
        else:
            print("Checkout btn is disabled. Try checkin in first.")


    if page != None and page.status_code == 200:
        print("Completed.")
    elif page == None:
        print('Try later.')
    else:
        print("work page error:", page.status_code)
        print(page.text)
        raise Exception('work page ERROR. Check the code !!!!!')


    # log out
    #logout_req = s.get('http://ekiss.huvitz.com/logout.aspx', headers=header)
    #soup = bs(logout_req.text, 'html.parser')
    #print(soup)

    # dbg halt
    #print("dbg halt")
    #sys.exit(0)
