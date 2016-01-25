import os,inspect
import sys

class lgt:
    global path
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    def cklgt(self,data,lgts,lgtc,respcode,requrl,respurl,ref):
        if lgts!='' and lgts!=None:
            if data.find(lgts) >=0:
                print "The string '%s' was encountered in response" %(lgts)
                print "The application has logged out\n"
                print "Scan result observed till now is stored in reflected.txt file\n"
                sys.exit(0)
        if lgtc!='' and lgtc!=None:
            if str(lgtc)[0] == '3':
                if requrl != respurl:
                    print "Redirection was observed to %s" %(respurl)
                    print "The application has logged out\n"
                    print "Scan result observed till now is stored in reflected.txt file"
                    sys.exit(0)
            if str(respcode) == str(lgtc):
                print "Response with code '%s' was observed" %(str(lgtc))
                print "The application has logged out\n"
                print "Scan result observed till now is stored in reflected.txt file\n"
                sys.exit(0)