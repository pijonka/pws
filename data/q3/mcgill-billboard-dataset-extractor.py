# import the csv dataset
# the dataset should be formatted as such for the Python script to work:
# (in the same order as the directories in billboard [
#   {
#       "song": csv song,
#       "chart_date": csv chart date,
#       etc for each csv variable
#   },
#   *
# ]

# write_dataset = csv dataset

# define hardcoded I - V - IV - iv chord progression object, with strings of the progression in each key
FORMS_OF_CHORD_PROG = {
    "c_maj": "| C:maj | G:maj | F:maj | F:min |"
}

# for every element in dataset (iterate, it's an array)
    #   use_of_chord_prog_counter = 0

    #   open the os directory billboard-2.0-salami_chords/[000{element.array location} but remove zeroes accordingly such that it is always four integers]
    #   open the salami_chords.txt file
    #   song_chords = the contents of salami_chords.txt as a string

    #   for every key-value pair in FORMS_OF_CHORD_PROG literal:   
        # if any substring of the song_chords string is equal to the value of this key
            # add 1 to the use_of_chord_prog_conuter
    #   append to the csv dataset the use_of_chord_prog_counter

# write to a new dataset file the contents of write_dataset

# the dataset will look as such:
# [
#   "song": csv.song
#   "popularity": (100 - csv.peak_rank) * csv.weeks_on_chart
# ]