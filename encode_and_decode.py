from tkinter import * 
import base64

root = Tk()

root.geometry('500x300')
root.resizable(0, 0)
root.title("Message Encode and Decode")

Label(root, text= 'ENCODE DECODE', font = 'arial 20 bold').pack()

Text = StringVar()
keys = StringVar()
mode = StringVar()
result = StringVar()

enc = []
def Encode(key,message):

    for i in range(len(message)):
        key_c= key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return
base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)

def Mode():
    if(mode.get() == 'e'):

        result.set(Encode(keys.get(),Text.get()))
    elif(mode.get() == 'd'):

        result.set(Decode(keys.get(),Text.get()))
    else:
        result.set('Invalid mode')

def Exit():
    root.destroy()

def Reset():
    Text.set("")
    mode.set("")
    keys.set("")
    result.set("")

Label(root, font= 'aril 12 bold', text='message').place(x=60, y=60)
Entry(root, font= 'aril 10', textvariable= Text, bg= 'ghost white').place(x=290, y=60)

Label(root, font= 'aril 12 bold', text='key').place(x=60, y=90)
Entry(root, font= 'aril 10', textvariable= keys, bg= 'ghost white').place(x=290, y=90)

Label(root, font= 'aril 12 bold', text='MODE(e-encode, d-decode)').place(x=60, y=120)
Entry(root, font= 'aril 10', textvariable= mode, bg= 'ghost white').place(x=290, y=120)
Entry(root, font= 'aril 10', textvariable= result, bg= 'ghost white').place(x=290, y=150)

Button(root, font= 'arial 10 bold', text = 'RESULT', padx= 2, bg= 'lightgray', command= Mode).place(x=60, y=150)
Button(root, font= 'arial 10 bold', text = 'RESET', width=6, padx= 2, bg= 'limegreen', command= Reset).place(x=80, y=190)
Button(root, font= 'arial 10 bold', text = 'EXIT',width= 6, padx= 2, pady= 2, bg= 'orangered', command= Exit).place(x=180, y=190)

root.mainloop()

