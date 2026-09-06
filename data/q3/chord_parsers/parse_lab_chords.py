def parse_lab_chords(song_chords: str):
    song_chords_per_line = song_chords.splitlines()
    chord_list = [line.strip().split()[-1] for line in song_chords_per_line if line.strip()]
    return chord_list