# Maintainer: @brunton
# Web: http://brunston.io

import urllib.request as urlreq

fn = "urls.txt"
urls = [line.rstrip('\n') for line in open(fn)]
total = len(urls)
for url in urls:
    # URLs on txti.es must be loaded twice in 6 months to stay active.
    for i in range(2):
        req = urlreq.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0')
        res = urlreq.urlopen(req)
        data = res.read()

    # Backs up the webpages to html files with the txti.es url as the name
    f = open('backups/' + url.lstrip("http://txti.es/") + ".html" , 'w')
    f.write(data.decode('utf-8'))
    f.close()
    # print(data) # debug

print("Backup has concluded. Backed up {0} urls.".format(total))
