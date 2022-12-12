# استدعى مكتبة التيكنتر ومن ثم استدعى منها نجمة وتعنى كل شئ فى المكتبة
from tkinter import *
# استدعى من التيكنتر مكتبة جاهزة عن اظهار الرسائل المنبثقة
from tkinter import messagebox
from tkinter import font
import webbrowser  # مكتبة مسؤلة عن التعامل مع المتصفح
import os  # مكتبة للتعامل مع مسارات النظام
import sys  # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# يستدعي كل شي في مكتبه tkinter
import math
import random
import os
import sys
import webbrowser  # وطباعه الفةاتير و المعادلات و المسارات
from tkinter import messagebox
from tkinter import font
from tkinter.font import BOLD
# -------------------------------------------------------------------------------
global pro
pro = Tk()  # pro متغير يمكن تسميتة اى اسم #Tk كلاس جاهز مسؤل عن النافذة الصغيرة
pro.geometry('800x450+250+50')  # الدالة المسؤلة عن عرض وارتفاع النافذة
# false لاظهارة  المسؤل عن ظهور زر تكبير وتصغير الشاشة لاخفائة true
pro.resizable(False, False)
pro.title('contoso market')  # لاضافة اسم
# pro.iconbitmap('C:\\Users\\Magic\\Desktop\\png.ico')  # لاضافة ايقونة للبرنامج
title = Label(pro, text='contoso market', fg='black',
              bg='#89cff0', font=('tajwal', 16, 'bold'))
title.pack(fill=X)  # من اجل اظهار السطر اللى قبلة
# --------------------------------------------------------------------------------
u1 = 'https://www.facebook.com'
u2 = 'https://t.me/+JPjCOulEGhczMzg8'

u4 = 'https://www.google.com/?hl=ar'
u5 = 'https://www.youtube.com/'


def open1():
    webbrowser.open_new(u1)


def open2():
    webbrowser.open_new(u2)


def open4():
    webbrowser.open_new(u4)


def open5():
    webbrowser.open_new(u5)


def number():
    messagebox.showinfo("phone number", "01271597951")

# ----------------------------------------------------


class super:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x750')
        self.root.title('Contoso market')
        # متغيرات الحساب الكلى
        self.elmoadelgesaia = StringVar()
        self.housewar = StringVar()
        self.electricaltools = StringVar()
        # variables=====
        self.name = StringVar()
        self.phone = StringVar()
        self.fatora = StringVar()
        x = random.randint(1, 1000)
        self.fatora.set(str(x))
        # المواد الغذائية
        self.q1 = IntVar()
        self.q2 = IntVar()
        self.q3 = IntVar()
        self.q4 = IntVar()
        self.q5 = IntVar()
        self.q6 = IntVar()
        self.q7 = IntVar()
        self.q8 = IntVar()
        self.q9 = IntVar()
        self.q10 = IntVar()
        # adwat
        self.qq1 = IntVar()
        self.qq2 = IntVar()
        self.qq3 = IntVar()
        self.qq4 = IntVar()
        self.qq5 = IntVar()
        self.qq6 = IntVar()
        self.qq7 = IntVar()
        self.qq8 = IntVar()
        self.qq9 = IntVar()
        self.qq10 = IntVar()
        # kahraba
        self.qqq1 = IntVar()
        self.qqq2 = IntVar()
        self.qqq3 = IntVar()
        self.qqq4 = IntVar()
        self.qqq5 = IntVar()
        self.qqq6 = IntVar()
        self.qqq7 = IntVar()
        self.qqq8 = IntVar()
        self.qqq9 = IntVar()
        self.qqq10 = IntVar()

# -------------------------------------------------------------------------
# buyer's dateجزء ال
# ------------------------------------------------------------------------
        f1 = Frame(root, bd=2, width=330, height=300, bg='#4A708B')
        f1.place(x=1000, y=24)
        tit = Label(f1, text="buyer's date :",
                    font=30, bg='#4A708B', fg='white')
        tit.place(x=20, y=0)
        hisname = Label(f1, text='customer name :',
                        font=20, bg='#4A708B', fg='white')
        hisname.place(x=20, y=35)

        hisname2 = Label(f1, text='customer number :',
                         font=20, bg='#4A708B', fg='white')
        hisname2.place(x=1, y=65)

        hisname3 = Label(f1, text='invoice number :',
                         font=20, bg='#4A708B', fg='white')
        hisname3.place(x=21, y=95)

        entname = Entry(f1, textvariable=self.name, justify='center')
        entname.place(x=158, y=38)

        entname2 = Entry(f1, textvariable=self.phone, justify='center')
        entname2.place(x=158, y=68)

        entname3 = Entry(f1, textvariable=self.fatora,
                         justify='center')
        entname3.place(x=158, y=98)

       # custmor = Button(f1, font=20,  width=28, height=1,
        #                 text='search', fg='black')
        #custmor.place(x=25, y=150)

