#!C:\Users\Megha Home\AppData\Local\Programs\Python\Python310\python
# Import Basic OS functions
import os
# Import modules for CGI handling
import cgi, cgitb
import urllib.request
from Cryptography import encryption

#from HaarWavelet import *
from FunFactory import *
from DBInsertion import *
from DBInsertion1 import *
from DBInsertion2 import *
from encrypt1 import *

#from HOG import *


# enable debugging
cgitb.enable()
# print content type
print("Content-type:text/html\r\n\r\n")
#print("path="+os.getcwd()) 
#print() 
#form=cgi.FieldStorage()

fid="2.jpg"
# HTML INPUT FORM
HTML ="""  
<html>
<head>
<title></title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/fontawesome-all.min.css">
    <link rel="stylesheet" href="assets/plugins/testimonial/css/owl.carousel.min.css">
    <link rel="stylesheet" href="assets/plugins/testimonial/css/owl.theme.min.css">
    <link rel="stylesheet" href="assets/plugins/sticky/css/slick.css">
    <link rel="stylesheet" href="assets/plugins/sticky/css/slick-theme.css">
    <link rel="stylesheet" href="assets/plugins/revolution/css/settings.css" />
    <link rel="stylesheet" href="assets/css/style.css">

</head>
<body>
 <div class="container-fluid">

        <!--  ************************* Header Starts Here ************************** -->
        <header>
            <div class="header-top row d-none d-sm-block">
                <div class="container">
                    <div class="row ">
                        <div class="col-sm-12">
                         <h1> <a href="home">
                     Online secure Cloud Data Sharing System with Data Dispersion Scheme 
                       </a></h1>
                              </div>
                       
                    </div>
                </div>
            </div>

            <nav id="nav-head" class="row">

                <div class="container">
                    <div class="row">
                      
                        <div class="col-md-3 col-sm-4">
                       
                        </div>
                        <div  class="col-md-9 col-sm-8">
                           
                            <a data-toggle="collapse" data-target="#menu" href="#menu" href="#"><i class="fas d-block d-sm-none small-menu fa-bars"></i></a>
                            <ul id="menu" class="nav-links menu-tab">
                               
                               </ul>
                            
                        </div>
                        
                    </div>
                </div>

            </nav>
        </header>
        <!-- ######## Header End ####### -->


    <!-- //header -->
      <!-- inner banner -->
    <div class="innerbanner">
    </div>
    <!-- //inner banner -->
   
<div class="container">
<div class="row">

<div class="col-md-6">
<img src="assets/images/upload.png" width="70%"/>
</div>
<div class="col-md-6">

  <h1>Upload File</h1>
   <table class="tblform">
									  
									     
									  <tr>
									 <td>Title
									 </td>
									 <td> 
								 <input type="text" name="title" required class="form-control"/>
									 </td>
									 </tr>
									  <tr>
									 <td>Description
									 </td>
									 <td> 
								 <input type="text" name="docdesc" required class="form-control"/>
									 </td>
									 </tr>
									 
	           <tr> <td>  Document</td>
		            <td>
		             <input type="file" name="file" class="form-control" required ></input>
  
		            </td>
            </tr>
								 
	 

									 <tr>
									 <td colspan="2"><input type="submit" value="Submit" class="btn btn-primary"/>
                                     <img src="loading.gif" width="25px"/>
									 </td></tr>
									 </table> 
    

</body>
</html>
 """
#print(HTML)
filename=""
ext=""
uploaded_file_path=""
inFileData = None
form = cgi.FieldStorage() 
docid=getMaxIdDoc1()
UPLOAD_DIR=os.getcwd()+"\\Documents\\temp\\" 
#print("value="+form.getvalue("uid"))
# IF A FILE WAS UPLOADED (name=file) we can find it here.
#fid=form.getvalue("fid")
#print(form)
if "file" in form:
    form_file = form['file']
   
    # form_file is now a file object in python
    if form_file.filename:
        #print("file name"+os.path.basename(form_file.filename))
        nm,ext=os.path.basename(form_file.filename).split('.')
        filename=os.path.basename(form_file.filename)
        #print("original file name")
        #(filename)
        #print(str(docid)+"."+ext)
        filename=str(docid)+"."+ext
        uploaded_file_path = os.path.join(UPLOAD_DIR, filename)
        #print(uploaded_file_path)
        with open(uploaded_file_path, 'wb') as fout:
            # read the file in chunks as long as there is data
            while True:
                chunk = form_file.file.read(100000)
                if not chunk:
                    break
                # write the file content on a file on the hdd
                fout.write(chunk)

        # load the written file to display it
        with open(uploaded_file_path, 'r',errors='ignore') as fin:
            inFileData = ""
            for line in fin:
                inFileData += line

    
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
#print(jinja2.Environment().from_string(HTML).render(filedata=inFileData)) 
#w2d("E:\\python\\1.jpg",'haar','111')
#print(form.getvalue("fid"))
title=form.getvalue("title")
userid=form.getvalue("userid")
docdesc=form.getvalue("docdesc")
dt=form.getvalue("dt")
tm=form.getvalue("tm")
seckey=form.getvalue("seckey")
#print(docid)
#print(userid+" "+title+" "+docdesc)
#print("ext="+ext)
#ext="."+ext
deleteDocPart()
str1=encryption(filename,ext,seckey,docid)
#encrypt(getKey(seckey), filename)
insertDoc1(userid,title,filename,docdesc,dt,tm,seckey,str1)
insertDoc2(userid,title,filename,docdesc,dt,tm,str1)
insertDoc3(userid,title,filename,docdesc,dt,tm,str1)
print("<html>")
print("<head>")
print("<meta http-equiv='refresh' content='0;url=http://localhost:8081/datasetInsrtPython1?docid="+str(docid)+"&sts=success'/>")
print("</head>")
print("</html>")