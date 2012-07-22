#!../bin/python
import feedparser
from bs4 import BeautifulSoup
import urllib2
import codecs
import json
import string
import datetime

base_dir = 'out/'
def format_url(link, base):
  if link is None:
    return None
  if 'http://' != link[0:len('http://')]:
    return base + '/' + link
  else:
    return link

def print_feed(feed):
  entries = []
  entries.extend(feed["items"])
  sorted_entries = entries#sorted(entries, key=lambda entry: entry["date_parsed"], reverse=True)
  if sorted_entries == []:
    print "Not an RSS Feed"
    
  for entry in sorted_entries:
    #try:
    #  f = urllib2.urlopen(entry['link'])
    #  html = f.read()
    #  soup = BeautifulSoup(html)
     # text = soup.get_text()
     # links = [format_url(link.get('href'), entry['link']) for link in soup.find_all('a')]
    #except urllib2.HTTPError as e:
    #  print "%s error: %s" % (entry['link'], str(e))
    if entry['link'] is not None:
      title = entry['title'].replace('/', '_')
      f = codecs.open(base_dir + title + '.txt', encoding='utf-8', mode='w+')
    
      f.write("%s\n\n%s\n\nlink: %s\n\n" % (entry['title'], entry['summary'], entry['link']))
      if "comments" in entry:
        f.write("comments: %s\n" % entry["comments"])
      if "date" in entry:
        f.write("date: %r\n" % entry["date"])
      if "published" in entry:
        f.write("published: %r\n" % entry["published"])
      else:
        f.write("published: %s\n" % str(datetime.datetime.now()))
      
      
      f.write("keys: %r\n" % [x for x in entry.iterkeys()])  
      
      if 'http://' in entry['link']:  
        base = entry['link'][len('http://'):]
        proto = 'http://'
      elif 'https://' in entry['link']:
        base = entry['link'][len('https://'):]
        proto = 'https://'
      else:
        base = None
        proto = None
      
      splits = string.split(base, '/')
      
      pr = urllib2.urlopen("http://josh-fowler.com/prapi/?url=%s" % (proto + splits[0]))
      page_rank = pr.read()
      f.write("pagerank: %s\n" % page_rank)
    
      try:
        fb = urllib2.urlopen("http://api.facebook.com/method/fql.query?query=select%20like_count%20from%20link_stat%20where%20url='" + entry['link'] +"'&format=json")
        fb_text = fb.read() 
        likes = json.loads(fb_text)
        if len(likes) == 1 and u'like_count' in likes[0]:
          likes = likes[0][u'like_count']
          f.write("# of likes: %s\n" % likes)  
      except ValueError as e:
        print str(e)
        
      
      #f.write("text: %s\n" % text)
      #f.write("links: \n%r\n" % links)
      f.close()


def parse_feeds(url_list):
  feeds = [feedparser.parse(rss_url) for rss_url in url_list]
  for feed in feeds:
    print "Feed: %s" % feed['url']
    print_feed(feed)

if __name__ == '__main__':
  print "hello world"
  parse_feeds(["http://news.ycombinator.com/rss", "http://www.engadget.com/rss.xml"])
  #parse_feeds(["http://www.engadget.com/rss.xml"])