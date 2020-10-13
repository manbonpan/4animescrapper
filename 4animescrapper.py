import socket
import urllib.request
from urllib.request import Request
import re
import time
#Will be removed when converted to object
#query = input('Enter Anime Name :').replace(' ','%20')
initial=time.time()
query='Tokyo+Ghoul+re'
# Scrapping
exception=['https://horriblesubs.info/release-schedule/','https://discord.gg/TzuEpf8','reddit.com','https://www.reddit.com/r/4anime']
req = Request('https://4anime.to/?s={0}'.format(query),headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70'})
with urllib.request.urlopen(req) as response:
   html = response.read()
obj=html.decode()
pattern=re.compile(r'<a[^>]* href="([^"]*)"')
paternel=re.compile("<li>(.*?)</li>")
def first(obj):
   nel=[]
   x=pattern.findall(obj)
   for i in x:
       j=i.replace("'",'')
       nel.append(j)
       
   return nel
    
def first_link():
    flink=''
    x=first(obj)
    down_l=[]
    for i in x:
        
        if i[0] != 'h' or (i in exception or 'bit.ly' in i)  :
            continue
        else:
            eps=scrapeps(i)
            break
    print(eps)
    for i in eps:
        print(i)
        if i[0] != 'h' or (i in exception) :
            continue
        else:
            if 'genre' in i:
                continue
                if 'bit.ly' in i:
                    continue
                continue
            print('else')
            x=episvidlin(i)
            down_l.append(x)

    return down_l
            
            
    
def scrapeps(link):
    req = Request(link,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70'})
    with urllib.request.urlopen(req) as response:
       html = response.read()
    flink=html.decode()
    x=pattern.findall(flink)
    return x


def episvidlin(link):
    req = Request(link,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70'})
    with urllib.request.urlopen(req) as response:
       html = response.read()
    epli=html.decode()
    bruh=re.findall('''mirror_dl''',epli)
    for i in bruh:
        span=i.span()[1]
    epli=epli[span:]
    x=pattern.search(epli)
    x=x.group(0)
    return x
    
    
cod=first_link()
print(cod)
    
