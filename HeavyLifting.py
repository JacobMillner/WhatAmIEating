#Lib to read/write meals to csv
import ctypes  #for alert messages
import easygui

def msgBox(message):
    easygui.msgbox(message, title="Alert!")

def addMeal(date, name, link):
    #open() with the 'a' parameter allows you to append to file
    f = open('meals.csv','a')
    
    #TODO: validation
    #TODO: Check if first row, if not:\n and comma
    mealRow = "{0}, {1}, {2}".format(date, name, link)
    
    f.write(mealRow)
    f.close()

    msgBox("Meal added!")

    
