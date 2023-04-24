# Pipefy
  
Módulo para automatizar pipefy a través de su API. Permite crear tarjetas, moverlas, editarlas, etc.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Overview


1. Conectar a pipefy  
Con este comando se establece la autenticación con Pipefy

2. Obtener Pipe por ID  
Con este comando puedes obtener información de los campos de un pipe desde su id

3. Crear Tarjeta  
Con este comando puedes crear una tarjeta

4. Subir archivo  
Con este comando puedes subir un documento a los servidores de Pipefy, devuelve la URL del archivo subido

5. Actualizar Tarjeta  
Con este comando puedes actualizar una tarjeta

6. Mover tarjeta  
Con este comando puedes mover una tarjeta de una fase a otra dentro de un pipe. Puedes obtener el ID de la fase con el comando 'Obtener Pipe por ID'

7. Eliminar tarjeta  
Con este comando puedes eliminar una tarjeta de Pipefy  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**requests**](https://pypi.org/project/requests/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)