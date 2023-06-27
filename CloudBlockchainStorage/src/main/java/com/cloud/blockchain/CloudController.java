package com.cloud.blockchain;

import java.io.File;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.List;
import java.util.Vector;

import javax.servlet.ServletRequest;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.springframework.boot.web.servlet.error.ErrorController;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.context.annotation.SessionScope;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.ModelAndView;

import beans.Base64Encoder;
import beans.Mail; 
import models.CheckUser;
import models.Documents;
import models.Offices;
import models.Pass;
import models.PasswordRecovery;
import models.ShareDoc;
import models.Users;
import services.CloudFuns;
import services.GetURL;

@Controller
public class CloudController implements ErrorController{
	@RequestMapping("/home")
	public String index()
	{
		return "index.jsp";
	}
	@RequestMapping("/Cities")
	public String cities()
	{
		return "Cities.jsp";
	}

	@RequestMapping("/ShareImgWithGroups")
	public ModelAndView SubmitReqDocs(HttpServletRequest request,HttpSession ses)
	{
		ModelAndView mv=new ModelAndView();
		//System.out.println("docs="+request.getParameter("chkdoc").toString().trim());
		try {
		    Enumeration  e=request.getParameterNames();
		    String groupName="",docid="";
		    Vector v=new Vector();
		    Vector v1=new Vector();
		    while(e.hasMoreElements())
		    {
		    String Chknm=(String)e.nextElement();
		      if(Chknm.trim().equals("docid"))
		      {
		    	  docid=request.getParameter("docid").toString().trim();
		    	  System.out.println("docid="+docid);
		      }
		      else
		      {
		    	  v.addElement(Chknm.trim());
		    	  v1.addElement(request.getParameter(Chknm.trim()));
		    	  System.out.println("docid="+Chknm);
		      }
		      for(int i=0;i<v.size();i++)
		      {
		    	ShareDoc obj=new ShareDoc();
		    	obj.setGroupName(v.elementAt(i).toString().trim());
		    	obj.setUserid(v1.elementAt(i).toString().trim());
		    	obj.setMsgid(docid);
		    	obj.shareDocsWithGroups();
		      }
		    }
		        
		    mv.setViewName("Success.jsp?type=ShareDoc");
		    mv.addObject("activity","ShareDoc");
		}
		catch (Exception e) {
			// TODO: handle exception
			System.out.println("err="+e.getMessage());
		}
		return mv;
	}
	@RequestMapping("/logout")
	public String logout(HttpSession session) {
        session.invalidate();
		return "Logout.jsp";
	}
	@RequestMapping("/regOffice")
	public String registration()
	{
		return "Register.jsp";
	}
	@RequestMapping("/datasetInsrtPython1")
   	public ModelAndView datasetInsrtPython1(ServletRequest request)
   	{
   		ModelAndView mv=new ModelAndView();  
   		 try {
   			  
   			 
   			 String st=request.getParameter("sts").toString().trim();
   			String docid=request.getParameter("docid").toString().trim();
   		 mv.setViewName("gotoPython.jsp");
   		 mv.addObject("path", services.GetURL.getPythonServerURL()+"/saveDoc.py?docid="+docid);
			
   		  }
   		 catch (Exception e) {
   			// TODO: handle exception
   			 mv.setViewName("Failure.jsp?type=DocUpload");
   		} 
   		// mv.addObject("activity","DocUpload");
   		 return mv;
   		
   	}
	@RequestMapping("/datasetInsrtPython2")
   	public ModelAndView datasetInsrtPython2(ServletRequest request)
   	{
   		ModelAndView mv=new ModelAndView();  
   		 try {
   			  
   			 
   			 String st=request.getParameter("sts").toString().trim();
   			String docid=request.getParameter("docid").toString().trim();
   		 mv.setViewName("gotoPython.jsp");
   		 mv.addObject("path", services.GetURL.getPythonServerURL1()+"/saveDoc.py?docid="+docid);
			
   		  }
   		 catch (Exception e) {
   			// TODO: handle exception
   			 mv.setViewName("Failure.jsp?type=DocUpload");
   		} 
   		// mv.addObject("activity","DocUpload");
   		 return mv;
   		
   	}
	@RequestMapping("/user")
	public String student()
	{
		return "User.jsp";
	}
	@RequestMapping("/dealer")
	public String staff()
	{
		return "Dealer.jsp";
	}
	@RequestMapping("/uploaddoc")
	public String uploaddoc()
	{
		return "UploadDocs.jsp";
	}
	@RequestMapping("/admin")
	public String admin()
	{
		return "Admin.jsp";
	}
	 @RequestMapping("/error")
    public String handleError() {
        //do something like logging
		return "home";
    }
  
