# Pytest
https://docs.pytest.org/en/latest/contents.html


## pytest.ini
Nos sirve para especificar los nombres de las funciones, clases, files que queremos correr con el comando pytest.
´´´
[pytest]
python_files = test_*
python_functions = test_*
python_classes = *Test
´´´

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