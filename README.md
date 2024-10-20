# Proyecto Urban Grocers 

### Contenido
- Descripción
- Lista de comprobación
- Archivos del Proyecto
- Recursos
- Instrucciones para las pruebas

---

### Descripción

Se está comprobando cómo la aplicación Urban Grocers crea kits de productos.
El objetivo de este proyecto hacer pruebas positivas y negativas para el campo "name" tomando en cuenta sus requisitos en la solicitud de creación de un kit de productos.
Se revisará que los códigos de respuesta obtenidos coincidan con los esperados y además, en el caso de las pruebas positivas, que el campo "name" en el cuerpo de la respuesta coincida con el de la solicitud enviada.

---

### Lista de comprobación

| №    | Description                                                                               | ER: | 
|------|-------------------------------------------------------------------------------------------|-| 
| 1    | **El número permitido de caracteres (1):** kit_body = { "name": "a"}                      |Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 2    | **El número permitido de caracteres (511):** kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"} |Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 3    | **El número de caracteres es menor que la cantidad permitida (0):** kit_body = { "name": "" }	 |Código de respuesta: 400|
| 4    | **El número de caracteres es mayor que la cantidad permitida (512):** <br/>kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” } |Código de respuesta: 400|
| 5    | **Se permiten caracteres especiales:** kit_body = { "name": ""№%@"," }	                   |Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 6    | **Se permiten espacios:** kit_body = { "name": " A Aaa " }	                               |Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 7    | **Se permiten números:** kit_body = { "name": "123" }	                                    |Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 8    | **El parámetro no se pasa en la solicitud:** kit_body = { }	                              |Código de respuesta: 400|
| 9    | **Se ha pasado un tipo de parámetro diferente (número):** kit_body = { "name": 123 }	     |Código de respuesta: 400|

### Archivos del Proyecto

- **configuration.py:** Este archivo contiene el URL y las rutas de solicitud. 
- **data.py:** Este archivo contiene los cuerpos necesarios para las solicitudes. 
- **sender_stand_request.py:** Este archivo contiene todas las solicitudes para POST para crear una cuenta de usuario y crear un kit.
- **create_kit_name_kit_test.py:** Este archivo contiene todos los tests.
- **README.md:** Este archivo incluye una descripción del proyecto. 
- **.gitignore:** Incluye los archivos que no se deben subir a los repositorios.

---

### Recursos

**Paquetes instalados**
- requests
- pytest

**Documentación**
- URL + /docs/
  - "Main.User" → "Creación de cuenta”
  - "Main.Kits" → "Crear un kit”

---

### Instrucciones 

- Ejecuta todas las pruebas del proyecto a través de la terminal de PyCharm: escribe pytest create_kit_name_kit_test.py en la terminal.
- Ejecuta todas las pruebas a través de la interfaz de PyCharm haciendo clic en el botón con un triángulo verde en la parte superior.
  - Asegúrate de ejecutarlas en el archivo correcto, una forma sencilla de hacer esto es ir al archivo y seleccionar "Current File" antes de hacer clic en el botón con un triángulo verde.
- Otra forma de ejecutar las pruebas es haciendo clic en las flechas verdes junto a las pruebas en el código.
- Algunas pruebas devolverán FAILED como resultado; no te preocupes, es un comportamiento esperado dentro de la lista de comprobaciones.