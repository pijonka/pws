import json
import re 
# import the billboard dataset
# the dataset should be formatted as such for the Python script to work:
# (in the same order as the directories in billboard [
#   {
#       "song": billboard song,
#       "chart_date": billboard chart date,
#       etc for each billboard variable
#   },
#   *
# ]

# dataset to read
with open(R"C:\Users\pijonka\Documents\PWS\data\q3\dataset-20thcent-mcgill-billboard\billboard-2.0-index.json") as f:
    READ_DATASET = json.load(f)

# new dataset to write to
write_dataset = []

# define hardcoded I - V - IV - iv chord progression object, with strings of the progression in each key
FORMS_OF_CHORD_PROG = {
    "c_maj": ["C:maj", "G:maj", "F:maj", "F:min"],
    "g_maj": ["G:maj", "D:maj", "C:maj", "C:min"],
    "d_maj": ["D:maj", "A:maj", "G:maj", "G:min"],
    "a_maj": ["A:maj", "E:maj", "D:maj", "D:min"],
    "e_maj": ["E:maj", "B:maj", "A:maj", "A:min"],
    "b_maj": ["B:maj", "F#:maj", "E:maj", "E:min"],
    "f_maj": ["F:maj", "C:maj", "Bb:maj", "Bb:min"],
    "bb_maj": ["Bb:maj", "F:maj", "Eb:maj", "Eb:min"],
    "eb_maj": ["Eb:maj", "Bb:maj", "Ab:maj", "Ab:min"],
    "ab_maj": ["Ab:maj", "Eb:maj", "Db:maj", "Db:min"],
    "db_maj": ["Db:maj", "Ab:maj", "Gb:maj", "Gb:min"],
    "gb_maj": ["Gb:maj", "Db:maj", "Cb:maj", "Cb:min"],
    "f_sharp_maj": ["F#:maj", "C#:maj", "B:maj", "B:min"],
    "c_sharp_maj": ["C#:maj", "G#:maj", "F#:maj", "F#:min"],
}

LIST_REMOVE_OUT_STRING = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "(",
    ")",
    "/"
    ".",
    " ",
]

# extracts strings of chord data out of majmin.lab files 
def parse_lab_chords(song_chords: str):
    song_chords_per_line = song_chords.splitlines()
    chord_list = [line.strip().split()[-1] for line in song_chords_per_line if line.strip()]
    return chord_list

# for every element in dataset (iterate, it's an array)
for element in READ_DATASET:
    use_of_chord_prog_counter = 0

    #   open the majmin.lab file corresponding to the id of this element
    try:
        with open(rf"C:\Users\pijonka\Documents\PWS\data\q3\dataset-20thcent-mcgill-billboard\LAB-McGill-Billboard\{element["id"].zfill(4)}\majmin.lab") as f:
            unmod_song_chords = f.read()
    except:
        continue

    # clean chords list
    song_chords_list = parse_lab_chords(unmod_song_chords)
    
    #   for every key-value pair in FORMS_OF_CHORD_PROG literal:   
    for key, list_of_chords_in_prog in FORMS_OF_CHORD_PROG.items():
        # index / position of iteration in song chord list
        song_chord_i = 0

        # for every chord in the song
        while song_chord_i < len(song_chords_list):
            # if the current point on the song chord list is the first chord of the list
            if song_chords_list[song_chord_i] == list_of_chords_in_prog[0]:
                base_song_chord_i = song_chord_i 
                stack_chord_i = 1
                # THIS MEANS SECOND CHORD IN CHORD PROG LIST (this variable holds the chord in the chord progression the loop is currently trying to find
                chord_of_chord_prog_i = 1 
                while True:
                    if base_song_chord_i + stack_chord_i != len(song_chords_list):
                        # if the chord the stack pointer is pointing to (usually the next chord) is equal to the chord the base pointer is on (the "current" chord)
                        if song_chords_list[base_song_chord_i + stack_chord_i] == song_chords_list[base_song_chord_i]:
                            # it's the same chord, try to look at one further
                            stack_chord_i += 1
                            # LOOP
                        # if the chord the stack pointer is pointing to (usually the next chord) is equal to the next chord in the chord progression (e.g. if base = I and stack = V)
                        elif song_chords_list[base_song_chord_i + stack_chord_i] == list_of_chords_in_prog[chord_of_chord_prog_i]:
                            # we have found a consequent chord in the progression!
                            chord_of_chord_prog_i += 1

                            # move the base pointer to the stack pointer, such that base saves the "current" chord
                            base_song_chord_i += stack_chord_i

                            # if this is the last chord in the progression
                            if chord_of_chord_prog_i == 4:
                                # INSTANCE OF CHORD PROGRESSION SUCCESSFULLY FOUND!
                                use_of_chord_prog_counter += 1

                                # set the index here so that it doesn't double check the same chord
                                song_chord_i = base_song_chord_i
                                
                                chord_of_chord_prog_i = 0

                                # stop looping
                                break

                            stack_chord_i = 1
                            # LOOP
                        else: # if the stack's chord is nothing special
                            song_chord_i += 1
                            # stop looping
                            break # eradicate the pointers completely and just keep moving normally
                    else:
                        song_chord_i = len(song_chords_list)
                        break # stop looping
            else: # if the current point is not the first chord of chord progression
                # just keep iterating through it
                song_chord_i += 1

    #   append to the dataset the use_of_chord_prog_counter
    write_dataset.append({
        "title": element["title"],
        "artist": element["artist"],
        "popularity": (100 - int(element["peak_rank"])) * int(element["weeks_on_chart"]),
        "use_of_chords": use_of_chord_prog_counter
        })

# write to a new dataset file the contents of write_dataset
with open(fr"C:\Users\pijonka\Documents\PWS\data\q3\pi-mcgill.json", "w") as f:
    json.dump(write_dataset, f, indent=4)
    
# print(write_dataset)

# the dataset will look as such:
# [
#   "title": csv.title
#   "popularity": (100 - csv.peak_rank) * csv.weeks_on_chart
#   "use_of_chords": use_of_chord_prog_counter
# ]