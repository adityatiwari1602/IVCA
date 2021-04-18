#Command Module
import time
import threading
import GUI as gui
import SpeechText as st
import datetime
import subprocess
import re
import wikipedia #pip3 install wikipedia
import webbrowser
import smtplib
import pyautogui
from email.mime.text import MIMEText #pip3 install email-to
from pyowm import OWM #pip3 install pyowm
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from subprocess import Popen, PIPE
from selenium import webdriver #pip3 install selenium

white = gui.white

#def updateDB():
#    sp = Popen('sudo updatedb', shell=True, stdin=PIPE)
#    out, err = sp.communicate(b'NSTPG79911110@#$'+b'\n')

def optimizeQuery(query):
   stopWords = set(stopwords.words('english'))
   words = word_tokenize(query)
   wordsFiltered = []
   for w in words:
      if w not in stopWords:
         wordsFiltered.append(w)
   returnQuery = ""
   word = ""
   for word in wordsFiltered:
      word = word+" "
      returnQuery = returnQuery+word
   returnQuery = returnQuery[:-1]
   return returnQuery

def search_extension(ext):
   ext_dict = {
   "mp3":"mp3",
   "text":"txt",
   "c":"c",
   "python":"py"
   }
   if ext in ext_dict:
     exten = ext_dict[ext]
     return exten

def contact(to):
    contact_dict = {
            "aditya":"adityagagtiwari@gmail.com",
            "gaurav":"gaurav2016das@gmail.com",
            "anand sir":"anand.pashupatimath@gmail.com",
            "tejas":"tejaspradhan94@gmail.com",
            "shivam":"srivashivam20@gmail.com"
            }
    return contact_dict[to]
def wishMe():
    #gameDisplay.blit(carImg,(0,0))
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        gui.message_display("Good Morning!")
        st.speak("Good Morning!")
        gui.sleep(2)
        gui.gameDisplay.fill(white)

    elif hour >= 12 and hour < 17:
        gui.message_display("Good Afternoon!")
        st.speak("Good Afternoon!")
        gui.sleep(2)
        gui.gameDisplay.fill(white)

    else:  
        gui.message_display("Good Evening!")
        st.speak("Good Evening!")
        gui.sleep(2)
        gui.gameDisplay.fill(white)
      
    gui.message_display("Please tell me how may I help you")
    st.speak("Please tell me how may I help you") 
    gui.sleep(2)
    gui.gameDisplay.fill(white)

#open whatsapp
#download latest version of chromedriver from "http://chromedriver.chromium.org/"
def wabot():
    driver = webdriver.Chrome('/home/rockie/Downloads/chromedriver')
    driver.get('https://web.whatsapp.com/')

    gui.message_display("Process will be started after the QR code is scanned. Please Wait for 30 seconds!!!")
    st.speak("Process will be started after the QR code is scanned. Please Wait for 30 seconds.")
    gui.sleep(30)
    gui.gameDisplay.fill(white)

    while True:
        gui.message_display("Tell me the name of user.")
        st.speak("Tell me the name of user.")
        gui.sleep(2)
        gui.gameDisplay.fill(white)
        name = str(st.takeCommand())
        parts = name.split()
        l = len(parts)
        for i in range(l):
            parts[i] = parts[i].capitalize()
        name = ' '.join(parts)
        print(name)
        gui.message_display("What shall be the message to "+name+"?")
        st.speak("What shall be the message to "+name+"?")
        gui.sleep(2)
        gui.gameDisplay.fill(white)
        msg = str(st.takeCommand())

        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()

        msg_box = driver.find_element_by_class_name('_1Plpp')

        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()
        
        gui.sleep(2)
        gui.message_display("Message sent successfully!!!")
        st.speak("Message sent successfully")
        gui.sleep(2)
        gui.gameDisplay.fill(white)

        gui.message_display("Do you want to send any more messages?")
        st.speak("Do ypu want to send any more messages?")
        gui.sleep(2)
        gui.gameDisplay.fill(white)
        ans = str(st.takeCommand())

        if ans=='no':
            break

#set reminder
def remind():
    gui.message_display("What shall I remind you about?")
    st.speak("What shall I remind you about?")
    gui.sleep(2)
    gui.gameDisplay.fill(white)
    text="None"
    while(text == "None"):
      text = str(st.takeCommand())
      if(text != "None"):
         break
    gui.message_display("In how many minutes?")
    st.speak("In how many minutes?")
    gui.sleep(2)
    gui.gameDisplay.fill(white)
    _time="None"
    while(_time == "None"):
         _time = str(st.takeCommand())
         if(_time != "None"):
           break
    local_time=float(_time)
    t1 = threading.Thread(target=timer, args=(local_time,text,)) 
    t1.start() 
    gui.sleep(2)
    gui.gameDisplay.fill(white)
    
#timer<-----reminder
def timer(local_time,text):
    local_time = local_time * 60
    time.sleep(local_time)
    gui.message_display("It is time for "+text)
    st.speak("It is time for "+text)
    gui.sleep(2)
    gui.gameDisplay.fill(white)

#sending of email
def sendEmail(query):
    reg_ex = re.search('send mail (.*)', query)
    to = reg_ex.group(1)
    to = contact(to.lower())
    st.speak("what should i say to him ?")
    content = str(st.takeCommand().lower())
    msg = MIMEText(content)
    msg['Subject'] = "Demo"
    msg['From'] = 'demoprojectdemo@gmail.com'
    msg['To'] = to
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('demoprojectdemo007@gmail.com', 'qwerty@1234')
    server.sendmail('demoprojectdemo007@gmail.com', to, msg.as_string())
    server.close()
    gui.message_display("email sent successfully")
    st.speak("email sent successfully")
    gui.sleep(2)
    gui.gameDisplay.fill(white)

