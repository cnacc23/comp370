import argparse
from collections import Counter, defaultdict
import re
from pathlib import Path
import json
import math


def clean_text(text):
    """Convert text to lowercase and remove punctuation."""
    return re.sub(r'[^\w\s]', '', text.lower())


def tokenize_and_clean(file_path, stopwords=None):
    """Tokenize, clean, and filter stopwords from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        titles = file.readlines()

    # Clean and split titles into words
    words = [word for title in titles for word in clean_text(title).split() if not stopwords or word not in stopwords]
    return words


def compute_tf(word_counts):
    """Compute Term Frequency (TF) for a document."""
    total_words = sum(word_counts.values())
    return {word: count / total_words for word, count in word_counts.items()}


def compute_idf(doc_word_counts, num_docs):
    """Compute Inverse Document Frequency (IDF) for words."""
    idf_scores = {}
    for word, doc_set in doc_word_counts.items():
        idf_scores[word] = math.log(num_docs / len(doc_set))
    return idf_scores


def compute_tfidf(tf_scores, idf_scores):
    """Computcate TF-IDF scores by combining TF and IDF."""
    return {word: tf_scores[word] * idf_scores[word] for word in tf_scores}


def read_stop_words(file_path):
   
    with open(file_path, 'r') as f:
        return set(word.strip().lower() for word in f)


def process_files(input_files, stopwords):

    doc_word_counts = []
    global_word_occurrence = defaultdict(set)

    # count total words per document 
    for i, input_file in enumerate(input_files):
        words = tokenize_and_clean(input_file, stopwords)
        word_counts = Counter(words)
        doc_word_counts.append(word_counts)

        # Track word occurrences across documents
        for word in word_counts:
            global_word_occurrence[word].add(i)

    num_docs = len(input_files)

    #calculate idf
    idf_scores = compute_idf(global_word_occurrence, num_docs)

    #calculate tf-idf for each word
    results = {}
    for i, input_file in enumerate(input_files):
        tf_scores = compute_tf(doc_word_counts[i])
        tfidf_scores = compute_tfidf(tf_scores, idf_scores)

        # get top 10 tf-idf scores 
        top_10 = sorted(tfidf_scores.items(), key=lambda x: -x[1])[:10]
        results[Path(input_file).name] = [{"word": word, "score": score} for word, score in top_10]

    return results


def main():
    parser = argparse.ArgumentParser(description="Compute TF-IDF scores for input files.")
    parser.add_argument('-o', "--output", required=True, help="Output JSON file.")
    parser.add_argument('input_files', nargs='+', help="List of input files.")
    parser.add_argument('-s', '--stopwords', help="Optional stopwords file.")

    args = parser.parse_args()

    # Read stopwords if provided
    stopwords = None
    if args.stopwords:
        stopwords = read_stop_words(args.stopwords)

    # Compute TF-IDF scores
    tfidf_results = process_files(args.input_files, stopwords)

    # Write results to JSON file
    with open(args.output, 'w', encoding='utf-8') as outfile:
        json.dump(tfidf_results, outfile, indent=2)

    print(f"TF-IDF scores saved to {args.output}")


if __name__ == "__main__":
    main()
