my_str = "The roots and trunks of the brachial plexus lie above clavicle."

words = [word.lower() for word in my_str.split()]
words.sort()

print("The sorted words are:")
for word in words:
   print(word)