<%@page import="services.UpdateCloudRent"%>
<%@page import="java.util.Date"%>
<%@page import="java.util.List"%>
<%@page import="models.*"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
 <!DOCTYPE html>
 
<html lang="">
<!-- To declare your language - read more here: https://www.w3.org/International/questions/qa-html-language-declarations -->
<head>
<title>Data Integrity and Recovery</title>
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
 
</head> 
<body>

    <div class="container-fluid">

        <!--  ************************* Header Starts Here ************************** -->
        <header>
            <div class="header-top row d-none d-sm-block">
                <div class="container-fluid">
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

                <div class="container-fluid">
                    <div class="row">
                      
                       
                        <div  class="col-md-12 col-sm-12">
                           
                            <a data-toggle="collapse" data-target="#menu" href="#menu" href="#"><i class="fas d-block d-sm-none small-menu fa-bars"></i></a>
                            <ul id="menu" class="nav-links menu-tab">
                                 
                                  <li><a href="/<%=session.getAttribute("usertype").toString().trim()%>">Home</a></li>
                              <%if(session.getAttribute("usertype").toString().trim().equals("admin"))
                                	{
                                	%>
                                	 
		 
		<li><a href="viewUsers" >View Users</a></li>
		
		   <li> <a  href="MonthlyCloudUsage.jsp?page=admin">Total Cloud Usage</a></li>
			 <li> <a href="MonthlyCloudRent.jsp">Monthly Cloud Usage Statistics</a></li>
			 <li> <a  href="YearlyPayment History.jsp">Payment Summary</a></li>
		
		
								 <%} else if(session.getAttribute("usertype").toString().trim().equals("user"))
                            	{
                            	%>
                            	  <li><a href="uploaddoc" >Upload Documents </a></li>
		 
		  <li><a href="viewdocs">View Documents</a></li>
		  
         <li><a href="viewSharedDocs">Shared Documents</a>
                       <li> <a  href="MonthlyCloudUsage.jsp?page=user">Total Cloud Usage</a></li>
			 <li> <a href="MonthlyCloudRent.jsp">Monthly Cloud Usage Statistics</a></li>
			 <li> <a  href="YearlyPayment History.jsp">Payment Summary</a></li>
		
                            	<%}  %> 
                            	<li><a href="ChangePass">Change Password</a></li>
								<li><a href="logout">Logout</a></li>
                           
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
   <%
  try{
     Date dt=new Date();
 UpdateCloudRent upd=new UpdateCloudRent();
     upd.updcloudrent((dt.getMonth()+1),(dt.getYear()+1900));
}catch(Exception ex)
{
    	System.out.println("err="+ex.getMessage());
    	 
}%>
                             
    <div class="container"> 
Logged in as </span> <%=session.getAttribute("userid").toString() %> (<%=session.getAttribute("usertype").toString() %>)
 
       