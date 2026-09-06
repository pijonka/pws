import json
import chord_analyzer
import chord_parsers

with open(R"C:\Users\pijonka\Documents\PWS\data\q3\dataset-20thcent-mcgill-billboard\billboard-2.0-index.json") as f:
    READ_DATASET = json.load(f)

# WARNING: this dictionary is AI-generated (by Claude) and not completely verified. The objects of each chord progression could contain faulty chords that do not correspond to the roman numeral chords.
FORMS_OF_CHORD_PROGS = {
    "I - V - IV - IV": {
        "c_maj": ["C:maj", "G:maj", "F:maj", "F:maj"],
        "g_maj": ["G:maj", "D:maj", "C:maj", "C:maj"],
        "d_maj": ["D:maj", "A:maj", "G:maj", "G:maj"],
        "a_maj": ["A:maj", "E:maj", "D:maj", "D:maj"],
        "e_maj": ["E:maj", "B:maj", "A:maj", "A:maj"],
        "b_maj": ["B:maj", "F#:maj", "E:maj", "E:maj"],
        "f_maj": ["F:maj", "C:maj", "Bb:maj", "Bb:maj"],
        "bb_maj": ["Bb:maj", "F:maj", "Eb:maj", "Eb:maj"],
        "eb_maj": ["Eb:maj", "Bb:maj", "Ab:maj", "Ab:maj"],
        "ab_maj": ["Ab:maj", "Eb:maj", "Db:maj", "Db:maj"],
        "db_maj": ["Db:maj", "Ab:maj", "Gb:maj", "Gb:maj"],
        "gb_maj": ["Gb:maj", "Db:maj", "Cb:maj", "Cb:maj"],
        "f_sharp_maj": ["F#:maj", "C#:maj", "B:maj", "B:maj"],
        "c_sharp_maj": ["C#:maj", "G#:maj", "F#:maj", "F#:maj"],
    },
    "I - V - IV - iv": {
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
    },
    "I - V - iv - iv": {
        "c_maj": ["C:maj", "G:maj", "F:min", "F:min"],
        "g_maj": ["G:maj", "D:maj", "C:min", "C:min"],
        "d_maj": ["D:maj", "A:maj", "G:min", "G:min"],
        "a_maj": ["A:maj", "E:maj", "D:min", "D:min"],
        "e_maj": ["E:maj", "B:maj", "A:min", "A:min"],
        "b_maj": ["B:maj", "F#:maj", "E:min", "E:min"],
        "f_maj": ["F:maj", "C:maj", "Bb:min", "Bb:min"],
        "bb_maj": ["Bb:maj", "F:maj", "Eb:min", "Eb:min"],
        "eb_maj": ["Eb:maj", "Bb:maj", "Ab:min", "Ab:min"],
        "ab_maj": ["Ab:maj", "Eb:maj", "Db:min", "Db:min"],
        "db_maj": ["Db:maj", "Ab:maj", "Gb:min", "Gb:min"],
        "gb_maj": ["Gb:maj", "Db:maj", "Cb:min", "Cb:min"],
        "f_sharp_maj": ["F#:maj", "C#:maj", "B:min", "B:min"],
        "c_sharp_maj": ["C#:maj", "G#:maj", "F#:min", "F#:min"],
    },
    "I - v - iv - iv": {
        "c_maj": ["C:maj", "G:min", "F:min", "F:min"],
        "g_maj": ["G:maj", "D:min", "C:min", "C:min"],
        "d_maj": ["D:maj", "A:min", "G:min", "G:min"],
        "a_maj": ["A:maj", "E:min", "D:min", "D:min"],
        "e_maj": ["E:maj", "B:min", "A:min", "A:min"],
        "b_maj": ["B:maj", "F#:min", "E:min", "E:min"],
        "f_maj": ["F:maj", "C:min", "Bb:min", "Bb:min"],
        "bb_maj": ["Bb:maj", "F:min", "Eb:min", "Eb:min"],
        "eb_maj": ["Eb:maj", "Bb:min", "Ab:min", "Ab:min"],
        "ab_maj": ["Ab:maj", "Eb:min", "Db:min", "Db:min"],
        "db_maj": ["Db:maj", "Ab:min", "Gb:min", "Gb:min"],
        "gb_maj": ["Gb:maj", "Db:min", "Cb:min", "Cb:min"],
        "f_sharp_maj": ["F#:maj", "C#:min", "B:min", "B:min"],
        "c_sharp_maj": ["C#:maj", "G#:min", "F#:min", "F#:min"],
    },
    "i - v - iv - iv": {
        "c_maj": ["C:min", "G:min", "F:min", "F:min"],
        "g_maj": ["G:min", "D:min", "C:min", "C:min"],
        "d_maj": ["D:min", "A:min", "G:min", "G:min"],
        "a_maj": ["A:min", "E:min", "D:min", "D:min"],
        "e_maj": ["E:min", "B:min", "A:min", "A:min"],
        "b_maj": ["B:min", "F#:min", "E:min", "E:min"],
        "f_maj": ["F:min", "C:min", "Bb:min", "Bb:min"],
        "bb_maj": ["Bb:min", "F:min", "Eb:min", "Eb:min"],
        "eb_maj": ["Eb:min", "Bb:min", "Ab:min", "Ab:min"],
        "ab_maj": ["Ab:min", "Eb:min", "Db:min", "Db:min"],
        "db_maj": ["Db:min", "Ab:min", "Gb:min", "Gb:min"],
        "gb_maj": ["Gb:min", "Db:min", "Cb:min", "Cb:min"],
        "f_sharp_maj": ["F#:min", "C#:min", "B:min", "B:min"],
        "c_sharp_maj": ["C#:min", "G#:min", "F#:min", "F#:min"],
    },
    "I - V - vi - IV": {
        "c_maj": ["C:maj", "G:maj", "A:min", "F:maj"],
        "g_maj": ["G:maj", "D:maj", "E:min", "C:maj"],
        "d_maj": ["D:maj", "A:maj", "B:min", "G:maj"],
        "a_maj": ["A:maj", "E:maj", "F#:min", "D:maj"],
        "e_maj": ["E:maj", "B:maj", "C#:min", "A:maj"],
        "b_maj": ["B:maj", "F#:maj", "G#:min", "E:maj"],
        "f_maj": ["F:maj", "C:maj", "D:min", "Bb:maj"],
        "bb_maj": ["Bb:maj", "F:maj", "G:min", "Eb:maj"],
        "eb_maj": ["Eb:maj", "Bb:maj", "C:min", "Ab:maj"],
        "ab_maj": ["Ab:maj", "Eb:maj", "F:min", "Db:maj"],
        "db_maj": ["Db:maj", "Ab:maj", "Bb:min", "Gb:maj"],
        "gb_maj": ["Gb:maj", "Db:maj", "Eb:min", "Cb:maj"],
        "f_sharp_maj": ["F#:maj", "C#:maj", "D#:min", "B:maj"],
        "c_sharp_maj": ["C#:maj", "G#:maj", "A#:min", "F#:maj"],
    },
    "I - V - vi - iii - IV": {
        "c_maj": ["C:maj", "G:maj", "A:min", "E:min", "F:maj"],
        "g_maj": ["G:maj", "D:maj", "E:min", "B:min", "C:maj"],
        "d_maj": ["D:maj", "A:maj", "B:min", "F#:min", "G:maj"],
        "a_maj": ["A:maj", "E:maj", "F#:min", "C#:min", "D:maj"],
        "e_maj": ["E:maj", "B:maj", "C#:min", "G#:min", "A:maj"],
        "b_maj": ["B:maj", "F#:maj", "G#:min", "D#:min", "E:maj"],
        "f_maj": ["F:maj", "C:maj", "D:min", "A:min", "Bb:maj"],
        "bb_maj": ["Bb:maj", "F:maj", "G:min", "D:min", "Eb:maj"],
        "eb_maj": ["Eb:maj", "Bb:maj", "C:min", "G:min", "Ab:maj"],
        "ab_maj": ["Ab:maj", "Eb:maj", "F:min", "C:min", "Db:maj"],
        "db_maj": ["Db:maj", "Ab:maj", "Bb:min", "F:min", "Gb:maj"],
        "gb_maj": ["Gb:maj", "Db:maj", "Eb:min", "Bb:min", "Cb:maj"],
        "f_sharp_maj": ["F#:maj", "C#:maj", "D#:min", "A#:min", "B:maj"],
        "c_sharp_maj": ["C#:maj", "G#:maj", "A#:min", "E#:min", "F#:maj"],
    },
    "vi - V - IV - V": {
        "c_maj": ["A:min", "G:maj", "F:maj", "G:maj"],
        "g_maj": ["E:min", "D:maj", "C:maj", "D:maj"],
        "d_maj": ["B:min", "A:maj", "G:maj", "A:maj"],
        "a_maj": ["F#:min", "E:maj", "D:maj", "E:maj"],
        "e_maj": ["C#:min", "B:maj", "A:maj", "B:maj"],
        "b_maj": ["G#:min", "F#:maj", "E:maj", "F#:maj"],
        "f_maj": ["D:min", "C:maj", "Bb:maj", "C:maj"],
        "bb_maj": ["G:min", "F:maj", "Eb:maj", "F:maj"],
        "eb_maj": ["C:min", "Bb:maj", "Ab:maj", "Bb:maj"],
        "ab_maj": ["F:min", "Eb:maj", "Db:maj", "Eb:maj"],
        "db_maj": ["Bb:min", "Ab:maj", "Gb:maj", "Ab:maj"],
        "gb_maj": ["Eb:min", "Db:maj", "Cb:maj", "Db:maj"],
        "f_sharp_maj": ["D#:min", "C#:maj", "B:maj", "C#:maj"],
        "c_sharp_maj": ["A#:min", "G#:maj", "F#:maj", "G#:maj"],
    },
}

global_chord_use_counter = dict.fromkeys(FORMS_OF_CHORD_PROGS, 0)

for element in READ_DATASET:
    for roman_chord_obj_chord_prog, roman_chord_obj_val in FORMS_OF_CHORD_PROGS.items():
        #   open the majmin.lab file corresponding to the id of this element
        try:
            with open(rf"C:\Users\pijonka\Documents\PWS\data\q3\dataset-20thcent-mcgill-billboard\LAB-McGill-Billboard\{element["id"].zfill(4)}\majmin.lab") as f:
                unmod_song_chords = f.read()
        except:
            continue

        # clean chords list
        song_chords_list = chord_parsers.parse_lab_chords(unmod_song_chords)

        use_of_chord_prog_counter = chord_analyzer.count_chord_progs_ignore_reps(song_chords_list, roman_chord_obj_val)

        global_chord_use_counter[roman_chord_obj_chord_prog] += use_of_chord_prog_counter
        

print(global_chord_use_counter)