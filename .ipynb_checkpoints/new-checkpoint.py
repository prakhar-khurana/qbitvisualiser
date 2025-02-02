import tkinter
import qiskit
from tkinter import PhotoImage, LEFT
#define the window for the app
root = tkinter.Tk()
root.title("Quantum eyes")
#set the icon
try:
    icon = PhotoImage(file='/Users/prakharkhurana/Desktop/quantum computing projects/icon.png')  # Change to .png if needed
    root.iconphoto(True, icon)

except Exception as e:
    print(f"Error loading icon: {e}")

root.geometry('399x410')
root.resizable(0,0) #(x,y) direction allowance ##done this to block the resizing of the window


#defining the colors and fonts
background='#2c94c8'
buttons='#834558'
special_buttons = '#bc3454'
button_font=('Futura', 18)
display_font=('Futura', 32)

#define the frames of the app
display_frame = tkinter.LabelFrame(root)
button_frame=tkinter.LabelFrame(root, bg='black')
display_frame.pack()
button_frame.pack(fill="both", expand=True)

#define the display frame of the app 
display = tkinter.Entry(display_frame, width=120, font=display_font, bg=background, borderwidth=10, justify=LEFT)
display.pack(padx=3, pady=4)
#run the main loop
print ("ok")
root.mainloop()