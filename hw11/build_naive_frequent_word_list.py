import argparse 
from collections import Counter
import re
from pathlib import Path 
import json 

def clean_text(f):

    #convert all to lowercase
    return re.sub(r'[^\w\s]', '', f.lower())

def count_most_frequent(f, stopwords= None):

     with open(f, 'r', encoding='utf-8') as file:
        titles = file.readlines()


    
        # Clean and split titles into words
        if stopwords is None:
            words = [word for title in titles for word in clean_text(title).split()]
        else:
            words = [word for title in titles for word in clean_text(title).split() if word not in stopwords]
    
        # Count word frequencies
        word_counts = Counter(words)
    
        # Get top 10 most frequent words
        top_10 = word_counts.most_common(10)
    
        return top_10

def read_stop_words(file_path):
    with open(file_path, 'r') as f:
        return set(word.strip().lower() for word in f)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', "--output")
    parser.add_argument('input_files', nargs='+')
    parser.add_argument('-s', '--stopwords')
    args = parser.parse_args()

    result = {}
    stopwords = None
    if args.stopwords: 
        stopwords = read_stop_words(args.stopwords)
    
    for input_file in args.input_files:
        file_path = Path(input_file)
        if file_path.exists():
            result[file_path.name] = count_most_frequent(file_path, stopwords)
        else:
            print(f"Warning: File {input_file} not found. Skipping.")
    
        # Write results to JSON file
        with open(args.output, 'w', encoding='utf-8') as outfile:
            json.dump(result, outfile, indent=2)

        

if __name__ == "__main__":
    main()

