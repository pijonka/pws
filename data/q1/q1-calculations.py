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


# hardcoded ji chord ratio values
MAJOR_TRIAD_RATIO = (4, 5, 6)
MINOR_TRIAD_RATIO = (10, 12, 15)
OCTAVE_TRIAD_RATIO = ( )

MAJOR_TH = tenny_height(MAJOR_TRIAD_RATIO)
MINOR_TH = tenny_height(MINOR_TRIAD_RATIO)

print("Major TH = ", MAJOR_TH)
print("Minor TH = ", MINOR_TH)
print("Average TH of I - V - IV - iv = ", statistics.mean([MAJOR_TH, MAJOR_TH, MAJOR_TH, MINOR_TH]))
print("Average TH of = ", statistics.mean([MAJOR_TH, MAJOR_TH, MAJOR_TH, MINOR_TH]))