import requests
import json 
import os 
import sys
import time

#API_KEY = os.environ.get('NEWS_KEY')
API_KEY = 'qUbmg59imcsB8GH5kK58pmCMlsmZpyEx'

BASE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?'


#adjust dates as needed, but make sure to keep track of whether appending or writing to file
bdate = "begin_date=20191002"
edate = "end_date=20200108"
query ="q=hong+kong"


def write_list2file(list, file): 
    with open(file, 'w+') as f: 
        for index, line in enumerate(list): 
            if line:
                f.write(str(index) + "." + line+'\n')

abstracts = []
snippets = []
lead_paragraphs = [] 
main_headlines = [] 
print_headlines = [] 
pub_date = ''


with open('nyt_response.json', 'w') as f: 

    numhits = float('INF')
    seen = 0
    page = 1
    while seen < numhits:
        URL = BASE_URL + bdate + "&" + edate + "&" + query + " &page="+str(page) + "&api-key=" + API_KEY
        response = requests.get(URL)
        print(response)
        if response.status_code != 200: 
            print(response.content)
        res = json.loads(response.content)

        f.write(json.dumps(res, indent=4))
        meta = res['response']['meta']
        numhits = meta['hits']
        if page == 1 : print(numhits)
        articles = res['response']['docs']
        for a in articles: 
            pub_date = a['pub_date'].split('T')[0]
            if not pub_date: 
                pub_date = '0000-00-00'
            abstracts.append(pub_date + " . " + str(a['abstract']))
            snippets.append(pub_date + " . " + str(a['snippet']))
            lead_paragraphs.append(pub_date + " . " + str(a['lead_paragraph']))
            main_headlines.append(pub_date + " . " + str(a['headline']['main']))
            print_headlines.append(pub_date + " . " + str(a['headline']['print_headline']))
            

        write_list2file(abstracts, 'nyt_abstracts.txt')
        write_list2file(snippets, 'nyt_snippets.txt')
        write_list2file(lead_paragraphs, 'nyt_lead_paragraphs.txt')
        write_list2file(main_headlines, 'nyt_main_headlines.txt')
        write_list2file(print_headlines, 'nyt_print_headlines.txt')

        seen +=10
        page +=1
        time.sleep(10)

