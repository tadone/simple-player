#! /usr/bin/python3
# import external libraries
# import wx # 2.8
import vlc

# import standard libraries
import os
import sys
import random
import time
from itertools import count
# def rnd_mp3(dir):
#     randomfile = random.choice(os.listdir("/home/pi/music/"))
# 	file = ' /home/pi/music/'+ randomfile
# 	os.system ('mplayer' + file)
counter = 0
streams_file = 'streams/streams.txt'


def main_menu():
    # os.system('clear')
    # Show menu #
    print(40 * '-')
    print("          M A I N - M E N U")
    print(40 * '-')
    print("1. Music")
    print("2. Podcasts")
    print("3. Streams")
    print("\n0. Exit")
    print(40 * '-')
    choice = input('Enter your choice [1-3] : ')
    exec_menu(choice)

    return


# Execute menu
def exec_menu(choice):
    # os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return


# Menu 1
def music():
    print("Music...\n")
    songs = [os.path.join('music', f) for f in os.listdir('music')]  # List of songs in music folder
    songs.sort()  # Sort the list
    # random_songs = songs
    # random.shuffle(random_songs)  # Randomize songs in this list
    global counter
    for song in songs:
        if len(songs) < 0:
            print('No songs in music folder')
        else:
            counter += 1
            print(str(counter) + '. ' + song)
    # VLC Handler
    Instance = vlc.Instance()
    vlc_player = Instance.media_player_new()
    # Music Menu
    print('\n' + 40 * '-')
    # is_random = input('Shuffle? [y/N]: ')
    # if is_random.lower() == 'y':
    #     print('Shuffle ON')
    #     rand = True
    # else:
    #     print('Shuffle OFF')
    #     rand = False
    # choice = input('(P)lay/Pause\t9. Back\t0. Exit\n->> ')
    # ch = choice.lower()
    # if ch == 'p' and not vlc_player.is_playing():
    # num = random.randint(0, len(songs) - 1)
    # if rand:
    #     vlc_player.set_mrl(random_songs[x])
    #     print('\nPlaying {}\n'.format(random_songs))
    # else:
    #     vlc_player.set_mrl(songs[x])
    #     print('\nPlaying {}\n'.format(songs))
    x = 0
    vlc_player.set_mrl(songs[x])
    rand = False
    while True:
        choice = input('(S) Shuffle * (P)lay/Pause * (N)ext Song * P(r)evious Song * (X) Stop * (9) Back * (0) Exit: ')
        ch = choice.lower()
        if ch == 's' and not rand:
            rand = True
            random.shuffle(songs)
            print('Shuffle ON')
        elif ch == 's' and rand:
            rand = False
            songs.sort()
            print('Shuffle OFF')
        elif ch == 'p' and not vlc_player.is_playing():
            vlc_player.play()
            print('Playing...')
        elif ch == 'p' and vlc_player.is_playing():
            vlc_player.pause()
            print('Pausing...')
        elif ch == 'n':
            x += 1
            if x > len(songs) - 1 and not rand:
                x = 0
            elif x > len(songs) - 1 and rand:
                x = 0
                random.shuffle(songs)
                print('Reshuffling Songs...')
            vlc_player.set_mrl(songs[x])
            print('Playing Next: {}'.format(songs[x]))
            vlc_player.play()
        elif ch == 'r':
            x -= 1
            if x < 0 and not rand:
                x = 0
            elif x < 0 and rand:
                x = 0
                random.shuffle(songs)
                print('Reshuffling Songs...')
                time.sleep(0.2)
            vlc_player.set_mrl(songs[x])
            print('Playing Next: {}'.format(songs[x]))
            vlc_player.play()
        elif ch == 'x':
            vlc_player.stop()
        else:
            exec_menu(ch)
            print('Wrong choice...')
        continue
    # else:
    #     exec_menu(ch)


# Menu 1
def podcasts():
    print("Podcasts...\n")
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return


# Menu 1
def streams():
    print("Streams...\n")
    try:
        with open(streams_file, 'r') as f:
            streams = [x.strip('\n') for x in f.readlines()]
    except FileNotFoundError:
        print('File Not Found')
    for stream in streams:
        print(stream)
    random_streams = streams
    random.shuffle(random_streams)
    choice = input('(P)lay/Pause\t9. Back\t0. Exit\n->> ')
    ch = choice.lower()

    exec_menu(ch)
    return

# def vlc_player(media)
# i = vlc.Instance() # New VLC instance
# m = i.media_new('http stream') # Set the mp3 http server URL
# p = m.player_new_from_media() # Create a player for the stream
# p.play() # Start playing the stream
# m.parse() # Synchronous parse of the stream
# song = m.get_meta(12) # Get song title and artist (Artist - Title)


def sub_menu():
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return


# Back to main menu
def back():
    menu_actions['main_menu']()


# Exit program
def exit():
    sys.exit()


# Menu definition dictionary
menu_actions = {
    'main_menu': main_menu,
    '1': music,
    '2': podcasts,
    '3': streams,
    '9': back,
    '0': exit,
}

# menu_play = {
#     's': vlc_play_pause,
#     'd': vlc_play_next,
#     'a': vlc_play_prev,
#     'w': vlc_stop,
# }

# instance=vlc.Instance()
# for song in song_list:
#     player=instance.media_player_new()
#     media=instance.media_new(song)
#     print(song)
#     media.get_mrl()
#     player.set_media(media)
#     player.play()
#     playing = set([1,2,3,4])
#     time.sleep(1) #Give time to get going
#     duration = player.get_length() / 1000
#     mm, ss = divmod(duration, 60)
#     print("Playing", song, "Length:", "%02d:%02d" % (mm,ss))
#     while True:
#         state = player.get_state()
#         if state not in playing:
#             break
#         continue


# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
