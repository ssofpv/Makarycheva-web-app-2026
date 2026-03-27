
import re
with open('example.txt', encoding='utf-8') as f:
    words = re.findall(r"[A-Za-zА-Яа-я]+", f.read())
maxlen = max(len(w) for w in words)
for w in words:
    if len(w) == maxlen:
        print(w)
