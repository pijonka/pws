def append_use_and_pop_data(song: dict, use_of_chord_prog_counter: int):
    write_to_dataset_dict = {
        "title": song["title"],
        "artist": song["artist"],
        "popularity": (100 - int(song["peak_rank"])) * (int(song["weeks_on_chart"])),
        "use_of_chords": use_of_chord_prog_counter
    }
    return write_to_dataset_dict