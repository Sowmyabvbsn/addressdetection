import extractor
import regex_import
import csv_import
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
import openpyxl
from PIL import ImageTk, Image
import os
import imutils

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        self.master.geometry(self._geom)
        self._geom = geom

def check():
    result = extractor.get_string(dirname)
    pincode = regex_import.pin_finder(result)[0]
    address = csv_import.csv_reader(pincode)
    s1 = "Pin Code: " + (str(address[0]))
    s2 = "District: " + (str(address[1]))
    s3 = "Post Office(s): " + (str(address[2]))
    s4 = "State: " + (str(address[3]))
    s5 = "Division Name: " + (str(address[4]))
    s6 = "Taluk: " + (str(address[5]))
    var1.set(s1)
    var2.set(s2)
    var3.set(s3)
    var4.set(s4)
    var5.set(s5)
    var6.set(s6)
def givepath():
    root1 = Tk()
    root1.withdraw()
    global dirname
    dirname = filedialog.askopenfilename()
    root1.destroy()

def window():
    global root
    root = Tk()
    root.resizable(False, False)
    root.geometry("1000x800")
    app = FullScreenApp(root)
    root.title('Automatic Address Tracer')

    style = Style()
    style.configure("TButton", font=('Helvetica', 12), padding=6)
    style.configure("TLabel", font=('Helvetica', 12))

    # Main Frame
    main_frame = Frame(root, padding="20")
    main_frame.pack(expand=True, fill=BOTH)

    # Header Section
    header_frame = Frame(main_frame)
    header_frame.pack(side=TOP, pady=10)
    header_label = Label(header_frame, text="POSTAL ADDRESS TRACER", font=("Courier", 20, "bold"))
    header_label.pack()

    # Description Section
    desc_frame = Frame(main_frame, padding="20")
    desc_frame.pack(side=TOP, pady=10)
    description = Text(desc_frame, height=5, width=80, wrap=WORD, font=("Helvetica", 12))
    description.insert(END, '''Easily uncover the full postal address details in seconds! Upload an image of any postal address, and our tool will instantly identify the pin code, along with key information like the district, city, and state. Simple, fast, and efficient—get precise location insights with just a click!''')
    description.config(state=DISABLED)
    description.pack()
    
    img_frame = Frame(main_frame)
    img_frame.pack(side=TOP, pady=10)
    img = PhotoImage(file="Post_Office_Logo_RGB.png")  # Ensure you have this image in your project folder
    img_label = Label(img_frame, image=img)
    img_label.pack()

    # Select File Button
    button_frame = Frame(main_frame)
    button_frame.pack(side=TOP, pady=10)
    select_button = Button(button_frame, text="Select Postal Address Image File", command=givepath)
    select_button.pack(pady=5)

    # Submit Button
    submit_button = Button(button_frame, text="Submit", command=check)
    submit_button.pack(pady=5)

    # Results Section
    global var1, var2, var3, var4, var5, var6
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()
    var6 = StringVar()
    result_frame = Frame(main_frame, padding="10")
    result_frame.pack(side=TOP, pady=20)

    result_label1 = Label(result_frame, textvariable=var1, font=("Helvetica", 12))
    result_label1.pack(pady=3)

    result_label2 = Label(result_frame, textvariable=var2, font=("Helvetica", 12))
    result_label2.pack(pady=3)

    result_label3 = Label(result_frame, textvariable=var3, font=("Helvetica", 12))
    result_label3.pack(pady=3)

    result_label4 = Label(result_frame, textvariable=var4, font=("Helvetica", 12))
    result_label4.pack(pady=3)
    
    result_label5 = Label(result_frame, textvariable=var5, font=("Helvetica", 12))
    result_label5.pack(pady=3)

    result_label6 = Label(result_frame, textvariable=var6, font=("Helvetica", 12))
    result_label6.pack(pady=3)

    root.mainloop()

if __name__ == '__main__':
    window()
