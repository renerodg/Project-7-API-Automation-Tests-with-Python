# Proyecto de API Urban.Grocers de Gestión de Kits

Este proyecto implementa y prueba la funcionalidad de Urban.Grocers para la gestión de kits de productos. La API permite a los usuarios crear kits de productos, y las pruebas automatizadas aseguran que la API maneje correctamente varias condiciones de entrada.

## Estructura del Proyecto

- **configuration.py**: Define las configuraciones del servicio, incluyendo las URLs y rutas necesarias para las solicitudes.
- **data.py**: Contiene los datos de ejemplo y funciones para manipular el cuerpo de las solicitudes.
- **sender_stand_request.py**: Implementa las funciones para realizar solicitudes HTTP a la API, incluyendo la creación de usuarios y kits.
- **create_kit_name_kit_test.py**: Contiene las pruebas automatizadas utilizando `pytest` para verificar la correcta funcionalidad de la API.

## Funciones Principales

### sender_stand_request.py
- `post_new_user(body)`: Envía una solicitud POST para crear un nuevo usuario.
- `post_new_client_kit(kit_body, auth_token)`: Envía una solicitud POST para crear un nuevo kit de producto usando un token de autenticación.

### data.py
- `get_kit_body(name=None)`: Genera un cuerpo de solicitud para la creación de un kit, opcionalmente incluyendo un nombre de kit.

## Pruebas Automatizadas

Las pruebas están escritas utilizando `pytest` y se encuentran en el archivo `create_kit_name_kit_test.py`. Las pruebas cubren las siguientes situaciones:
## Lista de Comprobación de Pruebas

| №  | Descripción                                                                                                  | ER                                                                                                     |
|----|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| 1  | El número permitido de caracteres (1): `kit_body = { "name": "a"}`                                           | Código de respuesta: 201. El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 2  | El número permitido de caracteres (511): `kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}` | Código de respuesta: 201. El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 3  | El número de caracteres es menor que la cantidad permitida (0): `kit_body = { "name": "" }`                  | Código de respuesta: 400                                                                               |
| 4  | El número de caracteres es mayor que la cantidad permitida (512): `kit_body = { "name":"El valor de prueba para esta comprobación será inferior a" }` | Código de respuesta: 400                                                                               |
| 5  | Se permiten caracteres especiales: `kit_body = { "name": "№%@," }`                                           | Código de respuesta: 201. El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 6  | Se permiten espacios: `kit_body = { "name": " A Aaa " }`                                                     | Código de respuesta: 201. El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 7  | Se permiten números: `kit_body = { "name": "123" }`                                                          | Código de respuesta: 201. El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 8  | El parámetro no se pasa en la solicitud: `kit_body = { }`                                                    | Código de respuesta: 400                                                                               |
| 9  | Se ha pasado un tipo de parámetro diferente (número): `kit_body = { "name": 123 }`                           | Código de respuesta: 400                                                                               |

