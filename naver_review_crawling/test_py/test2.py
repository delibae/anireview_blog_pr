

a = '아마존종합동물병원'

b = '아마존동물병원'

try:
    c = a.replace("동물병원", "")
except:
    c = a
try:
    d = b.replace("동물병원","")
except:
    d = b


from difflib import SequenceMatcher

print(SequenceMatcher(None, c, d).ratio())
print(SequenceMatcher(None, d, c).ratio())
