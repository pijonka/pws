import matplotlib.pyplot as plt
import pandas
import math
import statistics 
import numpy
import scipy.stats as stats

# import dataset
dataset = pandas.read_csv(R"C:\Users\pijonka\Documents\PWS\data\q2\q2 results exported from google sheets.csv", usecols=range(13))

# const of population of research
POPULATION = 650 * pow(10, 6)

# order results of each fragment in a list
frags_results = {
    "frag:A": dataset["frag:A"],
    "frag:B": dataset["frag:B"],
    "frag:C": dataset["frag:C"],
    "frag:D": dataset["frag:D"],
    "frag:E": dataset["frag:E"],
    "frag:F": dataset["frag:F"],
    "frag:G": dataset["frag:G"],
    "frag:H": dataset["frag:H"],
    "frag:I": dataset["frag:I"],
    "frag:J": dataset["frag:J"]
}

for frag_name, frag_res in frags_results.items():
    print(f"mean of ", frag_name, statistics.mean(frag_res))

