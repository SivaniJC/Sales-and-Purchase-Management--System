from tkinter import *

import tkinter.messagebox
import sqlite3

#FrontEnd

class Product:
    def __init__(self,root):

        p =  Database()
        p.conn()

        self.root = root
        self.root.title("Warehouse Invertory sales puchase management system")
        self.root.geometry("1325x690")
        self.root.config(bg="orange")

        pId=StringVar()
        pName=StringVar()
        pPrice=StringVar()
        pQty=StringVar()
        pCompany=StringVar()
        pContact=StringVar()

        def close():
            print("Product: close method called ")
            close = tkinter.messagebox.askyesno("WAREHOUSE INVENTORY SALES PUCHASE MANAGEMENT SYSTEM","Really.... Do you want to close the system")
            if close > 0:
                root.destroy()
                print("Product: close method finished\n")
                return

        def clear():
            print("Product: clear method called")
            self.entrypId.delete(0,END)
            self.entrypName.delete(0,END)
            self.entrypPrice.delete(0,END)
            self.entrypQty.delete(0,END)
            self.entrypCompany.delete(0,END)
            self.entrypContact.delete(0,END)
            print("Product: clear method finished")

        def insert():
            print("Product: insert method called")
            if (len(pId.get())!=0):
                p.insert(pId.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get())
                productList.delete(0,END)
                productList.insert(END,pId.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get())
                showList()
            else:
                tkinter.messagebox.askyesno("WAREHOUSE INVENTORY SALES PUCHASE MANAGEMENT SYSTEM","atleast.... Enter Product ID")

            print("Product: insert method finished")

        def showList():
            print("Product: Show method called")
            productList.delete(0,END)
            for row in p.show():
                productList.insert(END,row,str(""))
            print("Product : Show method finished")

        def productRec(event):
            print("Product: productRec method called")
            global pd

            searchPd = productList.curselection()[0]
            pd = productList.get(searchPd)

            self.entrypId.delete(0,END)
            self.entrypId.insert(END,pd[0])

            self.entrypName.delete(0,END)
            self.entrypName.insert(END,pd[1])

            self.entrypPrice.delete(0,END)
            self.entrypPrice.insert(END,pd[2])

            self.entrypQty.delete(0,END)
            self.entrypQty.insert(END,pd[3])

            self.entrypCompany.delete(0,END)
            self.entrypCompany.insert(END,pd[4])

            self.entrypContact.delete(0,END)
            self.entrypContact.insert(END,pd[5])

            print("Product: productRec method finished\n")

        def delete():
            print("Product: Delete method called")
            if(len(pId.get())!=0):
                p.delete(pd[0])
                clear()
                showList()
                print("Product: Delete method finished\n")


        def search():
            print("Product: Search method called")
            productList.delete(0,END)
            for row in p.search(pId.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get()):
                productList.insert(END,row,str(""))

            print("Product: Search method finished\n")

        def update():
            print("Product: Update method called")
            if(len(pId.get())!=0):
                print("pd[0]",pd[p])
                p.delete(pd[0])
            if(len(pId.get())!=0):
                p.insert(pId.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get())
                productList.delete(0,END)
                
            productList.insert(END,(pId.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get()))
            print("Product: Update method finished\n")


        MainFrame = Frame(self.root,bg="red")
        MainFrame.grid()

        HeadFrame = Frame(MainFrame, bd=1, padx=50, pady=10, bg='white', relief=RAISED)
        HeadFrame.pack(side=TOP)

        self.ITitle= Label(HeadFrame, font=('arial',50,'bold'), fg='red',text ='Warehouse Inventory sales purchase ',bg='white')
        self.ITitle.grid()

        OperationFrame = Frame(MainFrame, bd=2, width=1325, height=60, padx=50,pady=20,bg='white',relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)

        BodyFrame = Frame(MainFrame, bd=2, width=1300, height=500, padx=30,pady=20,bg='white',relief=SUNKEN)
        BodyFrame.pack(side=BOTTOM)

        LeftBodyFrame = LabelFrame(BodyFrame,bd=2, width=600, height=400, padx=20,pady=10,bg='yellow',relief=RAISED, font=('arial',15,'bold'),text='Product Item Details:')
        LeftBodyFrame.pack(side=LEFT)

        RightBodyFrame = LabelFrame(BodyFrame,bd=2, width=500, height=400, padx=20,pady=10,bg='yellow',relief=RAISED, font=('arial',15,'bold'),text='Product Item Information:')
        RightBodyFrame.pack(side=RIGHT)


        self.labelpId=Label(LeftBodyFrame, font=('arial',15,'bold'),text="Product Id", padx=2, pady=2,bg='white', fg='Blue')
        self.labelpId.grid(row=0,column=0,sticky=W)

        self.entrypId = Entry(LeftBodyFrame, font=('arial',20,'bold'),textvariable=pId, width=35)
        self.entrypId.grid(row=0,column=1,sticky=W)

        self.labelpName=Label(LeftBodyFrame, font=('arial',15,'bold'),text="Product Name", padx=2, pady=2, bg='white', fg='Blue')
        self.labelpName.grid(row=1,column=0,sticky=W)

        self.entrypName = Entry(LeftBodyFrame, font=('arial',20,'bold'),textvariable=pName, width=35)
        self.entrypName.grid(row=1,column=1,sticky=W)

        self.labelpPrice=Label(LeftBodyFrame, font=('arial',15,'bold'),text="Product Price", padx=2, pady=2, bg='white', fg='Blue')
        self.labelpPrice.grid(row=2,column=0,sticky=W)

        self.entrypPrice = Entry(LeftBodyFrame, font=('arial',20,'bold'),textvariable=pPrice, width=35)
        self.entrypPrice.grid(row=2,column=1,sticky=W)

        self.labelpQty=Label(LeftBodyFrame, font=('arial',15,'bold'),text="Product Quantity", padx=2, pady=2,bg='white', fg='Blue')
        self.labelpQty.grid(row=3,column=0,sticky=W)

        self.entrypQty = Entry(LeftBodyFrame, font=('arial',20,'bold'),textvariable=pQty, width=35)
        self.entrypQty.grid(row=3,column=1,sticky=W)

        self.labelpCompany=Label(LeftBodyFrame, font=('arial',15,'bold'),text="Mfg. Company", padx=2, pady=2,bg='white', fg='Blue')
        self.labelpCompany.grid(row=4,column=0,sticky=W)

        self.entrypCompany = Entry(LeftBodyFrame, font=('arial',20,'bold'),textvariable=pCompany, width=35)
        self.entrypCompany.grid(row=4,column=1,sticky=W)

        self.labelpContact=Label(LeftBodyFrame, font=('arial',15,'bold'),text="Company Contact", padx=2, pady=2,bg='white', fg='Blue')
        self.labelpContact.grid(row=5,column=0,sticky=W)

        self.entrypContact = Entry(LeftBodyFrame, font=('arial',20,'bold'),textvariable=pContact, width=35)
        self.entrypContact.grid(row=5,column=1,sticky=W)

        self.labelpC1=Label(LeftBodyFrame, padx=2,pady=2)
        self.labelpC1.grid(row=6,column=0,sticky=W)
        self.labelpC2=Label(LeftBodyFrame, padx=2,pady=2)
        self.labelpC2.grid(row=7,column=0,sticky=W)
        self.labelpC3=Label(LeftBodyFrame, padx=2,pady=2)
        self.labelpC3.grid(row=8,column=0,sticky=W)
        self.labelpC4=Label(LeftBodyFrame, padx=2,pady=2)
        self.labelpC4.grid(row=9,column=0,sticky=W)
        self.labelpC5=Label(LeftBodyFrame, padx=2,pady=2)
        self.labelpC5.grid(row=10,column=0,sticky=W)

        scroll =Scrollbar(RightBodyFrame)
        scroll.grid(row=0, column=1, sticky='ns')
        productList=Listbox(RightBodyFrame, width=40, height=16, font=('arial',12,'bold'), yscrollcommand=scroll.set)

        productList.bind('<<ListboxSelect>>',productRec)

        productList.grid(row=0, column=0, padx=8)
        scroll.config(command=productList.yview)

        self.buttonSave = Button(OperationFrame, text='Save', font=('arial',15,'bold'),bg='green',fg='white',height=1,width=10,bd=4,command=insert)
        self.buttonSave.grid(row=0,column=0)

        self.buttonShow = Button(OperationFrame, text='Show', font=('arial',15,'bold'),bg='green',fg='white',height=1,width=10,bd=4,command=showList)
        self.buttonShow.grid(row=0,column=1)

        self.buttonReset = Button(OperationFrame, text='Reset', font=('arial',15,'bold'),bg='green',fg='white',height=1,width=10,bd=4,command=clear)
        self.buttonReset.grid(row=0,column=2)

        self.buttonDelete = Button(OperationFrame, text='Delete', font=('arial',15,'bold'),bg='green',fg='white',height=1,width=10,bd=4,command=delete)
        self.buttonDelete.grid(row=0,column=3)

        self.buttonSearch = Button(OperationFrame, text='Search', font=('arial',15,'bold'),bg='green',fg='white',height=1,width=10,bd=4,command=search)
        self.buttonSearch.grid(row=0,column=4)

        self.buttonUpdate = Button(OperationFrame, text='Update', font=('arial',15,'bold'),bg='green',fg='white',height=1,width=10,bd=4,command=update)
        self.buttonUpdate.grid(row=0,column=5)

        self.buttonClose = Button(OperationFrame, text='Close', font=('arial',15,'bold'),bg='green',fg='white',height=1,width=10,bd=4,command=close)
        self.buttonClose.grid(row=0,column=6)


