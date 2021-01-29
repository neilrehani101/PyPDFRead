from tkinter import filedialog
from tkinter import *
root = Tk()
root.title('PyPDFRead')
def r():
    import PyPDF2 as p2
    path = filedialog.askopenfilename(title='Open PDF To Read')
    file = open(path, 'rb')
    reading = p2.PdfFileReader(file)
    i = 0
    while i < reading.getNumPages():
        page = reading.getPage(i)
        txt.insert(0.0, page.extractText())
        txt.insert(0.0, '''
''')
        i = i + 1
root.geometry('700x700')
root.config(bg='skyblue')
l = Label(text='PyPDFRead',font=('SignPainter', 72, 'bold'), bg='skyblue')
l.pack()
get_img = Button(text='Select PDF', width=10, height=3, command=r)
get_img.pack()
get_img.place(x=300,y=150)
txt = Text()
txt.pack()
txt.place(x=50, y=250)
root.mainloop()