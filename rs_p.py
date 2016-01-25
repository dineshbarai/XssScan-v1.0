import os,inspect
import urllib

class resp:
    global path
    global ref_file
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    def resp1(self,resp_data,resp1,scr,par,strip):
        value = 0
        scr =scr.replace('+',' ')
        za = scr.upper().lower()
        zb = urllib.unquote(za)
        zc = urllib.unquote(zb)
        if (resp_data.upper().lower().find(za) >=0) and (par ==None):
            print "The page is reflecting value: " ,za
            print "Number of places reflecting: %s" %(str(resp_data.upper().lower().count(za)))
            ref_file = open(path+'/'+'reflected.txt','a')
            ref_file.write("Found reflection '"+za+"' for payload '"+scr.replace('+',' ')+"'\n")
            ref_file.close()
            value += 1
        if (resp_data.upper().lower().find(zb) >=0) and (par ==None) and (za!=zb):
            print "The page is reflecting value: " ,zb
            print "Number of places reflecting: %s" %(str(resp_data.upper().lower().count(zb)))
            ref_file = open(path+'/'+'reflected.txt','a')
            ref_file.write("Found reflection '"+zb+"' for payload '"+scr.replace('+',' ')+"'\n")
            ref_file.close()
            value += 1
        if (resp_data.upper().lower().find(zc) >=0) and (par ==None) and (za !=zc and zb!=zc):
            print "The page is reflecting value: " ,zc
            print "Number of places reflecting: %s" %(str(resp_data.upper().lower().count(zc)))
            ref_file = open(path+'/'+'reflected.txt','a')
            ref_file.write("Found reflection '"+zc+"' for payload '"+scr.replace('+',' ')+"'\n")
            ref_file.close()
            value += 1
        if (resp_data.upper().lower().find(za) >=0) and (par !=None):
            print "The page is reflecting value: " ,za
            print "Number of places reflecting: %s" %(str(resp_data.upper().lower().count(za)))
            ref_file = open(path+'/'+'reflected.txt','a')
            ref_file.write("Found reflection '"+za+"' for payload '"+scr.replace('+',' ')+"' on parameter '" + par +"'\n")
            ref_file.close()
            value += 1
        if (resp_data.upper().lower().find(zb) >=0) and (par !=None) and (za!=zb):
            print "The page is reflecting value: " ,zb
            print "Number of places reflecting: %s" %(str(resp_data.upper().lower().count(zb)))
            ref_file = open(path+'/'+'reflected.txt','a')
            ref_file.write("Found reflection '"+zb+"' for payload '"+scr.replace('+',' ')+"' on parameter '" + par +"'\n")
            ref_file.close()
            value += 1
        if (resp_data.upper().lower().find(zc) >=0) and (par !=None) and (za !=zc and zb !=zc):
            print "The page is reflecting value: " ,zc
            print "Number of places reflecting: %s" %(str(resp_data.upper().lower().count(zc)))
            ref_file = open(path+'/'+'reflected.txt','a')
            ref_file.write("Found reflection '"+zc+"' for payload '"+scr.replace('+',' ')+"' on parameter '" + par +"'\n")
            ref_file.close()
            value += 1
        for resp in resp1.split(','):
            resp = resp.lstrip()
            resp = resp.rstrip()
            if resp =='':
                continue
            if (resp_data.upper().lower().find(resp.upper().lower()) >=0) and (par ==None):
                print "The page is reflecting value: " ,resp
                print "Number of places reflecting: %s" %(str(resp_data.upper().lower().count(resp.upper().lower())))
                ref_file = open(path+'/'+'reflected.txt','a')
                ref_file.write("Found reflection '"+resp.upper().lower()+"' for payload '"+scr.replace('+',' ')+"'\n")
                ref_file.close()
                value += 1
            if resp_data.upper().lower().find(resp.upper().lower()) >=0 and (par !=None):
                print "The page is reflecting value: " ,resp
                print "Number of places reflecting: %s" %(str(resp_data.upper().lower().count(resp.upper().lower())))
                ref_file = open(path+'/'+'reflected.txt','a')
                ref_file.write("Found reflection '"+resp.upper().lower()+"' for payload '"+scr.replace('+',' ')+"' on parameter '" + par +"'\n")
                ref_file.close()
                value += 1
            """else:
                print "Payload: '"+resp.upper().lower()+"' Not reflecting\n"""
        if strip !=None:
            scr1 = urllib.unquote(scr.upper().lower())
            for st in strip.split(','):
                if st !='':
                    scr1 = scr1.upper().lower().replace(st.upper().lower(),'')
            if scr1 == scr or scr1 == za or scr1 == zb:
                return value
            za1 = scr1.upper().lower()
            zb1 = urllib.unquote(za1)      
            if (resp_data.upper().lower().find(za1) >=0) and (par ==None):
                print "The page is reflecting value: " ,za1
                print "Number of places reflecting: %s" %(str(resp_data.upper().lower().count(za1)))
                ref_file = open(path+'/'+'reflected.txt','a')
                ref_file.write("Found reflection '"+za1+"' for payload '"+scr+"'\n")
                ref_file.close()
                value += 1
            if (resp_data.upper().lower().find(zb1) >=0) and (par ==None) and (za1!=zb1):
                print "The page is reflecting value: " ,zb1
                print "Number of places reflecting: %s" %(str(resp_data.upper().lower().count(zb1)))
                ref_file = open(path+'/'+'reflected.txt','a')
                ref_file.write("Found reflection '"+zb1+"' for payload '"+scr+"'\n")
                ref_file.close()
                value += 1
            if (resp_data.upper().lower().find(za1) >=0) and (par !=None):
                print "The page is reflecting value: " ,za1
                print "Number of places reflecting: %s" %(str(resp_data.upper().lower().count(za1)))
                ref_file = open(path+'/'+'reflected.txt','a')
                ref_file.write("Found reflection '"+za1+"' for payload '"+scr+"'\n")
                ref_file.close()
                value += 1
            if (resp_data.upper().lower().find(zb1) >=0) and (par !=None) and (za1!=zb1):
                print "The page is reflecting value: " ,zb1
                print "Number of places reflecting: %s" %(str(resp_data.upper().lower().count(zb1)))
                ref_file = open(path+'/'+'reflected.txt','a')
                ref_file.write("Found reflection '"+zb1+"' for payload '"+scr+"'\n")
                ref_file.close()
                value += 1
        if value > 0:
		    fl = 1
        else:
            fl = 0
        return value,fl