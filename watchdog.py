#!/usr/bin/python
import subprocess
import datetime

now = datetime.datetime.now()
n = now.strftime("%Y-%m-%d %H:%M")

#change the path for ./start on both variables to your path
status = subprocess.Popen(['./cs_go/start.sh','status'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
start = subprocess.Popen(['./cs_go/start.sh','start'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

ret = status.communicate()[0]
out = open('./cs_go/log_watchdog.txt','a')
def watchdog():
  if 'UP' in ret:
    out.write(str(n)+": Server UP \n")
  elif 'DOWN' in ret:
    out.write(str(n)+': Your server was DOWN \n')
  return start
  
watchdog()
out.close()
