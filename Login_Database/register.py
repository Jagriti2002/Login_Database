from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql

class Register:
     def __init__(self,root):
          self.root=root
          self.root.title("Registration Window")
          self.root.geometry("1350x700+0+0")
          self.root.config(bg="sky blue")
          self.root.resizable(False,False)

          self.bg=ImageTk.PhotoImage(file="images/b2.jpg")
          bg=Label(self.root,image=self.bg,bg="sky blue").place(x=250,y=0,relwidth=1,relheight=1)

          self.left=ImageTk.PhotoImage(file="images/side.jpg")
          left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

          frame1=Frame(self.root,bg="white")
          frame1.place(x=480,y=100,width=700,height=500)

          title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)


         
          f_name=Label(frame1,text="FIRST NAME",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=100)
          self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgrey")
          self.txt_fname.place(x=50,y=130,width=250)

          l_name=Label(frame1,text="LAST NAME",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=100)
          self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgrey")
          self.txt_lname.place(x=370,y=130,width=250)

          contact=Label(frame1,text="FIRST CONTACT NO.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=170)
          self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgrey")
          self.txt_contact.place(x=50,y=200,width=250)

          email=Label(frame1,text="EMAIL ADDRESS",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=170)
          self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgrey")
          self.txt_email.place(x=370,y=200,width=250)

          question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=240)

          self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
          self.cmb_quest['values']=("Select","Your Pet Name","Your Birth Place","Your Best Friend Name")
          self.cmb_quest.place(x=50,y=270,width=250)
          self.cmb_quest.current(0)

          answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=240)
          self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgrey")
          self.txt_answer.place(x=370,y=270,width=250)

          password=Label(frame1,text="PASSWORD",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=310)
          self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgrey")
          self.txt_password.place(x=50,y=340,width=250)

          cpassword=Label(frame1,text="CONFIRMED PASSWORD",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=310)
          self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgrey")
          self.txt_cpassword.place(x=370,y=340,width=250)

          self.var_chk=IntVar()
          chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12),cursor="hand2").place(x=50,y=380)
          
          btn_register=Button(frame1,text="< Register Now >",font=("times new roman",15,"bold"),bg="green",fg="white",cursor="hand2",command=self.register_data).place(x=250,y=420)
          btn_login=Button(self.root,text="Sign In",command=self.Login_window,font=("times new roman",20,"bold"),bg="Sky Blue",cursor="hand2").place(x=200,y=460,width=180)
     
     def Login_window(self):
          self.root.destroy()
          import Login 

     def clear(self):
          self.txt_fname.delete(0,END)
          self.txt_lname.delete(0,END)
          self.txt_contact.delete(0,END)
          self.txt_email.delete(0,END)
          self.cmb_quest.delete(0,END)
          self.txt_answer.delete(0,END)
          self.txt_password.delete(0,END)
          self.txt_cpassword.delete(0,END)
          self.cmb_quest.current(0)

     def register_data(self):
          if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.txt_contact.get()=="" or self.cmb_quest.get()=="select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
               messagebox.showerror("Error","All Fields Are Required",parent=self.root)
          elif self.txt_password.get()!=self.txt_cpassword.get():
               messagebox.showerror("Error","Password And Confirmed Did'nt Matched",parent=self.root)  
          elif self.var_chk.get()==0:
               messagebox.showerror("Error","Please Agree Our Terms & Conditions",parent=self.root)  
          else:
               try:
                    con=pymysql.connect(host="localhost",user="root",password="",database="quiz")
                    cur=con.cursor()
                    cur.execute("select * from login where email=%s",self.txt_email.get())
                    row=cur.fetchone()
                    #print(row)
                    if row!=None:
                         messagebox.showerror("Error","User already exists ,please try with another email",parent=self.root)
                    else:                           
                         cur.execute("insert into login (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                        (self.txt_fname.get(),
                                        self.txt_lname.get(),
                                        self.txt_contact.get(),
                                        self.txt_email.get(),
                                        self.cmb_quest.get(),
                                        self.txt_answer.get(),
                                        self.txt_password.get()
                                        ))
                         con.commit()
                         con.close()
                         messagebox.showinfo("Success","Register Successfull!!!!!!!",parent=self.root) 
                         self.clear() 
               except Exception as es:
                    messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)      
               




root=Tk()
obj=Register(root)
root.mainloop()