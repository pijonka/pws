# sources:
# Arithmetic of Listening - Kyle Gann
# Khan Academy SAT math: ratios (maybe not really a source ig)
import math
import statistics

# calculates the sum of tenny height of a list of frequency ratios in tuple form
def tenny_height(ratios):
    product = math.prod(ratios)
    return math.log2(product)

def equal_temperament_frequency_calculator(deviation_from_a4):
    return 440 * pow(2, deviation_from_a4/12)

# get the LCM of the denominator of ratio a and numerator of ratio b
def combine_ratios(ratio_a: tuple[int, int], ratio_b: tuple[int, int]):
    aden_bnum_common = math.lcm(ratio_a[1], ratio_b[0])
    x = ratio_a[0] * (aden_bnum_common // ratio_a[1])
    y = aden_bnum_common
    z = ratio_b[1] * (aden_bnum_common // ratio_b[0])

    gcd_all = math.gcd(x, y, z)
    return (x // gcd_all, y // gcd_all, z // gcd_all)

# hardcoded pythagoras ratio values
PYTHAGOREAN_MAJ3 = (81, 64)
PYTHAGOREAN_MIN3 = (32, 27)
OCTAVE = (2, 1)
PERF5 = (3, 2)
PYTHAGOREAN_HALF_STEP = (256, 243)

# constexpr chord ratio values
MAJOR_TRIAD_RATIO = combine_ratios(PYTHAGOREAN_MAJ3, PERF5)
MINOR_TRIAD_RATIO = combine_ratios(PYTHAGOREAN_MIN3, PERF5)
OCTAVE_TRIAD_RATIO = combine_ratios(OCTAVE, OCTAVE)
ADJ_TRIAD_RATIO = combine_ratios(PYTHAGOREAN_HALF_STEP, PYTHAGOREAN_HALF_STEP)


MAJOR_TH = tenny_height(MAJOR_TRIAD_RATIO)
MINOR_TH = tenny_height(MINOR_TRIAD_RATIO)
OCTAVE_TH = tenny_height(OCTAVE_TRIAD_RATIO)
ADJ_TH = tenny_height(ADJ_TRIAD_RATIO)

chords = {
    "octave": [OCTAVE_TH],
    "I_V_IV_IV": [MAJOR_TH, MAJOR_TH, MAJOR_TH, MAJOR_TH],
    "I_V_IV_iv": [MAJOR_TH, MAJOR_TH, MAJOR_TH, MINOR_TH],
    "I_V_iv_iv": [MAJOR_TH, MAJOR_TH, MINOR_TH, MINOR_TH],
    "I_v_iv_iv": [MAJOR_TH, MINOR_TH, MINOR_TH, MINOR_TH],
    "i_v_iv_iv": [MINOR_TH, MINOR_TH, MINOR_TH, MINOR_TH],
    "adj": [ADJ_TH],
}



print("Ratio major", MAJOR_TRIAD_RATIO)
print("Ratio minor", MINOR_TRIAD_RATIO)
print("Ratio octave", OCTAVE_TRIAD_RATIO)
print("Ratio adjacent notes", ADJ_TRIAD_RATIO)

for chord_prog_name, th_list in chords.items():
    # print(f"Average TH of {chord_name} = ", statistics.mean(th_list))
    print(f"Average dissonance Pythagorean normalized of {chord_prog_name} = ", (((statistics.mean(th_list) - OCTAVE_TH) / (ADJ_TH - OCTAVE_TH)* 100)) )

for chord_prog_name, th_list in chords.items():
    print(f"Arc of dissonance of {chord_prog_name} = ", " - ".join(map(str, th_list)))