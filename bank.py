from Tkinter import *
from sqlite3 import *
from tkMessageBox import *
import sys,copy,math,time,random

class ritu(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.label=Label(self,text="State Bank of India",font="Times 60 bold",fg="blue").grid(row=0,column=1,columnspan=1)
        self.label2=Label(self,text="Address-Juet A.B Road Raghogarh ",font="Times 20 bold",fg="black").grid(row=2,column=0,columnspan=7)
        self.label3=Label(self,text="Dist-Guna  State-MadhyaPradesh",font="Times 20 bold",fg="black").grid(row=3,column=0,columnspan=3)
        
        self.label5=Label(self,text="Contact here...",font="Times 20 bold",fg="black").grid(row=2,column=6,columnspan=3)
        
        
        self.label7=Label(self,text="Nominee Detail",font="Times 20 bold",fg="red").grid(row=10,column=0)
        self.label8=Label(self,text="Click here to view Nominee Detail....",font="Times 20 bold",fg="purple").grid(row=11,column=0,columnspan=4)
        self.button=Button(self,text="View",font="Times 20 bold",fg="purple",padx=10,pady=5,bd=10,command=self.press)
        self.button.grid(row=11,column=2,columnspan=7)
        self.button.bind("<Enter>",self.pr)
        self.button.bind("<Leave>",self.clk)
        self.label9=Label(self,text="Account Detail",font="Times 20 bold",fg="red").grid(row=13,column=0)
        self.label10=Label(self,text="Click here to make changes in Nominee Detail....",font="Times 20 bold",fg="purple").grid(row=14,column=0,columnspan=5)
        self.button2=Button(self,text="View",font="Times 20 bold",fg="purple",padx=10,pady=5,bd=10,command=self.remove)
        self.button2.grid(row=14,column=2,columnspan=7)
        self.button2.bind("<Enter>",self.pr)
        self.button2.bind("<Leave>",self.clk)
        self.label11=Label(self,text="Create a Database for Nominee Detail...",font="Times 30 bold",fg="green").grid(row=15,column=1)
        self.button3=Button(self,text="New Nominee record",font="Times 20 bold",fg="purple",padx=10,pady=5,bd=10,command=self.create)
        self.button3.bind("<Enter>",self.pr)
        self.button3.bind("<Leave>",self.clk)
        self.button3.grid(row=17,column=1,columnspan=4)
       
    def clk(self,sonu):
        sonu.widget.config(relief="raised")
    def pr(self,sonu):
        sonu.widget.config(relief=GROOVE)
    def remove(self):
        class pusa(Frame):
            def __init__(self,master):
                Frame.__init__(self,master)
                self.grid()
                
                self.label=Label(self,text="Make changes in account....",font="Times 40 bold",fg="blue").grid(row=0,column=0,columnspan=2)
                ## update name
                self.label=Label(self,text="Enter Nominee Id",font="Times 20 bold",fg="green").grid(row=2,column=0)
                self.entry5=Entry(self,width=20,font="Times 20 bold",fg="blue")
                self.entry5.grid(row=2,column=1)
                self.label=Label(self,text="Enter New Name",font="Times 20 bold",fg="green").grid(row=3,column=0)
                self.entry6=Entry(self,width=20,font="Times 20 bold",fg="green")
                self.entry6.grid(row=3,column=1)
                
                ##update new address
                self.label=Label(self,text="Enter Nominee Id",font="Times 20 bold",fg="green").grid(row=6,column=0)
                self.entry2=Entry(self,width=20,font="Times 20 bold",fg="purple")
                self.entry2.grid(row=6,column=1)
                self.label=Label(self,text="Enter New Address",font="Times 20 bold",fg="green").grid(row=7,column=0)
                self.entry3=Entry(self,width=20,font="Times 20 bold",fg="purple")
                self.entry3.grid(row=7,column=1)
                
                
                self.button3=Button(self,text="Update Name",font="Times 20 bold",fg="red",padx=10,pady=5,bd=10,command=self.name)
                self.button3.bind("<Enter>",self.pr)
                self.button3.bind("<Leave>",self.clk)
                self.button3.grid(row=5,column=0,columnspan=2)
                self.button2=Button(self,text="Delete",font="Times 20 bold",fg="blue",padx=10,pady=5,bd=10,command=self.delete)
                self.button2.bind("<Enter>",self.pr)
                self.button2.bind("<Leave>",self.clk)
                self.button2.grid(row=14,column=0,columnspan=2)
                self.button1=Button(self,text="Update Add",font="Times 20 bold",fg="green",padx=10,pady=5,bd=10,command=self.add)
                self.button1.bind("<Enter>",self.pr)
                self.button1.bind("<Leave>",self.clk)
                self.button1.grid(row=9,column=0,columnspan=2)
                
                ##Amount Transfer
                self.label3=Label(self,text="Amount Transfer...",font="Times 20 bold",fg="red").grid(row=3,column=2)

                self.label=Label(self,text="From..",font="Times 20 bold",fg="blue").grid(row=4,column=2)
                self.label=Label(self,text="Enter Nominee Id",font="Times 20 bold",fg="green").grid(row=5,column=2,columnspan=3)
                self.entry=Entry(self,width=20,font="Times 20 bold",fg="blue")
                self.entry.grid(row=5,column=5,columnspan=2)
                self.label=Label(self,text="Enter Amount to\nTransfer...",font="Times 20 bold",fg="green").grid(row=6,column=2)
                self.entry7=Entry(self,width=20,font="Times 20 bold",fg="blue")
                self.entry7.grid(row=6,column=5,columnspan=2)
                self.label4=Label(self,text="To..",font="Times 20 bold",fg="blue").grid(row=7,column=2)
                self.label=Label(self,text="Enter Nominee Id",font="Times 20 bold",fg="green").grid(row=8,column=2)
                self.entry8=Entry(self,width=20,font="Times 20 bold",fg="blue")
                self.entry8.grid(row=8,column=5,columnspan=2)
                self.label3=Label(self,text="Click here to Transfer...",font="Times 20 bold",fg="red").grid(row=9,column=2)

                self.button1=Button(self,text="Press",font="Times 20 bold",fg="green",padx=10,pady=5,bd=10,command=self.transfer)
                self.button1.bind("<Enter>",self.pr)
                self.button1.bind("<Leave>",self.clk)
                self.button1.grid(row=9,column=5,rowspan=3)






                
            def transfer(self):
                content=self.entry.get()
                content4=self.entry7.get()
                content5=self.entry8.get()
                content6=time.asctime()
                self.conn=connect("example.db")
                self.cur=self.conn.cursor()
                self.cur.execute("insert into ritu(cust_id,amt_withdraw,date6)values(?,?,?)",(content,content4,content6))
                self.cur.execute("insert into ritu(cust_id,balance,date6)values(?,?,?)",(content5,content4,content6))
                
                self.conn.commit()
                
            def clk(self,sonu):
                sonu.widget.config(relief="raised")
            def pr(self,sonu):
                sonu.widget.config(relief=GROOVE)
           
                                
             ##update name   
            def name(self):
                content=self.entry5.get()
                content2=self.entry6.get()
                self.conn=connect("example.db")
                self.cur=self.conn.cursor()
                
                self.cur.execute("update monu set fn='%s'where monu.id is %s" %(content2,content))
                result=self.cur.fetchall()
                self.conn.commit()
               
                
             ##update address   
            def add(self):
                content=self.entry2.get()
                content2=self.entry3.get()
                self.conn=connect("example.db")
                self.cur=self.conn.cursor()
                
                self.cur.execute("update monu set city='%s' where monu.id is %s" %(content2,content))
               
                result=self.cur.fetchall()
                self.conn.commit()
                
             ##delete record   
            def delete(self):
                content=self.entry4.get()
                self.conn=connect("example.db")
                self.cur=self.conn.cursor()
                raj=askquestion("Message","Do you want to permanently delete this account?")
                
                
                self.cur.execute("delete from monu where monu.id is %s" %(content))
                result=self.cur.fetchall()
                self.conn.commit()

                
                        
                
        bitu=Tk()
        bitu.geometry('1350x760')
        bitu2=pusa(bitu)
        bitu.mainloop()
        
    def press(self):
        class golu(Frame):
            
            def __init__(self,master):
                Frame.__init__(self,master)
                self.pack()
                self.create_widgets()
            def create_widgets(self):
                self.label=Label(self,text="State Bank of India",font="Times 60 bold",fg="blue").grid(row=0,column=1,columnspan=1)
                self.label2=Label(self,text="Address-Juet A.B Road Raghogarh ",font="Times 20 bold",fg="black").grid(row=2,column=0,columnspan=5)
                self.label3=Label(self,text="Dist-Guna  State-MadhyaPradesh",font="Times 20 bold",fg="black").grid(row=3,column=0,columnspan=3)
                self.label4=Label(self,text="IFSC Code/ MICR Code / Branch Code - CBIN0282156 / NON-MICR / 282156",font="Times 20 bold",fg="black").grid(row=4,column=0,columnspan=4)
                self.label5=Label(self,text="Contact here...",font="Times 20 bold",fg="black").grid(row=2,column=4,columnspan=3)
                self.label6=Label(self,text="Mob-8602218669",font="Times 20 bold",fg="red").grid(row=3,column=4,columnspan=3)
                self.label7=Label(self,text="Nominee Detail.....",font="Times 30 bold",fg="red").grid(row=7,column=0)
                self.label8=Label(self,text="Enter Nominee id here...",font="Times 20 bold",fg="green").grid(row=9,column=0)
                self.e=StringVar()


                self.entry=Entry(self,textvariable=self.e,width=20,font="Times 20 bold",fg="purple")
                self.entry.grid(row=9,column=0,columnspan=2)
                self.button=Button(self,text="View Detail",font="Times 20 bold",fg="red",bd=10,padx=20,pady=10,command=self.click)
                self.button.grid(row=12,column=0,columnspan=1)
                self.button.bind("<Enter>",self.pr)
                self.button.bind("<Leave>",self.clk)
                self.button=Button(self,text="Back",font="Times 20 bold",fg="red",bd=10,padx=10,pady=5,command=self.go)
                self.button.grid(row=0,column=0)
                self.button.bind("<Enter>",self.pr)
                self.button.bind("<Leave>",self.clk)
                self.g=StringVar()
                self.h=StringVar()
                
            def go(self):
                
                raju.destroy()
                monu=Tk()
                monu.destroy()
                monu.mainloop()
                 
                        
            def clk(self,sonu):
                sonu.widget.config(relief="raised")
            def pr(self,sonu):
                sonu.widget.config(relief=GROOVE)
            def click(self):
                
                content=self.entry.get()
                self.conn=connect("example.db")
                self.cur=self.conn.cursor()
                self.cur.execute("select id,fn,city,balance,amt_withdraw,sum(balance),sum(amt_withdraw),date6 from ritu,monu where ritu.cust_id==monu.id and cust_id is %s" %(content))
                result=self.cur.fetchall()
                
                class munna(Frame):

                    def __init__(self,master):
                        Frame.__init__(self,master)
                        self.pack()
                        munna=()
                        for item in result:
                            munna+=copy.deepcopy(item)
                        self.widgets(munna)


                    def widgets(self,munna):
                        self.label=Label(self,text="Nominee Personal information here..",font="Times 40 bold",fg="red")
                        self.label.grid(row=0,columnspan=2)
                        ritu=['Nominee Id','Name','Address','Account Particulars...']
                        i=1
                        for item in ritu:
                            if item==ritu[-1]:
                                 self.label=Label(self,text=item,font="Times 30 bold",fg="red")
                                 self.label.grid(row=i,column=0,columnspan=5)
                                 
                            else:
                                
                                self.label=Label(self,text=item,font="Times 20 bold",fg="green")
                                self.label.grid(row=i,column=0,columnspan=2)
                                i+=1
                      
                        ritu=['Current Deposit','Current withdraw','Total Amount Deposit','Total withdraw','Date','Remaining Bal']
                        i=7
                        for item in ritu:
                             self.label=Label(self,text=item,font="Times 20 bold",fg="green")
                             self.label.grid(row=i,column=0,columnspan=2)
                             i+=1

                       
                        self.label3=Label(self,text="Click here to see previous record...",font="Times 30 bold",fg="red")
                        self.label3.grid(row=13,column=0)
                        self.button=Button(self,text="Previous Record",font="Times 20 bold",fg="green",bd=10,command=self.check)
                        self.button.grid(row=15,column=0)
                        self.button.bind("<Enter>",self.pr)
                        self.button.bind("<Leave>",self.clk)
                        self.button=Button(self,text="Back",font="Times 20 bold",fg="red",bd=10,command=self.go2)
                        self.button.grid(row=0,column=6)
                        self.button.bind("<Enter>",self.pr)
                        self.button.bind("<Leave>",self.clk)
                        
                        ### here account information
                        '''self.label4=Label(self,text="Account  information..",font="Times 20 bold",fg="red")
                        self.label4.grid(row=6,column=0)
                        self.label4=Label(self,text="Amount Borrow-%s"%content2,font="Times 20 bold",fg="red")
                        self.label4.grid(row=8,column=0)
                        self.label4=Label(self,text="Amount paid-%s"%content3,font="Times 20 bold",fg="red")
                        self.label4.grid(row=10,column=0)
                        self.label4=Label(self,text="Balance still to paid-%s"%content4,font="Times 20 bold",fg="red")
                        self.label4.grid(row=12,column=0)'''
                        
                        
                        raj=list(munna)
                        raj.append(raj[5]-raj[6])
                        
                        
                        
                        i=0       
                        while i<3:
                             self.label4=Label(self,text=raj[i],font="Times 20 bold",fg="blue")
                             i+=1
                             self.label4.grid(row=i,column=1)
                          
                        k=7
                        while i>2 and i<len(raj):
                            if i==len(raj)-2:
                                self.label4=Label(self,text=raj[i],font="Times 20 bold",fg="green")
                                self.label4.grid(row=k,column=1)
                                k+=1
                                i+=1
                            else:
                                
                                self.label4=Label(self,text=raj[i],font="Times 20 bold",fg="blue")
                                self.label4.grid(row=k,column=1)
                                i+=1
                                k+=1
                                
                               
                       
                               
                    
                    def go2(self):
                        window.destroy()
                        raju=Tk()
                        raju.destroy()
                        raju.mainloop()
                                        
                        
                    def check(self):
                    
                        class label(Frame):
                            def __init__(self,master):
                                Frame.__init__(self,master)
                                self.grid()
                                self.label4=Label(self,text="Nominee Previous record here....",font="Times 25 bold",fg="green")
                                self.label4.grid(row=0,column=1,columnspan=2)
                                self.button=Button(self,text="Back",font="Times 20 bold",fg="red",bd=10,command=self.go3)
                                self.button.grid(row=0,column=0)
                                self.button.bind("<Enter>",self.pr)
                                self.button.bind("<Leave>",self.clk)
                                
                                ritu=['Nominee Id','Deposit Amount','Amount Withdraw','Trans Date and Time']
                                i=1
                                j=0
                                for item in range(len(ritu)):
                                    self.label4=Label(self,text=ritu[item],font="Times 20 bold",fg="red")
                                    self.label4.grid(row=i,column=j)
                                    j+=1
                                
                                
                                self.conn=connect("example.db")
                                self.cur=self.conn.cursor()
                                self.cur.execute("select id,balance,amt_withdraw,date6 from ritu,monu where ritu.cust_id==monu.id and cust_id is %s" %(content))
                                result=self.cur.fetchall()
                                ritu=()
                                for item in result:
                                    ritu+=copy.deepcopy(item)
                                raj=list(ritu)
                                print len(raj)
                                
                                j=0
                                i=4
                                for item in raj[0:4]:
                                     self.label4=Label(self,text=item,font="Times 20 bold",fg="blue")

                                     self.label4.grid(row=i,column=j )
                                     j+=1
                                     if j==len(raj) and item==raj[3]:
                                          self.label=Label(self,text='<==current',font="Times 40 bold",fg="red")

                                          self.label.grid(row=i,column=5 )
                                            
                                l=5
                                k=0
                                x=4
                                y=8
                                j=0
                                temp=len(raj[x:])
                                #print temp
                               
                                while k<temp:
                                    
                                    
                                            
                                    
                                    if x==temp:
                                        for item in raj[x:]:
                            
                            
                                            self.label5=Label(self,text=item,font="Times 20 bold",fg="green")

                                            self.label5.grid(row=l,column=j )
                                            j+=1
                                            if item==raj[temp+3]:
                                                self.label5=Label(self,text='<==current',font="Times 40 bold",fg="red")

                                                self.label5.grid(row=l,column=5 )
                                            
                                    else:
                                        for item in raj[x:y]:
                                            self.label4=Label(self,text=item,font="Times 20 bold",fg="blue")

                                            self.label4.grid(row=l,column=j )
                                            j+=1
                                            
                                            
                                    x+=4
                                    k+=1
                                    l+=1
                                    j=0
                                    y+=4
                                    
                                          
                            def go3(self):
                                    sachin.destroy()
                                    window=Tk()
                                    window.destroy()
                                    window.mainloop()
                                        
                                
                                
                            def clk(self,sonu):
                                sonu.widget.config(relief="raised")
                            def pr(self,sonu):
                                sonu.widget.config(relief=GROOVE)

                                                        
                                        
                                        
                                       
                                            
                                           
                                        
                                         
                        sachin=Tk()
                        sachin.geometry("1350x760")
                        app=label(sachin)
                        sachin.mainloop()
                                            
                                    
                        
                                
                                
                        
                        
                                       
                    def clk(self,sonu):
                        
                      
                        sonu.widget.config(relief="raised")
                    def pr(self,sonu):
                        
                        sonu.widget.config(relief=GROOVE)        

            
                window=Tk()
                mun=munna(window)
                window.geometry("1350x760")
                window.mainloop()
                monu.destroy()
                    
                        
                


        raju=Tk()
        monu2=golu(raju)
        raju.geometry("1350x760")
        raju.mainloop()
                        
        


    def create(self):
    
    
            
        class katrina(Frame):
            def __init__(self,master):
                Frame.__init__(self,master)
                
                self.grid()
                self.create_widgets()
            def record(self):
                
            
                a1=self.entry.get()
                
                b1=self.entry2.get()
                c1=self.entry3.get()
                
               
                self.cur=self.conn.cursor()
                self.cur.execute("insert into monu(id,fn,city ) values(?,?,?)",(a1,b1,c1))
                self.conn.commit()
            
            def record2(self):
                
                a2= (self.entry4.get())
                b2=(self.entry5.get())
                c2=(self.entry6.get())
                d2=time.asctime()
            
                self.cur=self.conn.cursor()
                
                self.cur.execute("insert into ritu(cust_id,balance,amt_withdraw,date6) values(?,?,?,?)",(a2,b2,c2,d2))    

                self.conn.commit()
               
            def create_widgets(self):
                self.a=StringVar()
                self.b=StringVar()
                self.c=StringVar()
                self.l=StringVar()

                self.m=StringVar()
                self.n=StringVar()
                self.label=Label(self,text="Nominee Record Analysis.... ",font="Times 30 bold",fg="red").grid(row=1,column=0)
                ##make connection
                self.button3=Button(self,text="First Make Connection",font="Times 20 bold",fg="purple",padx=10,pady=5,bd=10,command=self.data)
                self.button3.bind("<Enter>",self.pr)
                self.button3.bind("<Leave>",self.clk)
                self.button3.grid(row=3,column=0)
                ##make connection close
                self.button3=Button(self,text="Close Connection",font="Times 20 bold",fg="purple",padx=10,pady=5,bd=10,command=self.close)
                self.button3.bind("<Enter>",self.pr)
                self.button3.bind("<Leave>",self.clk)
                self.button3.grid(row=3,column=3)
                #insert record
                self.button3=Button(self,text="Insert record",font="Times 20 bold",fg="purple",padx=10,pady=5,bd=10,command=self.record)
                self.button3.bind("<Enter>",self.pr)
                self.button3.bind("<Leave>",self.clk)
                self.button3.grid(row=12,column=0,columnspan=2)
                self.button3=Button(self,text="Insert",font="Times 20 bold",fg="purple",padx=10,pady=5,bd=10,command=self.record2)
                self.button3.bind("<Enter>",self.pr)
                self.button3.bind("<Leave>",self.clk)
                self.button3.grid(row=19,column=0,columnspan=2)
                #view record
                self.button3=Button(self,text="View record",font="Times 20 bold",fg="purple",padx=10,pady=5,bd=10,command=self.show)
                self.button3.bind("<Enter>",self.pr)
                self.button3.bind("<Leave>",self.clk)
                self.button3.grid(row=19,column=3)
                  
                
                self.label6=Label(self,text="Insert new record in Database.... ",font="Times 35 bold",fg="green").grid(row=6,column=0,columnspan=6)
                self.label6=Label(self,text="See record here.... ",font="Times 20 bold",fg="red").grid(row=7,column=1,columnspan=7)

                self.label6=Label(self,text="Enter Nominee id",font="Times 25 bold",fg="red").grid(row=8,column=0)
                self.label6=Label(self,text="Name",font="Times 25 bold",fg="red").grid(row=9,column=0)
                self.label6=Label(self,text="Address",font="Times 25 bold",fg="red").grid(row=10,column=0)
                self.label6=Label(self,text="Account information...",font="Times 35 bold",fg="green").grid(row=14,column=0,columnspan=1)
                self.label6=Label(self,text="Enter amount to deposit",font="Times 25 bold",fg="red").grid(row=17,column=0)
                self.label6=Label(self,text="Amount withdraw",font="Times 25 bold",fg="red").grid(row=18,column=0)
                self.label6=Label(self,text="Nominee id..",font="Times 25 bold",fg="red").grid(row=16,column=0)
                
                self.entry=Entry(self,width=10,textvariable=self.a,font="Times 20 bold",fg="purple")
                self.entry.grid(row=8,column=1)
                self.entry2=Entry(self,width=10,textvariable=self.b,font="Times 20 bold",fg="purple")
                self.entry2.grid(row=9,column=1)
                self.entry3=Entry(self,width=10,textvariable=self.c,font="Times 20 bold",fg="purple")
                self.entry3.grid(row=10,column=1)
                self.entry4=Entry(self,width=10,textvariable=self.l,font="Times 20 bold",fg="purple")
                self.entry4.grid(row=16,column=1)
               
                self.entry5=Entry(self,width=10,textvariable=self.m,font="Times 20 bold",fg="purple")
                self.entry5.grid(row=17,column=1)
                self.entry6=Entry(self,width=10,textvariable=self.n,font="Times 20 bold",fg="purple")
                self.entry6.grid(row=18,column=1)
                ##connection made
            
            def data(self):
        
                self.conn=connect("example.db")
                self.cur=self.conn.cursor()
                self.cur.execute("create table if not exists monu(id integer primary key,fn text,city text)")
                self.cur.execute("create table if not exists ritu(cust_id integer,balance real,amt_withdraw real,foreign key(cust_id) references monu(id))")
                self.cur.execute("alter table ritu add column date6 text")
                


            ##show record
            def show(self):
                
               
                #try:
                self.cur=self.conn.cursor()
                content=self.entry4.get()
                for item in self.cur.execute("select cust_id,fn,city,balance,amt_withdraw,sum(balance),sum(amt_withdraw),date6 from ritu,monu where ritu.cust_id==monu.id  and cust_id is %s" %(content)):
                    self.text=Text(self,width=50,height=30,font="Times 10 bold",fg="purple")
                    self.text.grid(row=7,column=4,columnspan=7,rowspan=15)
                    self.text.insert(0.0,item)
             ##close connection   
            def close(self):
                self.conn.close()
                sonu.destroy()
                    
            def clk(self,sonu):
                sonu.widget.config(relief="raised")
            def pr(self,sonu):
                sonu.widget.config(relief=GROOVE)
            
        #monu.destroy()
            
        sonu=Tk()
        
        monu=katrina(sonu)
        sonu.geometry("1350x760")
        sonu.mainloop()
        
        
    
monu=Tk()
monu.geometry("1350x760")

raj=ritu(monu)
monu.mainloop()
