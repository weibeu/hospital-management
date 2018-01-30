import time    
import pickle
import os
class Hospital:
    def _init_(self):
        self.sno=0
        self.name=' '
        self.age=0
        self.sex=""
        self.email=" "
        self.fname=" "
        self.address=''
        self.city=''
        self.state=''
        self.height=0
        self.weight=0
        self.doctor=''
        self.med=''
        self.bill=0
        self.paymethod=''
        self.pno=0
        self.bgroup=''
        self.dname=''

    def Input(self):
        self.sno=input("Enter Serial number:")
        self.name=raw_input("Enter Patinet's Name:")
        self.age=input("Enter Patinet's Age:")
        self.sex=raw_input("Enter Patinet's Sex (Male/Female):")
        self.height=input("Enter Patinet's Height:")
        self.weight=input("Enter Patinet's Weight(In Kgs):")
        self.bgroup=raw_input("Enter Patient's Blood Group:")
        self.fname=raw_input("Enter Fathers Name:")
        self.address=raw_input("Enter Address:")
        self.city=raw_input("Enter City:")
        self.state=raw_input("Enter State:")
        self.pno=input("Enter Phone number:")
        self.email=raw_input("Enter E-Mail:")
        self.doctor=raw_input("Enter Doctor's Name:")
        self.dname=raw_input("Enter Disease Name:")
        self.med=raw_input("Enter Prescribed Medicine:")
        self.bill=input("Enter Bill Amount: Rs.")
        self.paymethod=raw_input("Enter Payment Method(Cash/Cheque/Card):")
    def Output(self):
        print "SERIAL NUMBER:-",self.sno
        print "PATIENT'S NAME:-",self.name
        print "PATIENT'S AGE:-",self.age
        print "PATIENT'S SEX:-",self.sex
        print "PATIENT'S HEIGHT:-",self.height
        print "PATIENT'S WEIGHT:-",self.weight
        print "PATIENT'S BLOOD GROUP:-",self.bgroup
        print "FATHERS NAME:-",self.fname
        print "ADDRESS:-",self.address
        print "CITY:-",self.city
        print "STATE:-",self.state
        print "CONTACT NUMBER:-",self.pno
        print "E-MAIL ADDRESS:-",self.email
        print "DISEASE NAME:-",self.dname
        print "DOCTOR'S NAME:-",self.doctor
        print "PRESCRIBED MEDICINES:-",self.med
        print "BILL AMOUNT:-",self.bill
        print "PAYMENT METHOD:-",self.paymethod

#FUNCTION
import time
import pickle
import os
def WriteHospital():
    fout=open("Hospital1.DAT","ab")
    ob=Hospital()
    print "Enter Details::"
    ob.Input()
    pickle.dump(ob,fout)
    print "Record Saved"
    fout.close()
def ReadHospital():
    fin=open("Hospital1.DAT","rb")
    ob=Hospital()
    try:
        print "Hospital Details are::"
        while True:
            ob=pickle.load(fin)
            ob.Output()
            print    
    except EOFError:
        fin.close
def SearchHospitalSno(n):       #to search on the basis of sno
    fin=open("Hospital1.DAT","rb")
    ob=Hospital()
    flag=False
    try:
        print
        print"\nHospital Details Are:--"
        while True:
            ob=pickle.load(fin)
            if ob.sno==n:
                ob.Output()
                flag=True
    except EOFError:
        if not flag:
            print "\n"
            print "\n"
            print "               ____________________________________________ " 
            print "               |  ... RECORD... DOES... NOT... EXIST ...  | "
            print "               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
        fin.close()
def SearchHospitalemail(n):       #to search on the basis of email
    fin=open("Hospital1.DAT","rb")
    ob=Hospital()
    flag=False
    try:
        print"\nHospital Details Are:--"
        while True:
            ob=pickle.load(fin)
            if ob.email==n:
                ob.Output()
                flag=True
                break
    except EOFError:
        if not flag:
            print "\n"
            print "\n"
            print "               ____________________________________________ " 
            print "               |  ... RECORD... DOES... NOT... EXIST ...  | "
            print "               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
        fin.close() 
