
import easygui as eg
import sys

while 1:

    msg ="Let's begin please choose a number below to begin. Remember to try you're best and have fun! "
    title = "Learn My Times Tables For Adults and Teenagers"
    choice = eg.enterbox(msg, title)
    def exit():
          eg.msgbox("Click to exit")
          sys.exit()


    # These are the different levels that a user might choose
    def ones():
        onecalc = (0)
        startones = eg.msgbox("Welcome to the 1's! Please try you're ultimate best if you wish to succeed")
        for x in range(11): # This is used for a range of numbers 0 to 10| ex. What is 1 * {x} <--x is number range
            promptone = ("What is 1 X",x)  # This is used so that we can use the one's.
            startone=eg.enterbox(promptone, "Ones Multiplication")
            compitint = int(startone)  # Converts startone to a int so that we can compare it to x
            if compitint == (x):
                eg.msgbox("Yes you are correct!")
                onecalc += 1
                print (onecalc)
            elif compitint != (x):
                eg.msgbox("WRONG")
            if x == (10):
                eg.msgbox("The total amount you got correct was", onecalc)  # Fix bug

    def two():
        for x in range(11):
            twocalc = (0)
            prompttwo = ("What is 2 times", x)
            twostart = eg.enterbox(prompttwo, "Two Multiplication")
            twoint = int(twostart)
            comparetwo = (2 * x)
            if twoint == comparetwo:
                eg.msgbox("You are once more correct!")
                twocalc += 1 
            elif twoint != comparetwo:
                eg.msgbox("Sorry but you are incorrect ")

    def three():
        for x in range(11):
            threecalc = (0)
            prompthree = ("What is 3 times", x)
            threestart = eg.enterbox(prompthree, "Three Multiplication")
            threeint = int(threestart)
            comparethree = (3 * x)
            if threeint == comparethree:
                eg.msgbox("You are once more correct!")
                threecalc += 1 
            elif threeint != comparethree:
                eg.msgbox("Sorry but you are incorrect")


    def four():
        for x in range(11):
            fourcalc = (0)
            promptfour = ("What is 4 times", x)
            fourstart = eg.enterbox(promptfour, "Four Multiplication")
            fourint = int(fourstart)
            comparefour = (4 * x)
            if fourint == comparefour:
                eg.msgbox("Yes you are correct")
                fourcalc += 1
            elif fourint != comparefour:
                eg.msgbox("Sorry but you are incorrect ")

    def five():
        for x in range(11):
            fivecalc = (0) 
            promptfive = ("What is 5 times", x)
            fivestart = eg.enterbox(promptfive, "Five Multiplication")
            fiveint = int(fivestart)
            comparefive = (5 * x)
            if fiveint == comparefive:
                eg.msgbox("Yes that is correct")
                fivecalc += 1 
            elif fiveint != comparefive:
                eg.msgbox("Sorry but this is incorrect")

    def six():
        for x in range(11):
            sixcalc = (0)
            promptsix = ("What is 6 times", x)
            sixstart = eg.enterbox(promptsix, "Six Multiplication")
            sixint = int(sixstart)
            comparesix = (6 * x)
            if sixint == comparesix:
                eg.msgbox("Yes this is correct")
                sixcalc += 1
            elif sixint != comparesix:
                eg.msgbox("Sorry but this is incorrect")

    def seven():
        for x in range(11):
            sevencalc = (0)
            promptseven = ("What is 7 times", x)
            sevenstart = eg.enterbox(promptseven, "Seven Multiplication")
            sevenint = int(sevenstart)
            compareseven = (7 * x)
            if sevenint == compareseven:
                eg.msgbox("Yes this is correct")
                sevencalc += 1
            elif sevenint != compareseven:
                eg.msgbox("Sorry but this is incorrect")

    def eight():
        for x in range(11):
            eightcalc = (0) 
            prompteight = ("What is 8 times", x)
            eightstart = eg.enterbox(prompteight, "Eight Multiplication")
            eightint = int(eightstart)
            compareeight = (8 * x)
            if eightint == compareeight:
                eg.msgbox("Yes this is correct")
                eightcalc += 1
            elif eightint != compareeight:
                eg.msgbox("Sorry but this is incorrect")

    def nine():
        for x in range(11):
            ninecalc = (0)
            promptnine = ("What is 9 times", x)
            ninestart = eg.enterbox(promptnine, "Nine Multiplication")
            nineint = int(ninestart)
            comparenine = (9 * x)
            if nineint == comparenine:
                eg.msgbox("Yes this is correct")
                ninecalc += 1
            elif nineint != comparenine:
                eg.msgbox("Sorry but this is incorrect")

    def ten():
        for x in range(11):
            tencalc = (0)
            promptten = ("What is 10 times", x)
            tenstart = eg.enterbox(promptten, "Ten Multiplication")
            tenint = int(tenstart)
            compareten = (10 * x)
            if tenint == compareten:
                eg.msgbox("Yes this is correct")
                tencalc += 1
            elif tenint != compareten:
                eg.msgbox("Sorry but this is incorrect")
        





        
# This is the choices that a user can make to go to a level. | Ex. choice == 5, goes to definition called 5 and runs the 5's           
    
    if choice == ("1"):
        StartOne = (ones())
    if choice == ("2"):
        StartTwo = (two())
    if choice == ("3"):
        StartThree = (three())
    if choice == ("4"):
        StartFour = (four())
    if choice == ("5"):
        StartFive = (five())
    if choice == ("6"):
        StartSix = (six())
    if choice == ("7"):
        StartSeven = (seven())
    if choice == ("8"):
        StartEight = (eight())
    if choice == ("9"):
        StartNine = (nine())
    if choice == ("10"):
        Startten = (ten())
