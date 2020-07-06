# Creating class
class DNA_parsing:

    # Intialising class
    def __init__(self):
        pass

    def dna_parsing(self, dna_string):
        # Creating variables
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0
        # Searching through characters in dna_string
        for char in dna_string:
            if char.lower() == "a":
                a_count += 1
            elif char.lower() == "c":
                c_count += 1
            elif char.lower() == "g":
                g_count += 1
            elif char.lower() == "t":
                t_count += 1
            else:
                print("Error")

        # Printing counts
        print(a_count, c_count, g_count, t_count)

# Testing
obj1 = DNA_parsing()
obj1.dna_parsing("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")