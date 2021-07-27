#coding:utf-8

import curses
import lib.view as view

def center(win, type):
    y, x = win.getmaxyx()
    return y//2 + 2 if type == 'y' else x//2

def boxCenter(win, type):
    return [[1, 2], [center(win, 'y'), center(win, 'x')]]

def menuCurses(win, name, options):
    name = convertMenuName(name)
    convertMenuOptions(options)

    view.box(win, center(win, 'y') - len(options) - 4, center(win, 'x') - getMaxSize(options)//2 - 7, center(win, 'y') + len(options), center(win, 'x') + getMaxSize(options)//2 + 7, 0)

    win.attron(curses.color_pair(1))
    win.addstr(center(win, 'y') - len(options) - 4, center(win, 'x') - len(name)//2, name)
    win.attroff(curses.color_pair(1))

    win.attron(curses.color_pair(2))
    win.addstr(center(win, 'y') - len(options) + (2 * 0) - 1, center(win, 'x') - len(options[0])//2, options[0])
    win.attroff(curses.color_pair(2))

    for i in range(1, len(options)):
        win.addstr(center(win, 'y') - len(options) + (2 * i) - 1, center(win, 'x') - len(options[i])//2, options[i])
    
    win.refresh()

    selected = 0

    key = win.getch()
    while key != curses.KEY_ENTER and key != 13 and key != 10:
        if key == curses.KEY_DOWN:
            if selected < len(options) - 1:
                win.addstr(center(win, 'y') - len(options) + (2 * selected) - 1, center(win, 'x') - len(options[selected])//2, options[selected])
                selected += 1
                win.attron(curses.color_pair(2))
                win.addstr(center(win, 'y') - len(options) + (2 * selected) - 1, center(win, 'x') - len(options[selected])//2, options[selected])
                win.attroff(curses.color_pair(2))
                win.refresh()
        elif key == curses.KEY_UP:
            if selected > 0:
                win.addstr(center(win, 'y') - len(options) + (2 * selected) - 1, center(win, 'x') - len(options[selected])//2, options[selected])
                selected -= 1
                win.attron(curses.color_pair(2))
                win.addstr(center(win, 'y') - len(options) + (2 * selected) - 1, center(win, 'x') - len(options[selected])//2, options[selected])
                win.attroff(curses.color_pair(2))
                win.refresh()
        key = win.getch()
    return selected

def convertMenuName(name):
    new = ""
    for i in name:
        new = new + " " + i.upper()
    return new + " "

def convertMenuOptions(tab):
    maxSize = getMaxSize(tab) + 6
    for i in range(0, len(tab)):
        tmpLen = len(tab[i])
        if tmpLen < maxSize:
            for j in range(maxSize - tmpLen):
                if j % 2 == 0:
                    tab[i] = tab[i] + " "
                else:
                    tab[i] = " " + tab[i]

def getMaxSize(tab):
    size = 0
    for i in tab:
        if len(i) > size:
            size = len(i)
    return size

def askYN(win, message):
    win.clear()
    win.attron(curses.color_pair(5))
    textpad.rectangle(win, center(win, 'y') - 6, center(win, 'x') - len(message)//2 - 5, center(win, 'y') + 4, center(win, 'x') + len(message)//2 + 5)
    win.addstr(center(win, 'y') - 16, center(win, 'x') - 8, "Lucky Sudoku Solver")
    win.addstr(center(win, 'y') - 15, center(win, 'x') - len(version)//2, version)
    win.attroff(curses.color_pair(5))
    win.addstr(center(win, 'y') - 3, center(win, 'x') - len(message)//2, message)
    choice = False
    waiting = True
    while(waiting):
        if(choice):
            win.attron(curses.color_pair(2))
            win.addstr(center(win, 'y'), center(win, 'x') - 9, "[ YES ]")
            win.attroff(curses.color_pair(3))
            win.addstr(center(win, 'y'), center(win, 'x') + 2, "  NO!  ")
        else:
            win.attron(curses.color_pair(4))
            win.addstr(center(win, 'y'), center(win, 'x') + 2, "[ NO! ]")
            win.attroff(curses.color_pair(3))
            win.addstr(center(win, 'y'), center(win, 'x') - 9, "  YES  ")
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