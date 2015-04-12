#coding=utf-8
import urllib
import re
import threading
import Queue
q = Queue.Queue()
mylock = threading.RLock()  
r = re.compile(r'href="(http://www\.cnpythoner\.com.+?)"')
urls = []
def save_contents_from_url(url,contents):
    filename = url.replace("http://","")
    filename = filename.replace(".","_")
    filename = filename.replace("/","|")

    opene = open("/tmp/c/%s"%filename,"w")
    opene.write(contents)
    opene.close()
    return 
def set_urls_from_contents(contents):
    g = r.finditer(contents)
    mylock.acquire()  
    for url in g :
        url = url.groups()[0]
        print url
        if url in urls:
            continue
        else:
            urls.append(url)
            q.put(url)
    mylock.release()  
def save_contents():
    while True:
        url = q.get()
        try:
            opener = urllib.urlopen(url)
            contents = opener.read()
            opener.close()
            set_urls_from_contents(contents)
            save_contents_from_url(url,contents)
        except:
            continue
q.put("http://www.cnpythoner.com")
ts = []
for i in range(1,100):
    t = threading.Thread(target=save_contents)
    t.start()
    ts.append(t)
for t in ts:
    t.join()