#BackEnd Database Operations

class Database:

    def conn(self):
        print("Database: connection method called")
        con = sqlite3.connect("inventory.db")
        cur=con.cursor()
        query = "create table if not exists product(pid integer primary key , pname text, price text,qty text,company text,contact text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database: connection methods finished\n")

    def insert(self,pid,name,price,qty,company,contact):
        print("Database: insert method called\n")
        con = sqlite3.connect("inventory.db")
        cur=con.cursor()
        query="insert into product values(?,?,?,?,?,?)"
        cur.execute(query,(pid,name,price,qty,company,contact))
        con.commit()
        con.close()
        print("Database: insert method finished\n")

    def show(self):
        print("Database: show method called\n")
        con = sqlite3.connect("inventory.db")
        cur=con.cursor()
        query="select * from product"
        cur.execute(query)
        rows=cur.fetchall()
        con.close()
        print("Database: show method finished\n")
        return rows

    def delete(self,pid):
        print("Database: delete method called",pid)
        con = sqlite3.connect("inventory.db")
        cur=con.cursor()
        cur.execute("delete from product where pid=?",(pid,))
        con.commit()
        con.close()
        print(pid,"Database: delete method finished\n")

    def search(self,pid="",pname="",price="",qty="",company="",contact=""):
        print("Database: search method called")
        con = sqlite3.connect("inventory.db")
        cur=con.cursor()
        cur.execute("select * from product where pid=? or pname=? or price=? or qty=? or company=? or contact=?",(pid,pname,price,qty,company,contact))
        row=cur.fetchall()
        con.close()
        print("Database : search method finished\n")
        return row

    def update(self,pid="",pname="",price="",qty="",company="",contact=""):
        print("Database: update method called")
        con = sqlite3.connect("inventory.db")
        cur=con.cursor()
        cur.execute("update product set pid=? or pname=? or price=? or qty=? or company=? or contact=? where pid=?",(pid,name,price,qty,company,contact,pid))
        con.commit()
        con.close()
        print(pid,"Database: Update method finished\n")



if __name__ == '__main__':
    root =Tk()
    application = Product(root)
    root.mainloop()
