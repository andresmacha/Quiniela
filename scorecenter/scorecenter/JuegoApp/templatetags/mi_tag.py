from django import template
register = template.Library()

@register.inclusion_tag('juegos_semana.html')

