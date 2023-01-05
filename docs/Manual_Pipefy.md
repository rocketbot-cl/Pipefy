# Pipefy
  
Module to automate Pipefy through its API  

*Read this in other languages: [English](Manual_Pipefy.md), [Español](Manual_Pipefy.es.md), [Portugues](Manual_Pipefy.pr.md).*
  
![banner](imgs/Banner_Pipefy.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Connect to Pipefy
  
With this command the authentication against Pipefy is established
|Parameters|Description|example|
| --- | --- | --- |
|Session|Identifier for when you connect with more than one account|account1|
|Token|Get the token in https//app.pipefy.com/tokens|eyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWls.eyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlseyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlsIeyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlseyJ1c2VyIjp7ImlkIjozMDEzMDY4NzYsImVtYWlsa_kYAjHu7vN8k4_KKRcM7hVivhR1sr7RnCA|

### Create Card
  
With this command can create a card
|Parameters|Description|example|
| --- | --- | --- |
|Session|Identifier for when you connect with more than one account|account1|
|Pipe Id|Get id from pipe url|301741450|
|Fields Attributes|Array of inputs to fill card's fields. You can get the field_id with the command Get Pipe by Id|[{ 'field_id': 'nome_do_solicitante','field_value': 'Lucas'},{'field_id': 'e_mail_do_solicitante','field_value': 'user@email.com'}]|
|Attached File|Path of the file to be attached to the card|C:\User\Desktop\test.txt|
|Assign to Variable|Var name without {}|variable|

### Get Pipe by ID
  
With this command you can obtain information about the fields of a pipe from its id
|Parameters|Description|example|
| --- | --- | --- |
|Session|Identifier for when you connect with more than one account|account1|
|Pipe Id|Get id from pipe url|301741450|
|Assign to Variable|Var name without {}|variable|
