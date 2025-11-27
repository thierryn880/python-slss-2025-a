# Data Analysis
# Author: Thierry Narcisse
#
import csv

# Analyse the data provided in class


def main():

    artist = "Kendrick Larmar"
    track_col = 0
    artist_col = 2
    yt_views_col = 11
    tik_view_col = 15


    with open("data/spotify2024.csv") as f:
        _ = f.readline()

        r = csv.reader(f)

        kendrick_songs = []
        for info in r:
                 if artist == info[artist_col]:
                     kendrick_songs.append(info)

             # print how many songs are in the list
             print(f"Number of Kendrick Songs: {len(kendrick_songs)}")

             #track name     Youtube views    titok views
             # i like frogs   100,250,132     1,000,001]
             #
             #
        print("Track Name\t\tYouTube Views\t\tTikTok Views") # header

        for song in kendrick_songs:
                        current_track = song[track_col]
                        current_ytviews = song[yt_views_col]
                        current_tiktokviews = song[tiktok_views_col]

                        print(f"{current_track}\t\t{current_ytviews}\t\t{current_tiktokviews}")


if __name__ == "__main__":
         main()
