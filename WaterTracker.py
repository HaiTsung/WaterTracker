from winotify import *
import customtkinter as ctk

water = Notification(app_id="Water Tracker", msg="Drink Water Now", title="Drink Water Now", icon=r"C:\Users\morte\Desktop\Python\PythonProject1\ressources\waterDrop.png")
water.add_actions(label="Remind in 5 min",
                  launch="https://github.com/versa-syahptr/winotify/")
water.add_actions(label="Done!",
                  launch="https://github.com/versa-syahptr/winotify/")

#water.show()

waterToday = 0

weekdays = ["Mon.", "Tue.", "Wed.", "Thu.", "Fri.", "Sat.", "Sun."]

root = ctk.CTk()
root.geometry("600x400")
root.title("Water today.")
root.configure(fg_color="#07172D")
root.resizable(False, False)



titleFont = ctk.CTkFont(family="Times New Roman", size=64)
amountFont = ctk.CTkFont(family="Times New Roman", size=36)
mlFont = ctk.CTkFont(family="Times New Roman", size=20)
historyFont = ctk.CTkFont(family="Times New Roman", size=24)


title = ctk.CTkLabel(root, text="Water\ntoday.",text_color="white", font=titleFont)
title.place(x=24, y=7)

historyFrame = ctk.CTkFrame(root)
historyFrame.configure(fg_color="transparent", width=546, height=149)
historyFrame.place(x=27, y=269)

glasses = ctk.CTkLabel(root, text="0 / 8 glasses.", text_color="white", font=amountFont, width=215)
glasses.place(x=290, y=55)

counterSectionLine = ctk.CTkFrame(root, height=1, width=121, bg_color="white")
counterSectionLine.place(x=337, y=109)

def addWater():
    global waterToday
    waterToday += 1
    updateUserInterface()

def removeWater():
    global waterToday
    if waterToday != 0:
        waterToday -= 1
        updateUserInterface()


def updateUserInterface():
    glasses.configure(text=f"{waterToday} / 8 glasses.")
    ml.configure(text=f"or {waterToday * 250}ml from 2000ml.")

plusButton = ctk.CTkButton(root, text="+1.", width=82, font=amountFont, fg_color="transparent", command=addWater,
                           hover_color="#07172D")
plusButton.place(x=293, y=167)

buttonSectionLine = ctk.CTkFrame(root, height=45, width=1, bg_color="white")
buttonSectionLine.place(x=398, y=167)

minusButton = ctk.CTkButton(root, text="-1.", width=82, font=amountFont, fg_color="transparent", command=removeWater,
                            hover_color="#07172D")
minusButton.place(x=413, y=167)

ml = ctk.CTkLabel(root, text="or 0ml from 2000ml.", text_color="#93C4FF", width=215, font=mlFont)
ml.place(x=290, y=122)

historyTitle = ctk.CTkLabel(root, text="last 5 days.", text_color="white", font=historyFont)
historyTitle.place(x=27, y=212)
sectionLine = ctk.CTkFrame(root, height=1, bg_color="white", width=546)
sectionLine.place(x=27, y=248)

for i in range(5):
    day = ctk.CTkLabel(historyFrame, text=weekdays[i], text_color="white", font=historyFont, width=68)
    day.grid(row=0, column=i, padx=(0,52), pady=0)
    dayData = ctk.CTkLabel(historyFrame, text="4/8\ngls.", text_color="#93C4FF", font=historyFont, width=68)
    dayData.grid(row=1, column=i, padx=(0,52), pady=8)





root.mainloop()


#def updateInterface():
