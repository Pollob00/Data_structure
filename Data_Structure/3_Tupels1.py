#Accessing Values in Tuples

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print("tup1[0]: ", tup1[0]);
print("tup2[1:5]: ", tup2[1:5]);

print("\n")

#Updating Tuples
#Tuples are immutable which means you cannot update or change the values of tuple elements.


tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print(tup3);

print("\n")
#Delete Tuple Elements

tup = ('physics', 'chemistry', 1997, 2000);
print(tup);
del tup;
print("After deleting tup :");
print(tup);

"""
This produces the following result. Note an exception raised,
this is because after del tup tuple does not exist any more 
"""


