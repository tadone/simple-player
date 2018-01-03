import tkinter as tk

root = tk.Tk()
root.geometry('320x240')

def callback():
    print('click')


topFrame = tk.Frame(root, background='blue', width=320, height=40)
midFrame = tk.Frame(root, background='red')
ctrlFrame = tk.Frame(root, background='black')

topFrame.pack(side="top", fill="x", expand=True)
midFrame.pack(fill="x", expand=True)
ctrlFrame.pack(side="bottom", fill="x")
# top_panel = tk.Label(root, text='Song Title', fg='green', background='black', height=2)
#mid_panel = tk.Label(root, text='Test', background='blue', height=2)

# top_panel.grid(row=0, column=0, columnspan=4, sticky='w')
#mid_panel.grid(row=1, column=0)
play_icon = tk.PhotoImage(file="buttons/yellow.gif")
stop_icon = tk.PhotoImage(file="buttons/yellow.gif")
next_icon = tk.PhotoImage(file="buttons/yellow.gif")
prev_icon = tk.PhotoImage(file="buttons/yellow.gif")
# play_icon = tk.PhotoImage(file="buttons/play-button.gif")
# stop_icon = tk.PhotoImage(file="buttons/play-button.gif")

stop_btn = tk.Button(ctrlFrame, image=stop_icon)
play_btn = tk.Button(ctrlFrame, image=play_icon)
prev_btn = tk.Button(ctrlFrame, image=prev_icon)
next_btn = tk.Button(ctrlFrame, image=next_icon)

btn1 = tk.Button(midFrame, image=stop_icon)
btn2 = tk.Button(midFrame, image=play_icon)
btn3 = tk.Button(midFrame, image=prev_icon)
btn4 = tk.Button(midFrame, image=next_icon)
#
# mode_up = tk.Button(root, height=3, width=10, text='Mode Up')
# mode_down = tk.Button(root, height=3, width=10, text='Mode Down')
# music_btn= tk.Button(root, height=6, width=10, text="Music")
# streams_btn = tk.Button(root, height=6, width=10, text="Streams")
# podcasts_btn = tk.Button(root, height=6, width=10, text='Podcasts')

stop_btn.pack(side='left', fill='both')
play_btn.pack(side='left', fill='both')
prev_btn.pack(side='left', fill='both')
next_btn.pack(side='left', fill='both')

btn1.pack(side='left', fill='both')
btn2.pack(side='left', fill='both')
btn3.pack(side='left', fill='both')
btn4.pack(side='left', fill='both')
#
# mode_up.grid(row=3, column=3, sticky='n')
# mode_down.grid(row=3, column=3, sticky='s')
# music_btn.grid(row=3, column=0)
# streams_btn.grid(row=3, column=1)
# podcasts_btn.grid(row=3, column=2)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print("Screen width:", screen_width)
print("Screen height:", screen_height)
root.mainloop()
