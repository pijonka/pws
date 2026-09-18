import matplotlib as plt
import pandas

dataset = pandas.read_csv(R"C:\Users\pijonka\Documents\PWS\data\q2\q2 results exported from google sheets.csv").dropna(how="all", axis=1)

print(dataset)

print(dataset["frag:A"])
# dataset_stats = dataset["frag:B"].tolist()