#Problem 1: Consider a shop UMKC with dictionary of all book items with their prices.
# Write a program to find the books from the dictionary in the range given by user.

book = {"Python": 50, "Web": 30, "C": 20,"Java": 40}
List = [x[0] for x in book.items() if 30<=x[1]<=40]
print("You can purchase book: ", List)