import urllib2, urllib
import socket
import re
import os, inspect
import a_cf
from optparse import OptionParser
import s_c
from r_q import rqs
import rs_p
from l_g import lgt
from o_n import onh
from r_p import f_p
import sys
import time
import signal

options = onh()

def signal_handler(signal, frame):    
    print "\n---------------------------------------------------------------\nScanning interrupted"
    print "Scan result observed till now is stored in reflected.txt file\n"
    if options.shreflected ==True:
        print "-----------------------Scan Details------------------------"
        ref_file = open(path+'/'+'reflected.txt','r')
        print ref_file.read()
        ref_file.close()
    sys.exit(0)

signal.signal(signal.SIGINT,signal_handler)

CRLF = '\r\n\r\n'
path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
req_file = open(path+'/'+options.request,'r')
postdata = req_file.read()
ref_file = open(path+'/'+'reflected.txt','w')
ref_file.close()
scr_file = open(path+'/'+'script.txt','r')
counter = scr_file.read()
resp_file = open(path+'/'+'response.txt','r') 
scr_file.seek(0	)
count = counter.count('\n')
cr = 0
dr = 0
param = None
print "payload count: %d\n" %(count)
c_l = f_p()
postdata = c_l.c_l(postdata)
ba = s_c.cscr()
csrfprint = a_cf.p_cf()
cc = rqs()
response_data = rs_p.resp()
checklogout = lgt()
data,respcode,requrl,respurl = cc.send_req(postdata,options.ssl,options.contimeout,options.shreflected)
for a in range(0,count+1):
    if options.scanone == True:
        cnt = 0
        checklogout.cklgt(data,options.logout,options.logoutcode,respcode,requrl,respurl,options.shreflected)
        if options.timedelay !=None:
            time.sleep(options.timedelay)
        resp = resp_file.readline()
        resp = resp.rstrip()
        postdata1, bb= ba.a_scr(postdata,options.urlencode)
        if bb == '' or bb == None:
            continue
        if options.blacklist !='' and options.blacklist !=None:
            try:
                for dd in options.blacklist.split(','):
                    de = urllib.unquote(bb)
                    if de.upper().lower().find(dd.upper().lower()) >=0:
                        cnt = cnt+1
            except:
                print "Black list data not provided in proper format"
        if cnt >0:
            continue
        if options.csrftoken != None:
            postdata1 = csrfprint.da_cf(postdata1,data,options.csrftoken,options.shreflected)
        postdata1 = c_l.c_l(postdata1)
        print"---------------------------------------"
        if options.verbose == True:
            print "Request:\n",postdata1
        print "Trying payload: '%s'" %(bb.replace('+',' '))
        data,respcode,requrl,respurl = cc.send_req(postdata1,options.ssl,options.contimeout,options.shreflected)
        print "Response status code observed:",respcode
        rp,fl = response_data.resp1(data,resp,bb,None,options.strip)
        cr +=rp
    else:
        resp = resp_file.readline()
        resp = resp.rstrip()
        for postdata1,bc,bd in ba.scr_iter(postdata,options.csrftoken,options.skipparam,options.urlencode,options.increferer,param):
            cnt = 0
            checklogout.cklgt(data,options.logout,options.logoutcode,respcode,requrl,respurl,options.shreflected)
            if options.timedelay !=None:
                time.sleep(options.timedelay)
            if bc == '' or bc ==None:
                continue
            if options.blacklist !='' and options.blacklist !=None:
                try:
                    for dd in options.blacklist.split(','):
                        de = urllib.unquote(bc)
                        if de.upper().lower().find(dd.upper().lower()) >=0:
                            cnt = cnt+1
                except:
                    print 'Black list data not provided in proper format.\nPlease include the characters within "" and separate each character using comma.\nEg:"$,@,!"'
            if cnt >0:
                continue
            if options.csrftoken != None:
                postdata1 = csrfprint.da_cf(postdata1,data,options.csrftoken,options.shreflected)
            postdata1 = c_l.c_l(postdata1)
            print"---------------------------------------"
            if options.verbose == True:
                print "Request:\n",postdata1
            print "Trying payload: '%s' on parameter '%s'" %(bc.replace('+',' '),bd)
            data,respcode,requrl,respurl = cc.send_req(postdata1,options.ssl,options.contimeout,options.shreflected)
            print "Response status code observed:",respcode
            rp,fl = response_data.resp1(data,resp,bc,bd,options.strip)
            cr +=rp
            dr +=fl
            if dr ==1:
                dr +=1
                print "\n-------------------------------------------------------------\n"
                print "Reflection was found on parameter '%s'" %(bd)
                print "Press 'y' to continue scanning all parameters, 't' to scan only this parameter for other payloads and 'n' to exit"
                while True:
                    try:
                        input = raw_input("Press 'y' or 't' or 'n'...\n")
                    except KeyboardInterrupt, e:
                        print "\n---------------------------------------------------------------\nScanning interrupted"
                        print "Scan result observed till now is stored in reflected.txt file\n"
                        sys.exit(0)
                    if input.lower() == 'y':
                        break
                    if input.lower() == 't':
                        param = bd
                        break
                    if input.lower() == 'n':
                        print "Exiting..."
                        print "The reflection results are stored in reflected.txt file"
                        req_file.close()
                        scr_file.close()
                        resp_file.close()
                        sys.exit(0)
if cr >0:
    print "-----------------------------------------------------------\n"
    print "REFLECTIONS WERE FOUND FOR SOME PAYLOADS"
    print "DETAILS ARE STORED IN reflected.txt\n"
else:
    print "-----------------------------------------------------------\n"
    print "No reflections for any payload was found\n"
    ref_file = open(path+'/'+'reflected.txt','w')
    ref_file.write("No reflections were found")
    ref_file.close()
if options.shreflected ==True:
    print "-----------------------Scan Details------------------------"
    ref_file = open(path+'/'+'reflected.txt','r')
    print ref_file.read()
    ref_file.close()
req_file.close()
scr_file.close()
resp_file.close()
print "-----------------------END OF SCAN-------------------------"
sys.exit(0)