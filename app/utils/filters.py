# formats to month/date/year
def format_date(date):
    return date.strftime('%m/%d/%y')

# formats url string into domain name instead
def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# corrects plurazing words
def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word


from datetime import datetime