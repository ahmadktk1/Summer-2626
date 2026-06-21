# how to make sure that we enter only words not integers 
# one way is to the for loop to check every characters and identify from decimals
# we will have to find another way that is more ok with me

# lets do the first way because I think the second way include search using re
name = input("Nmae ; ")
for char in name:
    if char in "0123456789":
        raise ValueError("No numbers allowed")