def SearchHospitalcontact(n):      #to search on the basis of Contact Number
    fin=open("Hospital1.DAT","rb")
    ob=Hospital()
    flag=False
    try:
        print"\nHospital Details Are:--"
        while True:
            ob=pickle.load(fin)
            if ob.pno==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print "\n"
                print "\n"
                print "               ____________________________________________ " 
                print "               |  ... RECORD... DOES... NOT... EXIST ...  | "
                print "               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
            fin.close()

def SearchBloodgroup(n):             #to search on the basis of Blood Group
    fin=open("Hospital1.DAT","rb")
    ob=Hospital()
    flag=False
    try:
        print"\nHospital Details are:"
        while True:
            ob=pickle.load(fin)
            if ob.bgroup==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print "\n"
                print "\n"
                print "               ____________________________________________ " 
                print "               |  ... RECORD... DOES... NOT... EXIST ...  | "
                print "               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
            fin.close()

def SearchAge(n):                        #to search on the basis of Age
    fin=open("Hospital1.DAT","rb")
    ob=Hospital()
    flag=False
    try:
        print"\nHospital Details are:"
        while True:
            ob=pickle.load(fin)
            if ob.age==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print "\n"
                print "\n"
                print "               ____________________________________________ " 
                print "               |  ... RECORD... DOES... NOT... EXIST ...  | "
                print "               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
            fin.close()
            
def SearchSex(n):                         #to search on the basis of Sex
    fin=open("Hospital1.DAT","rb")
    ob=Hospital()
    flag=False
    try:
        print"\nHospital Details are:"
        while True:
            ob=pickle.load(fin)
            if ob.sex==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print "\n"
                print "\n"
                print "               ____________________________________________ " 
                print "               |  ... RECORD... DOES... NOT... EXIST ...  | "
                print "               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
            fin.close()

def SearchDName(n):                         #to search on the basis of Disease Name
    fin=open("Hospital1.DAT","rb")
    ob=Hospital()
    flag=False
    try:
        print"\nHospital Details are:"
        while True:
            ob=pickle.load(fin)
            if ob.dname==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print "\n"
                print "\n"
                print "               ____________________________________________ " 
                print "               |  ... RECORD... DOES... NOT... EXIST ...  | "
                print "               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
            fin.close()

def SearchDoctor(n):                         #to search on the basis of Doctors Name
    fin=open("Hospital1.DAT","rb")
    ob=Hospital()
    flag=False
    try:
        print"\nHospital Details are:"
        while True:
            ob=pickle.load(fin)
            if ob.doctor==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print "\n"
                print "\n"
                print "               ____________________________________________ " 
                print "               |  ... RECORD... DOES... NOT... EXIST ...  | "
                print "               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
            fin.close()

def SearchPayment(n):                          #to search on the basis of Payment Method
    fin=open("Hospital1.DAT","rb")
    ob=Hospital()
    flag=False
    try:
        print"\nHospital Details are:"
        while True:
            ob=pickle.load(fin)
            if ob.paymethod==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print "\n"
                print "\n"
                print "               ____________________________________________ " 
                print "               |  ... RECORD... DOES... NOT... EXIST ...  | "
                print "               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
            fin.close()

