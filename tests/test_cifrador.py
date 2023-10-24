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

def test_desencriptar_traslacion(cifrado_traslacion):
    cifrado = cifrado_traslacion.desencriptar('e')
    assert cifrado == "z"

def test_encriptar_traslacion_error_no_ascii(cifrado_traslacion):
     with pytest.raises(Exception) as exinfo:
        cifrado_traslacion.encriptar("á")
     exinfo.match("ContieneNoAscii")


def test_encriptar_traslacion_error_contiene_numero (cifrado_traslacion):
    with pytest.raises(Exception) as exinfo:
        cifrado_traslacion.encriptar("1d2fa23l34")
    exinfo.match("ContieneNumero")
def test_encriptar_traslacion_error_sin_letras (cifrado_traslacion):
    with pytest.raises(Exception) as exinfo:
        cifrado_traslacion.encriptar("& $")
    exinfo.match("SinLetras")
def test_encriptar_traslacion_error_sin_letras_contiene_numero(cifrado_traslacion):
    with pytest.raises(Exception) as exinfo:
        cifrado_traslacion.encriptar("&1 $5")
    exinfo.match("SinLetras") and exinfo.match("ContieneNumero")


def test_encriptar_numerico (cifrado_numerico):
    cifrado = cifrado_numerico.encriptar('hola')
    assert cifrado == "520 555 540 485"


def test_desencriptar_numerico (cifrado_numerico):
    cifrado = cifrado_numerico.desencriptar("520 555 540 485")
    assert cifrado == 'hola'


def test_encriptar_numerico_error_no_ascii (cifrado_numerico):
    with pytest.raises(Exception) as exinfo:
        cifrado_numerico.encriptar("á")
    exinfo.match("ContieneNoAscii")


def test_encriptar_numerico_error_contiene_numero (cifrado_numerico):
    with pytest.raises(Exception) as exinfo:
        cifrado_numerico.encriptar("1d2fa23l34")
    exinfo.match("ContieneNumero")


def test_encriptar_numerico_error_no_trim(cifrado_numerico):
    with pytest.raises(Exception) as exinfo:
        cifrado_numerico.encriptar(" & $ ")
    exinfo.match("NoTrim")

def test_encriptar_numerico_error_doble_espacio(cifrado_numerico):
    with pytest.raises(Exception) as exinfo:
        cifrado_numerico.encriptar(" &  $ ")
    exinfo.match("DobleEspacio")


def test_encriptar_numerico_error_doble_espacio_contiene_numero (cifrado_numerico):
    with pytest.raises(Exception) as exinfo:
        cifrado_numerico.encriptar("&1  $5")
    exinfo.match("DobleEspacio") and exinfo.match("ContieneNumero")





