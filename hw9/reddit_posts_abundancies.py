import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np


def count_tags(file):

    df = pd.read_csv(file, sep="\t")

    #select only coding column
    annotations = df.iloc[:,2]

    #generate a dictionary with counts of each tag's frequency
    counts = annotations.value_counts().to_dict()

    #ensure dictionary includes all tags 
    tags = ['Course Specific Advice', 'Course Specific Exams', 'Social', 'International Student FAQ', 'Residence in Montreal', 'ISO',
            'General Advice', 'Administrative']
    

    for t in tags: 

        #initialize values not already in dictionary to be 0
        if t not in counts:
            counts[t] = 0

    return counts

def get_values(d):
    values = []
    for i in d: 
        values.append(d[i])
    
    return values

def main():
    mcgill_tags = count_tags('final_labeled_dataset_mcgill.tsv')
    concordia_tags = count_tags('final_labeled_dataset_concordia.tsv')
    print(concordia_tags)

    #x-axis 
    tags = list(mcgill_tags.keys())
    x = np.arange(len(tags))
    width = 0.35
   
    #y-axis values
    mcgill_values = get_values(mcgill_tags)
    concordia_values = get_values(concordia_tags)

    
    plt.bar(x-width/2, mcgill_values, width, label="McGill Reddit Topic Abundancies")
    plt.bar(x+width/2, concordia_values, width, label="Concordia Reddit Topic Abundancies")
    plt.xlabel("Reddit Post Categories")
    plt.xticks(x, tags, rotation=45, ha='right')
    plt.ylabel("Number of Posts")
    plt.title("Comparing the Types of Reddit Posts Between Students at Concordia and McGill")
    plt.legend()
    plt.tight_layout()
    plt.show()

    

if __name__ == "__main__":
    main()