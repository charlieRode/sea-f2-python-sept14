#!/usr/bin/env python

class Element(object):
    tag = "html"
    indent = ""
    
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
        ind += "    "
        file_out.write("<"+self.tag+">\n"+ind)
        for item in self.content:
            try:
                item.render(file_out, ind)
            except AttributeError:
                file_out.write(("\n"+ind).join(self.content))
        file_out.write(ind+"\n</" + self.tag + ">")

class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"
