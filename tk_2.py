import tkinter as tk

root = tk.Tk()
root.geometry('320x240')

def callback():
    print('click')

topFrame = tk.Frame(height=2)
ctrlFrame = tk.Frame(background='black')
topFrame.pack(side="top", fill="x", expand=True)
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

stop_btn = tk.Button(ctrlFrame, image=stop_icon, height=64, width=64, text='Stop', highlightthickness=0, borderwidth=0, padx=0, pady=0, bg = 'black', command=callback, default='disabled')
play_btn = tk.Button(ctrlFrame, image=play_icon, height=64, width=64, text="Play/Pause", borderwidth=0, padx=0, pady=0)
prev_btn = tk.Button(ctrlFrame, image=prev_icon, height=64, width=64, text="Prev", borderwidth=0, padx=0, pady=0)
next_btn = tk.Button(ctrlFrame, image=next_icon, height=64, width=64, text="Next", borderwidth=0, padx=0, pady=0)
#
# mode_up = tk.Button(root, height=3, width=10, text='Mode Up')
# mode_down = tk.Button(root, height=3, width=10, text='Mode Down')
# music_btn= tk.Button(root, height=6, width=10, text="Music")
# streams_btn = tk.Button(root, height=6, width=10, text="Streams")
# podcasts_btn = tk.Button(root, height=6, width=10, text='Podcasts')

stop_btn.pack()
play_btn.pack(side='left')
prev_btn.pack(side='left')
next_btn.pack(side='left')
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
