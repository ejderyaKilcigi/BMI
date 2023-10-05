from tkinter import *

screen = Tk()
screen.minsize(width=300, height=150)
screen.config(bg="#9EA7E2")
screen.config(padx=30, pady=15)

# Label Weight
labelWeight = Label()
labelWeight.pack()
labelWeight.config(text="Please Enter Your Weight (Kg) ", bg="#9EA7E2", pady=2)

# Entry Weight
entryWeight = Entry()
entryWeight.pack()
entryWeight.config(width=10)

# Label Height
labelHeight = Label()
labelHeight.pack()
labelHeight.config(text="Please Enter Your Height (Cm) ", bg="#9EA7E2", pady=2)

# Entry Height
entryHeight = Entry()
entryHeight.pack()
entryHeight.config(width=10)

# Result Label
resultLabel = Label()
resultLabel.pack()
resultLabel.config(text="", bg="#9EA7E2", pady=2)

def buttonClick():
    weight = entryWeight.get()
    height = entryHeight.get()
    if weight == "" or height == "":
        resultLabel.config(text="Weight or Height Empty")
    else:
        try:
            bmi = float(weight) / (float(height)/100) ** 2
            resultString = wrightResult(bmi)
            resultLabel.config(text=resultString)
        except:
            resultLabel.config(text="işlem hatası")


def wrightResult(bmi):
    result = f"Your BMI {round(bmi, 2)}. You Are "
    if bmi < 16.0:
        result += "Selevery UnderWeight"
    elif 16.1 < bmi < 18.4:
        result += "UnderWeight"
    elif 18.5 < bmi < 24.9:
        result += "Normal"
    elif 25 < bmi < 29.9:
        result += "OverWeight"
    elif 30.0 < bmi < 34.9:
        result += "Moderately Obese"
    elif 35.0 < bmi < 39.9:
        result += "Severely Obese"
    else:
        result += "Morbidly Obese"
    return result


# Button
showButton = Button()
showButton.pack()
showButton.config(text="Calculate", width=7, height=1, command=buttonClick)



screen.mainloop()