from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import math
from datetime import datetime
import csv

##################
root = Tk()
root.title('Boo ticket - จองตั๋วหนัง')
root.geometry("2000x1000") 
root.option_add('*font', '.')
frame = Frame(root) 
frame.config(bg='pink') 
frame.place(width=2000, height=1000, x=0, y=0)
###################################################################################cal
pay = 0
def price() :

    sk1 = pop1.get() * 139
    sk2 = pop2.get() * 300
    sk3 = pop3.get() * 400
    sk4 = pop4.get() * 350
    seat = selected_value1.get()
    seatp=0
    if seat == 'A':
        seatp=240
    elif seat == 'B':
        seatp=240
    elif seat == 'C':
        seatp=200
    elif seat == 'D':
        seatp=200
    else:
        seatp=180
        
    print(seatp,sk1,sk2,sk3,sk4)
    pay = seatp + sk1 + sk2 + sk3 + sk4
    print(pay)

    label6 = Label(frame, text="ราคา {} บาท".format(pay),width=40,height=4, bg="white")
    label6.place(x=1450,y=400)
###########################################################################
def enter():
    sk1 = pop1.get() * 139
    sk2 = pop2.get() * 300
    sk3 = pop3.get() * 400
    sk4 = pop4.get() * 350
    seat = selected_value1.get()
    seatp=0
    if seat == 'A':
        seatp=240
    elif seat == 'B':
        seatp=240
    elif seat == 'C':
        seatp=200
    elif seat == 'D':
        seatp=200
    else:
        seatp=180
        
    print(seatp,sk1,sk2,sk3,sk4)
    pay = seatp + sk1 + sk2 + sk3 + sk4
    print(pay)
    time=datetime.now().strftime('%d/%m/%Y %H:%M')
    name=v_data.get()
    seatabc=selected_value1.get()
    seatnum=selected_value2.get()
    mov = movie.get()
    if mov == 1:
        watch = 'Inside Out'
    elif mov == 2:
        watch = 'End Game'
    elif mov == 3:
        watch = 'เธอกับฉันกับฉัน'
    else:
        watch = 'Annabelle'
    text="{} ผู้จอง:{} หนัง:{} ที่นั่ง:{}{} ราคา: {} บาท ".format(time,name,watch,seatabc,seatnum,pay)
    message_box = messagebox.askquestion("ยืนยันการจอง",text)
    
    if message_box == 'yes':
        messagebox.showinfo('love ticket','ขอบคุณที่ใช้บริการ ขอให้คุณเจอรักที่ดี')
        def writecsv(infolist):
            with open('info.csv','a',encoding='utf-8',newline='') as file:
                fw = csv.writer(file)
                fw.writerow(infolist)
        info=[time,name,watch,seatabc,seatnum]
        writecsv(info)
    else:
        messagebox.showerror('love ticket','ยกเลิกการจองแล้ว')
        
##############################################################################
L1 = Label(root,text='Boo ticket',font=('Angsana New',50),fg='black')
L1.place(x=860,y=50)

#########################name
LF1 = ttk.LabelFrame(root,text='ชื่อผู้จอง')
LF1.place(x=1450,y=200)

v_data = StringVar()
E1 = ttk.Entry(LF1,textvariable=v_data,font=25)
E1.pack(pady=10,padx=87)
############################################
image1 = PhotoImage(file="seat.png")
label1 = Label(image=image1,compound="top", width=800, height=450 ,bg="#FFDDF6",foreground="Black")
label1.grid(column=0, row=4, padx=560, pady=190)

RF1 = ttk.LabelFrame(root,text='เลือกที่นั่ง')
RF1.place(x=1450,y=275)
selected_value1 = tk.StringVar()
selected_value2 = tk.StringVar()
abc = ttk.Combobox(RF1,textvariable=selected_value1,values=['A','B','C','D','E','F'])
abc.grid(column=0,row=1,columnspan=1,pady=10,padx=80)
row = ttk.Combobox(RF1,textvariable=selected_value2,values=['1','2','3','4','5','6','7','8','9','10','11','12'])
row.grid(column=0,row=2,columnspan=1,pady=10,padx=80)

############################################movie
label3 = Label(frame, text="ภาพยนตร์", width=50, bg="#FEA4B0")
label3.place(x=40,y=200)

movie = IntVar()
image3 = PhotoImage(file="inoutmovie.png")
movie1= Radiobutton(root,image=image3,compound='center',variable=movie,value=1)
movie1.place(x=45,y=260)

image4 = PhotoImage(file="endgamemovie.png")
movie2= Radiobutton(root,image=image4,compound='center',variable=movie,value=2)
movie2.place(x=280,y=260)

image5 = PhotoImage(file="youmemovie.png")
movie3= Radiobutton(root,image=image5,compound='center',variable=movie,value=3)
movie3.place(x=45,y=590)

image6 = PhotoImage(file="dollmovie.png")
movie4= Radiobutton(root,image=image6,compound='center',variable=movie,value=4)
movie4.place(x=280,y=587)

############################################ ขนม
label4 = Label(frame, text="ของว่าง", width=130, bg="#FEA4B0")
label4.place(x=610,y=690)

pop1 = IntVar()
image7 = PhotoImage(file="seta.png")
p1= Checkbutton(frame,image=image7,compound='center',variable=pop1,anchor=W ,command=lambda : price())
p1.place(x=630,y=735)

pop2 = IntVar()
image8 = PhotoImage(file="setb.png")
p2= Checkbutton(frame,image=image8,compound='center',variable=pop2,anchor=W ,command=lambda : price())
p2.place(x=880,y=735)

pop3 = IntVar()
image9 = PhotoImage(file="setc.png")
p3= Checkbutton(frame,image=image9,compound='center',variable=pop3,anchor=W ,command=lambda : price())
p3.place(x=1180,y=735)

pop4 = IntVar()
image10 = PhotoImage(file="setd.png")
p4= Checkbutton(frame,image=image10,compound='center',variable=pop4,anchor=W ,command=lambda : price())
p4.place(x=1440,y=735)
####################################################################All pay
label6 = Label(frame,text="ราคา 0",width=40,height=4, bg="white")
label6.place(x=1450,y=400)   

##################################################################confirm
book = tk.Button(root,text='ยืนยันการจอง',compound='center',command=enter,width=40,height=4,bg='#fc46aa',fg='white')
book.place(x=1450,y=500)



root.mainloop()
