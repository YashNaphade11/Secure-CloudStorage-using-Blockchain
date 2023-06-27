#!C:\Users\Megha Home\AppData\Local\Programs\Python\Python310\python
import mysql.connector as mycon

def connect() : 
    con=mycon.connect(host='localhost',user='root',password='crosspolo',database='cloudblockchainstoragedb')
    return con
def connect1() : 
    con=mycon.connect(host='bav64wdmsfiexcansaxz-mysql.services.clever-cloud.com',user='u7ctjedr51axblbx',password='U3Dx6wdfLZBj8l9Sc7vc',database='bav64wdmsfiexcansaxz')
    return con