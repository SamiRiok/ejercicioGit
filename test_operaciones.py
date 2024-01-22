import unittest
from operaciones import sumar, restar,dividir,multiplicar

class TestSumar(unittest.TestCase):
    
    def test_sumar(self):
        self.assertEqual(sumar(3,2),5)
        self.assertEqual(sumar(-1,1),0)
        self.assertEqual(sumar(-1,-1),-2)
        
    def test_resta(self):
        self.assertEqual(restar(3,2),1)
        self.assertEqual(restar(-1,1),-2)
        self.assertEqual(restar(-1,-1),0)
        
    def test_multiplicar(self):
        self.assertEqual(multiplicar(3,2),6)
        self.assertEqual(multiplicar(-1,1),-1)
        self.assertEqual(multiplicar(-1,-1),1)
        
    def test_division(self):
        self.assertEqual(dividir(6,2),3)
        self.assertEqual(dividir(10,2),5)
        self.assertEqual(dividir(100,10),10)
        
    def test_division_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            resultado = dividir(5, 0)
        
if __name__ == "__main__":
    unittest.main()