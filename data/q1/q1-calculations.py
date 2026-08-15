# sources:
# Arithmetic of Listening - Kyle Gann
# Khan Academy SAT math: ratios (maybe not really a source ig)
import math
import statistics

# calculates the sum of tenny height of a list of frequency ratios in tuple form
def tenny_height(ratios):
    product = math.prod(ratios)
    return math.log2(product)

# takes two ratio's and combines them into one ratio of three elements (a tuple with three elements)
def combine_ratios(ratio_a: tuple[int, int], ratio_b: tuple[int, int]) -> tuple[int, int, int]:
    lcm_of_fracs = math.lcm(ratio_a[1], ratio_b[1])
    x = lcm_of_fracs
    y = ratio_a[0]/ratio_a[1] * lcm_of_fracs
    z = ratio_b[0]/ratio_b[1] * lcm_of_fracs
    return (int(x), int(y), int(z))

# returns average dissonance of a chord
def ave_dissonance(chord: list):
    return round(((statistics.mean(chord) - OCTAVE_TH) / (ADJ_TH - OCTAVE_TH)* 100), 2)
# hardcoded ratio values 
OCTAVE = (2, 1)
OCTAVE_2 = (4, 1)
PERF5 = (3, 2)

# hardcoded pythagoras ratio values
PYTHAGOREAN_MAJ3 = (81, 64)
PYTHAGOREAN_MIN3 = (32, 27)
PYTHAGOREAN_HALF_STEP = (256, 243)

# hardcoded 5-limit ratio values
RATIO5_MAJ3 = (5, 4)
RATIO5_MIN3 = (6, 5)
RATIO5_HALF_STEP_MAJ = (16, 15)
RATIO5_HALF_STEP_MIN = (25, 24)
RATIO5_WHOLE_STEP_MIN = (9, 8)

# constexpr chord ratio values
MAJOR_TRIAD_RATIO = combine_ratios(RATIO5_MAJ3, PERF5)
MINOR_TRIAD_RATIO = combine_ratios(RATIO5_MIN3, PERF5)
OCTAVE_TRIAD_RATIO = combine_ratios(OCTAVE, OCTAVE_2)
ADJ_TRIAD_RATIO = combine_ratios(RATIO5_HALF_STEP_MIN, RATIO5_WHOLE_STEP_MIN)

MAJOR_TH = tenny_height(MAJOR_TRIAD_RATIO)
MINOR_TH = tenny_height(MINOR_TRIAD_RATIO)
OCTAVE_TH = tenny_height(OCTAVE_TRIAD_RATIO)
ADJ_TH = tenny_height(ADJ_TRIAD_RATIO)

chords = {
    "octave": [OCTAVE_TH],
    "I_V_IV_IV": [MAJOR_TH, MAJOR_TH, MAJOR_TH, MAJOR_TH],
    "! I_V_IV_iv": [MAJOR_TH, MAJOR_TH, MAJOR_TH, MINOR_TH],
    "I_V_iv_iv": [MAJOR_TH, MAJOR_TH, MINOR_TH, MINOR_TH],
    "I_v_iv_iv": [MAJOR_TH, MINOR_TH, MINOR_TH, MINOR_TH],
    "i_v_iv_iv": [MINOR_TH, MINOR_TH, MINOR_TH, MINOR_TH],
    "adj": [ADJ_TH],
    "(popular prog) I_V_vi_IV": [MAJOR_TH, MAJOR_TH, MINOR_TH, MAJOR_TH],
    "(popular prog) I_V_vi_iii_IV": [MAJOR_TH, MAJOR_TH, MINOR_TH, MINOR_TH, MAJOR_TH],
    "(popular prog) vi_V_IV_V": [MINOR_TH, MAJOR_TH, MAJOR_TH, MAJOR_TH],
}



print("Ratio major", MAJOR_TRIAD_RATIO)
print("Ratio minor", MINOR_TRIAD_RATIO)
print("Ratio octave", OCTAVE_TRIAD_RATIO)
print("Ratio adjacent notes", ADJ_TRIAD_RATIO)

for chord_prog_name, th_list in chords.items():
    # print(f"Average TH of {chord_name} = ", statistics.mean(th_list))
    ave_dissonance_chord = round(((statistics.mean(th_list) - OCTAVE_TH) / (ADJ_TH - OCTAVE_TH)* 100), 2)
    print(f"Average dissonance (5-limit ratio's) (normalized between bounds) of {chord_prog_name} = ", ave_dissonance_chord)

for chord_prog_name, th_list in chords.items():
    normalized_th_list = []
    for el in th_list:
        el = (el - OCTAVE_TH) / (ADJ_TH - OCTAVE_TH) * 100
        el = round(el, 2)
        normalized_th_list.append(el)

    print(f"Arc of dissonance of {chord_prog_name} = ", " - ".join(map(str, normalized_th_list)))

