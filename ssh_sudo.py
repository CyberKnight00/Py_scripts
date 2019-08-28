#!/usr/pkg/bin/python

#Importing modules
import paramiko
import sys
import time

#setting parameters like host IP, username, passwd and number of iterations to gather cmds
HOST = "192.168.2.145"
ITERATION = 100
user = 'employee'
#A function that logins and execute commands
def fn(USER):
  client1=paramiko.SSHClient()
  #Add missing client key
  client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  #connect to switch
  client1.connect(HOST,username=USER,password=USER)
  print "SSH connection to %s established" %HOST
  
  (stdin, stdout, stderr) = client1.exec_command("sudo -l", get_pty = True)
  time.sleep(0.1) # some enviroment maybe need this.
  stdin.write(USER + '\n')
  print stdout.read()
  stdin.flush()
  # (stdin, stdout, stderr) = client1.exec_command("id", get_pty = True)
  # print stdout.read()
  client1.close()
  print "Logged out of device %s" %HOST

#for loop to call above fn x times. Here x is set to 3
for i in range (1,100):
  USER = user+str(i)
  print USER
  fn(USER)
  time.sleep(1) #sleep for 5 seconds