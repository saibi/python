#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import random
import sys
from datetime import datetime
import time


Header = {
        'Referer' : 'http://ekiss.huvitz.com/',
        'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0)'
}

Agent_list = [
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0)',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
]

print("fill txtId & txtPwd first.");
sys.exit(0) 

LOGIN_INFO = {
    'txtId': 'FILL',
    'txtPwd': 'FILL',
    'btnLogin.x' : '62',
    'btnLogin.y' : '21' ,
    'ddlLang' : 'ko'
}

# select agent
agent = Agent_list[random.randrange(0,5)]
Header['User-Agent'] = agent


# default checkin/checkout time
NORMAL_CHECKIN_HOUR = 9
NORMAL_CHECKOUT_HOUR = 18
CHECKIN_HOUR = 9
CHECKOUT_HOUR = 18

# check date
#now = datetime.now()
now = datetime(2020,7,3,12,45,3)
print("set test datetime:", now)


print('*', now, agent)

if now.weekday() == 5 or now.weekday() == 6:
    print('Weekend. Do not login !!!!!')
    sys.exit(0) 

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



# exception rule

EXCEPTION_FILE="/tmp/checkin/exception_date.txt"
# format 
# yyyy/mm/dd [checkin [11|13]] [checkout [12]] 
# 2019/07/04 checkin checkout   # checkin ON, checkout ON
# 2019/07/04 checkin            # checkin ON, checkout OFF
# 2019/07/05 checkout           # checkin OFF, checkout ON
# 2019/07/05                    # checkin OFF, checkout OFF
# 2019/07/06 checkin 11         # checkin at 11:00 (10:40~10:55) : morning off (1/4)
# 2019/07/06 checkin 13         # checkin at 13:00 (12:40~12:55) : morning off (1/2)
# 2019/07/06 checkout 12        # checkout at 12:00 (12:00~12:55) : afternoon off (1/2)

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






exception_list = read_exception_file()
if exception_list:
    for line in exception_list:
        if line[0] == '#':
            continue
        if line.strip() == "":
            continue

        date_val = convert_line_to_date(line)
        if date_val != None:
            option_val = ""
            if 'check' in line:
                option_val = line.split(" ",maxsplit=1)[1]

            if date_val == now.date(): 
                print("DBG 1", line, option_val)
                # override checkin time
                if 'checkin' in option_val:
                    if '11' in option_val:
                        CHECKIN_HOUR=11
                    elif '13' in option_val:
                        CHECKIN_HOUR=13
                else:
                    checkin_flag = False
                    print("DBG 2")

                if not 'checkout' in option_val:
                    checkout_flag = False
                else:
                    if '12' in option_val:
                        CHECKOUT_HOUR=12

                print('Apply exception: "', line.rstrip('\n'), '"' )
                if CHECKIN_HOUR != NORMAL_CHECKIN_HOUR:
                    print("  Checkin hour :", CHECKIN_HOUR)
                    if now.hour < CHECKIN_HOUR-1:
                        print("Checkin hour not reached.")
                        checkin_flag = False
                    elif now.hour > CHECKIN_HOUR:
                        print("Checkin hour passed.")
                        checkin_flag = False
                    elif now.minute < 10:
                        print("Checkin minute not reached. (< 30min) ")
                        checkin_flag = False
                    else:
                        checkin_flag = True

                if CHECKOUT_HOUR != NORMAL_CHECKOUT_HOUR:
                    print("  Checkout hour :", CHECKOUT_HOUR)
                    if now.hour > CHECKOUT_HOUR + 1:
                        print("Checkout hour passed.")
                        checkout_flag = False
                    else: 
                        checkout_flag = True
                print("Checkin =", checkin_flag, ", Checkout =", checkout_flag)
                        
# check time
if now.hour > CHECKIN_HOUR and now.hour < CHECKOUT_HOUR:
    print('Working hours !!!!!')
    sys.exit(0) 

