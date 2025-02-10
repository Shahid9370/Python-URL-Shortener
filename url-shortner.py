# Importing all the libraries
from tkinter import *
import tkinter.messagebox as tkmsg
import PIL
from PIL import ImageTk, Image
from tkinter import filedialog
import pyshorteners
import clipboard
import webbrowser

# Function to short URL
def convert():
    s = pyshorteners.Shortener().tinyurl.short(url.get())
    shorturl.set(s)
    clipboard.copy(s)
    
    Label(root, text="Shortened URL copied to clipboard (Ctrl + V to paste)", 
          bg="#1F2833", fg="#66FCF1", font="poppins 9").place(x=8, y=360)

# Initializing the tkinter root window
root = Tk()
root.title("URL Shortener")
root.geometry("400x400")
root.resizable(False, False)
root.wm_iconbitmap("link.ico")
root.config(background="#0B0C10")

# Check if the footer is removed or modified
def check_footer():
    try:
        footer_frame = root.nametowidget("footer_frame")
        if not footer_frame.winfo_exists():
            raise ValueError("Footer is missing or has been modified.")
    except Exception as e:
        tkmsg.showerror("Error", "Footer section is mandatory. Project cannot run without it.")
        root.quit()

# Background Image
image = Image.open('bg3.png')
test = ImageTk.PhotoImage(image)
label = Label(image=test, bg="#0B0C10")
label.pack()

# Variables
url = StringVar()
shorturl = StringVar()

# Labels and Entry Fields
Label(root, text="Enter URL Here", bg="#1F2833", fg="#C5C6C7", font="poppins 13 bold", padx=3, pady=1).place(x=7, y=130)
Entry(root, textvariable=url, width=35, font="poppins 12", bg="#C5C6C7", fg="#0B0C10").place(x=7, y=155)

Label(root, text="Shortened URL", bg="#1F2833", fg="#C5C6C7", font="poppins 13 bold", padx=3, pady=1).place(x=8, y=300)
short = Entry(root, textvariable=shorturl, width=35, font="poppins 12", bg="#C5C6C7", fg="#0B0C10")
short.place(x=8, y=325)

Button(root, text="Shorten URL", bg="#45A29E", fg="#0B0C10", font="poppins 11 bold", 
       command=convert, relief=GROOVE, activebackground="#66FCF1", activeforeground="#0B0C10").place(x=8, y=220)


footer_frame = Frame(root, bg="#0B0C10", name="footer_frame")
footer_frame.place(x=0, y=370, relwidth=1, height=30)

footer_label = Label(footer_frame, text="Developed by Sk | ", bg="#0B0C10", fg="#C5C6C7", font="poppins 9")
footer_label.pack(side=LEFT, padx=5)

portfolio_link = Label(footer_frame, text="Know Who I Am", fg="#66FCF1", bg="#0B0C10", font="poppins 9 underline", cursor="hand2")
portfolio_link.pack(side=LEFT)


portfolio_link.bind("<Button-1>", lambda e: webbrowser.open_new("https://portfolio-shahid-shaikh.netlify.app/"))


check_footer()

root.mainloop()