# Pipefy
  
Módulo para automatizar pipefy a través de su API. Permite crear tarjetas, moverlas, editarlas, etc.  

*Read this in other languages: [English](Manual_Pipefy.md), [Português](Manual_Pipefy.pr.md), [Español](Manual_Pipefy.es.md)*
  
![banner](imgs/Banner_Pipefy.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Conectar a pipefy
  
Con este comando se establece la autenticación con Pipefy
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Identificador para cuando conectas con más de una cuenta|cuenta1|
|Token|Token obtenido en https//app.pipefy.com/tokens|eyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWls.eyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlseyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlsIeyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlseyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlsa_kYAjHu7vN8k4_KKRcM7hVivhR1sr7RnCA|
|Asignar resultado a variable|Variable donde se guardará el resultado de la conexión|result|

### Obtener Pipe por ID
  
Con este comando puedes obtener información de los campos de un pipe desde su id
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Identificador para cuando conectas con más de una cuenta|cuenta1|
|Id del Pipe|Id del pipe del que quieres obtener los campos. Puedes obtener el id en la url del pipe|301741450|
|Asignar a Variable|Variable donde se almacenará el resultado de la ejecución|variable|

### Crear Tarjeta
  
Con este comando puedes crear una tarjeta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Identificador para cuando conectas con más de una cuenta|cuenta1|
|Id del Pipe|Obten el id en la url del pipe|301741450|
|Título de la tarjeta|Título de la tarjeta que se creará|Borrador|
|Campo de atributos|Lista de input para completar los campos de la tarjeta. Puedes obtener los field_id con el comando Obtener pipe por id|[{ 'field_id': 'nombre_del_solicitante','field_value': 'Lucas'},{'field_id': 'email_del_solicitante','field_value': 'user@email.com'}]|
|Archivo Adjunto|Ruta del archivo que se quiere adjuntar a la card|C:\User\Desktop\test.txt|
|Asignar a Variable|Nombre de variable sin llaves {}|variable|

### Subir archivo
  
Con este comando puedes subir un documento a los servidores de Pipefy, devuelve la URL del archivo subido
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Identificador para cuando conectas con más de una cuenta|cuenta1|
|Asignar a Variable|Nombre de variable sin llaves {}|variable|
|Archivo Adjunto|Ruta del archivo que se quiere adjuntar a la card|C:\User\Desktop\test.txt|

### Actualizar Tarjeta
  
Con este comando puedes actualizar una tarjeta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Identificador para cuando conectas con más de una cuenta|cuenta1|
|Id de la tarjeta|Obten el id en la url del pipe|643648856|
|Nuevo título de la tarjeta|Título que tendrá la tarjeta. Deja en blanco si no quieres cambiarlo|Borrador|
|Id de los asignados|Array de ids de usuarios para asignar a la tarjeta. Deja en blanco si no quieres cambiarlo|[307721335, 307721336, 307721337]|
|Fecha de vencimiento|Fecha en la que la tarjeta vencerá. Deja en blanco si no quieres cambiarlo|2023-02-15T16:30:00+00:00|
|Label IDs|Array de ids de etiquetas para asignar a la tarjeta. Deja en blanco si no quieres cambiarlo|[307721335, 307721336, 307721337]|
|Asignar a Variable|Nombre de variable sin llaves {}|variable|

### Mover tarjeta
  
Con este comando puedes mover una tarjeta de una fase a otra dentro de un pipe. Puedes obtener el ID de la fase con el comando 'Obtener Pipe por ID'
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la tarjeta|Identificador de la tarjeta que quieres mover|643648856|
|ID de la fase|Identificador de la fase a la que quieres mover la tarjeta|643648856|
|Asignar a Variable|Nombre de variable sin llaves {}|variable|

### Eliminar tarjeta
  
Con este comando puedes eliminar una tarjeta de Pipefy
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la tarjeta|Identificador de la tarjeta que quieres eliminar|643648856|
|Asignar a Variable|Nombre de variable sin llaves {}|variable|
