from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag
def CACOTA(filename):
    return settings.MEDIA_FILES_DIR + filename
