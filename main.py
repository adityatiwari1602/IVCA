#Main Module

import GUI as gui
import command as cmd
import SpeechText as sttx
import re
green = gui.green
bright_green = gui.bright_green
red = gui.red
bright_red = gui.bright_red
def s2t():
    #while True:
        #gameDisplay.blit(carImg,(0,0))
        query = sttx.takeCommand().lower()
        query1 = cmd.optimizeQuery(query)
        print(query1)
        if re.search(r'open (.*) file', query1):
            cmd.openFile(query1)
        elif 'open' in query1:
            cmd.openWebsite(query1)
        elif re.search('play (.*) youtube', query1):
            cmd.playOnYoutube(query1)
        elif re.search('search (.*) google', query1):
            cmd.searchonGoogle(query1)
        elif 'send mail' in query1:
            cmd.sendEmail(query1)
        elif 'play song' in query1:
            cmd.playSong()
        elif re.search('tell (.*)', query1):
            cmd.search_wiki(query1)
        elif 'current weather' in query1:
            cmd.curr_weather(query1)
        elif 'screenshot' in query1:
            cmd.sc_shot()
        elif 'reminder' in query1:
            cmd.remind()
        elif 'whatsapp' in query1:
            cmd.wabot()
        elif 'bye' in query1:
            gui.message_display('Good bye sir')
            sttx.speak('Good bye sir')
            gui.sleep(2)
            quit()

def main():
    cmd.wishMe()
    while True:
        for event in gui.pygame.event.get():
            if event.type == gui.pygame.QUIT:
                gui.pygame.quit()
                quit()
        gui.button("Speak!", 150, 450, 100, 50, green, bright_green, s2t)
        gui.button("Quit", 550, 450, 100, 50, red, bright_red, gui.close)
        gui.pygame.display.update()
    
    while not gui.pygame.event.wait().type in (QUIT, KEYDOWN):
        pass

if __name__ == '__main__':
    main()
