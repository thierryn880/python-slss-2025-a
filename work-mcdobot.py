# work-mcdobot
# author-thierryn
# oct 6
# Write a McDonald's bot that asks if you want fries with your meal.
# Call it  work-mcdobot.py .
# It should accept  Yes/yes  or  No/no  as inputs, and reply
# appropriately depending on the answer.
# If the user inputs anything else, it should repeat back their answer
# and say that it does not understand.


fries = input("would you like fries with yor meal")
fries = fries.lower().strip().upper()

if fries == "yes":
    print("sure thing sigma")
elif "no":
    print("ok bye")
