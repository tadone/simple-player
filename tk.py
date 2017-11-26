import tkinter as tk

root = tk.Tk()
root.geometry('320x240')

def callback():
    print('Click')

top_panel = tk.Label(root, text='Song Title', fg='green', background='black', height=2, width=45)
#mid_panel = tk.Label(root, text='Test', background='blue', height=2)

top_panel.grid(row=0, column=0, columnspan=4, sticky='w')
#mid_panel.grid(row=1, column=0)

b1 = tk.Button(root, height=6, width=10, text='Stop', command=callback)
b2 = tk.Button(root, height=6, width=10, text="Play/Pause")
b3 = tk.Button(root, height=6, width=10, text="Prev")
b4 = tk.Button(root, height=6, width=10, text="Next")

mode_up = tk.Button(root, height=3, width=10, text='Mode Up')
mode_down = tk.Button(root, height=3, width=10, text='Mode Down')
music_btn= tk.Button(root, height=6, width=10, text="Music")
streams_btn = tk.Button(root, height=6, width=10, text="Streams")
podcasts_btn = tk.Button(root, height=6, width=10, text='Podcasts')

b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)
b4.grid(row=2, column=3)

mode_up.grid(row=3, column=3, sticky='n')
mode_down.grid(row=3, column=3, sticky='s')
music_btn.grid(row=3, column=0)
streams_btn.grid(row=3, column=1)
podcasts_btn.grid(row=3, column=2)
