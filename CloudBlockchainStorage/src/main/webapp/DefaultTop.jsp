<%@page import="java.util.List"%>
<%@page import="models.*"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
 <!DOCTYPE html>
 
<html lang="">
<!-- To declare your language - read more here: https://www.w3.org/International/questions/qa-html-language-declarations -->
<head>
<title> </title>
   
   <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/fontawesome-all.min.css">
    <link rel="stylesheet" href="assets/plugins/testimonial/css/owl.carousel.min.css">
    <link rel="stylesheet" href="assets/plugins/testimonial/css/owl.theme.min.css">
    <link rel="stylesheet" href="assets/plugins/sticky/css/slick.css">
    <link rel="stylesheet" href="assets/plugins/sticky/css/slick-theme.css">
    <link rel="stylesheet" href="assets/plugins/revolution/css/settings.css" />
    <link rel="stylesheet" href="assets/css/style.css">

    <title> </title>

<script language="Javascript" type="text/javascript">
 

function createRequestObject() {
    var tmpXmlHttpObject;
    if (window.XMLHttpRequest) {
            tmpXmlHttpObject = new XMLHttpRequest();
    } else if (window.ActiveXObject) {
        tmpXmlHttpObject = new ActiveXObject("Microsoft.XMLHTTP");
    }

    return tmpXmlHttpObject;
}


var http = createRequestObject();

function makeGetRequest(st) {
   // st=document.frm.state.value;
   
    http.open('get', 'Cities?state=' + st);
    http.onreadystatechange = processResponse;
    http.send(null);
}

function processResponse() {
    if(http.readyState == 4){
        var response = http.responseText;
        document.getElementById('cities').innerHTML = response;
    }
}
 
</script>

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
                       Secure Cloud Storage using Blockchain 
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
                                <li><a href="home">Home </a></li>
                                <li><a href="#reg">Registration</a></li>
                                <li><a href="#login">Login </a></li>
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
   