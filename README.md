# Pipefy
  
Module to automate pipefy through its API. It allows you to create cards, move them, edit them, etc.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Overview


1. Connect to Pipefy  
With this command you can establish the authentication with Pipefy

2. Get Pipe by ID  
With this command you can obtain information about the fields of a pipe from its id

3. Create Card  
With this command can create a card

4. Upload file  
With this command you can upload a document to the Pipefy servers, it returns the URL of the file uploaded

5. Update Card  
With this command you can update a card

6. Move card  
With this command you can move a card from one phase to another inside a pipe. You can obtain the phase ID 'Get Pipe by ID' command.

7. Delete card  
With this command you can delete a card from Pipefy  




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