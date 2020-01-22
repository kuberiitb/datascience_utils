# sort a dict on key/value
# returns list of tuples
dict_new = sorted(dict_old.items(), key = lambda kv:kv[1])

# counter
from collections import Counter
# Find the ten most common words in Hamlet
import re
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
Counter(words).most_common(10)
# [('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631), 
# ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]
