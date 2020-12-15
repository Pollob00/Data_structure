#Accessing Values in Dictionary
print("Accessing Values in Dictionary")

# Declare a dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Accessing the dictionary with its key
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

print("\n")

#Updating Dictionary

print("Updating Dictionary")

# Declare a dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

#Delete Dictionary Elements
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
#এটি নিম্নলিখিত ফলাফল উত্পাদন করে। নোট করুন যে একটি ব্যতিক্রম উত্থাপিত হয়েছে কারণ ডেল ডিক্ট ডিকশনারির পরে আর উপস্থিত নেই
"""
Ans:
dict['Age']:
Traceback (most recent call last):
   File "test.py", line 8, in 
      print "dict['Age']: ", dict['Age'];
TypeError: 'type' object is unsubscriptable"""