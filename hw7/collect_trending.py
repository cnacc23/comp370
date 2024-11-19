import requests
from bs4 import BeautifulSoup
import json
import argparse

# scraper to get 
def get_trending_stories():
   
    base_url = "https://montrealgazette.com/"
    url = f"{base_url}/category/news"
    headers = {
        'User-Agent': 'collect_trending.py/1.0'
    }


    # get url's HTML content 
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return

    # parse HTML content using bs4
    soup = BeautifulSoup(response.content, "html.parser")

    # find top 5 trending stories 
    articles = soup.find_all("a", class_="article-card__link", limit= 5)

    # create a dict of each article and url 
    top_5_trending = {}

    for i, article in enumerate(articles, start=1):
        title = article.get_text(strip=True)    #key 
        link = base_url + article['href']       #value 

        top_5_trending[title] = link 
    
    return top_5_trending

def get_indiv_info(d):

    headers = {
        'User-Agent': 'collect_trending.py/1.0'
    }

    #output list of information
    articles_info = []

    # run on each key-value pair in dictionary 
    for title, article_url in d.items(): 

        # get HTML content for each article 
        response = requests.get(article_url, headers=headers)

    
        if response.status_code != 200:
            print('Failed to return the webpage in get_indiv_info.')
            return 

        # parse HTML content 
        soup = BeautifulSoup(response.content, "html.parser")

        #scrape 
        article_title = title 
        publication_date = soup.find("span", class_="published-date__since")
        author = soup.find("span", class_="published-by__author") 
        blurb = soup.find("p", class_="article-subtitle")

        #output to list in a dict format 
        article_info= {
            "title": article_title, 
            "publication_date": publication_date.text.strip(), 
            "author": author.text.strip(), 
            "blurb": blurb.text.strip()
            }

        articles_info.append(article_info)

    
    return articles_info 

def main():

    # argparse for output file 
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help="Output JSON file")
    args = parser.parse_args()

    trending = get_trending_stories()
    article_data = get_indiv_info(trending)

    # write all info to json file 
    with open(args.output, 'w') as f:
     
        json.dump(article_data,f)
       


if __name__ == "__main__":
    main()


