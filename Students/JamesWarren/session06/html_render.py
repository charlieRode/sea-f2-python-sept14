#!/usr/bin/env python

class Element(object):
    tag = "html"
    ind = ""
    
    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self,append_content):
        """ append new content to element """
        self.content.append(append_content)

    def render(self, file_out, ind=""):
        """ render the content to the given file """
        cind = ind
        ind += "    "
        file_out.write("<%s>\n%s" % (self.tag, ind))
        for item in self.content:
            try:
                item.render(file_out, ind)
            except AttributeError:
                file_out.write(("\n"+ind).join(self.content))
        file_out.write("\n%s</%s>\n%s" % (cind, self.tag, cind))

class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def render(self, file_out, ind=""):
        ind += "    "
        file_out.write("<%s> %s </%s>%s" % (self.tag, self.content, self.tag, ind))

class Title(OneLineTag):
    tag = "title"