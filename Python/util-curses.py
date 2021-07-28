#coding:utf-8

import curses
from curses import textpad
import time

from lib.infos import green, red, yellow

def center(win, type):
    y, x = win.getmaxyx()
    return y//2 + 2 if type == 'y' else x//2

def boxCenter(win, type):
    return [[1, 2], [center(win, 'y'), center(win, 'x')]]

def box(win, y1 = 0, x1 = 0, y2 = 0, x2 = 0, color=green[0]):
    y1 = y1 if y1 > 0 else 2
    x1 = x1 if x1 > 0 else 4
    y2 = y2 if y2 > 0 else (2 * center(win, 'y')) - 6
    x2 = x2 if x2 > 0 else (2 * center(win, 'x')) - 6
    if color > 0:
        win.attron(curses.color_pair(color))
    textpad.rectangle(win, y1, x1, y2, x2)
    if color > 0:
        win.attroff(curses.color_pair(color))
    win.refresh()

def newWin(win, name, y, x, color):
    name = convertWinName(name)
    box(win, center(win, 'y') - y//2, center(win, 'x') - x//2, center(win, 'y') + y//2, center(win, 'x') + x//2, color)
    for i in range(center(win, 'y') - y//2 + 1, center(win, 'y') + y//2):
        win.addstr(i, center(win, 'x') - x//2 + 1, " " * ((x - 1) - 1))
    win.attron(curses.color_pair(green[0]))
    win.addstr(center(win, 'y') - y//2, center(win, 'x') - len(name)//2, name)
    win.attroff(curses.color_pair(green[0]))
    win.refresh()

def menu(win, name, options, selected):
    name = convertWinName(name)
    options = convertMenuOptions(options)
    printMenu(win, name, options, selected)
    key = win.getch()
    while key != curses.KEY_ENTER and key != 10 and key != 13:
        if key == curses.KEY_DOWN:
            if selected < len(options) - 1:
                selected += 1
            else:
                selected = 0
            printMenu(win, name, options, selected)
        elif key == curses.KEY_UP:
            if selected > 0:
                selected -= 1
            else:
                selected = len(options) - 1
            printMenu(win, name, options, selected)
        key = win.getch()
    return selected

def printMenu(win, name, options, selected):

    win.clear()

    box(win, center(win, 'y') - len(options) - 4, center(win, 'x') - getMaxSize(options)//2 - 7, center(win, 'y') + len(options), center(win, 'x') + getMaxSize(options)//2 + 7, 0)
    for i in range(center(win, 'y') - len(options) - 3, center(win, 'y') + len(options)):
        win.addstr(i, center(win, 'x') - getMaxSize(options) + 1, " " * (2 * getMaxSize(options) - 1))

    win.attron(curses.color_pair(green[0]))
    win.addstr(center(win, 'y') - len(options) - 4, center(win, 'x') - len(name)//2, name)
    win.attroff(curses.color_pair(green[0]))

    for i in range(0, len(options)):
        win.addstr(center(win, 'y') - len(options) + (2 * i) - 1, center(win, 'x') - len(options[i])//2 + 1, options[i])

    win.attron(curses.color_pair(1))
    win.addstr(center(win, 'y') - len(options) + (2 * selected) - 1, center(win, 'x') - len(options[selected])//2 + 1, options[selected])
    win.attroff(curses.color_pair(1))

    win.refresh()

def convertWinName(name):
    new = ""
    for i in name:
        new = new + " " + i.upper()
    return new + " "

def convertMenuOptions(tab):
    maxSize = getMaxSize(tab) + 6
    result = [i for i in tab]
    for i in range(0, len(result)):
        tmpLen = len(result[i])
        if tmpLen < maxSize:
            for j in range(maxSize - tmpLen):
                if j % 2 == 0:
                    result[i] = result[i] + " "
                else:
                    result[i] = " " + result[i]
    return result

def getMaxSize(tab):
    size = 0
    for i in tab:
        if len(i) > size:
            size = len(i)
    return size

def notice(win, msg, color = 0):
    box(win, center(win, 'y') - 3, center(win, 'x') - len(msg)//2 - 5, center(win, 'y') + 3, center(win, 'x') + len(msg)//2 + 5, color)
    win.attron(curses.color_pair(color))
    win.addstr(center(win, 'y') - 1, center(win, 'x') - len(msg)//2, msg)
    win.attron(curses.color_pair(green[1]))
    win.addstr(center(win, 'y') + 1, center(win, 'x') - 3, "[ OK ]")
    win.attroff(curses.color_pair(green[1]))
    win.refresh()
    key = win.getch()
    while key is not curses.KEY_ENTER and key != 10 and key != 13:
        key = win.getch()

def askYN(win, message):
    win.clear()
    newWin(win, "CONFIRM", 7, 50, 0)
    win.addstr(center(win, 'y') - 1, center(win, 'x') - len(message)//2, message)
    choice = False
    waiting = True
    while(waiting):
        if(choice):
            win.attron(curses.color_pair(green[1]))
            win.addstr(center(win, 'y') + 1, center(win, 'x') - 9, "[ YES ]")
            win.attroff(curses.color_pair(green[1]))
            win.addstr(center(win, 'y') + 1, center(win, 'x') + 2, "  NO!  ")
        else:
            win.attron(curses.color_pair(red[1]))
            win.addstr(center(win, 'y') + 1, center(win, 'x') + 2, "[ NO! ]")
            win.attroff(curses.color_pair(red[1]))
            win.addstr(center(win, 'y') + 1, center(win, 'x') - 9, "  YES  ")
        win.refresh()
        key = win.getch()
        if key == curses.KEY_LEFT:
            choice = True
        elif key == curses.KEY_RIGHT:
            choice = False
        elif key == curses.KEY_ENTER or key == 10 or key == 13:
            waiting = False
    win.clear()
    return choice

def enterRESET(win):
    newWin(win, "CONFIRM", 8, 65, red[0])
    win.addstr(center(win, 'y') - 2, center(win, 'x') - 15, "Please enter 'RESET' to confirm")
    win.attron(curses.color_pair(red[0]))
    win.addstr(center(win, 'y'), center(win, 'x') - 14, "You will loose all your data !")
    win.attroff(curses.color_pair(red[0]))
    win.addstr(center(win, 'y') + 2, center(win, 'x') - 3, "[.....]")
    curses.echo()
    curses.curs_set(1)
    result = win.getstr(center(win, 'y') + 2, center(win, 'x') - 2, 5).decode(encoding="utf-8")
    curses.noecho()
    curses.curs_set(0)
    return result == "RESET"

def bye(win):
    win.clear()
    box(win, center(win, 'y') - 1, center(win, 'x') - 11, center(win, 'y') + 1, center(win, 'x') + 11)
    msg = "Have a nice day! :)"
    for i in range(len(msg)):
        if i == len(msg) - 3:
            win.attron(curses.color_pair(yellow[0]))
        win.addstr(center(win, 'y'), center(win, 'x') - 9 + i, msg[i])
        win.refresh()
        time.sleep(0.05)
    win.attroff(curses.color_pair(yellow[0]))
    time.sleep(1)