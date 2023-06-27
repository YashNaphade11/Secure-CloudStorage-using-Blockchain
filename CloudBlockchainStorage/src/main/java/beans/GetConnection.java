package beans;

import java.sql.*;

public class GetConnection {

	private Connection dbconnection;
    public GetConnection()
    {
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
          //  dbconnection=DriverManager.getConnection("jdbc:mysql://u7ctjedr51axblbx:U3Dx6wdfLZBj8l9Sc7vc@bav64wdmsfiexcansaxz-mysql.services.clever-cloud.com:3306/bav64wdmsfiexcansaxz");
            dbconnection=DriverManager.getConnection("jdbc:mysql://localhost:3306/cloudblockchainstoragedb?user=root&password=crosspolo&useSSL=false&allowPublicKeyRetrieval=true");
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    }
    
    public Connection getConnection()
    {
        return(dbconnection);
    }
	
}
