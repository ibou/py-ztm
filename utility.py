import pyjokes, datetime
from collections import Counter, defaultdict, OrderedDict

# print(pyjokes.get_joke("en", "neutral"))

# li = [1,2,3,4,5,6,7,8,9]
# sentence = ['en', 'neutral', 'italic', 'bold']

# print(Counter(li))
# print(Counter(sentence))

# d = OrderedDict()
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# print(d)
print(datetime.datetime.now())
print(datetime.timedelta(days=365, hours=8, minutes=15, seconds=30))
print(datetime.date(year=2011, month=4, day=12))

import pdb

def add(num1, num2):
    print(num1 , num2)
    pdb.set_trace()
    return num1 + num2
  
add(2, "3")