import hashlib 
import os 
import random
import base64
import shutil
from DBInsertion import insertDocPart, insertDocPartBackup, saveFile
from FunFactory import convertToBase64

from encrypt1 import decrypt, encrypt, getKey
def encryption(infile="NA",ext="NA",seckey1="NA",docid=0):
    UPLOAD_DIR=os.getcwd()+"\\Documents\\temp\\" 
    UPLOAD_DIR1=os.getcwd()+"\\Documents\\" 
    outfile=UPLOAD_DIR1+infile
    docid=str(docid)
    metadataFile=str(docid)+".txt"
    ifile = open(UPLOAD_DIR+infile,'rb')    
    byt=ifile.read()
    len1=len(byt)
    len2=int(len1/4)
    len3=len1-(len2+len2+len2)
    #print(str(len1))
    ifile = open(UPLOAD_DIR+infile,'rb')
    data1 = ifile.read(len2)
    data2 = ifile.read(len2)
    data3 = ifile.read(len2)
    data4 = ifile.read(len3)

    skey1="key@"+str(random.randint(11,99))
    skey2="key@"+str(random.randint(11,99))
    skey3="key@"+str(random.randint(11,99))
    skey4="key@"+str(random.randint(11,99))


    #print(str(len(data1)))
    #print(str(len(data1)))
    with open(UPLOAD_DIR+"//"+docid+"_part1."+ext, 'wb') as ofile:
        ofile.write(data1) 
    with open(UPLOAD_DIR+"//"+docid+"_part2."+ext, 'wb') as ofile:
        ofile.write(data2) 
    with open(UPLOAD_DIR+"//"+docid+"_part3."+ext, 'wb') as ofile:
        ofile.write(data3) 
    with open(UPLOAD_DIR+"//"+docid+"_part4."+ext, 'wb') as ofile:
        ofile.write(data4) 
     
    encrypt(getKey(skey1),docid+"_part1."+ext,UPLOAD_DIR+"//") 
    encrypt(getKey(skey2),docid+"_part2."+ext,UPLOAD_DIR+"//")
    encrypt(getKey(skey3),docid+"_part3."+ext,UPLOAD_DIR+"//")
    encrypt(getKey(skey4),docid+"_part4."+ext,UPLOAD_DIR+"//")
     

    mylist = [0,1,2,3]
    #3|1|2|0
    random.shuffle(mylist)
    seq=str(mylist[0])+"|"+str(mylist[1])+"|"+str(mylist[2])+"|"+str(mylist[3])
   
    str1=str(skey1)+"|"+str(skey2)+"|"+str(skey3)+"|"+str(skey4)+"*"+seq
    file1="na"
    file2="na"
    if mylist[0]==0:
        file1="enc_"+docid+"_part1."+ext
    elif mylist[0]==1:
        file1="enc_"+docid+"_part2."+ext
    elif mylist[0]==2:
        file1="enc_"+docid+"_part3."+ext
    elif mylist[0]==3:
        file1="enc_"+docid+"_part4."+ext
    
    if mylist[1]==0:
        file2="enc_"+docid+"_part1."+ext
    elif mylist[1]==1:
        file2="enc_"+docid+"_part2."+ext
    elif mylist[1]==2:
        file2="enc_"+docid+"_part3."+ext
    elif mylist[1]==3:
        file2="enc_"+docid+"_part4."+ext

    if mylist[2]==0:
        file3="enc_"+docid+"_part1."+ext
    elif mylist[2]==1:
        file3="enc_"+docid+"_part2."+ext
    elif mylist[2]==2:
        file3="enc_"+docid+"_part3."+ext
    elif mylist[2]==3:
        file3="enc_"+docid+"_part4."+ext

    if mylist[3]==0:
        file4="enc_"+docid+"_part1."+ext
    elif mylist[3]==1:
        file4="enc_"+docid+"_part2."+ext
    elif mylist[3]==2:
        file4="enc_"+docid+"_part3."+ext
    elif mylist[3]==3:
        file4="enc_"+docid+"_part4."+ext
    
    #print("file1="+file1)
    #print(file2)
    ifile1 = open(UPLOAD_DIR+file1,'rb')
    data1 = ifile1.read()
    strdata1=convertToBase64(UPLOAD_DIR+file1)
    insertDocPart(strdata1,file1)
    insertDocPartBackup(strdata1,file1,docid)

    ifile2 = open(UPLOAD_DIR+file2,'rb')
    data2 = ifile2.read()
    strdata2=convertToBase64(UPLOAD_DIR+file2)
    insertDocPart(strdata2,file2)
    insertDocPartBackup(strdata2,file2,docid)

    strdata3=convertToBase64(UPLOAD_DIR+file3)
   
    insertDocPartBackup(strdata3,file3,docid)

    strdata4=convertToBase64(UPLOAD_DIR+file4)
   
    insertDocPartBackup(strdata4,file4,docid)

    with open(UPLOAD_DIR1+"/"+metadataFile, 'w') as ofile:
        ofile.write(str1) 
    #ofile.close()
    encrypt(getKey(seckey1),metadataFile,UPLOAD_DIR1+"//") 
    shutil.copy(UPLOAD_DIR+"/"+file3, UPLOAD_DIR1+"/"+file3)
    shutil.copy(UPLOAD_DIR+"/"+file4, UPLOAD_DIR1+"/"+file4)
    
    '''with open(UPLOAD_DIR+"//test1.png", 'wb') as ofile:
        ofile.write(data1) 
        ofile.write(data2)
        '''
    return str1



