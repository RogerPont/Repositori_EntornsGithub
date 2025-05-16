from Prova_Escrita_05 import *
import pytest

# Test per a la funció llibres_per_categoria
@pytest.mark.parametrize(
    "biblioteca, categoria, res_esperat",
    [
        # Cas de prova 1: Llibres de la categoria "novel·la"
        (
            [
                {"llibre": "El Quixot", "categoria": "novel·la"},
                {"llibre": "1984", "categoria": "ciència-ficció"}
            ],
            "novel·la",
            ["El Quixot"]
        ),
        # Cas de prova 2: Llibres de la categoria "fantasia"
        (
            [
                {"llibre": "El Senyor dels Anells", "categoria": "fantasia"},
                {"llibre": "Crim i Càstig", "categoria": "novel·la"}
            ],
            "fantasia",
            ["El Senyor dels Anells"]
        )
    ]
)
def test_llibres_per_categoria(biblioteca, categoria, res_esperat):
    """
    Prova la funció llibres_per_categoria per assegurar-se que retorna
    correctament els llibres d'una categoria específica.

    :param biblioteca: Llista de diccionaris amb informació sobre els llibres.
    :param categoria: Categoria dels llibres que es volen filtrar.
    :param res_esperat: Llista esperada de llibres d'aquesta categoria.
    """
    resultat = llibres_per_categoria(biblioteca, categoria)
    assert resultat == res_esperat

# Test per a la funció esta_disponible
@pytest.mark.parametrize(
    "biblioteca, llibre, res_esperat",
    [
        # Cas de prova 1: Llibre "El Quixot" no disponible
        (
            [
                {"llibre": "El Quixot", "prestecs": [
                    {"retornat": True},
                    {"retornat": False}
                ]}
            ],
            "El Quixot",
            False
        ),
        # Cas de prova 2: Llibre "1984" disponible
        (
            [
                {"llibre": "1984", "prestecs": [
                    {"retornat": True},
                    {"retornat": True}
                ]}
            ],
            "1984",
            True
        )
    ]
)
def test_esta_disponible(biblioteca, llibre, res_esperat):
    """
    Prova la funció esta_disponible per comprovar si un llibre està disponible
    basant-se en l'estat dels seus préstecs.

    :param biblioteca: Llista de diccionaris amb informació dels llibres.
    :param llibre: Nom del llibre que es vol consultar.
    :param res_esperat: Boolean indicant si el llibre està disponible.
    """
    resultat = esta_disponible(biblioteca, llibre)
    assert resultat == res_esperat

# Test per a la funció usuari_te_prestecs
@pytest.mark.parametrize(
    "biblioteca, usuari, res_esperat",
    [
        # Cas de prova 1: Usuària "Maria" amb préstecs pendents
        (
            [
                {"prestecs": [
                    {"usuari": "Joan", "retornat": True},
                    {"usuari": "Maria", "retornat": False}
                ]}
            ],
            "Maria",
            True
        ),
        # Cas de prova 2: Usuari "Pere" sense préstecs pendents
        (
            [
                {"prestecs": [
                    {"usuari": "Pere", "retornat": True}
                ]}
            ],
            "Pere",
            False
        )
    ]
)
def test_usuari_te_prestecs(biblioteca, usuari, res_esperat):
    """
    Prova la funció usuari_te_prestecs per comprovar si un usuari té préstecs pendents.

    :param biblioteca: Llista de diccionaris amb informació dels préstecs.
    :param usuari: Nom de l'usuari que es vol consultar.
    :param res_esperat: Boolean indicant si l'usuari té préstecs pendents.
    """
    resultat = usuari_te_prestecs(biblioteca, usuari)
    assert resultat == res_esperat

# Test per a la funció dies_prestec_total
@pytest.mark.parametrize(
    "biblioteca, llibre, res_esperat",
    [
        # Cas de prova 1: Total de dies de préstec del llibre "El Quixot"
        (
            [
                {"llibre": "El Quixot", "prestecs": [
                    {"dies": 15},
                    {"dies": 20}
                ]}
            ],
            "El Quixot",
            35
        ),
        # Cas de prova 2: Total de dies de préstec del llibre "1984"
        (
            [
                {"llibre": "1984", "prestecs": [
                    {"dies": 10},
                    {"dies": 25}
                ]}
            ],
            "1984",
            35
        )
    ]
)
def test_dies_prestec_total(biblioteca, llibre, res_esperat):
    """
    Prova la funció dies_prestec_total per calcular el total de dies de préstec d'un llibre.

    :param biblioteca: Llista de diccionaris amb informació dels llibres i els seus préstecs.
    :param llibre: Nom del llibre que es vol consultar.
    :param res_esperat: Total de dies esperat pels préstecs del llibre.
    """
    resultat = dies_prestec_total(biblioteca, llibre)
    assert resultat == res_esperat