def ModiHospital(b,a):#to modify details
    fin=open("Hospital1.DAT","rb")
    fout = open ("TEMP.DAT","ab")
    ob=Hospital()
    flag = False
    try:
        while True :
            ob=pickle.load(fin)
            if ob.sno==b:
                flag=True
                if n==1:
                    a=raw_input("ENTER NEW PATIENT'S NAME::")
                    ob.name=a
                    pickle.dump(ob,fout)
                elif n==2: 
                    a=input("ENTER NEW PATIENT'S AGE:-->")
                    ob.age=a
                    pickle.dump(ob,fout)
                elif n==3:
                    a=raw_input("ENTER NEW PATIENT'S SEX(Male/Female):-->")
                    ob.sex=a
                    pickle.dump(ob,fout)
                elif n==4:
                    a=input("ENTER NEW PATIENT'S HEIGHT:-->")
                    ob.height=a
                    pickle.dump(ob,fout)
                elif n==5:
                    a=input("ENTER NEW PATIENT'S WEIGHT(In Kgs):-->")
                    ob.weight=a
                    pickle.dump(ob,fout)
                elif n==6:
                    a=raw_input("ENTER NEW PATIENT'S BLOOD GROUP:-->")
                    ob.bgroup=a
                    pickle.dump(ob,fout)
                elif n==7:
                    a=raw_input("ENTER NEW FATHERS NAME:-->")
                    ob.fname=a
                    pickle.dump(ob,fout)
                elif n==8:
                    a=raw_input("ENTER NEW ADDRESS:-->")
                    ob.address=a
                    pickle.dump(ob,fout)
                elif n==9:
                    a=input("ENTER NEW CITY:-->")
                    ob.city=a
                    pickle.dump(ob,fout)
                elif n==10:
                    a=raw_input("ENTER NEW STATE:-->")
                    ob.state=a
                    pickle.dump(ob,fout)
                elif n==11:
                    a=input("ENTER NEW CONTACT NUMBER:-->")
                    ob.pno=a
                    pickle.dump(ob,fout)
                elif n==12:
                    a=raw_input("ENTER NEW E-MAIL ADDRESS:-->")
                    ob.email=a
                    pickle.dump(ob,fout)
                elif n==13:
                    a=raw_input("ENTER NEW DISEASE NAME:-->")
                    ob.dname=a
                    pickle.dump(ob,fout)
                elif n==14:
                    a=raw_input("ENTER NEW DOCTOR'S NAME:-->")
                    ob.doctor=a
                    pickle.dump(ob,fout)
                elif n==15:
                    a=raw_input("ENTER NEW PRESCRIBED MEDICINE:-->")
                    ob.med=a
                    pickle.dump(ob,fout)
                elif n==16:
                    a=input("ENTER NEW BILL AMOUNT:--> Rs.")
                    ob.bill=a
                    pickle.dump(ob,fout)
                elif n==17:
                    a=raw_input("ENTER NEW PAYMENT METHOD(Cash\Cheque\Card):-->")
                    ob.paymethod=a
                    pickle.dump(ob,fout)
                
                elif n==18:
                    print "__________________ENTER THE NEW DETAILS__________________"
                    ob.Input() 
                    pickle.dump(ob,fout)
                else:
                    print"Enter Valid Choice!"
            else:
                pickle.dump(ob,fout)
            
    except EOFError:
        if not flag:
            print "\n"
            print "\n"
            print "               ____________________________________________ " 
            print "               |  ... RECORD... DOES... NOT... EXIST ...  | "
            print "               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
        fin.close()

    fout.close()
    os.remove("Hospital1.DAT")
    os.rename("TEMP.DAT","Hospital1.DAT")

def DelHospital(n):
    fin=open("Hospital1.DAT","rb")
    fout=open("TEMP.DAT","wb")
    ob=Hospital()
    Flag=False
    try:
        while True:
            ob=pickle.load(fin)
            if ob.sno==n:
                Flag=True
                print"Rcord Deleted"
            else:
                
                pickle.dump(ob,fout)
    except EOFError:
        if not Flag:
            print"Record Does Not Exit"
        fin.close()
        fout.close()
        os.remove("Hospital1.DAT")
        os.rename("TEMP.DAT","Hospital1.DAT")

