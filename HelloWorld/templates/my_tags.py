from django import template
from django.utils.safestring import mark_safe

register = template.Library()  # register的名字是固定的,不可改變

# 自定義標籤
@register.simple_tag
def mul(v1, v2, v3):
    return v1 * v2 * v3

# 自定義標籤
@register.simple_tag
def my_input(v1, v2):
    temp_html = '''<div class="ts-input is-icon">
                       <span class="ts-icon" id="%s">@</span>
                       <input type="text" class="form-control" placeholder="%s" aria-label="name">
                   </div>''' % (v1, v2)
    return mark_safe(temp_html)

# 過濾器
@register.filter
def my_filter(v1, v2):
    return v1 * v2