#taking screenshot
def sc_shot():
    gui.message_display("By what name you want to save the screenshot?")
    st.speak("By what name you want to save the screenshot?")
    gui.sleep(2)
    gui.gameDisplay.fill(white)
    name = str(st.takeCommand())
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'/home/rockie/major_project/pictures/'+name+'.png')
    gui.message_display("Screenshot taken successfully")
    st.speak("Screenshot taken successfully")
    gui.sleep(2)
    gui.gameDisplay.fill(white)

#searching and opening of file
def openFile(query1):
    #updateDB()
    reg_ex = re.search('open (.*) file', query1)
    ext = reg_ex.group(1)
    cmd1 = "none"
    while(cmd1 == "none"):
       print("which file you want to open in "+ext)
       gui.message_display("which file you want to open in "+ext)
       st.speak("which file you want to open in "+ext)
       gui.sleep(2)
       gui.gameDisplay.fill(white)
       cmd1 = st.takeCommand().lower()
       cmd1 = str(cmd1)
       ext = search_extension(ext)
    cmd1 = cmd1+"."+ext
    cmd3 = cmd1
    cmd = "locate -b "
    cmd2 = cmd + cmd1
    cmd2 = cmd2 + "| grep ^/home/rockie"
    return_str = subprocess.check_output(cmd2, shell = True)
    cmd1 = str(return_str)
    cmd1 = cmd1[2:-3]
    print("This file is to be opened :"+cmd1)
    gui.message_display("The file to be opened is "+cmd3+".")
    st.speak("The file to be opened is "+cmd3)
    gui.sleep(2)
    gui.gameDisplay.fill(white)
    cmd = "xdg-open "
    cmd2 = cmd + cmd1
    subprocess.call(cmd2, shell = True)

#play any song
def playSong():
    cmd1="none"
    while(cmd1=="none"):
      gui.message_display("which Song would you like to play ?" )
      st.speak("which Song would you like to play ?" )
      gui.sleep(2)
      gui.gameDisplay.fill(white)
      cmd1 = str(st.takeCommand().lower())
      cmd1 = str(cmd1)
    print(cmd1)
    cmd = "locate -b "+str(cmd1)+".mp3"
    cmd2 = cmd
    return_str = subprocess.check_output (cmd, shell = True)
    cmd1 = str (return_str)
    cmd1 = cmd1[2:-3]
    print("This file is to be opened :" + cmd1)
    gui.message_display("The file to be opened is " + cmd2+".")
    gui.sleep(2)
    gui.gameDisplay.fill(white)
    print(cmd1)
    gui.message_display(cmd1)
    gui.sleep(2)
    gui.gameDisplay.fill(white)
    cmd = "xdg-open "
    cmd2 = cmd + cmd1
    subprocess.call (cmd2, shell = True)

#open browser
def openWebsite(query):
    reg_ex=re.search('open (.*)', query)
    website=reg_ex.group(1)
    url="https://"+website+".com"
    webbrowser.open(url)

#play on youtube
def playOnYoutube(query):     
     # play stan on youtube
    reg_ex=re.search('play (.*.) youtube',query)
    song=reg_ex.group(1)
    url5="https://www.youtube.com/results?search_query="+song
    webbrowser.open(url5)

#search on google
def searchonGoogle(query):     
     # play stan on youtube
    reg_ex=re.search('search (.*.) google',query)
    name=reg_ex.group(1)
    url5="https://www.google.com/search?q="+name+"&oq="+name+"&aqs=chrome..69i57j46j0l6.1342j1j7&sourceid=chrome&ie=UTF-8"
    webbrowser.open(url5)

#wikipedia searching module
def search_wiki(query):
    reg_ex=re.search('tell (.*)', query)
    print(str(reg_ex))
    try:
        if reg_ex:
             topic = reg_ex.group(1)
             ny = wikipedia.page(topic)
             content=str(ny.content[:500].encode('utf-8'))
            # content=content[2:]
             gui.paragraph(content)
             st.speak(content)
             gui.sleep(2)
             gui.gameDisplay.fill(white)
    except Exception as e:
        gui.message_display("unable to find!!!")
        st.speak("unable to find")
        gui.sleep(2)
        gui.gameDisplay.fill(white)

#current weather module
def curr_weather(query):
   reg_ex=re.search('current weather (.*)',query)
   if reg_ex:
      try:
        city = reg_ex.group(1)
        owm = OWM(API_key='3094f11e35656b4f090c0fb204f88680')
        obs = owm.weather_at_place(city)
        w = obs.get_weather()
        k = w.get_status()
        x = w.get_temperature(unit='celsius')
        report1="Current weather in "+city+" is "+k
        report2="minimum temperature is noted as "+str(x['temp_min'])+" where as maximum temperature is "+str(x['temp_max'])
        gui.message_display(report1)
        st.speak(report1)
        gui.sleep(2)
        gui.gameDisplay.fill(white)
        gui.message_display(report2)
        st.speak(report2)
        gui.sleep(2)
        gui.gameDisplay.fill(white)
      except Exception as e:
        gui.message_display("sorry but city not found")
        st.speak("sorry but city not found")
        gui.sleep(2)
        gui.gameDisplay.fill(white)
