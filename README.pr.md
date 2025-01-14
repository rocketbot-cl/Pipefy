



# Pipefy
  
Módulo para automatizar pipefy através de sua API. Permite criar cartões, movê-los, editá-los, etc.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Overview


1. Conectar ao pipefy  
Com este comando você pode estabelecer a autenticação com Pipefy

2. Obter Pipe por seu ID  
Com este comando você pode obter informações sobre os campos de um pipe a partir de seu id

3. Criar Card  
Com este comando pode-se criar uma card

4. Subir arquivo  
Com este comando você pode enviar um documento para os servidores do Pipefy, ele retorna a URL do arquivo enviado

5. Atualizar Card  
Com este comando você pode atualizar uma card

6. Mover card  
Com este comando você pode mover um card de uma fase para outra dentro de um pipe. Você pode obter o ID da fase com o comando 'Obter Pipe por ID'

7. Excluir card  
Com este comando você pode excluir um card do Pipefy  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**requests**](https://pypi.org/project/requests/)
### License
  
![MIT](https://img.shields.io/github/license/instaloader/instaloader.svg)  
[MIT](https://opensource.org/license/mit)