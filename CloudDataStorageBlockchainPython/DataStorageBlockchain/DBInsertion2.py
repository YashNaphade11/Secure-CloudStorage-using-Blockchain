import mysql.connector as mycon
def connect1() : 
    con=mycon.connect(host='beypjijz1nueczdcwe4e-mysql.services.clever-cloud.com',user='unxitdhg5x9nk0pr',password='iA6RYWA93JCsIQFyW0lw',database='beypjijz1nueczdcwe4e')
    return con
def insertDoc3(userid="NA",title="NA",docPath="NA",docDesc='NA',dt="NA",tm="NA",key='NA',) : 
    conn = connect1()    
    cursor = conn.cursor()
    args = [userid,docDesc,dt,tm,title,key,docPath]
    args1=cursor.callproc('insertDoc', args)
    #print("Return value:", args1)
    #for result in cursor.stored_results():
     #       print(result.fetchall())
    cnt=cursor.rowcount 
    conn.commit()