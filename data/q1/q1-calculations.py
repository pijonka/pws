import math

# calculates the sum of tenny height of a list of frequency ratios in tuple form
def tenny_height(ratios):
    product = math.prod(ratios)
    return math.log2(product)

# hardcoded ji chord ratio values
MAJOR_TRIAD_RATIOS = [ (5, 4), (6, 5), (3, 2)]
MINOR_TRIAD_RATIOS = [ (6, 5), (5, 4), (3, 2)]