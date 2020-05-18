#!/usr/bin/python3
import os
import threading
import requests

pid=os.getpid()
print("PID is : " , pid)


if os.name == "posix":
    print("Loadavg is : " , os.getloadavg())
else:
    print("OS system is not Linux")


one_min, five_min, fifteen_min = os.getloadavg()
count = os.cpu_count()

print("5 min loadavg is:" ,five_min)
print("Numbers of CPUs : " , count)

if(count-five_min < 1) :
    print("exit the script")
else : 
    print("loadavg value is not close to the cpu core count")


def checking(url):
    print("checking url...." , url)
    if(response.status_code ==200):
        print("The url is valid")
    else:
        print("The url is not found")

for url in ['https://api.github.com' , 'http://bilgisayar.mu.edu.tr/' , 'https://www.python.org', 'http://akrepnalan.com/ceng2034' , 'https://github.com/caesarsalad/wow']:
    response = requests.get(url)

    threads = threading.Thread(target = checking, args=(url,))
    threads.start()




