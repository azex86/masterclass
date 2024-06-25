# Cours sur l'écriture de tests en Python

# Les tests sont essentiels pour vérifier que votre code fonctionne comme prévu.
import unittest

# Exemple de fonction à tester
def addition(a, b):
    return a + b

# Classe de tests héritant de unittest.TestCase
class TestAddition(unittest.TestCase):

    # Méthode de test pour vérifier l'addition simple
    def test_addition_simple(self):
        self.assertEqual(addition(3, 5), 8)

    # Méthode de test pour vérifier l'addition de nombres négatifs
    def test_addition_negatives(self):
        self.assertEqual(addition(-3, -5), -8)

# Fonction principale pour exécuter les tests
if __name__ == '__main__':
    unittest.main()

# Exemple de sortie des tests :
#
# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.001s
#
# OK
