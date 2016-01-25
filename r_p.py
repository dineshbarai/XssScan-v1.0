import re
from re import sub,search,match
import os, inspect

class f_p:
    global CRLF
    CRLF = '\r\n\r\n'
    def f_par(self,post,mode):
        post = post + '\r\n\r\n'
        post = re.sub(r'\r?\n\r?\n\r?\n\r?\n',r'\r\n\r\n',post,re.I|re.M|re.S)
        h_p = r'.*?(?=(\r?\n\r?\n))'
        d_p = r'((?<=(\n\n))|(?<=(\r\n\r\n))).*'
        hd = search(h_p,post,re.I|re.M|re.S)
        bd = search(d_p,post,re.I|re.M|re.S)
        b=hd.group()
        bd = bd.group().rstrip()
        hrs = []
        regex = re.compile(r'^.*$',re.I|re.M)
        
        for match in regex.finditer(b):
            hrs.append(match.group())
        f_l = hrs[0] 
        del hrs[0]
        length = len(hrs)
        h_t ={}
        
        for count in range(0,length):
            sp = hrs[count].split(':',1)	
            h_t[sp[0]] = sp[1]
        method = f_l.split(' ',1)[0]
        if h_t['Host']:
            url = h_t['Host'].lstrip()+f_l.split()[1].lstrip()
        elif h_t['host']:
            url = h_t['host'].lstrip()+f_l.split()[1].lstrip()
        
        mode = mode.lower()
        if mode == 'http':
            url = 'http://'+ url
            url = url.replace(' ','+')
            url = url.replace('#',r'%23')
        elif mode =='https':
            url = 'https://'+ url
            url = url.replace(' ','+')
            url = url.replace('#','%23')
        else:
            print "Please select mode between HTTP or HTTPS"
            return 0,0,0,0
        
        return h_t,bd,method,url

    def c_l(self,post):
        post = post + CRLF
        post = re.sub(r'\r?\n\r?\n\r?\n\r?\n',r'\r\n\r\n',post,re.I|re.M|re.S)
        len1 = re.search(r'((?<=(\r\n\r\n))|(?<=(\n\n)))^.*((?=(\n\n))|(?=(\r\n\r\n)))',post,re.I|re.M|re.S)
        if len1:
            len2 = len(len1.group())
            post = re.sub(r'(?<=(Content-Length: )) *?\d+',str(len2),post,re.I|re.M)
        return post

