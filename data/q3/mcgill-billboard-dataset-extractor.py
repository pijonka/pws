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
with open(R"C:\Users\pijonka\Documents\PWS\data\q3\dataset-mcgill\billboard-2.0-index.json") as f:
    READ_DATASET = json.load(f)

# new dataset to write to
write_dataset = []

# define hardcoded I - V - IV - iv chord progression object, with strings of the progression in each key
FORMS_OF_CHORD_PROG = {
    "c_maj": "C:maj|G:maj|F:maj|F:min",
    "g_maj": "G:maj|D:maj|C:maj|C:min",
    "d_maj": "D:maj|A:maj|G:maj|G:min",
    "a_maj": "A:maj|E:maj|D:maj|D:min",
    "e_maj": "E:maj|B:maj|A:maj|A:min"
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
    ".",
    " ",
]

# formats salami_chords.txt in a proper format;
# TODO: currently does not correctly format "X:7" chords
def parse_salami_chords(song_chords: str):
    song_chords_in_lines = song_chords.splitlines()
    clean_chords = []
    for line in song_chords_in_lines:
        line = line.strip()
        bars_in_line = re.findall(r"\|([^\|]*.*)\|", line)
        clean_chords.extend(bars_in_line)

    clean_chords_string = "|".join(clean_chords)
    for char in LIST_REMOVE_OUT_STRING:
        clean_chords_string = clean_chords_string.replace(char, "")

    return clean_chords_string

# for every element in dataset (iterate, it's an array)
for element in READ_DATASET:
    use_of_chord_prog_counter = 0

    #   open the salami_chords.txt file corresponding to the id of this element
    try:
        with open(rf"C:\Users\pijonka\Documents\PWS\data\q3\dataset-mcgill\McGill-Billboard\{element["id"].zfill(4)}\salami_chords.txt") as f:
            unmod_song_chords = f.read()
    except:
        continue

    # clean chords formatted to work with the finder thing
    song_chords = parse_salami_chords(unmod_song_chords)
    
    #   for every key-value pair in FORMS_OF_CHORD_PROG literal:   
    for key, val in FORMS_OF_CHORD_PROG.items():
        # if any substring of the song_chords string is equal to the value of this key
            # add 1 to the use_of_chord_prog_conuter
            use_of_chord_prog_counter += song_chords.count(val)
        
    #   append to the dataset the use_of_chord_prog_counter
    write_dataset.append({
        "title": element["title"],
        "artist": element["artist"],
        "popularity": (100 - int(element["peak_rank"])) * int(element["weeks_on_chart"]),
        "use_of_chords": use_of_chord_prog_counter
        })

# write to a new dataset file the contents of write_dataset
with open("pi-mcgill.json", "w") as f:
    json.dump(write_dataset, f, indent=4)
    
# print(write_dataset)

# the dataset will look as such:
# [
#   "title": csv.title
#   "popularity": (100 - csv.peak_rank) * csv.weeks_on_chart
#   "use_of_chords": use_of_chord_prog_counter
# ]