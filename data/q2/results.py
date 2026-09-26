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

# for every fragment results list:
for frag_result_name, frag_result in frags_results.items():
    # -- AI GENERATED GRAPH --
    mean = statistics.mean(frag_result)
    stdev = statistics.stdev(frag_result)
    print(mean)
    print(stdev)

    plt.figure(figsize=(5, 3))

    plt.boxplot(
        frag_result,
        vert=False,
        widths=0.2,
        patch_artist=True,
        boxprops=dict(facecolor="lightblue", color="darkblue"),
        medianprops=dict(color="crimson", linewidth=2),
        whiskerprops=dict(color="darkblue"),
        capprops=dict(color="darkblue"),
    )

    plt.xlim(1, 5)
    plt.yticks([1], [f"Fragment {frag_result_name}"])
    plt.xlabel("Value")
    plt.title("Distribution of frag_result")
    plt.grid(axis="x", linestyle="--", alpha=0.7)

    plt.tight_layout()
    frag_result_file_name = frag_result_name.replace(":", "_")
    plt.savefig(f"./results_graphs/{frag_result_file_name}.pdf")