    public String getErrorPath() {
        return "/error";
    }
    @RequestMapping("/check")
	public String check(CheckUser cu,HttpServletRequest request) {
		
		String st=cu.checkUser(request);
		
		return st;
	}	  
     
    @RequestMapping("/datasetInsrtPython")
   	public ModelAndView datasetInsrtPython(ServletRequest request)
   	{
   		ModelAndView mv=new ModelAndView();  
   		 try {
   			  
   			 
   			 String st=request.getParameter("sts").toString().trim();
   				if(st.equals("success"))
   					mv.setViewName("Success.jsp");
   				else
   					mv.setViewName("Failure.jsp");
   		 }
   		 catch (Exception e) {
   			// TODO: handle exception
   			 mv.setViewName("Failure.jsp");
   		} 
   		 mv.addObject("activity","DocUpload");
   		 return mv;
   		
   	}	
	@RequestMapping("/viewUsers")
	@SessionScope
	public ModelAndView viewUsers() {
		
		List<Users> lst = new ArrayList<Users>();
		Users vs = new Users();
		lst=vs.getStudentReport();
		ModelAndView mv=new ModelAndView();
		mv.addObject("std",lst);
		mv.setViewName("ViewUsersReport.jsp");
		return mv;
	}
	@RequestMapping("/viewSharedDocs")
	@SessionScope
	public ModelAndView viewSharedDocs(HttpSession ses) {
		ModelAndView mv=new ModelAndView();
		try
		{
		List<models.Documents> lst = new ArrayList<Documents>();
		//CallMinnerAPI vs = new CallMinnerAPI();
		Documents obj=new Documents();
		 
		  obj.getDocs1(ses.getAttribute("userid").toString().trim());
		
		mv.addObject("std",obj.getLst());
		mv.setViewName("ViewSharedDocs.jsp");
		}
		catch (Exception e) {
			// TODO: handle exception
			System.out.println("err="+e.getMessage());
		}
		return mv;
	}
	@RequestMapping("/viewdocs")
	@SessionScope
	public ModelAndView viewMyDocs(HttpSession ses) {
		ModelAndView mv=new ModelAndView();
		try
		{
		List<models.Documents> lst = new ArrayList<Documents>();
		//CallMinnerAPI vs = new CallMinnerAPI();
		Documents obj=new Documents();
		 
		  obj.getDocs(ses.getAttribute("userid").toString().trim());
		
		mv.addObject("std",obj.getLst());
		mv.setViewName("ViewMyDocs.jsp");
		}
		catch (Exception e) {
			// TODO: handle exception
			System.out.println("err="+e.getMessage());
		}
		return mv;
	}
	@RequestMapping("/viewDocs11")
	@SessionScope
	public ModelAndView viewMyDocs11(HttpSession ses,HttpServletRequest request) {
		ModelAndView mv=new ModelAndView();
		try
		{
		List<models.Documents> lst = new ArrayList<Documents>();
		//CallMinnerAPI vs = new CallMinnerAPI();
		Documents obj=new Documents();
		 
		  obj.getDocs(request.getParameter("userid").toString().trim());
		
		mv.addObject("std",obj.getLst());
		mv.setViewName("ViewMyDocs1.jsp");
		}
		catch (Exception e) {
			// TODO: handle exception
			System.out.println("err="+e.getMessage());
		}
		return mv;
	}
	@SessionScope
	@RequestMapping("/sendOTP")
	public ModelAndView sendOTP(Documents eobj,HttpServletRequest request,HttpSession ses)
	{
	 ModelAndView mv=new ModelAndView();
	 
		 try {
			 eobj.setDocid( (request.getParameter("docId").trim()));
			 eobj.setFilePath(request.getParameter("path").trim());
			 eobj.setSeckey(request.getParameter("seckey").trim());
			 eobj.setUserid(ses.getAttribute("userid").toString().trim());
			 String otp= beans.RandomString.getAlphaNumericString(4);
			    mv.setViewName("OTPVerification.jsp");
			    System.out.println("path="+eobj.getFilePath()+" skey="+eobj.getSeckey());
				mv.addObject("path",eobj.getFilePath());
				mv.addObject("docId",eobj.getDocid());
				mv.addObject("seckey",eobj.getSeckey());
				mv.addObject("otp",otp);
				Mail mail=new   Mail();
				System.out.println("otp="+otp);
				CloudFuns jf=new CloudFuns();
				String qr="select emailid,usernm from userdetails where userid='"+ses.getAttribute("userid").toString().trim()+"'";
				Vector v=jf.getValue(qr, 2);
				ses.setAttribute("username", v.elementAt(1).toString().trim());
				ses.setAttribute("email", v.elementAt(0).toString().trim());
				String msg="Dear "+ses.getAttribute("username").toString().trim()+", your one time password is "+otp;
				
				try
				{
				if(mail.sendMail(msg, ses.getAttribute("email").toString().trim(),"One time Password"))
				{
					 jf.recordusage(ses.getAttribute("userid").toString().trim(), "email");
		   			
				}
				}
				catch (Exception e) {
					// TODO: handle exception
					System.out.println("err in mail="+e.getMessage());
				}
			  
		 }
		 catch (Exception e) {
			// TODO: handle exception
			 System.out.println("err="+e.getMessage());
			 mv.setViewName("Failure.jsp?type=sendOTP");
		}
		 return mv;
	}
	@SessionScope
	@RequestMapping("/OTPAuth")
	public ModelAndView OTPAuth(Documents eobj,HttpServletRequest request,HttpSession ses)
	{
		ModelAndView mv=new ModelAndView();
	 
		 try {
			 
			 eobj.setUserid(ses.getAttribute("userid").toString().trim());
			 if(eobj.getOtp().equals(eobj.getUotp()))
			 {
				 System.out.println("otp verified");
			       beans.Base64Encoder encoder=new  Base64Encoder();
				 mv.setViewName("gotoPython.jsp");
				 String seckey=request.getParameter("seckey").toString();
				 //String param= arr[2].trim()+"|"+arr[3].trim()+"|"+arr[4].trim()+"|"+arr[5].trim()+"|"+request.getParameter("filePath").toString().trim() ; 
				 String param= seckey+"|"+request.getParameter("filePath").toString().trim()+"|"+ses.getAttribute("userid").toString().trim() ;
				 System.out.println("param="+param);
				 param=encoder.encode(param.getBytes());
				 mv.addObject("path", GetURL.getPythonServerURL2()+"/DecryptDoc.py?param="+param);
				 
				 //mv.setViewName("Download.jsp");
				// mv.addObject("path","Uploads/temp/"+eobj.getDocpath());
			 }
			 else
			 { 
				mv.setViewName("Failure.jsp?type=OTPAuth"); 
			 }
		 }
		 catch (Exception e) {
			// TODO: handle exception
			 System.out.println("err="+e.getMessage());
			 mv.setViewName("Failure.jsp?type=OTPAuth"); 
		}
		 return mv;
	}
    