# ----------------------------------------------------------------
# جزء الفاتوره
# ---------------------------------------------------------------
        y = Label(f1, text='(invoice)', font=(
            "tajawal", 30, 'bold'), bg='#4A708B', fg='gold')
        y.place(x=70, y=200)

        invoice = Frame(root, bd=2, width=330,
                        height=400, bg='#4A708B')
        invoice.place(x=1000, y=310)

        scrol_y = Scrollbar(invoice, orient=VERTICAL)
        self.textarea = Text(invoice, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=LEFT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

# -----------------------------------------------------------------
# السعر ة العمليات الحسابيه
# -----------------------------------------------------------------
        f4 = Frame(root, bd=2, width=1000, height=210, bg='#4A708B')
        f4.place(x=0, y=610)
        o = Button(f4, text="calculate", font=20, bg='#4A708B',
                   fg='white', width=8, height=1, command=self.total)
        o.place(x=900, y=5)
        p = Button(f4, text="print", font=20, bg='#4A708B',
                   fg='white', width=8, height=1, command=self.billing)
        p.place(x=900, y=45)

        s = Button(f4, text="clear", font=20, bg='#4A708B',
                   fg='white', width=8, height=1, command=self.clear)
        s.place(x=810, y=5)

        q = Button(f4, text="exit", font=20, bg='#4A708B',
                   fg='white', width=8, height=1, command=quit)
        q.place(x=810, y=45)

        h1 = Label(f4, text=":حساب المواد الغذائية",
                   font=10, bg='#4A708B', fg='white')
        h1.place(x=650, y=5)

        h2 = Label(f4, text=":حساب الادوات المنزليه",
                   font=10, bg='#4A708B', fg='white')
        h2.place(x=615, y=30)

        h3 = Label(f4, text=":حساب الادوات الكهربيه",
                   font=10, bg='#4A708B', fg='white')
        h3.place(x=612, y=55)

        h11 = Entry(f4, textvariable=self.elmoadelgesaia, width=30)
        h11.place(x=370, y=8)

        h22 = Entry(f4, textvariable=self.housewar, width=30)
        h22.place(x=370, y=33)

        h33 = Entry(f4, textvariable=self.electricaltools, width=30)
        h33.place(x=370, y=58)

        w = Label(f4, text='oop project', bg='#4A708B',
                  fg='gold', font=('tajawal', 30))
        w.place(x=20, y=20)

# ---------------------------------------------------------------
# قسم البقوليات
# ---------------------------------------------------------------
        g1 = Frame(root, bd=2, width=333, height=581, bg='#6CA6CD')
        g1.place(x=1, y=26)

        t1 = Label(g1, text='مواد غذائية', bg='#4A708B',
                   fg='gold', font=('tajawal', 20))
        t1.place(x=120, y=2)

        a1 = Label(g1, text='الرز', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a1.place(x=290, y=50)

        a2 = Label(g1, text='مكرونه', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a2.place(x=270, y=100)

        a3 = Label(g1, text='فاصوليا', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a3.place(x=267, y=150)

        a4 = Label(g1, text='عدس', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a4.place(x=285, y=200)

        a5 = Label(g1, text='حمص', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a5.place(x=275, y=250)

        a6 = Label(g1, text='فول', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a6.place(x=290, y=300)

        a7 = Label(g1, text='ملح', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a7.place(x=290, y=350)

        a8 = Label(g1, text='سكر', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a8.place(x=285, y=400)

        a9 = Label(g1, text='فلفل', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a9.place(x=290, y=450)

        a10 = Label(g1, text='بسله', bg='#6CA6CD',
                    fg='white', font=('tajawal', 15))
        a10.place(x=285, y=502)

        c1 = Entry(g1, textvariable=self.q1, width=24)
        c1.place(x=100, y=55)

        c2 = Entry(g1, textvariable=self.q2, width=24)
        c2.place(x=100, y=105)

        c3 = Entry(g1, textvariable=self.q3, width=24)
        c3.place(x=100, y=155)

        c4 = Entry(g1, textvariable=self.q4, width=24)
        c4.place(x=100, y=205)

        c5 = Entry(g1, textvariable=self.q5, width=24)
        c5.place(x=100, y=255)

        c6 = Entry(g1, textvariable=self.q6, width=24)
        c6.place(x=100, y=305)

        c7 = Entry(g1, textvariable=self.q7, width=24)
        c7.place(x=100, y=355)

        c8 = Entry(g1, textvariable=self.q8, width=24)
        c8.place(x=100, y=405)

        c9 = Entry(g1, textvariable=self.q9, width=24)
        c9.place(x=100, y=455)

        c10 = Entry(g1, textvariable=self.q10, width=24)
        c10.place(x=100, y=505)


# ---------------------------------------------------------------
# قسم ادوات منزليه
# ---------------------------------------------------------------
        g2 = Frame(root, bd=2, width=333, height=581, bg='#6CA6CD')
        g2.place(x=335, y=26)

        t2 = Label(g2, text='ادوات منزليه', bg='#4A708B',
                   fg='gold', font=('tajawal', 20))
        t2.place(x=120, y=2)

        s1 = Label(g2, text='طبق', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        s1.place(x=290, y=50)

        s2 = Label(g2, text='كوبايه', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        s2.place(x=280, y=100)

        s3 = Label(g2, text='سكينه', bg='#6CA6CD',
                   fg='white', font=('0ajawal', 15))
        s3.place(x=280, y=150)

        s4 = Label(g2, text='شوكه', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        s4.place(x=285, y=200)

        s5 = Label(g2, text='خلاط', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        s5.place(x=280, y=250)

        s6 = Label(g2, text='معالق', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        s6.place(x=280, y=300)

        s7 = Label(g2, text='صحون', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        s7.place(x=275, y=350)

        s8 = Label(g2, text='شفشق', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        s8.place(x=280, y=400)

        s9 = Label(g2, text='برطمان', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        s9.place(x=270, y=450)

        s10 = Label(g2, text='سله', bg='#6CA6CD',
                    fg='white', font=('tajawal', 15))
        s10.place(x=285, y=502)

        c11 = Entry(g2, textvariable=self.qq1, width=24)
        c11.place(x=100, y=55)

        c12 = Entry(g2, textvariable=self.qq2, width=24)
        c12.place(x=100, y=105)

        c13 = Entry(g2, textvariable=self.qq3, width=24)
        c13.place(x=100, y=155)

        c14 = Entry(g2, textvariable=self.qq4, width=24)
        c14.place(x=100, y=205)

        c15 = Entry(g2, textvariable=self.qq5, width=24)
        c15.place(x=100, y=255)

        c16 = Entry(g2, textvariable=self.qq6, width=24)
        c16.place(x=100, y=305)

        c17 = Entry(g2, textvariable=self.qq7, width=24)
        c17.place(x=100, y=355)

        c18 = Entry(g2, textvariable=self.qq8, width=24)
        c18.place(x=100, y=405)

        c19 = Entry(g2, textvariable=self.qq9, width=24)
        c19.place(x=100, y=455)

        c20 = Entry(g2, textvariable=self.qq10, width=24)
        c20.place(x=100, y=505)


# ---------------------------------------------------------------
# قسم البقوليات
# ---------------------------------------------------------------
        g3 = Frame(root, bd=2, width=330, height=581, bg='#6CA6CD')
        g3.place(x=670, y=26)

        t3 = Label(g3, text='ادوات كهربيه', bg='#4A708B',
                   fg='gold', font=('tajawal', 20))
        t3.place(x=120, y=2)

        a1 = Label(g3, text='تليفزيون', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a1.place(x=260, y=50)

        a2 = Label(g3, text='غساله', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a2.place(x=270, y=100)

        a3 = Label(g3, text='تكييف', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a3.place(x=270, y=150)

        a4 = Label(g3, text='بوتجاز', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a4.place(x=260, y=200)

        a5 = Label(g3, text='مروحه', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a5.place(x=260, y=250)

        a6 = Label(g3, text='لابتوب', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a6.place(x=270, y=300)

        a7 = Label(g3, text='مكوي', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a7.place(x=270, y=350)

        a8 = Label(g3, text='مكرويف', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a8.place(x=260, y=400)

        a9 = Label(g3, text='كاتل', bg='#6CA6CD',
                   fg='white', font=('tajawal', 15))
        a9.place(x=270, y=450)

        a10 = Label(g3, text='موبايل', bg='#6CA6CD',
                    fg='white', font=('tajawal', 15))
        a10.place(x=260, y=502)

        c21 = Entry(g3, textvariable=self.qqq1, width=24)
        c21.place(x=100, y=55)

        c22 = Entry(g3, textvariable=self.qqq2, width=24)
        c22.place(x=100, y=105)

        c23 = Entry(g3, textvariable=self.qqq3, width=24)
        c23.place(x=100, y=155)

        c24 = Entry(g3, textvariable=self.qqq4, width=24)
        c24.place(x=100, y=205)

        c25 = Entry(g3, textvariable=self.qqq5, width=24)
        c25.place(x=100, y=255)

        c26 = Entry(g3, textvariable=self.qqq6, width=24)
        c26.place(x=100, y=305)

        c27 = Entry(g3, textvariable=self.qqq7, width=24)
        c27.place(x=100, y=355)

        c28 = Entry(g3, textvariable=self.qqq8, width=24)
        c28.place(x=100, y=405)

        c29 = Entry(g3, textvariable=self.qqq9, width=24)
        c29.place(x=100, y=455)

        c30 = Entry(g3, textvariable=self.qqq10, width=24)
        c30.place(x=100, y=505)

    def total(self):
        self.rez = self.q1.get()*1.5
        self.borgel = self.q2.get()*2
        self.fasoli = self.q3.get()*1
        self.ades = self.q4.get()*1.5
        self.makrona = self.q5.get()*2
        self.frika = self.q6.get()*2
        self.homes = self.q7.get()*1
        self.fol = self.q8.get()*1
        self.mlah = self.q9.get()*1.5
        self.skar = self.q10.get()*1

        self.totalito = float(
            self.rez +
            self.borgel +
            self.fasoli +
            self.ades +
            self.makrona +
            self.frika +
            self.homes +
            self.fol +
            self.mlah +
            self.skar
        )

        self.elmoadelgesaia.set(str(self.totalito)+" ج")
        self.rez2 = self.qqq1.get()*30
        self.borgel2 = self.qqq2.get()*140
        self.fasoli2 = self.qqq3.get()*300
        self.ades2 = self.qqq4.get()*40
        self.makrona2 = self.qqq5.get()*15
        self.frika2 = self.qqq6.get()*110
        self.homes2 = self.qqq7.get()*20
        self.fol2 = self.qqq8.get()*10
        self.mlah2 = self.qqq9.get()*15
        self.skar2 = self.qqq10.get()*140

        self.khrba = float(
            self.rez2 +
            self.borgel2 +
            self.fasoli2 +
            self.ades2 +
            self.makrona2 +
            self.frika2 +
            self.homes2 +
            self.fol2 +
            self.mlah2 +
            self.skar2

        )
        self.electricaltools.set(str(self.khrba)+" ج")
        self.rez1 = self.qq1.get()*1.5
        self.borgel1 = self.qq2.get()*0.5
        self.fasoli1 = self.qq3.get()*1
        self.ades1 = self.qq4.get()*1.5
        self.makrona1 = self.qq5.get()*2
        self.frika1 = self.qq6.get()*2
        self.homes1 = self.qq7.get()*1
        self.fol1 = self.qq8.get()*1
        self.mlah1 = self.qq9.get()*1.5
        self.skar1 = self.qq10.get()*1

        self.adoatdd = float(
            self.rez1 +
            self.borgel1 +
            self.fasoli1 +
            self.ades1 +
            self.makrona1 +
            self.frika1 +
            self.homes1 +
            self.fol1 +
            self.mlah1 +
            self.skar1

        )
        self.housewar.set(str(self.adoatdd)+" ج")
        self.all = float(self.totalito +
                         self.khrba +
                         self.adoatdd
                         )

        self.welcome()

    def welcome(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\t contoso market welcomes you. ")
        self.textarea.insert(
            END, "\n  ====================================")
        self.textarea.insert(END, f"\n\t B.NUM  : {self.fatora.get()}")
        self.textarea.insert(END, f"\n\t Name   : {self.name.get()}")
        self.textarea.insert(END, f"\n\t Phone  : {self.phone.get()}")
        self.textarea.insert(
            END, "\n======================================")
        self.textarea.insert(
            END, f"\nالسعر\t      العدد\t   المشتريات ")
        self.textarea.insert(
            END, "\n======================================")

    def billing(self):
        if self.name.get() == "" or self.phone.get() == "":
            messagebox.showerror(
                "حدث خطأ", "لا يجوز ترك حقل الاسم ورقم الهاتف فارغا")
        elif self.elmoadelgesaia.get() == "0.0 ج" and self.housewar.get() == "0.0 ج" and self.electricaltools.get() == "0.0 ج":
            messagebox.showerror(
                "حدث خطأ", " ليس هناك منتجات محددة ولم يتم اختيار احداها يجب اختيار عدد المنتجات")
        else:
            self.welcome()
            if self.q1.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.rez}\t\t{self.q1.get()}\tالرز ")
            if self.q2.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.borgel}\t\t{self.q2.get()}\tمكرنه")
            if self.q3.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.fasoli}\t\t{self.q3.get()}\tفاصولياء ")
            if self.q4.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.ades}\t\t{self.q4.get()}\tعدس ")
            if self.q5.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.makrona}\t\t{self.q5.get()}\t حمص ")
            if self.q6.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.frika}\t\t{self.q6.get()}\tفول ")
            if self.q7.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.homes}\t\t{self.q7.get()}\t ملح ")
            if self.q8.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.fol}\t\t{self.q8.get()}\t سكر ")
            if self.q9.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.mlah}\t\t{self.q9.get()}\tفلفل ")
            if self.q10.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.skar}\t\t{self.q10.get()}\t بسله ")

            if self.qq1.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.rez1}\t\t{self.qq1.get()}\t طبق")
            if self.qq2.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.borgel1}\t\t{self.qq2.get()}\t كوبايه")
            if self.qq3.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.fasoli1}\t\t{self.qq3.get()}\tسكينه ")
            if self.qq4.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.ades1}\t\t{self.qq4.get()}\t شوكه")
            if self.qq5.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.makrona1}\t\t{self.qq5.get()}\t خلاط")
            if self.qq6.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.frika1}\t\t{self.qq6.get()}\t معالق")
            if self.qq7.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.homes1}\t\t{self.qq7.get()}\t صحون")
            if self.qq8.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.fol1}\t\t{self.qq8.get()}\t شفشق")
            if self.qq9.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.mlah1}\t\t{self.qq9.get()}\t برطمان")
            if self.qq10.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.skar1}\t\t{self.qq10.get()}\tسله")

            if self.qqq1.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.rez1}\t\t{self.qqq1.get()}\t تليفزيون")
            if self.qqq2.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.borgel2}\t\t{self.qqq2.get()}\t غساله")
            if self.qqq3.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.fasoli2}\t\t{self.qqq3.get()}\t تكييف")
            if self.qqq4.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.ades2}\t\t{self.qqq4.get()}\t بوتاجاز")
            if self.qqq5.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.makrona2}\t\t{self.qqq5.get()}\t مروحه ")
            if self.qqq6.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.frika2}\t\t{self.qqq6.get()}\t  لابتوب")
            if self.qqq7.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.homes2}\t\t{self.qqq7.get()}\t مكوي")
            if self.qqq8.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.fol2}\t\t{self.qqq8.get()}\t  ميكرويف")
            if self.qqq9.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.mlah2}\t\t{self.qqq9.get()}\t  كاتل")
            if self.qqq10.get() != 0:
                self.textarea.insert(
                    END, f"\n {self.skar2}\t\t{self.qqq10.get()}\t   م وبايل")

            self.textarea.insert(
                END, "\n......................................")
            self.textarea.insert(
                END, f"\n\t{self.all} ج\t     المجموع الكلي")
            self.textarea.insert(
                END, "\n......................................")

    def clear(self):
        self.q1.set(0)
        self.q2.set(0)
        self.q3.set(0)
        self.q4.set(0)
        self.q5.set(0)
        self.q6.set(0)
        self.q7.set(0)
        self.q8.set(0)
        self.q9.set(0)
        self.q10.set(0)

        self.qq1.set(0)
        self.qq2.set(0)
        self.qq3.set(0)
        self.qq4.set(0)
        self.qq5.set(0)
        self.qq6.set(0)
        self.qq7.set(0)
        self.qq8.set(0)
        self.qq9.set(0)
        self.qq10.set(0)

        self.qqq1.set(0)
        self.qqq2.set(0)
        self.qqq3.set(0)
        self.qqq4.set(0)
        self.qqq5.set(0)

        self.qqq6.set(0)
        self.qqq7.set(0)
        self.qqq8.set(0)
        self.qqq9.set(0)
        self.qqq10.set(0)

        self.elmoadelgesaia.set(0)
        self.housewar.set(0)
        self.electricaltools.set(0)
        self.name.set('')
        self.phone.set('')
        self.fatora.set('')


