(Repo de pruebas, lo importante es la documentación en el readme)

# Pytest
https://docs.pytest.org/en/latest/contents.html
pytest
pytest -s : para ver los prints. Por defecto no los saca.

## pytest.ini
Nos sirve para especificar los nombres de las funciones, clases, files que queremos correr con el comando pytest.

```
[pytest]
python_files = test_*
python_functions = test_*
python_classes = *Test
```

## Markers
from pytest import mark

@mark.name
def XXX():

### Personalizar los markers
https://docs.pytest.org/en/latest/example/markers.html#mark-examples
En pytest.ini

markers =
    name: mark a test as a name test.
    name2: explicacion...

### Correr los test con markers
pytest -m name
pytest -m "name or name2"  // and // not

Si tenemos muchos test que queremos marcar como @mark.body -> Creamos una clase y marcamos la clase para no tener que ponerlo en cada función.
Todos los metodos de la clase quedan marcados con ese marcador automaticamente.

Para correrlos sin palabra exacta usar -k y puedes poner parte de la palabra.

### Listar todos los markers
pytest --markers
Hay que documentarlos en el pytest.ini para que los liste. (personalizar)

## Fixtures
Su potencial reside en que podemos hacer configuraciones de test y declararlas en un solo lugar, llamarlas tantas veces como queramos. Sin repetir código y mejorando el mantenimiento.
Se declaran en un fichero con nombre **conftest.py**

1. Cualquier test en el directorio o directorio inferiores tiene acceso a los fixtures del fichero conftest.py
2. No es necesario importarlo en los scripts de tests.

@fixture()
@fixture(scope = function) // session  (function ejecuta el codigo por cada funcion y session por vez que corres los tests. Por ejemplo: si hay un print con function se vera X veces y con session solo 1)

## Reporte HTML
pip install pytest-html

Crear reportes de los test en html

pytest --html="results.html"




## Ejecutar tests en carpetas hermanas.

myCode
|_tests
|_funcs

Existe un problema ya que la libreria se crea de la carpeta funcs y la carpeta test no tiene a priori acceso a estos paquetes.

Creando correctamente el __init__.py en funcs (from .fichero import XXX y luego importando en tests, import fucns) podemos correr pytes de la siguiente manera para que no de fallo.

Desde la carpeta padre (myCode)

```
python -m pytest tests
ó
python -m pytests tests -m nombremarker
```

Donde especificamos con -m que ejecutamos pytest como modulo en la caperta tests pero al estar haciendo la llamada desde la carpeta padre es capaz de ver los paquetes de funcs.

# TOX

Modulo que nos ayuda a separar las librerias lógicas de los tests que queremos realizar.
Además nos permite hacer los mismos tests en diferentes entornos virtuales que queremos darle soporte (env2.7, env3.6...)

```
pip install tox
```

Instalar en el entorno raiz ya que lo que nos permite es controlar los diversos entornos virtuales.

Hay que especificar un fichero tox.ini con la configuración. 
Despues corriendo tox crea los entornos automaticamente, testea lo especificado con las
'dependencies' y valores especificados.

```
[tox]
envlist = py36

[testenv]
deps = pytest

[pytest]
python_files = test_*
python_functions = test_*
python_classes = *Test
testpaths = tests
```

TODO: Comprobar si puedo testear un venv ya creado. 
Comprobar si tengo que instalar paquetes que se usen o se ponen en el setup...

