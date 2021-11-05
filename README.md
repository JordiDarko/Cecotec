# PRUEBA CECOTEC

Este proyecto es la solución al problema propuesto. Este README está pensado para ejecutar la aplicación en docker, pero el proyecto contiene los archivos pipenv por si se desea ejecutar dentro de un entorno virtual.

El funcionamiento general consiste en una base de datos con tres clases de objetos:
- Los productos
- Los pedidos
- Los items que contiene cada pedido

Y unos enpoints:
- Listar produtos
- Listar pedidos
- Recuperar un pedido en concreto
- Añadir un item a un pedido 
- Confirmar un pedido

De esta manera se van añadiendo los diferentes items a un pedido y cuando está listo para su confirmación se hace una llamada al endpoint correspondiente para que se calculen los gastos de envio y se marque el pedido como confirmado.


## REQUISITOS

- Python 3.7
- Docker y Docker-compose 


## INSTALACIÓN

- Clonación del repositorio 
` git clone https://github.com/JordiDarko/Cecotec.git `
- En la carpeta del proyecto ejecutamos las migraciones
` docker-compose run web python cecotec/manage.py migrate `
- Construimos el docker-compose
` docker-compose build `
- Lanzamos el docker
` docker-compose up `

En este punto ya tenemos el servicio funcionando en el puerto 8000 de nuestro localhost.


## USUARIOS Y BASE DE DATOS

En este servicio existen un usuario (username : client) y un superusuario (unsername : superuser). Ambos con la contraseña "cecotec123".
Para acceder al adminisitrador de django (http://localhost:8000/admin/) es necesario utilizar el superusuario.


## ENDPOINTS 

El servicio web cuenta con 5 endpoints diferentes, de los cuales 2 son accesibles unicamente por administradores (superuser)

- http://localhost:8000/product_list/  Este endpoint solo acepta GETS y no requiere ningún parametro más que los credenciales pertinentes (pueden acceder los usuarios y los super usuarios). Devuelve un JSON con la lista de los productos existentes en la base de datos.

- http://localhost:8000/order_list/  Este endpoint solo acepta GETS y no requiere ningún parámetro más que los credenciales pertinentes (solo puede acceder un superusuario). Devuelve un JSON con la lista de los pedidos existentes en la base de datos.

- http://localhost:8000/order/<id>/  Este endpoint solo acepta GETS y requiere un id dentro de la url para definir que pedido se requiere al servicio (solo puede acceder un superusuario). Devuelve un JSON con el objeto pedido que se requiere. En caso de enviar un id encorrecto el servicio devuelve un HTTP_400_BAD_REQUEST.

- http://localhost:8000/add_order/. Este endopoint solo acepta POST y requiere un json en el body de la petición con el parámetro "order_id" para identificar el pedido que se quiere confirmar (pueden acceder usuarios y superusuarios) por ejemplo:
{
  "order_id" : "13"
}
El servicio devuelve un JSON con el pedido confirmado.
En caso de enviar un id o parámetro incorrecto el servicio devuelve un HTTP_400_BAD_REQUEST.

- http://localhost:8000/add_item/  Este endpoint solo acepta POST y requiere un json en el body de la petición con los parámetros "product_id", "quantity" y "oder_id" (opcional). De esta manera definimos que producto y en que cantidad queremos añadir a un pedido en concreto, si no identificamos el pedido se genera uno nuevo (pueden acceder usuarios y superusuarios), por ejemplo:
{
  "product_id": "3",
  "quantity" : "1",
  "order_id" : "13"
}
El servicio devuelve un JSON con el pedido modificado.
En caso de enviar un id o parámetro incorrecto el servicio devuelve un HTTP_400_BAD_REQUEST.
  

  ## TEST
  
  El proyecto solo contiene dos tests en el archivo test.py. Para ejecutarlos:
  ` python manage.py test app1 `
  
