
from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("440x640")
# root.minsize(600,700)
root.maxsize(470, 650)
root.title("Calculator By Mohd Askery")
root.wm_iconbitmap("icon.ico")
root.configure(bg='#192734')
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, bg="#0092E3", fg="white", font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=11, padx=10)

# =======================================================
# BUTTONS
f = Frame(root, bg="#16a085")

# FRAME =================================

b = Button(f, text="9", padx=28,bg="#2c3e50", fg="white", pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
# ==============================================================
b = Button(f, text="8", padx=28,bg="#2c3e50", fg="white", pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
# =========================================================
b = Button(f, text="7", padx=28,bg="#2c3e50", fg="white", pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
# ====================
f.pack()
# =======================================================
# BUTTONS
f = Frame(root, bg="#16a085")
# ==========================================
b = Button(f, text="6",bg="#2c3e50", fg="white", padx=28, pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
# =======================================================

b = Button(f, text="5",bg="#2c3e50", fg="white", padx=28, pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
# =======================================================

b = Button(f, text="4",bg="#2c3e50", fg="white", padx=28, pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
# =======================================================

f.pack()

# =======================================================
# BUTTONS
f = Frame(root, bg="#16a085")
b = Button(f, text="3",bg="#2c3e50", fg="white", padx=28, pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
# =======================================================
b = Button(f, text="2",bg="#2c3e50", fg="white", padx=28, pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
# =======================================================
b = Button(f, text="1",bg="#2c3e50", fg="white", padx=28, pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
# =======================================================

f.pack()


f = Frame(root, bg="#16a085")
b = Button(f, text="0",bg="#2c3e50", fg="white", padx=30, pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-",bg="#2c3e50", fg="white", padx=29, pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*",bg="#2c3e50", fg="white", padx=30, pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="#16a085")
b = Button(f, text="/", padx=34, bg="#2c3e50", fg="white", pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="%",bg="#2c3e50", fg="white", padx=27, pady=11, font="lucida 18 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+",bg="#2c3e50", fg="white", padx=26, pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="#16a085")
b = Button(f, text="C",bg="#2c3e50", fg="white", padx=25, pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text=".",bg="#2c3e50", fg="white", padx=28, pady=0, font="lucida 30 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=",bg="#2c3e50", fg="white", padx=25, pady=11, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()
