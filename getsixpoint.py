import random, tkinter, sys

random.seed()

def exit():
    sys.exit()

gamer1score = 0
gamer2score = 0
resultcompare = 0
clicksgamer1 = 0
clicksgamer2 = -1

def compare():
    global gamer1score
    global gamer2score
    global resultcompare

    if gamer1score < gamer2score:
        while gamer1score < gamer2score:
            resultcompare += 1
            gamer1score += 1
    if gamer1score > gamer2score:
        while gamer1score > gamer2score:
            resultcompare += 1
            gamer1score -= 1
    resultcomparestring = resultcompare
    resultcomparestring = str(resultcomparestring)
    comparelabel.config(text = 'Difference between gamers: ' + resultcomparestring + ' points!')

def drawgamer1():
    global clicksgamer1
    global clicksgamer2
    global gamer1score

    gamer1value = random.randint(-10,10)

    if gamer1value == 10:
        gamer1valuestring = gamer1value
        gamer1valuestring = str(gamer1valuestring)
        drawlabelgamer1.config(text = 'You have won the best number: You going forward about: ' + gamer1valuestring + ' points!')
        gamer1score = gamer1score + gamer1value
        gamer1scorestring = gamer1score
        gamer1scorestring = str(gamer1scorestring)
        scorelabelgamer1.config(text='You current result: ' + gamer1scorestring + ' points!')
    elif gamer1value > 0 and gamer1value < 10:
        gamer1valuestring = gamer1value
        gamer1valuestring = str(gamer1valuestring)
        drawlabelgamer1.config(text = 'You are going forward about: ' + gamer1valuestring + ' points!')
        gamer1score = gamer1score + gamer1value
        gamer1scorestring = gamer1score
        gamer1scorestring = str(gamer1scorestring)
        scorelabelgamer1.config(text='You current result: ' + gamer1scorestring + ' points!')
    elif gamer1value == 0:
        drawlabelgamer1.config(text = 'You stand in place!')
        gamer1score = gamer1score + gamer1value
        gamer1scorestring = gamer1score
        gamer1scorestring = str(gamer1scorestring)
        scorelabelgamer1.config(text='You current result: ' + gamer1scorestring + ' points!')
    else:
        gamer1valuestring = gamer1value
        gamer1valuestring = str(gamer1valuestring)
        drawlabelgamer1.config(text = 'You are backing about: ' + gamer1valuestring + ' points!')
        gamer1score = gamer1score + gamer1value
        gamer1scorestring = gamer1score
        gamer1scorestring = str(gamer1scorestring)
        scorelabelgamer1.config(text='You current result: ' + gamer1scorestring + ' points!')

    if gamer1score > 5 and clicksgamer1 == clicksgamer2 and gamer1score > gamer2score:
        winlabel.config(text='Gamer 1 WIN! You final result: ' + gamer1scorestring + ' points! Congratulations!')
        compare()
    else:
        clicksgamer1 += 1

def drawgamer2():
    global clicksgamer1
    global clicksgamer2
    global gamer2score
    global gamer1score

    gamer2value = random.randint(-10,10)

    if gamer2value == 10:
        gamer2valuestring = gamer2value
        gamer2valuestring = str(gamer2valuestring)
        drawlabelgamer2.config(text = 'You have won the best number! You going forward about: ' + gamer2valuestring + ' points!')
        gamer2score = gamer2score + gamer2value
        gamer2scorestring = gamer2score
        gamer2scorestring = str(gamer2scorestring)
        scorelabelgamer2.config(text='You current result: ' + gamer2scorestring + ' points!')
    elif gamer2value > 0 and gamer2value < 10:
        gamer2valuestring = gamer2value
        gamer2valuestring = str(gamer2valuestring)
        drawlabelgamer2.config(text = 'You are going forward about: ' + gamer2valuestring + ' points!')
        gamer2score = gamer2score + gamer2value
        drawlabelgamer2.config(text='You are going forward about: ' + gamer2valuestring + ' points!')
        gamer2scorestring = gamer2score
        gamer2scorestring = str(gamer2scorestring)
        scorelabelgamer2.config(text='You current result: ' + gamer2scorestring + ' points!')
    elif gamer2value == 0:
        drawlabelgamer2.config(text = 'You stand in place!')
        gamer2score = gamer2score + gamer2value
        gamer2scorestring = gamer2score
        gamer2scorestring = str(gamer2scorestring)
        scorelabelgamer2.config(text='You current result: ' + gamer2scorestring + ' points!')
    else:
        gamer2valuestring = gamer2value
        gamer2valuestring = str(gamer2valuestring)
        drawlabelgamer2.config(text = 'You are backing about: ' + gamer2valuestring + ' points!')
        gamer2score = gamer2score + gamer2value
        drawlabelgamer2.config(text='You are backing about: ' + gamer2valuestring + ' points!')
        gamer2scorestring = gamer2score
        gamer2scorestring = str(gamer2scorestring)
        scorelabelgamer2.config(text='You current result: ' + gamer2scorestring + ' points!')

    if gamer2score > 5 and gamer2score > gamer1score:
        winlabel.config(text='Gamer 2 WIN! You final result: ' + gamer2scorestring + ' points! Congratulations!')
        compare()
    else:
        clicksgamer2 += 1
    if gamer1score > gamer2score and gamer1score > 5:
        gamer1scorestring = gamer1score
        gamer1scorestring = str(gamer1scorestring)
        winlabel.config(text='Gamer 1 WIN! You final result: ' + gamer1scorestring + ' points! Congratulations!')
        compare()

main = tkinter.Tk()
main.geometry('400x230')
main.title('GET 6 POINTS!')

gamenamelabel = tkinter.Label(main, text = 'GET 6 POINTS!')
drawbutton1 = tkinter.Button(main, text = 'Gamer 1! Click to draw your number!', command = drawgamer1)
drawlabelgamer1 = tkinter.Label(main, text = 'Gamer 1 - current result')
scorelabelgamer1 = tkinter.Label(main, text = 'Gamer 1 - sum result')

drawbutton2 = tkinter.Button(main, text = 'Gamer 2! Click to draw your number!', command = drawgamer2)
drawlabelgamer2 = tkinter.Label(main, text = 'Gamer2 - current result')
scorelabelgamer2 = tkinter.Label(main, text = 'Gamer 2 - sum result')

winlabel = tkinter.Label(main, text = 'Win info!')
comparelabel = tkinter.Label(main, text = 'Difference between gamers')
newgamebutton = tkinter.Button(main, text = 'Exit game!', command = exit)

gamenamelabel.pack()
drawbutton1.pack()
drawlabelgamer1.pack()
scorelabelgamer1.pack()
drawbutton2.pack()
drawlabelgamer2.pack()
scorelabelgamer2.pack()
winlabel.pack()
comparelabel.pack()
newgamebutton.pack()

main.mainloop()