    @RequestMapping("/FromPythonDec")
   	public ModelAndView FromPythonDec(ServletRequest request)
   	{
   		ModelAndView mv=new ModelAndView();  
   		 try {
   			  
   			String userid=request.getParameter("userid").toString().trim();
   			CloudFuns cf=new CloudFuns();
   			cf.recordusage(userid, "decryption");
   			 String st=request.getParameter("sts").toString().trim();
   				 
   					mv.setViewName("download.jsp");
   				 mv.addObject("sts",st);
   		 }
   		 catch (Exception e) {
   			// TODO: handle exception
   			 mv.setViewName("Failure.jsp");
   		} 
   		
   		 return mv;
   	}
    @RequestMapping("/shareWithGroups")
	public ModelAndView shareWithGroups(HttpSession ses,HttpServletRequest request)
	{
		List<Users> lst = new ArrayList<Users>();
		Users obj=new Users();
		lst=obj.getUserReport1(ses.getAttribute("userid").toString().trim(),request.getParameter("docid").toString().trim());
		 
		ModelAndView mv = new ModelAndView();

		mv.setViewName("ShareDoc.jsp");
		mv.addObject("docid",request.getParameter("docid").trim());
		mv.addObject("lst", lst); 
		System.out.println("lst="+lst.size());
		return mv;
		 
	}
    @RequestMapping("/registerOffice")
	public ModelAndView registerdealer(Offices stu,ServletRequest request)
	{
		ModelAndView mv=new ModelAndView();
		 try
		 {MultipartFile file=stu.getFile();
		 String filepath=request.getServletContext().getRealPath("/")+"/UploadsOffice/";
		 
		 
		 System.out.println("path="+filepath);
		 File f=new File(filepath);
		 f.mkdir();
		  
		 try {
			  
			 String fileName=stu.getUserid()+"."+ file.getOriginalFilename().split("\\.")[1];
			 file.transferTo(new File(filepath+"/"+fileName));
			 stu.setPath(fileName);
			 String st=stu.addNewUser();
				if(st.equals("success"))
					mv.setViewName("Success.jsp");
				else
					mv.setViewName("Failure.jsp");
		 }
		 catch (Exception e) {
			// TODO: handle exception
			 mv.setViewName("Failure.jsp");
		}}
		 catch (Exception e) {
				// TODO: handle exception
			 mv.setViewName("Failure.jsp");
			}
		 mv.addObject("activity","OfficeReg");
		 return mv;
		
	}	 
	@RequestMapping("/registeruser")
	public ModelAndView registeruser(Users stu,ServletRequest request)
	{
		ModelAndView mv=new ModelAndView();
		 try
		 {MultipartFile file=stu.getFile();
		 String filepath=request.getServletContext().getRealPath("/")+"/Uploads/";
		 
		 
		 System.out.println("path="+filepath);
		 File f=new File(filepath);
		 f.mkdir();
		  
		 try {
			  
			 String fileName=stu.getUserid()+"."+ file.getOriginalFilename().split("\\.")[1];
			 file.transferTo(new File(filepath+"/"+fileName));
			 stu.setPath(fileName);
			 String st=stu.addNewUser();
				if(st.equals("success"))
					mv.setViewName("Success.jsp");
				else
					mv.setViewName("Failure.jsp");
		 }
		 catch (Exception e) {
			// TODO: handle exception
			 mv.setViewName("Failure.jsp");
		}}
		 catch (Exception e) {
				// TODO: handle exception
			 mv.setViewName("Failure.jsp");
			}
		 mv.addObject("activity","UserReg");
		 return mv;
		
	}
	@RequestMapping("/updateuser")
	public ModelAndView updateuser(Users stu,ServletRequest request,HttpSession ses)
	{String fileName="NA";
		
	ModelAndView mv=new ModelAndView();
	try
		 {
			 stu.setUserid(ses.getAttribute("userid").toString().trim());
			 
		  
		 try {
			 MultipartFile file=stu.getFile();
			 String filepath=request.getServletContext().getRealPath("/")+"/Uploads/";
			 
			 
			 System.out.println("path="+filepath);
			 File f=new File(filepath);
			 f.mkdir();
			  fileName=stu.getUserid()+"."+ file.getOriginalFilename().split("\\.")[1];
			 file.transferTo(new File(filepath+"/"+fileName));
			 
		 }
		 catch (Exception e) {
			// TODO: handle exception
			// return "UserRegFailure.jsp";
		}
		 if(!fileName.equals("NA"))
		 {
			 ses.setAttribute("photo", fileName);
		 }
		 stu.setPath(fileName);
		 String st=stu.updateUser(stu.getUserid());
		 if(st.equals("success"))
				mv.setViewName("Success.jsp");
			else
				mv.setViewName("Failure.jsp");
		 }
		 catch (Exception e) {
			 System.out.println("in update="+e.getMessage());
				// TODO: handle exception
			 mv.setViewName("Failure.jsp");
			}
		 mv.addObject("activity","StudProfile");
		 return mv;
	}
	@RequestMapping("/updateDealer")
	public ModelAndView updatestaff(Offices stu,ServletRequest request,HttpSession ses)
	{
		ModelAndView mv=new ModelAndView();
		String fileName="NA";
		 try
		 {
			 stu.setUserid(ses.getAttribute("userid").toString().trim());
			
		 try {
			 MultipartFile file=stu.getFile();
			 String filepath=request.getServletContext().getRealPath("/")+"/UploadsDealer/";
			 
			 
			 System.out.println("path="+filepath);
			 File f=new File(filepath);
			 f.mkdir();
			  
			  fileName=stu.getUserid()+"."+ file.getOriginalFilename().split("\\.")[1];
			 file.transferTo(new File(filepath+"/"+fileName));
			 
		 }
		 catch (Exception e) {
			// TODO: handle exception
			// return "UserRegFailure.jsp";
		}
		 if(!fileName.equals("NA"))
		 {
			 ses.setAttribute("photo", fileName);
		 }
		 stu.setPath(fileName);
		 String st=stu.updateOffice(stu.getUserid());
		 if(st.equals("success"))
				mv.setViewName("Success.jsp");
			else
				mv.setViewName("Failure.jsp");
		 }
		 catch (Exception e) {
			 System.out.println("in update="+e.getMessage());
				// TODO: handle exception
			 mv.setViewName("Failure.jsp");
			}
		 mv.addObject("activity","StaffProfile");
		 return mv;
	}
	@RequestMapping("/forgetpassword")
	public String forgetpassword() {
		
		return("ForgetPassword.jsp");
	}
	@RequestMapping("/recoverpassword")
	public String recoverpassword(PasswordRecovery pr) {
		
		String sts=pr.getNewPassword();
		
		return(sts);
	}
	@RequestMapping("/ChangePass")
	public String ChangePass()
	{
		return "ChangePass.jsp";
	}
	@RequestMapping("/ChangePassService")
	public ModelAndView ChangePassService(Pass eobj,HttpSession ses)
	{
		ModelAndView mv=new ModelAndView();
		 try
		 {
			 
			 eobj.setUserid(ses.getAttribute("userid").toString().trim());
			 if(eobj.changePassword())
			 { 
				 mv.setViewName("Success.jsp");
			 }
			 else
			 { 
				 mv.setViewName("Failure.jsp");
			 }
		 }
		 catch (Exception e) {
			// TODO: handle exception
			 System.out.println("err="+e.getMessage());
			 mv.setViewName("Failure.jsp");
		}
		 mv.addObject("activity","changePass");
		 return mv;
		 
	}

	 

} 
