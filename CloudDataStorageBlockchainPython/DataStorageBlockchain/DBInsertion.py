from DBConnect import *
import os

from FunFactory import convertFromBase64
def insertDoc1(userid="NA",title="NA",docPath="NA",docDesc='NA',dt="NA",tm="NA",key='NA',dhash="NA") : 
    conn = connect()    
    cursor = conn.cursor()
    args = [userid,title,dt,tm,docDesc,key,docPath,dhash]
    args1=cursor.callproc('insertDoc', args)
    #print("Return value:", args1)
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
def saveFile(docid=0) : 
    lst=[]
    conn = connect()    
    cursor = conn.cursor()
    #cursor.execute("select* from userprofile where userid='"+uid+"'")
    #print("select * from documentsBackup")
    sql_select_query = "select * from documentsbackup where docid="+docid
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    #record = cursor.fetchall()
    final_result = [list(i) for i in record]
    #print(final_result)
    lst=[]
    uid="na"
    UPLOAD_DIR1=os.getcwd()+"\\Documents\\temp2\\"
    for row in final_result: 
        #print("fiinal")
        
        #print(row[0])
        path=row[2]
        doc=row[3]
        convertFromBase64(doc,UPLOAD_DIR1+path)
     

def insertDocPart(docstr="NA",path="NA") : 
    conn = connect()    
    cursor = conn.cursor()
    args = [docstr,path]
    args1=cursor.callproc('insertDocPart', args)
    #print("Return value:", args1)
    #for result in cursor.stored_results():
     #       print(result.fetchall())
    cnt=cursor.rowcount 
    conn.commit()
def insertDocPartBackup(docstr="NA",path="NA",docid=0) : 
    conn = connect()    
    cursor = conn.cursor()
    args = [docstr,path,docid]
    args1=cursor.callproc('insertDocPartBackup', args)
    #print("Return value:", args1)
    #for result in cursor.stored_results():
     #       print(result.fetchall())
    cnt=cursor.rowcount 
    conn.commit()
def deleteDocPart() : 
    conn = connect()    
    cursor = conn.cursor()
     
    args1=cursor.callproc('deleteDocPart')
    #print("Return value:", args1)
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
        #print(int(mxid)+1)
    return mxid
