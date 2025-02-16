from collections import Counter

text = "mississippi"
letter_counts = Counter(text)
most_common_letters = letter_counts.most_common(3)
print((most_common_letters))