def decryption(infile="NA",ext="NA",seckey1="NA",docid=0):
    UPLOAD_DIR1=os.getcwd()+"\\Documents\\"
    UPLOAD_DIR=os.getcwd()+"\\Documents\\temp\\" 
    #ifile = open(UPLOAD_DIR1+infile,'rb')    
    #byt=ifile.read()
    #decodedBytes = base64.b64decode(byt)
    #print("file="+UPLOAD_DIR1+"enc_"+docid)
    decrypt(getKey(seckey1),UPLOAD_DIR1+"enc_"+docid+".txt",UPLOAD_DIR+docid+".txt") 
    
    getMetadataFile = open(UPLOAD_DIR+"/"+docid+".txt",'r')
    metadata = getMetadataFile.read()
    #print("file="+metadata)
    keys,seq=metadata.split('*')
    #print("keys============"+keys+" ---------------")
    klst=keys.split("|")
    #print(keys)
    #print("======="+str(klst)+"-------")
   
    lstseq=seq.split('|')
    #print("sequence")
    #print(str(lstseq))
    saveFile(docid)
   
    
    for i in lstseq:
        #print("i=")
        #print(i)
        #ifile = open(UPLOAD_DIR1+"\\temp2\\enc_"+docid+"_part"+i+"."+ext,'rb')
        filepath=UPLOAD_DIR1+"\\temp2\\enc_"+docid+"_part"+str(int(i)+1)+"."+ext
        outfilepath=UPLOAD_DIR1+"\\temp3\\enc_"+docid+"_part"+str(int(i)+1)+"."+ext
        if int(i)==0:
            #print("seq==")
            #print(lstseq[int(i)]) 
            #data1 = ifile.read()
            #print("=========="+str(klst[int(0)])+"============")
            decrypt(getKey(klst[int(0)]),filepath,outfilepath)
            ifile = open(outfilepath,'rb')
            data1=ifile.read()
        elif int(i)==1:
            #print("seq==")
            #print(lstseq[int(i)])
            decrypt(getKey(klst[int(1)]),filepath,outfilepath)
            ifile = open(outfilepath,'rb')
            data2=ifile.read()
            
        elif int(i)==2:
            #print("seq==")
            #print(int(i))
            decrypt(getKey(klst[int(2)]),filepath,outfilepath)
            ifile = open(outfilepath,'rb')
            data3=ifile.read()
        else: 
             
            #print("seq==")
            #print(lstseq[int(i)])
            decrypt(getKey(klst[int(3)]),filepath,outfilepath)
            ifile = open(outfilepath,'rb')
            data4=ifile.read()

    with open(UPLOAD_DIR+"\\combined_dec1_"+docid+"."+ext, 'wb') as ofile:
        ofile.write(data1) 
        ofile.write(data2) 
        ofile.write(data3) 
        ofile.write(data4) 


     
    return "combined_dec1_"+docid+"."+ext
    
 
def combineFiles(path1="NA",path2="NA",path3="NA",path4="NA",combinedPath="NA"):
    ifile = open(path1,'rb')
    data1 = ifile.read()

    ifile = open(path2,'rb')
    data2 = ifile.read()

    ifile = open(path3,'rb')
    data3 = ifile.read()

    ifile = open(path4,'rb')
    data4 = ifile.read()
    mylist = [0,1,2,3]
    #3|1|2|0
    random.shuffle(mylist)
    arr=[[data1],[data2],[data3],[data4]]
    with open(combinedPath, 'wb') as ofile:
        for i in mylist:
            if i==0:
                data11=data1
            elif i==1:
                data11=data2
            elif i==2:
                data11=data3
            elif i==3:
                data11=data4
            ofile.write(data11) 
             
    #ifile = open(combinedPath,'rb')
    #data = ifile.read()
    #encoded = base64.b64encode(data)
    #with open(combinedPath, 'wb') as ofile:
    #    ofile.write(data) 
    seq=str(mylist[0])+"|"+str(mylist[1])+"|"+str(mylist[2])+"|"+str(mylist[3])
    return seq

def getHash(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()
