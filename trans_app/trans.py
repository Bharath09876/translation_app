#to run cd translator_app 
#Scripts\activate
# pip install googletrans==3.1.0a0   
#pip3 install googletrans
from googletrans import *
from tkinter.simpledialog import *
import tkinter as tk
import pyttsx3

# Top level window
frame = tk.Tk()
frame.title("Translation app")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it
# at label widget

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    inp_lan = inputtxt_lan.get(1.0, "end-1c")
    
    translator = Translator()
    #print(googletrans.LANGUAGES)
    # specify source language
    #input_text = "എങ്ങനെയിരിക്കുന്നു"
    #language_text = input("Language: ")
    translation = translator.translate(inp , src=inp_lan)
    convert_text = str(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    
    lbl.config(text = "Translated : "+convert_text)
    
def print_into_file():
    inp = inputtxt.get(1.0, "end-1c")
    inp_lan = inputtxt_lan.get(1.0, "end-1c")
    translator = Translator()
    translation = translator.translate(inp , src=inp_lan)
    f =open("translated.txt",'w')
    convert_text = str(f"{translation.text}")
    f.write(convert_text)
    f.close()

def read():
    f =open("translated.txt",'r')
    content = f.read()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 
    engine.setProperty('rate', 130)
    engine.setProperty('voice', voices[1].id)
    engine.say(content)
    engine.runAndWait()
    f.close() 
    

# TextBox Creation
inputtxt = tk.Text(frame,height = 5,width = 20)
label_1 = tk.Label(frame,text="Enter language of the given text: ")
inputtxt_lan = tk.Text(frame,height = 1,width = 20)

inputtxt.pack()
label_1.pack()
inputtxt_lan.pack()

# Button Creation
printButton = tk.Button(frame,text = "Translate",command = printInput)
printButton.pack()
printButton = tk.Button(frame,text = "Translate to file",command = print_into_file)
printButton.pack()
printButton = tk.Button(frame,text = "read from file",command = read)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()