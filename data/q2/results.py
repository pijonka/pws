import matplotlib as plt
import pandas
import math
import statistics 

dataset = pandas.read_csv(R"C:\Users\pijonka\Documents\PWS\data\q2\q2 results exported from google sheets.csv", usecols=range(13))

# TEST
frag_results_list = dataset["frag:A"].tolist()
# calculate mean

# calculate stdev

# output matplotlib trust interval or whatever
print(frag_results_list)
print(statistics.mean(frag_results_list))
print(statistics.stdev(frag_results_list))