import  pytest

from cifradorMensajes.modelo.implementacion import *
from cifradorMensajes.modelo.cifrador import *
from  cifradorMensajes.modelo.errores import *

@pytest.fixture(scope='function')
def regla_tralacion():
    return  ReglaCifradoTraslacion(5)



@pytest.fixture(scope='function')
def regla_numerico():
    return  ReglaCifradoNumerico(5)

@pytest.fixture(scope ='function' )
def cifrado_numerico(regla_numerico):
    return Cifrador(regla_numerico)

@pytest.fixture(scope ='function' )
def cifrado_traslacion(regla_tralacion):
    return Cifrador(regla_tralacion)

def test_encriptar_traslacion(cifrado_traslacion):
    cifrado = cifrado_traslacion.encriptar('a')
    assert cifrado == "f"

def test_encriptar_traslacion_error_no_ascii(cifrado_traslacion):
    cifrado_traslacion.encriptar("2")

