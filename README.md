# Calculator

**Calculator** es una *API Restful* la cual funciona como una calculadora simple.

## Instalación

Como único paso se deben instalar los requerimientos del proyecto:

```shell
pip install -r requirements.txt
```

## Uso

Para ejecutar el proyecto debes dirigirte al directorio principal e iniciar el servidor:

```shell
python manage.py runserver
```

La API tiene 2 endpoints, *addition* y *substraction* que solamente aceptan *GET requests* a los cuales debes pasar 2 parámetros en el query string: **operand1** y **operand2**, la API responderá con un *response* en formato **json** con el resultado de la operación correspondiente.
