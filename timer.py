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

def startCountdown(t):
    while t:
        # minutes = t * 60
        minutes = t / 60
        print(minutes)
        time.sleep(1)
        t -= 1
        #print(time.localtime().tm_hour)
    notify()

startCountdown(25)
# notify()
