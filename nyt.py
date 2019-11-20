from newsapi import NewsApiClient 
import json 
import os 

API_KEY = os.environ.get('NEWS_KEY')

newsapi = NewsApiClient(api_key=API_KEY)

with open('nyt_data.json', 'w+') as file: 

    nyt_hk = newsapi.get_everything(q='Hong Kong', 
                                    sources='the-new-york-times',
                                    language='en',
                                    from_param='2019-10-20',
                                    to='2019-11-18',
                                    sort_by='publishedAt',
                                    page=5)

    file.write(json.dumps(nyt_hk,indent=4))
