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
song_list=['SampleAudio.mp3','SampleAudio.mp3']
counter = 0

def main_menu():
    # os.system('clear')
    # Show menu #
    print(30 * '-')
    print("   M A I N - M E N U")
    print(30 * '-')
    print("1. Music")
    print("2. Podcasts")
    print("3. Streams")
    print("\n0. Exit")
    print(30 * '-')
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
    songs = os.listdir('music')  # List of songs in music folder
    global counter
    for song in songs:
        if len(songs) < 0:
            print('No songs in music folder')
        else:
            counter += 1
            print(str(counter) + '. ' + song)



    elif ch == 's':


def play_opts():
    choice = input('\ns - Play/Pause\td - Next\ta - Previous\tw - Stop: ')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_play[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return

    # try:
    #     while player.is_playing():
    #         time.sleep(5)
    #         continue
    # except Exception:
    #     print('There was an issue')

    # choice = raw_input('\nP - Play\tN - Next\tP - Previous\tS - Stop: ')
    # ch = choice.lower()
    # if ch == '':
    #     menu_actions['main_menu']()
    # else:
    #     try:
    #         for song in songs:
    #             vlc_play('music/' + song)
    #     except Exception:
    #         print "There was an exception.\n"
    #         menu_actions['main_menu']()
    # return


# Menu 1
def podcasts():
    print("Podcasts...\n")
    print("9. Back")
    print("0. Quit")
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


# Menu 1
def streams():
    print("Streams...\n")
    print("9. Back")
    print("0. Quit")
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


# def vlc_play(song):
#     '''Play audio from selected directory'''
#     instance = vlc.Instance()
#     player = instance.media_player_new()
#     media = instance.media_new(song)
#     player.set_media(media)
#     player.play()
#     time.sleep(1)  # Give time to get going
#     while True:
#         state = player.get_state()
#         if state not in playing:
#             break
#         continue


def vlc_play_pause(song):
    player = vlc.MediaPlayer(song)
    player.play()
    # player.get_instance()
    player = vlc.MediaPlayer('music/' + songs[0])
    print('playing ' + songs[0])
    player.play()
    time.sleep(1)
    while player.is_playing():
        print(player.get_state())
        time.sleep(2)
        continue


def sub_menu():
    print("9. Back")
    print("0. Quit")
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


# Back to main menu
def back():
    menu_actions['main_menu']()


# Exit program
def exit():
    sys.exit()


# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': music,
    '2': podcasts,
    '9': back,
    '0': exit,
}

menu_play = {
    's': vlc_play_pause,
    'd': vlc_play_next,
    'a': vlc_play_prev,
    'w': vlc_stop,
}

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
