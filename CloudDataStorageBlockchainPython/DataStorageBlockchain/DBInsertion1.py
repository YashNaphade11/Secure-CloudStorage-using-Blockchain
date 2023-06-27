import mysql.connector as mycon
def connect2() : 
    con=mycon.connect(host='bfj6qe07bmhfpleovqxq-mysql.services.clever-cloud.com',user='u59axfrnxxv7iae4',password='ExrJXgQfqfbBRbDvzlGR',database='bfj6qe07bmhfpleovqxq')
    return con
def insertDoc2(userid="NA",title="NA",docPath="NA",docDesc='NA',dt="NA",tm="NA",key='NA',) : 
    conn = connect2()    
    cursor = conn.cursor()
    args = [userid,docDesc,dt,tm,title,key,docPath]
    args1=cursor.callproc('insertDoc', args)
    #print("Return value:", args1)
    #for result in cursor.stored_results():
     #       print(result.fetchall())
    cnt=cursor.rowcount 
    conn.commit()