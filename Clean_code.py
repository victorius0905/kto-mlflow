import unittest

"""
Count names with more than seven letters
"""
def count_names(prenoms : str, number_of_letter: int) -> str :
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > number_of_letter:
            more_than_seven += 1
            print("Prenom supérieur à", number_of_letter, " : " + prenom)
        else:
            print("Prenom inférieur ou égal à", number_of_letter, " : " + prenom)
    return more_than_seven

class Test_Names_Method(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = count_names(prenoms=prenoms, number_of_letter=7)
        self.assertEqual(more_than_seven, 4) 

if __name__ == '__main__':
    unittest.main()