if checkin_flag == False and checkout_flag == False:
    print("Canceled.")
    sys.exit(0)


# error code
ERR_LOGIN = 1
ERR_MOBILE_AUTH = 2
ERR_PAGE = 3
ERR_LATER = 4
ERR_ALREADY = 5
ERR_CHECKIN_FIRST = 6

def login_ekiss(open_type):

    # start ekiss login
    with requests.Session() as s:

        print("open ekiss.huvitz.com")
        first_page = s.get('http://ekiss.huvitz.com/', headers=Header)
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

        # dump Header & login info
        #print(Header)
        #print(LOGIN_INFO)

        WAIT_SEC = 2 
        print("wait", WAIT_SEC, " seconds")
        time.sleep(WAIT_SEC) 

        # try login
        print("Login ekiss...")
        login_req = s.post('http://ekiss.huvitz.com/login.aspx', headers=Header,data=LOGIN_INFO)
        # login_req.status_code 200 means success
        
        if login_req.status_code != 200:
            print('LOGIN ERROR. Check the code !!!!!', login_req.status_code)
            print(html)
            return ERR_LOGIN

        time.sleep(1) 

        # main page
        soup = bs(login_req.text, 'html.parser') 
        result = soup.find('a', { 'class' : 'btn_logout' } )
        if result == None:
            # need mobile msg auth
            print("NEED MOBILE MSG AUTH")
            print(login_req.text)
            return ERR_MOBILE_AUTH

        print("OK")

        page = None
        Header['Referer'] = 'http://ekiss.huvitz.com/main.aspx'

        if open_type == "checkin":
            result = soup.find('a', { 'id' : 'btnWorkIn' } )
            if result != None and str(result).find('btn_attendance_off') < 0:
                #print("Open checkin page...")
                #page = s.get('http://ekiss.huvitz.com/board/work_In.aspx', headers=Header) 
                print("Open fake checkin page...")
                page = s.get('http://ekiss.huvitz.com/main.aspx', headers=Header) 
            else:
                print("already checked in.")
                return ERR_ALREADY
        elif open_type == "checkout":
            result = soup.find('a', { 'id' : 'btnWorkOut' } )
            if result != None and str(result).find('btn_attendance_off') < 0:
                #print("Open checkout page...")
                #page = s.get('http://ekiss.huvitz.com/board/work_Out.aspx', headers=Header) 
                print("Open fake checkout page...")
                page = s.get('http://ekiss.huvitz.com/main.aspx', headers=Header) 
            else:
                print("Checkout btn is disabled. Try checkin first.")
                return ERR_CHECKIN_FIRST
        else:
            print("invalid type")

        if page != None and page.status_code == 200:
            print("Completed.")
        elif page == None:
            print('Try later.')
            return ERR_LATER
        else:
            print("work page error:", page.status_code)
            print(page.text)
            return ERR_PAGE

        return 0



# need random sleep 
sleep_sec = random.randrange(0, 60 * 15)
#print("Sleep", sleep_sec, "second(s)...")
#time.sleep(sleep_sec) 
print("skip Sleep", sleep_sec, "second(s)...")


if checkin_flag:
    open = "checkin"
elif checkout_flag:
    open = "checkout"

retry_count = 0
while retry_count <= 3:
    if retry_count > 0:
        print("Retry #", retry_count, ".....")
        time.sleep(1)

    ret = login_ekiss(open)
    if ret == ERR_MOBILE_AUTH:
        retry_count = retry_count + 1
        print("mobile auth. wait 60 seconds")
        time.sleep(60)
    elif ret == ERR_LATER:
        retry_count = retry_count + 1
        time.sleep(30)
    elif ret == ERR_LOGIN:
        retry_count = retry_count + 1
        time.sleep(20)
    elif ret == ERR_PAGE:
        retry_count = retry_count + 1
        time.sleep(10)
    else: 
        break;