def log():
    user = EN1.get()
    password = EN2.get()
    if user == 'oop project' and password == '123456':
       # مكتبه جاهزه لاظهار الرسايل

        # from typing_extensions import Self
        pro.destroy()

        root = Tk()
        ob = super(root)
        root.resizable(False, False)
     # root.iconbitmap('C:\\Users\\TAS\\Desktop\\super-market.ico')
        Title = Label(root, text='super market ststem ',
                      fg='white', bg='#4A708B', font=20)
        Title.pack(fill=X)
        # root.mainloop()
    else:
        messagebox.showinfo(
            "error", "please enter correct username and password")

# ------------------------------------------------------------------------------------


# f1=Frame(master,Options)#frame مسؤل تقسيم الشاشة#master مكان ظهور # option الخصائص
f1 = Frame(pro, width=230, height=420, bg='#89cff0')
f1.place(x=570, y=30)  # المكان اللى هيكون فية الفريم المتحدد
# title1 =Label(master) #عنوان للجزء اللى متحدد فوق
# ---------------------------------------------------------------------------------------------
# title1 = Label(f1, text='syper market system', bg='#4A708B',
#               fg='black', font=('tajwal', 15, 'bold'))
#title1.place(x=20, y=20)

# title2 = Label(f1, text='oop project', bg='#4A708B',
#               fg='black', font=('tajwal', 15, 'bold'))
#title2.place(x=50, y=60)

