import json
import chord_analyzer
import chord_parsers

with open(R"C:\Users\pijonka\Documents\PWS\data\q3\dataset-20thcent-mcgill-billboard\billboard-2.0-index.json") as f:
    READ_DATASET = json.load(f)

FORMS_OF_CHORD_PROGS = {
    "I - V - IV - IV": {
        
    },
    "I - V - IV - iv": {

    },
    "I - V - iv - iv": {

    },
    "I - v - iv - iv": {

    },
    "i - v - iv - iv": {

    },
    "I_V_vi_IV": {

    },
    "I_V_vi_iii_IV": {

    },
    "vi_V_IV_V": {

    }
}


for element in READ_DATASET:
    #   open the majmin.lab file corresponding to the id of this element
    try:
        with open(rf"C:\Users\pijonka\Documents\PWS\data\q3\dataset-20thcent-mcgill-billboard\LAB-McGill-Billboard\{element["id"].zfill(4)}\majmin.lab") as f:
            unmod_song_chords = f.read()
    except:
        continue

    # clean chords list
    song_chords_list = chord_parsers.parse_lab_chords(unmod_song_chords)

    use_of_chord_prog_counter = chord_analyzer.count_chord_progs_ignore_reps(song_chords_list, )