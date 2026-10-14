from collections import Counter
import re

text = input().lower()

words = re.findall(r'[a-zA-Z]+', text)
freq = Counter(words)

result = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

for word, count in result[:3]:
    print(f"{word}:{count}")