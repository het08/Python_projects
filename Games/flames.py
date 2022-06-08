import tkinter as tk

FLAMES = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

def flames(name1, name2):
    char_counts1 = {}
    for chr in name1.lower():
        char_counts1[chr] = char_counts1.get(chr, 0) + 1

    char_counts2 = {}
    for chr in name2.lower():
        char_counts2[chr] = char_counts2.get(chr, 0) + 1

    num_unshared = 0
    keys = set(char_counts1.keys()).union(char_counts2.keys())
    for chr in keys:
        count1 = char_counts1.get(chr, 0)
        count2 = char_counts2.get(chr, 0)
        num_unshared += abs(count1 - count2)

    if num_unshared == 0:
        return FLAMES[0]

    flames_indices = list(range(len(FLAMES)))
    idx = 0
    while len(flames_indices) > 1:
        idx += num_unshared - 1
        idx %= len(flames_indices)
        flames_indices.pop(idx)
        if idx == len(flames_indices):
            idx = 0

    return FLAMES[flames_indices[0]]

root=tk.Tk()

canvas1 = tk.Canvas(root, width = 600, height = 600, relief = 'raised', bg = 'black')
canvas1.pack()

label1 = tk.Label(root, text = 'FLAMES')
label1.config(bg = 'black', fg = 'red', font = ('algerian', 74, 'bold'))
canvas1.create_window(300, 70, window = label1)

label2 = tk.Label(root, text = 'Enter your name')
label2.config(bg = 'black', fg = 'white', font = ('gabriola', 24))
canvas1.create_window(300, 150, window = label2)

entry1 = tk.Entry(root)
canvas1.create_window(300, 200, window = entry1)

label3 = tk.Label(root, text = 'Enter your crush name')
label3.config(bg = 'black', fg = 'white', font = ('gabriola', 24))
canvas1.create_window(300, 250, window = label3)

entry2 = tk.Entry(root)
canvas1.create_window(300, 300, window = entry2)

label4 = tk.Label(root)
label4.config(bg = 'black', fg = 'white', font = ('gabriola', 24))
canvas1.create_window(300, 480, window = label4)

def flames_result():
    name1 = entry1.get().strip()
    name2 = entry2.get().strip()

    if name1 == "" or name2 == "":
        label4.configure(text="Enter both the names!")
    else:
        label4.configure(text=flames(name1, name2))

button1 = tk.Button(text = 'FLAMES', command = flames_result, bg = 'white', fg = 'red', font = ('helvetica', 24, 'bold'))
canvas1.create_window(300, 400, window = button1)

root.mainloop()