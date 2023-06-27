#!C:\Users\Megha Home\AppData\Local\Programs\Python\Python310\python
# Import Basic OS functions
import os
# Import modules for CGI handling
import cgi, cgitb
import urllib.request
#from HaarWavelet import * 
from DBInsertion import *
 

#from HOG import *


# enable debugging
cgitb.enable()
# print content type
print("Content-type:text/html\r\n\r\n")
#print("path="+os.getcwd()) 
 
form = cgi.FieldStorage()  
    
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
#print(jinja2.Environment().from_string(HTML).render(filedata=inFileData)) 
#w2d("E:\\python\\1.jpg",'haar','111')
docid=form.getvalue("docid")
#print(form.getvalue("docid"))
saveFile(docid) 
 
 
print("<html>")
print("<head>")
print("<meta http-equiv='refresh' content='0;url=http://localhost:8081/datasetInsrtPython?sts=success'/>")
#print("<meta http-equiv='refresh' content='0;url=http://localhost:80/CovidVaccineManagementBC/BCServer2/PlaceOrder.py?param="+param1+"'/>")
print("</head>")
print("</html>")
 