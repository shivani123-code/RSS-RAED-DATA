import feedparser
def parseRSS( rss_url ):
    return feedparser.parse( rss_url )

def getHeadlines(rss_url):
    headlines = []
 
    
    feed = parseRSS(rss_url)
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])
 
    return headlines
 
 
 
allheadlines = []
 
 
newsurls = {
 
    'googlenews': 'https://zeenews.india.com/rss/india-national-news.xml',
    'zeenews': 'https://zeenews.india.com/rss/india-national-news.xml',
    
    
 
}
 
 
for key, url in newsurls.items():
    
    allheadlines.extend(getHeadlines(url))
 
 
for hl in allheadlines:
    print(hl)