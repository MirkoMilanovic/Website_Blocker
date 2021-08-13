'''
This app blocks specific websites in some specific time span during the day.
'''

from datetime import datetime as dt
import time


host_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    now = dt.now().time()
    if '14:00:00' < str(now) < '16:00:00':
        hosts = open(host_temp, 'r+')
        content = hosts.read()
        for website in website_list:
            if website not in content:
                hosts.write(redirect + ' ' + website + '\n')
    else:
        hosts = open(host_temp, 'r+')
        content = hosts.readlines()
        for website in website_list:
            for line in content:
                if website not in line:
                    hosts.write(line)
    time.sleep(5)

