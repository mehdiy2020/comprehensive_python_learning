import re
from bs4 import BeautifulSoup

# First Solution
text = '$12.23'
out = text.replace("$", "")
float(out)

# Second Solution
expression = r"\$([0-9]*\.[0-9]*)"

outcome = re.search(expression, text)
outcome.group(0)

the_price = outcome.group(1)
float(the_price)