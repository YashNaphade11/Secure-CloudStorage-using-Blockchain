 <%@page import="models.*"%>
<%@page import="models.GetStateNCities"%>
<%@page import="java.util.List"%>
<%@page import="beans.BranchList"%>
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

    <title>  </title>

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


        <!--  ************************* Slider Starts Here ************************** -->
        <div id="slider" class="slider row">
        
            <!-- START REVOLUTION SLIDER 3.1 rev5 fullwidth mode -->
            <div class="fullwidthbanner-container">
                <div class="fullwidthbanner" >
                    <ul>
                    
                      <!-- SLIDE 1 -->
                        <li data-transition="fade" data-slotamount="7" data-masterspeed="300" >
                            <!-- MAIN IMAGE -->
                            <img src="assets/images/slider/slide-02-bg.jpg" data-fullwidthcentering="on" alt="slidebg2"  data-bgfit="cover" data-bgposition="center center" data-bgrepeat="no-repeat">
                            
                            <!-- LAYER NR. 1 -->
                            <div class="tp-caption uppercase big_font_size boldest_font_weight dark_font_color sft start"
                                data-x="440"
                                data-y="125"
                                
                                data-speed="300"
                                data-start="1600"
                                data-easing="easeOutExpo"><span class="accent-color">We provide Solutions</span> <br>that  you  need!
                            </div>
                            
                            <!-- LAYER NR. 2 -->
                            <div class="tp-caption medium_font_size regular_font_weight dark_font_color sfl start"
                                data-x="440"
                                data-y="208"
                                
                                data-speed="300"
                                data-start="1900"
                                data-easing="easeOutExpo">Secure Cloud Storage
                            </div>
                            
                            <!-- LAYER NR. 3 -->
                            <div class="tp-caption mini_font_size light_font_weight gray_font_color sfr start"
                                data-x="440"
                                data-y="250"
                                
                                data-speed="300"
                                data-start="2200"
                                data-easing="easeOutExpo">Blockchain Technology for decentralized Storage
                            </div>
                            
                             
                            
                            <!-- LAYER NR. 5 -->
                            <div class="tp-caption sfl start"
                                data-x="60"
                                data-y="bottom"
                                
                                data-speed="1000"
                                data-start="1000"
                                data-easing="Power1.easeOut"><img src="assets/images/slider/slide-02-image-01.png" alt="" />
                            </div>
                            
                        </li>
                        
                        <!-- SLIDE 2  -->
                        <li data-transition="fade" data-slotamount="7" data-masterspeed="300" >
                            <!-- MAIN IMAGE -->
                            <img src="assets/images/slider/slide-03-bg.jpg" data-fullwidthcentering="on" alt="slidebg3"  data-bgfit="cover" data-bgposition="center center" data-bgrepeat="no-repeat">
                            
                            <!-- LAYER NR. 1 -->
                            <div class="tp-caption mini_font_size bold_font_weight dark_font_color gray_bg sfl start"
                                data-x="left"
                                data-y="110"
                                
                                data-speed="300"
                                data-start="1600"
                                data-easing="easeInOutExpo">Unbreakable Modified AES Algorithm for Document Encryption
                            </div>
                            
                            <!-- LAYER NR. 2 -->
                            <div class="tp-caption mini_font_size bold_font_weight dark_font_color gray_bg sfr start"
                                data-x="left"
                                data-y="150"
                                
                                data-speed="300"
                                data-start="1900"
                                data-easing="easeInOutExpo">Blockchain Enabled Document Storage
                            </div>
                            
                            <!-- LAYER NR. 3 -->
                            <div class="tp-caption mini_font_size bold_font_weight dark_font_color gray_bg sfl start"
                                data-x="left"
                                data-y="190"
                                
                                data-speed="300"
                                data-start="2200"
                                data-easing="easeInOutExpo">Blockchain management using SHA algorithm
                            </div>
                            
                            <!-- LAYER NR. 4 -->
                            <div class="tp-caption  mini_font_size bold_font_weight dark_font_color gray_bg sfr start"
                                data-x="left"
                                data-y="230"
                                
                                data-speed="300"
                                data-start="2500"
                                data-easing="easeInOutExpo">Modified AES encryption
                            </div>
                             
                            
                            <!-- LAYER NR. 7 -->
                            <div class="tp-caption sfr start"
                                data-x="center"
                                data-y="60"
                                data-hoffset="100"
                                
                                data-speed="600"
                                data-start="1000"
                                data-easing="easeOutBack"
                                style="z-index: 2"><img src="assets/images/slider/slide-03-image-01.png" alt="" />
                            </div>
                            
                            <!-- LAYER NR. 8 -->
                            <div class="tp-caption sfl start"
                                data-x="right"
                                data-y="70"
                                data-hoffset="-100"

                                data-speed="600"
                                data-start="1300"
                                data-easing="easeOutBack"
                                style="z-index: 1"><img src="images/slide-03-image-02.png" alt="" />
                            </div>
                            
                        </li>
                        
                        
                            
                        </li>
                        
                    </ul>
                    <div class="tp-bannertimer" style="visibility:hidden;"></div>
                </div>
            </div>
            
           
                 
        </div>
        <!-- ######## Slider End ####### -->

