from django import template
from datetime import timedelta

register = template.Library()

@register.simple_tag
def my_url(value, field_name, urlencode=None):
  url ='?{}={}'.format(field_name, value)

  if urlencode:
    querystring = urlencode.split('&')
    filtered_querystring = filter(lambda p: p.split('=')[0]!=field_name, querystring)
    encoded_querystring = '&'.join(filtered_querystring)
    url = '{}&{}'.format(url, encoded_querystring)

  return url

@register.simple_tag
def change_to_7_days(assign, process, stages):
  val = None

  if stages == '9' or stages == '10' or stages == '11' or stages == '12' or stages == '13':
    if assign is None and process is None:
      return '-'
    else:
      if process is not None:
        val = process + timedelta(days=7, hours=+8)
      else:
        val = assign + timedelta(days=7, hours=+8)
      return val.strftime("%d/%m/%Y - %I:%M %p")
  else:
    return '-'