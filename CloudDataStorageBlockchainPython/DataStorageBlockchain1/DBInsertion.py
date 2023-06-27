from DBConnect import *
import os

from FunFactory import convertFromBase64
def insertDoc1(userid="NA",title="NA",docPath="NA",docDesc='NA',dt="NA",tm="NA",key='NA',) : 
    conn = connect()    
    cursor = conn.cursor()
    args = [userid,title,dt,tm,docDesc,key,docPath]
    args1=cursor.callproc('insertDoc', args)
    print("Return value:", args1)
    #for result in cursor.stored_results():
     #       print(result.fetchall())
    cnt=cursor.rowcount 
    conn.commit()
def saveFile() : 
    lst=[]
    conn = connect()    
    cursor = conn.cursor()
    #cursor.execute("select* from userprofile where userid='"+uid+"'")
    print("select * from documentsTemp")
    sql_select_query = "select * from documentstemp"
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    #record = cursor.fetchall()
    final_result = [list(i) for i in record]
    print(final_result)
    lst=[]
    uid="na"
    UPLOAD_DIR1=os.getcwd()+"\\Documents\\"
    for row in final_result: 
        print("fiinal")
        
        print(row[0])
        path=row[0]
        doc=row[1]
        convertFromBase64(doc,UPLOAD_DIR1+path)
     

    #args = [userid,title,docPath,docDesc,dt,tm,key]
    #args1=cursor.callproc('insertDoc', args)
    #print("Return value:", args1)
    #for result in cursor.stored_results():
    #        print(result.fetchall())
    #cnt=cursor.rowcount
    conn.commit()
    #return cnt
def insertDocPart(docstr="NA",path="NA") : 
    conn = connect()    
    cursor = conn.cursor()
    args = [docstr,path]
    args1=cursor.callproc('insertDocPart', args)
    print("Return value:", args1)
    #for result in cursor.stored_results():
     #       print(result.fetchall())
    cnt=cursor.rowcount 
    conn.commit()


    #args = [userid,title,docPath,docDesc,dt,tm,key]
    #args1=cursor.callproc('insertDoc', args)
    #print("Return value:", args1)
    #for result in cursor.stored_results():
    #        print(result.fetchall())
    #cnt=cursor.rowcount
    conn.commit()
    #return cnt
 
def getMaxIdDoc1():
    conn = connect()
    #integrated security 
    cursor = conn.cursor() 
    cursor.execute('select (ifnull(max(docid),1000)+1) as mxid from documents;')
    mxid=0
    for row in cursor: 
        mxid=row[0]
        print(int(mxid)+1)
    return mxid
