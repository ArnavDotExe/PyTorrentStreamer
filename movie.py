
from tabulate import tabulate
import sys
import subprocess


class Movie:
    def __init__(self, movie_list):
        self.table = []
        self.table.append(['Index', 'Name', 'Year', 'Description', 'Size', 'Quality seed peers'])
        self.movies = []
        self.count = 1
        self.valid_index = True
        self.download = False
        self.movie_list = movie_list


    def display_movies(self):
        for movie in self.movie_list['data']['movies']:
            torrentInfo = movie['torrents']
            quality = ""

            for ti in torrentInfo:
                quality += f"{ti['quality']}  {ti['seeds']}  {ti['peers']}"

            tableRow = [self.count, movie['title'], movie['year'], movie['summary'][:50], torrentInfo[0]['size'], quality]
            self.table.append(tableRow)
            self.count += 1
            self.movies.append(movie)

        print(tabulate(self.table, tablefmt='fancy_grid'))

    
    def handle_movie_stream(self, user_choice):
        if int(user_choice) <= len(self.movies):
            self.valid_index = False
            user_selected_movie = self.movies[int(user_choice) - 1]
            torrentInfo = user_selected_movie['torrents']
            print("\n")
            print("Available movie quality => ")

            if len(torrentInfo) > 1:
                for ti in torrentInfo:
                    quality_count = 1
                    for ti in torrentInfo:
                        print(f"{quality_count}. {ti['quality']}")
                        quality_count += 1

            print("Please enter the index of the quality which you'd like to stream / download.")

            selected_quality = input()
            selected_quality_int = quality_count - 2

            try:
                selected_quality_int = int(selected_quality) - 1
            except:
                print("Invalid quality figure")
                print("selected_quality")

            if selected_quality_int >= quality_count:
                selected_quality_int = quality_count - 1

            magnet = f'magnet:?xt=urn:btih:{torrentInfo[selected_quality_int]["hash"]}&dn={user_selected_movie["title"]}&tr=udp://open.demonii. com:1337/announce&tr=udp://tracker.openbittorrent.com:80&tr=udp://tracker.coppersurfer.tk:6969&tr=udp://glotorrents.pw:6969/ announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://torrent.gresille.org:80/announce&tr=udp://p4p.arenabg.com:13378 tr=udp://tracker.leechers-paradise.org:6969'
            self.stream(magnet)

        else:
            magnet = f'magnet:?xt=urn:btih:{torrentInfo[0]["hash"]}&dn={user_selected_movie["title"]}&tr=udp://open.demonii.com:1337/announce& tr=udp://tracker.openbittorrent.com:80&tr=udp://tracker.coppersurfer.tk:6969&tr=udp://glotorrents.pw:6969/announce&tr=udp://tracker. opentrackr.org:1337/announce&tr=udp://torrent.gresille.org:80/announce&tr=udp://p4p.arenabg.com:1337&tr=udp://tracker.leechers-paradise.org:6969'
            self.stream(magnet)

    def stream(self, magnet_link):
        if sys.platform.startswith('linux'):
            cmd = []
            cmd.append('webtorrent')
            cmd.append(magnet_link)
            if not self.download:
                print("Streaming...")
                cmd.append('--vlc')
            subprocess.call(cmd)

        elif sys.platform.startswith('win32'):
            cmd = ""
            cmd += "webtorrent download "
            cmd = cmd + '"{}"'.format(magnet_link)
            if not self.download:
                print("Streaming....")
                cmd+= ' ---vlc'
            subprocess.call(cmd, shell=True)
