from django import template
register = template.Library()

@register.filter(name='cut')
def get_file_type(value):
    """Removes all values of arg from the given string"""
    
    
