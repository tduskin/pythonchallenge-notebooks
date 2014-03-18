# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # InspectorGadget
# #### a class to parse HTML documents and find stuff

# <codecell>

import urllib2
from HTMLParser import HTMLParser

# <codecell>

class InspectorGadget(HTMLParser, object):
    commentlist = []
    
    taglist = []
    
    def __init__(self, doc=None, url=None):
        super(InspectorGadget, self).__init__()
        if url:
            page = urllib2.urlopen(url)
            doc = page.read()
        if doc:
            super(InspectorGadget, self).feed(doc)
        else:
            return
    
    def handle_comment(self, data):
        self.save_comment(data)
        print "Found %s comment(s)!" % len(self.commentlist)
        
    def handle_starttag(self, tag, attrs):
        self.save_tag(tag, attrs)
        print "Found tag: %s" % tag
        
    def save_comment(self, data):
        self.commentlist.append(data)
        return
    
    def save_tag(self, tag, attrs):
        self.taglist.append({tag: attrs})
        
    def get_comments(self):
        return self.commentlist
    
    def get_tags(self):
        return self.taglist

