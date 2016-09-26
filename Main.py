
#making a simple GUI

from Tkinter import *

#create the window
root = Tk()

#modify root window
root.title("What am I eating?")
root.geometry("250x200")

#creates&adds frame&label&buttons into grid
#main menu options for user to add,view,modify&delete meals
app = Frame(root)
app.grid()

menuLabel = Label(app, text = "Please select an option:")
menuLabel.grid()

addMeal = Button(app, text = "Add Meal")
addMeal.grid()

viewMeal = Button(app, text = "View Meal")
viewMeal.grid()

editMeal = Button(app, text = "Edit Meal")
editMeal.grid()

deleteMeal = Button(app, text = "Delete Meal")
deleteMeal.grid()

#kick off the event loop
root.mainloop()

