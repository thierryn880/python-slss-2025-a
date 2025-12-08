# Intro to Sort
# Author: Thierry Narcisse
# 4 December

import csv

# Sorting Algorithms
# The code below uses linear search to find songs from a particular artist
# We're going to sort the results using Selection Sort
#     * implement basic version
#     * implement sort with songs based on YouTube views in descending order


def selection_sort(l: list[int], ascending=True) -> list[int]:
    """Sorts a given list using selection sort

    Params:
        l - list of nums to be sorted
        ascending - True if order is ascending

    Returns:
        a sorted list"""

    num_items = len(l)
    for i in range(num_songs):

        candidate_val = helper_spotify.string_to_num(songs[i][col])
        candidate_index = i

        for j in range(i + 1, num_songs):
            if ascending:
             this_song_val = helper_spotify.string_to_num(songs[j][col])
             if this_song_val < candidate_val
                candidate_val = this_song_val
                candidate_index = j
        else:his_song_val < candidate_val
        candidate_val = this_song_val
        candidate_index = j

            # Get songs from an artist

            # Use Selection Sort to sort songs
            # # Starting at the beginning of the list
            # Set this value to the candidate's value
            # Set this index to the candidate's index
                # Check the rest of the list
                # If ascending
                    # If this value is lower than candidate
                        # Set candidate val to this val
                        # Set candidate idx to this idx
                # If not ascending
                    # If this val is higher than candidate
                        # Set candidate val to this val
                        # Set candidate idx to this idx


    if ascending:
        # start at the beginning of the list
        for i in range(num_items):
            candidate_num = l[i]
            candidate_index = i

            #  check rest of the list
            for j in range(i + 1, num_items):
                if ascending:
                    if l[j] < candidate_num:
                        candidate_num = l[j]
                        candidate_index = j

                else:
                    if l[j] > candidate_num:
                        candidate_num = l[j]
                        candidate_index = j

            # swap current index with the lowest
            l[i], l[candidate_index] = l[candidate_index], l[i]

        return l

        def sort_songs(
            songs: list[list[str]], col: int, ascending=True
        ) -> list[list[str]]:
            """Sort a list of spotify songs in place

            Params:
                songs - list of songs
                col - column to sort
                ascending - will sort ascending by default

            Returns: sorted list"""



if __name__ == "__main__":
    helper_spotify.songs_by_artist("data/spotify2024-day1")
    taylors_songs = sort_songs("taylors_songs , 11, ascending=False")
