import requests
import subprocess
import json
import sys
import pyfiglet


def supermain(folder):

 
    def banne32r():
        ascii_banner = pyfiglet.figlet_format("Welcome Sir")

        prints("created by mr Sasank")
        print(ascii_banner)
    def main():
        speak('Enter the movie name:')
        movie_name = input("Enter the movie name:\n")
        print(f"Searching for {movie_name}")
        # speak()
        base_url = f"https://api.sumanjay.cf/torrent/?query={movie_name}"
        torrent_results = requests.get(url=base_url).json()
        index = 1
        magnet = []
        for result in torrent_results:
            if 'movie' in result['type'].lower():
                print(index, ") ", result['name'], "-->", result['size'])
                index += 1
                magnet.append(result['magnet'])
        if magnet:
            print('Enter the index of the movie which you want to stream')
            choice = int(
                input("Enter the index of the movie which you want to stream\n"))
           
            try:
                magnet_link = magnet[choice-1]
                download = False  # Default is streaming
                print('Press 1 to stream or Press 2 to download the movie')

                stream_choice = int(
                    input("Press 1 to stream or Press 2 to download the movie\n"))
                if stream_choice == 2:
                    download = True
                    # print(magnet_link)
                webtorrent_stream(magnet_link, download)
                # exit()
            except IndexError:
                print("Incorrect Index entered")
        else:
            print(f"No results found for {movie_name}")
            exit()

    # Handle Streaming


    def webtorrent_stream(magnet_link: str, download: bool):
        cmd = []
        cmd.append("webtorrent")
        cmd.append(magnet_link)
        if not download:
            cmd.append('-- vlc')
        else:
            cmd.append(f"-- out {folder}" )    

        if sys.platform.startswith('linux'):
            subprocess.call(cmd)
        elif sys.platform.startswith('win32'):
            subprocess.call(cmd, shell=True)
    try:
        main()        
    except Exception as e:
        print("movie not found try after sometime")    





supermain()





















