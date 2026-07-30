import math

# calculates the sum of tenny height of a list of frequency ratios in tuple form
def tenny_height(intervals):
    return sum(math.log2(n * d) for n, d in intervals)

# hardcoded ji chord ratio values
MAJOR_TRIAD_RATIOS = [ (5, 4), (6, 5), (3, 2)]
MINOR_TRIAD_RATIOS = [ (6, 5), (5, 4), (3, 2)]

print("Major TH = ", tenny_height(MAJOR_TRIAD_RATIOS))
print("Minor TH = ", tenny_height(MINOR_TRIAD_RATIOS))