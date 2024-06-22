name = input("What's your name? ")

# 1st way -> can't in a line
# print("Hello, ")
# print(name)
# 1st way fix
# print("Hello ", end="")
# print(name, end="")
# print("!")

# 2nd way -> can in a line but complicated
# print("Hello " + name + "!")

# 3rd way -> simpler but have space between diff types
# print("Hello", name, "!")
# 3rd way fix
# print("Hello ", name, "!", sep="")

# 4th way -> great
print(f"Hello {name}!")
print("How to show \"\"")