#MAIN PROGRAM
while True:
    print"\n"
    print"\n"
    print"1.WRITE RECORD\n2.SHOW ALL RECORDS\n3.SEARCH BY SERIAL NUMBER"
    print"4.SEARCH BY CONTACT NUMBER\n5.SEARCH BY BLOOD GROUP\n6.SEARCH BY AGE\n7.SEARCH BY SEX"
    print"8.SEARCH BY DISEASE NAME\n9.SEARCH BY DOCTORS NAME\n10.SEARCH BY PAYMENT METHOD\n11.SEARCH BY E-MAIL"
    print"12.MODIFY RECORD\n13.DELETE RECORD\n14.EXIT"
    ch=input("\nPLEASE ENTER YOUR CHOICE:--")
    if ch==1:
        WriteHospital()
    elif ch==2:
        ReadHospital()
    elif ch==3:
        n=input("PLEASE ENTER SERIAL NUMBER TO SEARCH:--")
        SearchHospitalSno(n)
    elif ch==4:
        n=input("PLEASE ENTER CONTACT NUMBER TO SEARCH:--")
        SearchHospitalcontact(n)
    elif ch==5:
        n=raw_input("PLEASE ENTER BLOOD GROUP TO SEARCH:--")
        SearchBloodgroup(n)
    elif ch==6:
        n=input("PLEASE ENTER AGE TO SEARCH:--")
        SearchAge(n)
    elif ch==7:
        n=raw_input("PLEASE ENTER SEX TO SEARCH:--")
        SearchSex(n)
    elif ch==8:
        n=raw_input("PLEASE ENTER DISEASE NAME TO SEARCH:--")
        SearchDName(n)
    elif ch==9:
        n=raw_input("PLEASE ENTER DOCTORS NAME TO SEARCH:--")
        SearchDoctor(n)
    elif ch==10:
        n=raw_input("PLEASE ENTER PAYMENT METHOD TO SEARCH:--")
        SearchPayment(n)
    elif ch==11:
        n=raw_input("PLEASE ENTER E-MAIL ADDRESS TO SEARCH:--")
        SearchHospitalemail(n)
    elif ch==12:
        m=input("ENTER SERIAL NUMBER TO MODIFY:--")
        print "\n"
        print "               ____________________________________________ " 
        print "               |  ......... ENTER YOUR CHOICE ..........  | "
        print "               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
        print "\n"
        print "WHAT DO YOU WANT TO MODIFY:"
        print 
        print "1.PATIENT'S NAME"
        print "2.PATIENT'S AGE"
        print "3.PATIENT'S SEX"
        print "4.PATIENT'S HEIGHT"
        print "5.PATIENT'S WEIGHT"
        print "6.PATIENT'S BLOOD GROUP:-"
        print "7.FATHERS NAME:-"
        print "8.ADDRESS:-"
        print "9.CITY:-"
        print "10.STATE:-"
        print "11.CONTACT NUMBER:-"
        print "12.E-MAIL ADDRESS:-"
        print "13.DISEASE NAME:-"
        print "14.DOCTOR'S NAME:-"
        print "15.PRESCRIBED MEDICINES:-"
        print "16.BILL AMOUNT:-"
        print "17.PAYMENT METHOD:-"
        print "18.ALL"
        n=input("::--")
        ModiHospital(m,n)
    elif ch==13:
        n=input("ENTER SERIAL NUMBER TO DELETE:-")
        DelHospital(n)
    elif ch==14:
        print "\n"
        print "EXITING",
        time.sleep(.8)
        print ".",
        time.sleep(.8)
        print ".",
        time.sleep(.8)
        print ".",
        time.sleep(.8)
        print ".",
        time.sleep(.8)
        print "."
        break
    else:
        print "Analysing your input.",
        time.sleep(.6)
        print ".",
        time.sleep(.6)
        print ".",
        time.sleep(.6)
        print ".",
        time.sleep(.6)
        print ".",
        time.sleep(.6)
        print "."
        print"\n\n\n~~~~~~~~~~~~~~~~~~~~WRONG CHOICE!!!~~~~~~~~~~~~~~~~~~~\n\n\n"
        

        



        
        
