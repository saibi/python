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

# select agent
agent = agent_list[random.randrange(0,5)]
header['User-Agent'] = agent


# check date
now = datetime.now()
print('*', now, agent)

if now.weekday() == 5 or now.weekday() == 6:
    print('Weekend. Do not login !!!!!')
    #sys.exit(0) DBG

CHECKIN_HOUR = 9
CHECKOUT_HOUR = 18

# check time
if now.hour > CHECKIN_HOUR and now.hour < CHECKOUT_HOUR:
    print('Working hours !!!!!')
    #sys.exit(0) DBG

if now.hour < CHECKIN_HOUR:
    print("Checkin time")
    checkin_flag = True
else:
    checkin_flag = False

if now.hour >= CHECKOUT_HOUR:
    print("Checkout time")
    checkout_flag = True
else:
    checkout_flag = False



EXCEPTION_FILE="/tmp/checkin/exception_date.txt"

def read_exception_file():
    try:
        f = open(EXCEPTION_FILE, 'r')
    except FileNotFoundError:
        return []

    lines = f.readlines()
    f.close()

    return lines


def convert_line_to_date(line):
    try:
        val = datetime.strptime(line.rstrip('\n').split(" ")[0], "%Y/%m/%d").date()
    except ValueError:
        return None

    return val



# exception rule

exception_list = read_exception_file()
if exception_list:
    for line in exception_list:
        date_val = convert_line_to_date(line)
        if date_val != None:
            if date_val == datetime.now().date():
                if not 'checkin' in line:
                    checkin_flag = False
                if not 'checkout' in line:
                    checkout_flag = False

                print('Apply exception: "', line.rstrip('\n'), '"' )
                print("Checkin =", checkin_flag, ", Checkout =", checkout_flag)

if checkin_flag == False and checkout_flag == False:
    print("Canceled.")
    sys.exit(0)


with requests.Session() as s:

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


    # try login
    print("Login ekiss...")
    login_req = s.post('http://ekiss.huvitz.com/login.aspx', headers=header,data=LOGIN_INFO)
    # login_req.status_code 200 means success
    
    if login_req.status_code != 200:
        print('LOGIN ERROR. Check the code !!!!!', login_req.status_code)
        print(html)
        sys.exit(0)

    
    # main page
    page = s.get('http://ekiss.huvitz.com/main.aspx')
    soup = bs(page.text, 'html.parser') 

    result = soup.find('a', { 'class' : 'btn_logout' } )
    if result == None:
        # need mobile msg auth
        print("NEED MOBILE MSG AUTH")
        print(page.text)
        sys.exit(0)

    print("OK")

    # need random sleep 
    sleep_sec = random.randrange(0, 60 * 10)
    print("Sleep", sleep_sec, "second(s)...")
    #time.sleep(sleep_sec)

    #page = None
    header['Referer'] = 'http://ekiss.huvitz.com/main.aspx'
    if checkin_flag: 
        result = soup.find('a', { 'id' : 'btnWorkIn' } )
        if result != None and str(result).find('btn_attendance_off') < 0:
            print("Open checkin page...")
            #page = s.get('http://ekiss.huvitz.com/board/work_In.aspx', headers=header)
        else:
            print("already checked in.")
    elif checkout_flag:
        result = soup.find('a', { 'id' : 'btnWorkOut' } )
        if result != None and str(result).find('btn_attendance_off') < 0:
            print("Open checkout page...")
            #page = s.get('http://ekiss.huvitz.com/board/work_Out.aspx', headers=header)
        else:
            print("Checkout btn is disabled. Try checkin first.")


    if page != None and page.status_code == 200:
        print("Completed.")
    elif page == None:
        print('Try later.')
    else:
        print("work page error:", page.status_code)
        print(page.text)
        sys.exit(0)


    # log out
    #logout_req = s.get('http://ekiss.huvitz.com/logout.aspx', headers=header)
    #soup = bs(logout_req.text, 'html.parser')
    #print(soup)

    # dbg halt
    #print("dbg halt")
    #sys.exit(0)
