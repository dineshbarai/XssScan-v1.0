import os,inspect,re
import urllib

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
global scr_file
scr_file = open(path+'/'+'script.txt','r')
regex = r'((?<=\?)|(?<=&)|(?<=\r\n\r\n)|(?<=\n\n)).*?=.*?((?=&)|(?=\s)|(?=$))'
global comp
comp = re.compile(regex,re.I|re.M)

class cscr:
    def __init__(self):
        pass
    def m_scr(self):
        scr = scr_file.readline()
        scr = scr.replace(' ','+')
        scr = scr.replace('&',r'%26')
        scr = scr.rstrip()
        return scr
	
    def a_scr(self,postdata,un):
        b =self.m_scr()
        if un == True:
            b = urllib.quote_plus(b)
        postdata1 = postdata.replace('*',b)
        return postdata1,b

    def scr_iter(self,postdata,cst,pms,un,inr,scn1):
        b = self.m_scr()
        if un == True:
            b = urllib.quote_plus(b)
        postdata1 = postdata
        if inr == False:
            refreg = r'Referer\ ?:.*?((\r\n)|(\n))'
            postdata1 = re.sub(refreg,"",postdata1,re.I|re.M)
        for match in comp.finditer(postdata1):
            param = match.group().split('=',1)[0]
            if scn1 != None and scn1 != param:
                continue
            cmp = 0
            if (cst!=None) and (match.group().split('=',1)[0].find(cst)>=0):
                continue
            if (pms!=None) and (pms!=''):
                checkparam = pms.split(',')
                for par in checkparam:
                    if match.group().split('=',1)[0].find(par)>=0:
                        cmp = cmp+1
            if cmp >0:
                continue
            if inr == False:
                postdata2 = postdata.replace(match.group(),match.group()+b,1)
            else:
                postdata2 = postdata.replace(match.group(),match.group()+b)
            yield postdata2,b,param




