from tkinter import *
from tkinter.ttk import *
from time import strftime
import pyttsx3
import smtplib
from email.message import EmailMessage
from time import strftime

####################################################################

def sendEmailAlert(timeString):
    EMAIL_ADDRESS = 'ourpythonproject2021@gmail.com'
    EMAIL_PASSWORD = 'Python2021'
    SEND_EMAIL_TO_ADDRESS = 'ourpythonproject2021@gmail.com'
    msg = EmailMessage()
    msg['Subject'] = 'Email send from python smart clock program!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = SEND_EMAIL_TO_ADDRESS
    msg.set_content('Your Alarm time is: ' + timeString)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print('Email Alert was sent out to: ' + SEND_EMAIL_TO_ADDRESS)


def sayAlert(timeString):
    speaker = pyttsx3.init()
    speaker.say('This is your alarm.  The time is now: ' + timeString)
    speaker.say('I will send out an email to you also')
    speaker.runAndWait()

def checkAlert(timeString):
    if (timeString == ALARM_TIME):
        print('Alert time')
        sayAlert(timeString)
        sendEmailAlert(timeString)


def time():
    tString="%I:%M:%S %p"
    timeDisplayString = strftime("TIME: " + tString +" - (Alarm: " + ALARM_TIME + ")")
    timeString = strftime(tString)
    label.config(text=timeDisplayString)
    label.after(1000, time)  # 1000 is in ms which is equal to 1 second
    checkAlert(timeString)

def getAlarmTime():
    print('Please enter your alarm time: ')
    HOUR = input("enter your hour: ")
    MINUTE = input("enter your minutes: ")
    SECOND = input("enter your seconds: ")
    AM_PM_NUMBER = input("enter 1 for AM, 2 for PM:")
    if AM_PM_NUMBER == 1:
        AM_PM = 'AM'
    elif AM_PM_NUMBER == 2:
        AM_PM = 'PM'
    else:
        AM_PM = 'AM'
    ALARM_TIME = HOUR + ':' + MINUTE + ':' + SECOND + ' ' + AM_PM
    print('ALARM You entered is: ' + ALARM_TIME)
    return(ALARM_TIME)

def startClock():
    time()
    tk.mainloop()

####################################################################

tk = Tk()
tk.title("Smart-Clock")
label = Label(tk, font=("ds-digital", 30), background="black", foreground="cyan")
label.pack(anchor='center')

ALARM_TIME = getAlarmTime()

startClock()
