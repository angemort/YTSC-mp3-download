#!/usr/bin/env python

#
# yt-mp3-download
# copyright 2020 AngeMort
# 09/03/2020
#
import os
import time
import subprocess

from pytube import Playlist, YouTube

def format(filename):
    filtre = { ' ','   ','?' }
    for fil in filtre:
        filename.replace(fil, '-')
    return filename

def run_playlist(pl):
    # download each item in the list
    for video in pl:
        # converts the link to a YouTube object
        yt = YouTube(video)
        # takes first stream; since ffmpeg will convert to mp3 anyway
        music = yt.streams.first()

        # gets the filename of the first audio stream
        default_filename = format(music.default_filename)
        # clean text
        print("Downloading " + default_filename + "...")
        
        # downloads first audio stream
        yt.streams.first().download(filename=default_filename)
        time.sleep(1)
        
        # creates mp3 filename for downloaded file
        new_filename = default_filename[0:-3] + "mp3"
        print("### Converting to MP3 ###")
        # Converting
        ffmpeg = ('ffmpeg -i '+default_filename[0:-4] + "mp4.mp4"+' '+new_filename)
        subprocess.call(ffmpeg, shell=True)

    print("Download finished.")

def run_single(yt):
    music = yt.streams.first()
    default_filename = music.default_filename.replace(' ', '-').replace('   ', '-')
    print("Downloading " + default_filename + "...")
    yt.streams.first().download(filename=default_filename)
    time.sleep(1)
    new_filename = default_filename[0:-3] + "mp3"
    print("### Converting to MP3 ###")
    # Converting
    ffmpeg = ('ffmpeg -i ' + default_filename[0:-4] + 'mp4.mp4 ' + new_filename)
    print(ffmpeg)
    subprocess.call(ffmpeg, shell=True)

    print("Download finished.")

if __name__ == "__main__":
    options = input("[1] Playlist - [2] Single: ")
    if options == "1":
        url = input("Please enter the url of the playlist you wish to download: ")
        pl = Playlist(url) #"https://www.youtube.com/playlist?list=PLynhp4cZEpTbRs_PYISQ8v_uwO0_mDg_X"
        print('Number of videos in playlist: %s' % len(pl.video_urls))
        run_playlist(pl)
    elif options == "2":
        url = input("Please enter the url: ")
        yt = YouTube(url)
        run_single(yt)