title3 = Label(f1, text='contact us', bg='white',
               fg='black', font=('tajwal', 15, 'bold'))
title3.place(x=50, y=20)


# --------------------------------------------------------------------------------------------

B1 = Button(f1, text='Facebook page', width=21, height=1,
            bg='white', fg='black', font=('tajwal', 13, 'bold'), command=open1)
B1.place(x=5, y=70)

B2 = Button(f1, text='Telegram Group', width=21, height=1,
            bg='white', fg='black', font=('tajwal', 13, 'bold'), command=open2)
B2.place(x=5, y=120)

B3 = Button(f1, text='Phone number ', width=21, height=1, bg='white',
            fg='black', font=('tajwal', 13, 'bold'), command=number)
B3.place(x=5, y=170)

B4 = Button(f1, text='Address', width=21, height=1, bg='white',
            fg='black', font=('tajwal', 13, 'bold'), command=open4)
B4.place(x=5, y=220)

B5 = Button(f1, text='Youtube chanel', width=21, height=1, bg='white',
            fg='black', font=('tajwal', 13, 'bold'), command=open5)
B5.place(x=5, y=270)

B6 = Button(f1, text='Exit', width=21, height=1, bg='white',
            fg='black', font=('tajwal', 13, 'bold'), command=exit)
B6.place(x=5, y=320)
# ------------------------------------------------------------------------------------------
#photo = PhotoImage(file="C:\\Users\\DellG3\\Desktop:bola.PNG")
#imo = Label(pro, image=photo)
#imo.place(x=0, y=48, width=570, height=292)

