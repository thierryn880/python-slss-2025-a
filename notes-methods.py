# methods
# author: Thierryn
# #  october 6
# ask the user what the weather is like
print("whats the weather like?")

weather = input()
if weather.lower() == "rainy":
    print("you should bring an umbrella")
elif weather.lower().strip("!").upper() == "sunny":
    print("you should bring sunscreen.")

else:
    print("i see...")
