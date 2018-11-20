#!/usr/bin/env python

import time

# Requires libnotify and python-gobject
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

def notify():
    Notify.init('Ça va')
    Hello = Notify.Notification.new('Ça va', 'Le minuteur est fini')
    Hello.show()

def getInput():
    time = input('How long would you like to set the timer for?\n')
    return int(time)

def startCountdown(t):
    minutes = t * 60
    while minutes:
        time.sleep(1)
        minutes -= 1
        #print(time.localtime().tm_hour)
    notify()

startCountdown(getInput())
