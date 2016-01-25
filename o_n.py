import sys
from optparse import OptionParser
import os,inspect,re

class onh:
    print "\nXSSScan v 1.0: XSS scanning tool by Dinesh Barai.\nHttps site scanning needs Python version 2.7.9 and above.\nIt is recommended to read doc.txt file before using the tool.\n" 
    usage = "Usage: %prog [options]\n"
    usage += "Mandatory option: -r or --request"
    parser = OptionParser(usage=usage)
    parser.add_option("-r", "--request", dest="request", help="Name of the file containing the request. Must be in the same directory as of this script.", action="store",default=None)
    parser.add_option("-t", "--scanone", dest="scanone", help="Scan a single position (marked by *). Default is scan every parameter within a request", action="store_true", default=False)
    parser.add_option("--doc", dest="doc", help="Shows Documentation stored in doc.txt", action="store_true", default=False)
    parser.add_option("-i", "--increferer", dest="increferer", help="Includes Referer parameters also for scanning. By default Referer header parameters are not included", action="store_true", default=False)
    parser.add_option("-c", "--csrftoken", dest="csrftoken", help="Parameter name containing Anti-csrf token. The tool would automatically take Anti-csrf token from response and send it in request. Ensure unused Anti-CSRF token is present in the initial request.", action="store", default=None)
    parser.add_option("-v","--verbose", dest="verbose", help="Turn on verbosity", action="store_true", default=False)
    parser.add_option("-s", "--skipparam", dest="skipparam", help="Comma separated list of parameters to be excluded from testing",action="store",default=None)
    parser.add_option("--ssl", dest="ssl", help="Enable ssl for application on HTTPS", action="store_true", default=False)
    parser.add_option("-b", "--blacklist", dest="blacklist", help='Specify characters or words(case insensitive) blacklisted by application. Usually application logs out on use of these chars or words as input. Include the characters within "" and separate each character using comma.\nEg:"$,@,!,alert"', action="store", default=None)
    parser.add_option("-u", "--urlencode", dest="urlencode", help="Url encode the script payload before including in the request", action="store_true", default=False)
    parser.add_option("-l", "--logout", dest="logout", help="Specify unique string in response that indicates that the application has logged out", action="store", default=None)
    parser.add_option("--logoutcode", dest="logoutcode", help="Specify response code that indicates that the application has logged out", action="store", default=None)
    parser.add_option("--shreflected", dest="shreflected", help="Show Scan results (Reflected payloads and point of reflection)", action="store_true", default=False)
    parser.add_option("--contimeout", dest="contimeout", help="Specify connection timeout for request. Default is 30 secs. Use this if there is significant lag in response",type="int", action="store", default=30)
    parser.add_option("--timedelay", dest="timedelay", help="Time delay in seconds between subsequent requests.",type="int", action="store", default=None)
    parser.add_option("--strip", dest="strip", help='Specify any characters or word(case insensitive) that the application is stripping before reflecting the data in response for provided input. This would help in better matching of reflection points. Include the characters or word within "" and separate each character using comma.\nEg:"$,@,!,alert"', action="store", default=None)
    
    (options, args) = parser.parse_args()
    scanone = options.scanone
    increferer = options.increferer
    csrftoken = options.csrftoken
    verbose = options.verbose
    request = options.request
    skipparam = options.skipparam
    ssl = options.ssl
    blacklist = options.blacklist
    urlencode = options.urlencode
    logout = options.logout
    logoutcode = options.logoutcode
    doc = options.doc
    shreflected = options.shreflected
    contimeout = options.contimeout
    timedelay = options.timedelay
    strip = options.strip
    if len(sys.argv) <2:
        parser.print_help()
        sys.exit(0)
    if options.doc:
        path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        #try:
        doc_file = open(path+'/'+'doc.txt','r')
        print doc_file.read()
        doc_file.close()
        sys.exit(0)
    if options.request == None:
        print "Please specify the request file containing the request using option -r <request_file>or --request=<request_file>"
        print "For complete list of options, use option -h or --help"
        sys.exit(0)