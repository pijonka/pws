# analyzes chords of a given "song chords list", where each element is a chord, e.g. ["C:maj", "G:maj"], for use of chord progressions given in a dictionary of the format {"c_maj": ["C:maj", "G:Maj"]}. Returns use of second argument's chord progressions in first argument
def count_chord_progs_ignore_reps(song_chords_list: list, chord_progs_to_find: dict[str, list[str]]):
    use_of_chord_prog_counter = 0
    
    #   for every key-value pair in FORMS_OF_CHORD_PROG literal:   
    for key, list_of_chords_in_prog in chord_progs_to_find.items():
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

    return use_of_chord_prog_counter
