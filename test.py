import tkinter as tk

counter = 0
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()


root = tk.Tk()
root.title("Music Player")
root.resizable(width=None, height=None)
root.geometry('{}x{}'.format(320, 240))
# root.wm_attributes('-fullscreen', 1)

# create all of the main containers
top_frame = tk.Frame(root, bg='black', width=320, height=40, pady=6)
center_frame = tk.Frame(root, bg='blue', width=320, height=100, padx=0, pady=0)
btm_frame = tk.Frame(root, bg='green', width=320, height=100, pady=0, padx=0)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center_frame.grid(row=1, sticky="ew")
btm_frame.grid(row=2, sticky="ew")

category = tk.Label(top_frame, fg='white', bg='black', height=2, width=10, text='Podcasts').pack(side='left')
now_playing = tk.Label(top_frame, fg='green', bg='black', height=2, width=30, text='New Podcast Playing').pack(side='right')
# create the center widgets
# center_frame.grid_rowconfigure(0, weight=1)
# center_frame.grid_columnconfigure(1, weight=1)

button1 = tk.Button(center_frame, text='Stop', width=6, height=6, command=root.destroy).grid(row=0, column=0)
button2 = tk.Button(center_frame, text='Play', width=8, height=6, command=root.destroy).grid(row=0, column=1)
button3 = tk.Button(center_frame, text='Next', width=6, height=6, command=root.destroy).grid(row=0, column=2)
button4 = tk.Button(center_frame, text='Prev', width=6, height=6, command=root.destroy).grid(row=0, column=3)

button5 = tk.Button(btm_frame, text='Exit', width=6, height=6, command=root.destroy).grid(row=0, column=0)
button6 = tk.Button(btm_frame, text='Pause', width=8, height=6, command=root.destroy).grid(row=0, column=1)
button7 = tk.Button(btm_frame, text='Down', width=6, height=6, command=root.destroy).grid(row=0, column=2)
button8 = tk.Button(btm_frame, text='Up', width=6, height=6, command=root.destroy).grid(row=0, column=3)
#
# button1.pack(side='left')
# button2.pack(side='left')
# button3.pack(side='left')
# button4.pack(side='left')
#
# button5.pack(side='left')
# button6.pack(side='left')
# button7.pack(side='left')
# button8.pack(side='left')

root.mainloop()
