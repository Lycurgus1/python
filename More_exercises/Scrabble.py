# Creating class
class Scrabble:

    # Intialising class
    def __init__(self):
        pass

    # Scrabble function
    def scrabble(self, word):
        # Creating new variable
        score = 0
        # Searching through characters in word, and score calculation
        for char in word:
            if char.upper() in ("A, E, I, O, U, L, N, R, S, T"):
                score = score + 1
            elif char.upper() in ("D, G "):
                score = score + 2
            elif char.upper() in ("B, C, M, P"):
                score = score + 3
            elif char.upper() in ("F, H, V, W, Y"):
                score = score + 4
            elif char.upper() in ("K"):
                score = score + 5
            elif char.upper() in ("J, X"):
                score = score + 8
            elif char.upper() in ("Q, Z"):
                score = score + 10

        # Printing out score
        print(score)

# Testing
obj1 = Scrabble()
obj1.scrabble("cheese")