'''
Please enable permision by logging in from the "From address"and follow link
"https://www.google.com/settings/security/lesssecureapps"
'''
import tkinter
from tkinter import *
import webbrowser
import time
import smtplib
from email.mime.text import MIMEText

root = tkinter.Tk()
root.title('Mail-ER by RAKi')
root.config(bg='white')
root.geometry('1366x768')


def sendMail():
    FromAddr = FromAddr1.get()
    Pwd = Pwd1.get()
    ToAddr = ToAddr1.get()
    Sub = Sub_Box.get("1.0","end-1c")
    Body =Msg_Box.get("1.0","end-1c")
    msg = MIMEText(Body)
    Err_msg=StringVar()

    msg['From'] = FromAddr
    msg['To'] = ToAddr
    msg['Subject'] = Sub

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    try:
        server.login(FromAddr,Pwd)
        server.send_message(msg)
    except smtplib.SMTPAuthenticationError:
        Err_msg.set("Email or Password is wrong please check !!!")
        Error_Label = Label(root,textvariable=Err_msg,bg='white',fg='red')
        Error_Label.place(x=10,y=250)
        root.update()
        time.sleep(3)
        Err_msg.set(" ")
    except TypeError:
        Err_msg.set("Entery fields empty please check !!!")
        Error_Label = Label(root,textvariable=Err_msg,bg='white',fg='red')
        Error_Label.place(x=10,y=250)
        root.update()
        time.sleep(3)
        Err_msg.set(" ")
    else:
        Err_msg.set("Message sending ->")
        Error_Label = Label(root,textvariable=Err_msg,bg='white',fg='green')
        Error_Label.place(x=10,y=250)
        root.update()
        time.sleep(1)
        Err_msg.set("Message sending - ->")
        root.update()
        time.sleep(1)
        Err_msg.set("Message sending - - ->")
        root.update()
        time.sleep(1)
        Err_msg.set("Message sent successfully !!!")
        root.update()
        time.sleep(1)
        Err_msg.set("")

    finally:
        print('--------------------------------------')
        print('From address :',FromAddr)
        print('Pwd : Cant display it!!!')
        print('To address :',ToAddr)
        print('Subject is:',Sub)
        print('Message is :',Body)
        print('--------------------------------------')

        server.quit()



Show_string='*'
def show_click():
    Show_string=''
    Pwd_Entry = Entry(root,textvariable=Pwd1,justify=LEFT,show=Show_string)
    Pwd_Entry.place(x=100,y=50,width=200)
    root.update()

def hide_click():
    Show_string='*'
    Pwd_Entry = Entry(root,textvariable=Pwd1,justify=LEFT,show=Show_string)
    Pwd_Entry.place(x=100,y=50,width=200)
    root.update()

def OpenWeb(url):
    webbrowser.open_new(url)


FA_Label = Label(root,text='From Email: ',bg='white')
FA_Label.place(x=10,y=10)
FromAddr1=StringVar()
FA_Entry = Entry(root,textvariable=FromAddr1,justify=LEFT)
FA_Entry.place(x=100,y=10,width=200)

Pwd_Label = Label(root,text='Password: ',bg='white')
Pwd_Label.place(x=10,y=50)
Pwd1=StringVar()
Pwd_Entry = Entry(root,textvariable=Pwd1,justify=LEFT,show=Show_string)
Pwd_Entry.place(x=100,y=50,width=200)

Show_Button = Button(root,text='Show',bg='white',command=show_click)
Show_Button.place(x=100,y=75,width=50,height=15)
Hide_Button = Button(root,text='Hide',bg='white',command=hide_click)
Hide_Button.place(x=150,y=75,width=50,height=15)

TA_Label = Label(root,text='To Email: ',bg='white')
TA_Label.place(x=10,y=120)
ToAddr1=StringVar()
TA_Entry = Entry(root,textvariable=ToAddr1,justify=LEFT)
TA_Entry.place(x=100,y=120,width=200)

Sub_Label = Label(root,text='Subject',bg='white')
Sub_Label.place(x=600,y=20)
Sub_Box = Text(root)
Sub_Box.place(x=600,y=50,width=500,height=50)

Msg_Label = Label(root,text='Message',bg='white')
Msg_Label.place(x=600,y=120)
Msg_Box = Text(root)
Msg_Box.place(x=600,y=150,width=500,height=200)

Send_Button = Button(root,text='Send',command=sendMail,bg='white').place(x=10,y=200)

info="""Note:
For security reasons google.com donot allow third party apps to send mail
So please login with your gmail account and allow 'less secure apps'
To Enable : """
Info_Label = Label(root,text=info,bg='white',justify=LEFT)
Info_Label.place(x=10,y=500)
Link1 = Label(root,text='Click Here',bg='white',fg='blue')
Link1.place(x=75,y=550)
Link1.bind("<Button-1>",lambda e:OpenWeb("https://www.google.com/settings/security/lesssecureapps"))

root.mainloop()
