from django.shortcuts import render
import urllib.request 
import json

def home(request):
    api=urllib.request.urlopen('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=aa1d6bb1e67a481c955fbb4bd085d20c').read()
    headline=json.loads(api)
    news_articles=headline['articles']
    title=[]
    image=[]
    desc=[]
    url=[]
    for i in range(len(news_articles)):
        head=news_articles[i]
        title.append(head["title"])
        image.append(head["urlToImage"])
        desc.append(head["description"])
        url.append(head["url"])
        combine=zip(title,image,desc,url)
    return render(request,"index.html",context={"news_content":combine})
    
    