# -------------------------------------------------------------------------------------------

F2 = Frame(pro, width=570, height=120, bg='#89cff0')
F2.place(x=0, y=330)
# ---------------------------------------------------------------------------------------------
l1 = Label(F2, text='username', bg='white',
           fg='black', font=('tajwal', 15, 'bold'))
l1.place(x=35, y=24)
l2 = Label(F2, text='password', bg='white',
           fg='black', font=('tajwal', 15, 'bold'))
l2.place(x=35, y=70)
# ---------------------------------------------------------------------------------------------
EN1 = Entry(F2, font=('tajwal', 14), justify="center")
EN1.place(x=150, y=26)
EN2 = Entry(F2, font=('tajwal', 14), justify="center")
EN2.place(x=150, y=72)
B = Button(F2, text='sign in', width=12, height=4, fg='black',
           bg='white', font=('tajwal', 13, 'bold'), command=log)
B.place(x=400, y=20)
# -----------------------------------------------------------------------------------
f3 = Frame(pro, width=563, height=290, bg='WHITE')
f3.place(x=3, y=32)

title1 = Label(f3, text='supermarket system', bg='WHITE',
               fg='black', font=('disblay', 30, 'bold'))
title1.place(x=95, y=40)
  
title2 = Label(f3, text='oop project', bg='white',
               fg='black', font=('tajwal', 30, 'bold'))
title2.place(x=170, y=150)
# --------------------------------------------------------------------------------------------
pro .mainloop()
