"""Template for completing assignment 2."""

import re

from assignment_05_text import nom_text
# print(nom_text)  # uncomment to see the text

# See assignment description on Learning Suite.
# Make sure that you *manually* check the results of your regexes as you go.

gerund_re = r'.*ing\b'  # <--needs improving!
gerunds = re.findall(gerund_re, nom_text)
gerund_count = len(gerunds)

print('Gerunds:', gerund_count)


total = gerund_count  # plus others that you come up with
print('Total nominalizations:', total)
