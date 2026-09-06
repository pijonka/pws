import json
import chord_analyzer
import chord_parsers
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


# for every element in dataset (iterate, it's an array)
for element in READ_DATASET:
    #   open the majmin.lab file corresponding to the id of this element
    try:
        with open(rf"C:\Users\pijonka\Documents\PWS\data\q3\dataset-20thcent-mcgill-billboard\LAB-McGill-Billboard\{element["id"].zfill(4)}\majmin.lab") as f:
            unmod_song_chords = f.read()
    except:
        continue

    # clean chords list
    song_chords_list = chord_parsers.parse_lab_chords(unmod_song_chords)

    use_of_chord_prog_counter = chord_analyzer.count_chord_progs_ignore_reps(song_chords_list, FORMS_OF_CHORD_PROG)

    #   append to the dataset the use_of_chord_prog_counter
    write_dataset.append({
        "title": element["title"],
        "artist": element["artist"],
        "popularity": (100 - int(element["peak_rank"])) * (int(element["weeks_on_chart"])),
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