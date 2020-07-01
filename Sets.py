# Sets - basically unordered lists

sports = {"Tennis", "Football", "Rugby"} # Creating a set
sports.add("Cricket") # Adding item to set
sports.discard("Tennis")  # Removing item from set
print(sports)

x = frozenset([1, 2, 3, 4])# Frozen set, rarely used.
print(type(x))