import ssl,urllib2
from r_p import f_p
from StringIO import StringIO
import gzip
import zlib
import socket
import os,inspect
import sys

class rqs:
    global file_parsing
    file_parsing = f_p()
    global path
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    def ch_en(self,response):
        if response.info().get('Content-Encoding') == 'gzip' or response.info().get('Content-Encoding') == 'x-gzip':
            buf = StringIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
        elif response.info().get('Content-Encoding') == 'deflate':
            f = StringIO.StringIO(zlib.decompress(response.read()))
            data = f.read()
        else:
            data = response.read()
        return data
    def send_req(self,postdata,ssla,tm,ref):
        if ssla == True:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            header,body,method,url = file_parsing.f_par(postdata,'Https')
            if method.upper() == 'GET':
                req = urllib2.Request(url,headers=header)
                try:
                    response = urllib2.urlopen(req, context=ctx,timeout=tm)
                except socket.timeout, e:
                    print "\n---------------------------------------------------------------\n---------------------------------------------------------------\nThe connection has timed out. Please check the network connectivity or increase the connection timeout using option --contimeout."
                    print "Scan result observed till now is stored in reflected.txt file\n"
                    sys.exit(0)
                except urllib2.HTTPError, response:
                    pass
                except urllib2.URLError,response:
                    print "\n---------------------------------------------------------------\nError occured.\nError Message:",response.args[0]
                    sys.exit(0)
                data = self.ch_en(response)
                return data,response.code,url,response.url
            elif method.upper() == 'POST':
                req = urllib2.Request(url,body,header)
                try:
                    response = urllib2.urlopen(req, context=ctx,timeout=tm)
                except socket.timeout, e:
                    print "\n---------------------------------------------------------------\nThe connection has timed out. Please check the network connectivity or increase the connection timeout using option --contimeout"
                    print "Scan result observed till now is stored in reflected.txt file\n"
                    sys.exit(0)
                except urllib2.HTTPError, response:
                    pass
                except urllib2.URLError,response:
                    print "\n---------------------------------------------------------------\nError occured.\nError Message:",response.args[0]
                    sys.exit(0)
                data = self.ch_en(response)
                return data,response.code,url,response.url
            else:
                print "Method not supported:", method
                sys.exit(0)
        else:
            header,body,method,url = file_parsing.f_par(postdata,'Http')
            if method.upper() == 'GET':
                req = urllib2.Request(url,headers=header)
                try:
                    response = urllib2.urlopen(req,timeout=tm)
                except socket.timeout, e:
                    print "\n---------------------------------------------------------------\nThe connection has timed out. Please check the network connectivity or increase the connection timeout using option --contimeout"
                    print "Scan result observed till now is stored in reflected.txt file\n"
                    sys.exit(0)
                except urllib2.HTTPError, response:
                    pass
                except urllib2.URLError,response:
                    print "\n---------------------------------------------------------------\nError occured.\nError Message:",response.args[0]
                    sys.exit(0)
                data = self.ch_en(response)
                return data,response.code,url,response.url
            elif method.upper() == 'POST':
                req = urllib2.Request(url,body,header)
                try:
                    response = urllib2.urlopen(req,timeout=tm)
                except socket.timeout, e:
                    print "\n---------------------------------------------------------------\nThe connection has timed out. Please check the network connectivity or increase the connection timeout using option --contimeout"
                    print "Scan result observed till now is stored in reflected.txt file\n"
                    sys.exit(0)
                except urllib2.HTTPError, response:
                    pass
                except urllib2.URLError,response:
                    print "\n---------------------------------------------------------------\nError occured.\nError Message:",response.args[0]
                    sys.exit(0)
                data = self.ch_en(response)
                return data,response.code,url,response.url
            else:
                print "Method not supported:", method
                sys.exit(0)