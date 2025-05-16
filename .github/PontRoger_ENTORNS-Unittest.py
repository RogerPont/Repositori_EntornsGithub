# Importem les funcions i classes necessàries del fitxer Prova_escrita_03
from Prova_escrita_03 import *
# Importem les funcions i classes necessàries del fitxer Prova_escrita_04
from Prova_escrita_04 import *

# Importem la llibreria unittest per fer proves unitàries
import unittest


class Testprova03(unittest.TestCase):
    """
    Classe de proves per a les funcions definides a Prova_escrita_03.
    Conté tests per validar les funcionalitats bàsiques.
    """
    def test_trobar_min_max_rendiment(self):
        """
        Test per a la funció `trobar_min_max_rendiment`.
        Comprova si retorna correctament el mínim i màxim d'un conjunt de valors.
        """
        # Cridem la funció amb valors de prova i guardem el resultat
        min_max = trobar_min_max_rendiment(10.00, 12.00, 15.00)
        # Comprovem que el resultat sigui correcte, mínim 10.00 i màxim 15.00
        self.assertEqual(min_max, (10.00, 15.00))

    def test_comptar_estudiant(self):
        """
        Test per a la funció `comptar_estudiants`.
        Comprova si retorna correctament el nombre total d'estudiants.
        """
        # Diccionari amb les notes de diversos estudiants per matèries
        notes_estudiants = {
            "Anna": {"Matemàtiques": 8, "Història": 7},
            "Marc": {"Matemàtiques": 6},
            "Laura": {"Ciències": 9, "Matemàtiques": 10},
            "Jordi": {"Història": 5}
        }
        # Cridem la funció comptar_estudiants i guardem el resultat
        resultat = comptar_estudiants(notes_estudiants)
        # Comprovem que el nombre d'estudiants sigui correcte (4 en aquest cas)
        self.assertEqual(resultat, 4)
    
    def test_comptar_estudiants_materia(self):
        """
        Test per a la funció `comptar_estudiants_matèria`.
        Comprova si retorna correctament el nombre d'estudiants que fan una matèria específica.
        """
        # Diccionari amb les notes de diversos estudiants per matèries
        notes_estudiants = {
            "Anna": {"Matemàtiques": 8, "Història": 7},
            "Marc": {"Matemàtiques": 6},
            "Laura": {"Ciències": 9, "Matemàtiques": 10},
            "Jordi": {"Història": 5}
        }
        # Cridem la funció comptar_estudiants_matèria per a la matèria "Matemàtiques"
        resultat = comptar_estudiants_matèria(notes_estudiants, "Matemàtiques")
        # Comprovem que el nombre d'estudiants que fan "Matemàtiques" sigui correcte (3)
        self.assertEqual(resultat, 3)
   

class Testprova04(unittest.TestCase):
    """
    Classe de proves per a les funcions definides a Prova_escrita_04.
    Conté tests per validar operacions amb matrius.
    """
    def test_cercar_el(self):
        """
        Test per a la funció `cercar_el`.
        Comprova si l'element indicat es troba a la matriu i retorna les seves coordenades.
        """
        # Matriu d'exemple
        m_ex = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        
        # Cerquem un element que no existeix (10) a la matriu
        resultat1 = cercar_el(m_ex, 10)
        # Comprovem que el resultat indiqui que no es troba (False, None)
        self.assertEqual(resultat1, (False, None))
        
        # Cerquem un element que existeix (1) amb coordenades incloses
        resultat2 = cercar_el(m_ex, 1, True)
        # Comprovem que el resultat sigui correcte (True, (0, 0))
        self.assertEqual(resultat2, (True, (0, 0)))

    def test_sumar_fila(self):
        """
        Test per a la funció `sumar_fila`.
        Comprova la suma dels elements d'una fila específica.
        """
        # Matriu d'exemple
        m_ex = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        
        # Sumem els elements de la fila 2 (índex 2)
        resultat1 = sumar_fila(m_ex, 2)
        # Comprovem que el resultat sigui correcte (24)
        self.assertEqual(resultat1, 24)
        
        # Intentem sumar una fila que no existeix (índex 10)
        resultat2 = sumar_fila(m_ex, 10)
        # Comprovem que el resultat sigui None
        self.assertIsNone(resultat2)

    def test_sumar_matriu(self):
        """
        Test per a la funció `sumar_matriu`.
        Comprova la suma de tots els elements d'una matriu.
        """
        # Matriu d'exemple
        m_ex = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        
        # Sumem tots els elements de la matriu
        resultat = sumar_matriu(m_ex)
        # Comprovem que el resultat sigui correcte (45)
        self.assertEqual(resultat, 45)

    def test_transformar(self):
        """
        Test per a la funció `transformar`.
        Comprova si els elements d'una matriu es modifiquen correctament segons l'operació indicada.
        """
        # Matriu d'exemple
        m_ex = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        
        # Modifiquem la matriu sumant 10 a tots els elements
        transformar(m_ex, 10, "+")
        # Comprovem que la matriu transformada sigui correcta
        self.assertEqual(m_ex, [[11, 12, 13], [14, 15, 16], [17, 18, 19]])


# Indiquem que, si aquest fitxer es crida directament, s'executin les proves unitàries
if __name__ == '__main__':
    unittest.main()
