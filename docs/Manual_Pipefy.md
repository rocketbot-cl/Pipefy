



# Pipefy
  
Module to automate pipefy through its API. It allows you to create cards, move them, edit them, etc.  

*Read this in other languages: [English](Manual_Pipefy.md), [Português](Manual_Pipefy.pr.md), [Español](Manual_Pipefy.es.md)*
  
![banner](imgs/Banner_Pipefy.png o jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Connect to Pipefy
  
With this command you can establish the authentication with Pipefy
|Parameters|Description|example|
| --- | --- | --- |
|Session|Identifier for when you connect with more than one account|account1|
|Token|Get the token in https//app.pipefy.com/tokens|eyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWls.eyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlseyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlsIeyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlseyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlsa_kYAjHu7vN8k4_KKRcM7hVivhR1sr7RnCA|
|Asignar resultado a variable|Variable where the result of the connection will be saved|result|

### Get Pipe by ID
  
With this command you can obtain information about the fields of a pipe from its id
|Parameters|Description|example|
| --- | --- | --- |
|Session|Identifier for when you connect with more than one account|account1|
|Pipe Id|Id of the pipe that you want to get the fields. You can get the id in the url of the pipe|301741450|
|Assign to Variable|Variable where the result of the execution will be stored|variable|

### Create Card
  
With this command can create a card
|Parameters|Description|example|
| --- | --- | --- |
|Session|Identifier for when you connect with more than one account|account1|
|Pipe Id|Get id from pipe url|301741450|
|Card Title|Title of the card which will be created|Draft|
|Fields Attributes|Array of inputs to fill card's fields. You can get the field_id with the command Get Pipe by Id|[{ 'field_id': 'applicant_name','field_value': 'Lucas'},{'field_id': 'applicant_email','field_value': 'user@email.com'}]|
|Attached File|Path of the file to be attached to the card|C:\User\Desktop\test.txt|
|Assign to Variable|Var name without {}|variable|

### Upload file
  
With this command you can upload a document to the Pipefy servers, it returns the URL of the file uploaded
|Parameters|Description|example|
| --- | --- | --- |
|Session|Identifier for when you connect with more than one account|account1|
|Assign to Variable|Var name without {}|variable|
|Attached File|Path of the file to be attached to the card|C:\User\Desktop\test.txt|

### Update Card
  
With this command you can update a card
|Parameters|Description|example|
| --- | --- | --- |
|Session|Identifier for when you connect with more than one account|account1|
|Card Id|Get id from pipe url|643648856|
|New Card Title|Title that the card will have. Leave blank if you don't want to change it|Draft|
|Asignee IDs |Array of user ids to assign to the card. Leave blank if you don't want to change it|[307721335, 307721336, 307721337]|
|Due Date|Date when the card will be due. Leave blank if you don't want to change it|2023-02-15T16:30:00+00:00|
|IDs de las etiquetas|Array of label ids to assign to the card. Leave blank if you don't want to change it|[307721335, 307721336, 307721337]|
|Assign to Variable|Var name without {}|variable|

### Move card
  
With this command you can move a card from one phase to another inside a pipe. You can obtain the phase ID 'Get Pipe by ID' command.
|Parameters|Description|example|
| --- | --- | --- |
|Session|Identifier for when you connect with more than one account|account1|
|Card ID|Card ID to move|643648856|
|Phase ID|Phase ID to move the card|643648856|
|Assign to Variable|Var name without {}|variable|

### Delete card
  
With this command you can delete a card from Pipefy
|Parameters|Description|example|
| --- | --- | --- |
|Session|Identifier for when you connect with more than one account|account1|
|Card ID|Card ID to delete|643648856|
|Assign to Variable|Var name without {}|variable|
