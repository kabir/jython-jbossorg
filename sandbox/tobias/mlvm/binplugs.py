# -*- coding: utf-8 -*-
from __future__ import with_statement

import re
import urllib
import sys
import os
from md5 import md5
from contextlib import closing

linkpat = re.compile(r'href="([^"]+)"')

def diff(one, two):
    score = abs(len(one)-len(two))
    for i in range(min(len(one),len(two))):
        if one[i] != two[i]:
            score += 1
    return score

def download(url):
    localpath = url.split('/')[-1]
    def verify(data):
        assert checkdigest(data), "MD5 verification of %s failed" % url
        return data
    try:
        with closing(urllib.urlopen(url[:-3]+'md5')) as md5file:
            digest = md5file.read().split('=')[1].strip()
    except:
        def checkdigest(data):
            print "WARNING: could not access the MD5 verification file, download is not verified."
            return True
    else:
        def checkdigest(data):
            return md5(data).hexdigest() == digest
    if os.path.exists(localpath):
        with open(localpath,'rb') as file:
            if checkdigest(file.read()):
                return None
    with closing(urllib.urlopen(url)) as webfile:
        with open(localpath,'w') as localfile:
            localfile.write(verify(webfile.read()))
    return localpath

if __name__ == '__main__':
    url = "http://download.java.net/openjdk/jdk7/promoted/%s/" % sys.argv[1].split('-')[1]
    sysname, _,_,_, machine = os.uname()
    with closing(urllib.urlopen(url)) as page:
        links = []
        for link in linkpat.findall(page.read()):
            if link.endswith('jar') and 'ea-plug' in link:
                ix = link.find(sysname.lower())
                if ix == -1: continue
                platform = link[ix:].split('-')[1]
                if platform == machine:
                    break
                else:
                    links.append((diff(machine, platform), link))
        else:
            if links:
                link = sorted(links)[0][1]
            else:
                print "Could not find any applicable binary plugs."
                sys.exit(1)
    print "Downloading file", link
    archive = download(urllib.basejoin(url, link))
    if archive:
        path = os.path.realpath('')
        print 'Extracting file "%s" to "%s".' % (archive, path)
        if os.system("java -jar %s" % (archive)):
            print "Extraction failed!"
        else:
            print "done"
    else:
        print "Binary plugs already installed."
