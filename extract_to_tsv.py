import argparse 
import json 
import random
import csv 

def count_articles(data, key):
  
    count = 0
    
    if isinstance(data, dict):
       
        if key in data:
            count += 1
        # Recursively call the function for each value
        for value in data.values():
            count += count_articles(value, key)
    
    # Check if the data is a list
    elif isinstance(data, list):
        # Recursively call the function for each item in the list
        for item in data:
            count += count_articles(item, key)
    
    return count




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_file", help="output tsv filename")
    parser.add_argument("json_file", help="json file for input")
    parser.add_argument("num_posts_to_output", help= "number of files to output")
    args = parser.parse_args()


    #open input json file 
    with open(args.json_file, 'r') as f: 
        data = json.load(f)
   
    
        # Extract posts from the JSON structure
        if isinstance(data, dict) and 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
        elif isinstance(data, list):
            posts = data
        else:
            print("Error: Unexpected JSON structure")
            return
        

        #check if num posts to ouput less than file 
        num_posts_in_file = count_articles(data, "data")
        
        num_posts = min(int(args.num_posts_to_output), num_posts_in_file)

        #randomly select posts
        selected_posts = random.sample(posts, num_posts)
       

        
    
       #writing posts to tsv output file 
        with open(args.output_file, 'w', newline='') as of:
            tsv_writer = csv.writer(of, delimiter='\t')

            
            #write header 
            tsv_writer.writerow(["Name", "Title", "Coding"])  
    

            #write post information 
            for item in selected_posts:
            
                name = item["data"]["name"]
                title = item["data"]['title']
                tsv_writer.writerow([name, title])
       

if __name__ == "__main__":
    main()


