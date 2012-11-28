import re

from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

def needs_autoescape_register(filter):
    filter = register.filter(filter) # for >1.3.1:  ...., needs_autoescape=True)
    filter.needs_autoescape = True
    return filter

@needs_autoescape_register
def linebreaksli(value, autoescape=None):
    """Break a string down based on newline characters and for each line, enclose it in the <li> and </li> without the <ul> and </ul> tags. 
           Similar to the unordered_list filter but not requiring a list"""
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    if value:
        value = re.sub(r'\r\n|\r|\n', '\n', value) # normalize newlines
        paras = re.split('\n', value)
    else:
        paras = []

    paras = ['<li>%s</li>' % esc(p.strip()).replace('\\n', '<br/>') for p in paras]
    return mark_safe('\n\n'.join(paras))