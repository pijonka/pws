import json
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
    read_dataset = json.load(f)

# new dataset to write to
write_dataset = []

# define hardcoded I - V - IV - iv chord progression object, with strings of the progression in each key
FORMS_OF_CHORD_PROG = {
    "c_maj": "| C:maj | G:maj | F:maj | F:min |"
}

# for every element in dataset (iterate, it's an array)
for element in read_dataset:
    use_of_chord_prog_counter = 0

    #   open the os directory billboard-2.0-salami_chords/[000{element.array location} but remove zeroes accordingly such that it is always four integers]
    #   open the salami_chords.txt file
    try:
        with open(rf"C:\Users\pijonka\Documents\PWS\data\q3\dataset-mcgill\McGill-Billboard\{element["id"].zfill(4)}\salami_chords.txt") as f:
            song_chords = f.read()
    except:
        continue

    #   for every key-value pair in FORMS_OF_CHORD_PROG literal:   
    for key, val in FORMS_OF_CHORD_PROG.items():
        # if any substring of the song_chords string is equal to the value of this key
            # add 1 to the use_of_chord_prog_conuter
            use_of_chord_prog_counter = song_chords.count(val)
        
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
    
print(write_dataset)

# the dataset will look as such:
# [
#   "title": csv.title
#   "popularity": (100 - csv.peak_rank) * csv.weeks_on_chart
#   "use_of_chords": use_of_chord_prog_counter
# ]