<!--  ************************* Key Featuees Starts Here ************************** -->
        <section class="key-feature-conten row">
            <div class="layy key-feature-1 col-md-3 col-sm-6">
                <div class="layy">
                    <i class="fas fa-cogs"></i><br>
                    <b>Secured Cloud Data Storage</b>
                     <p></p> </div>
            </div>
            <div class="layy key-feature-2 col-md-3 col-sm-6">
                <div class="layy">
                    <i class="fas fa-life-ring"></i><br>
                    <b>Blockchain Storage</b>
                   <p></p>
                </div>
            </div>
            <div class="layy key-feature-3 col-md-3 col-sm-6">
                <div class="layy">
                    <i class="fas fa-users"></i><br>
                    <b>Shared Cloud & Pay as you go service</b>
                      <p></p>
                </div>
            </div>
            <div class="layy key-feature-4 col-md-3 col-sm-6">
                <div class="layy">
                    <i class="fas fa-headphones"></i><br>
                    <b>24 x 7 Support</b>
                    <p></p>
                </div>
            </div>
        </section>
        <!-- ######## Key Features End ####### -->


        <!--  ************************* What we do Starts Here ************************** -->
        <section class="wat-we-do row" id="reg">
            <div class="container">
                <div class="sec-title">
                    <h2>Registration</h2>
                       </div>
                <div class="row">
                <div class="col-md-6">
                        <form name="frm" method="post" action="registeruser" enctype="multipart/form-data"><table class="tblform">
	<tr><td>Userid</td>
	<td><input type="text" name="userid" class="form-control" required></td>
	</tr>
	<tr><td>User Name</td>
	<td><input type="text" name="usernm" class="form-control" required></td>
	</tr>
	<tr><td>Password</td>
	<td><input type="password" name="pswd" class="form-control" required>
	 <input type="hidden" name="usertype" value="user"/>
	</td>
	</tr>
 
       <tr><td>Mobile Number</td>
       	<td><input type="text" name="mobileno"  pattern="^\d{10}$" class="form-control" required></td></tr>
       <tr>
		<td>Email Address</td>       
       <td><input type="text" name="emailid" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"  class="form-control" required></td>
       </tr>
     <%
									 GetStateNCities obj=new GetStateNCities();
									 obj.getStates();
									 List<States> lst=obj.getLststate();
									 %>
									  <tr>
									 <td>State
									 </td>
									 <td> 
									 <select required name="state" class="form-control" onchange="makeGetRequest(this.value)">
									 <option value=""><--select--></option>
										<%for(int i=0;i<lst.size();i++)
											{%>
									 <option value="<%=lst.get(i).getState() %>"><%=lst.get(i).getState() %></option>											
											<%}%>															  
									 </select>
									 </td>
									 </tr>
									   <tr>
									 <td>City
									 </td>
									 <td> 
									<div id="cities"></div>
									 </td>
									 </tr>
       <tr>
<td>Gender</td>
<td>
  <input type="hidden" name="userstatus" value="active"/>
<input type="radio" name="gender" value="Male"   checked="checked" required >Male 
<input type="radio" name="gender" value="Female"  required>Female 
</td>
</tr>
        
         <tr><td> Address</td>
	<td><textarea  name="addr" class="form-control" required></textarea></td>
	</tr>
	<tr><td>Pincode</td>
	<td><input type="text" name="pincode" class="form-control" required></td>
	</tr>
      
       <tr>
       	<td>Date Of Birth</td>
       	<td><input type="date" name="dob" class="form-control"></td>
       </tr>
       <tr><td>Photo</td>
       <td>
       <input type="file" name="file" class="form-control"/>
       </td>
	<tr>
	<td><input type="submit" value="Submit" class="btn btn-primary" ></td>
	</tr>
	</table>
</form>  </div> 
<div class="col-md-6">
<img src="assets/images/reg.jpg" width="80%"/>
</div>  
                </div>
            </div>
        </section>
        <!-- ######## What we Do End ####### -->



        <!--  ************************* About Us Starts Here ************************** -->
        <section class="row home-about" id="login">
            <div class="col-sm-6 about-img">
                <img src="assets/images/about_home.jpg" alt="About Home">
            </div>
            <div class="col-sm-6 adout-det">
               <div class="row">
                   
              
                <div class="layy">
                    <b>Login</b>
                         <form name="frm" method="post" action="check">
         <table class="tblform"> 
         <tr><td>Userid</td>
         <td>
          <input type="text" class="form-control" name="userid" required>
          </td>
          </tr>
          <tr><td>Password</td>
          <td> <input type="password"  class="form-control" name="pswd" required>
          </td>
          </tr>
          <tr><td colspan="2"><input type="submit" class="btn btn-primary" value="Submit"></td></tr>
          <tr><td colspan="2"><a href="forgetpassword" class="black">Forget Password?</a></td></tr>
         </table>
				<br/><br/>			 
							 
							 
						</form>        </div>
                 </div>
            </div>
        </section>
        <!-- ######## About Us End ####### -->


        


        <!--  ************************* Footer Starts Here ************************** -->
        
        <!-- ######## Footer End ####### -->


        <!--  ************************* Copyright Starts Here ************************** -->
        <div class="copy  row">
            <div class="container">
                 <p>2021-2022 © All Rights Reserved  </p> </div>
        </div>
    </div>
    <!-- ######## Copyright End ####### -->

    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="assets/js/jquery-3.2.1.min.js"></script>
    <script src="assets/js/popper.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>
    <script src="assets/plugins/testimonial/js/owl.carousel.min.js"></script>
    <script src="assets/plugins/sticky/js/slick.min.js"></script>
    <script src="assets/plugins/scroll-fixed/jquery-scrolltofixed-min.js"></script>
    <script type="text/javascript" src="assets/plugins/revolution/js/jquery.themepunch.plugins.min.js"></script>
    <script type="text/javascript" src="assets/plugins/revolution/js/jquery.themepunch.revolution.min.js"></script>
    <script src="assets/js/script.js"></script>
</body>

</html>
     
