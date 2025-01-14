# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

   sudo pip install <package> -t .

"""

import os
import sys

base_path = tmp_global_obj["basepath"] #get rocketbot directory
cur_path = os.path.join(base_path, 'modules', 'Pipefy', 'libs')

if cur_path not in sys.path:
    sys.path.append(cur_path)

GetParams = GetParams #pylint: disable=undefined-variable,self-assigning-variable
SetVar = SetVar #pylint: disable=undefined-variable,self-assigning-variable
PrintException = PrintException #pylint: disable=undefined-variable,self-assigning-variable


import traceback
from pipefy import Pipefy
import requests

# Globals declared here
global mod_pipefy_sessions
# Default declared here
SESSION_DEFAULT = "default"
# Initialize settings for the module here
try:
    if not mod_pipefy_sessions:
        mod_pipefy_sessions = {SESSION_DEFAULT: {}}
except NameError:
    mod_pipefy_sessions = {SESSION_DEFAULT: {}}


module = GetParams("module")
session = GetParams("session")
if not session:
    session = SESSION_DEFAULT

try:
    if module == "connect":

        # if conecting to pipefy is successful, save the pipe object in the session
        def check_connection(token) -> bool:
            headers = { "Authorization": f"Bearer {token}"}
            url = "https://api.pipefy.com/graphql"
            query = "{ pipes { edges { node { id } } } }"

            response = requests.post(url, headers=headers, json={"query": query})

            if response.status_code == 200:
                return True
            else:
                return False

        token = GetParams("token")
        result = GetParams("result")

        try:

            if check_connection(token):
                pipe = Pipefy(token)
                mod_pipefy_sessions[session]["pipe"] = pipe
                SetVar(result, True)
            else:
                SetVar(result, False)
                raise Exception("Invalid token")


        except Exception as e:
            PrintException()
            SetVar(result, False)
            raise e

    if module == "create_card":

        pipe_id = GetParams("pipe_id")
        title = GetParams("title")
        attached_file = GetParams("attached_file")
        fields_attributes = GetParams("fields_attributes")
        result = GetParams("result")

        if not attached_file:
            attached_file = "''"
            attached_file = eval(attached_file)


        resultado = []
        for atributo in eval(fields_attributes):
            atributo['field_id'] = atributo['field_id'].lower()
            resultado.append(atributo)


        if "pipe" not in mod_pipefy_sessions[session]:
            raise Exception("Execute connect command")
        
        pipe = mod_pipefy_sessions[session]["pipe"]
        res = pipe.create_card(pipe_id, resultado, title=title, upload_attachments=attached_file)
        SetVar(result, res)
        
        if res.get("errors"):
            raise Exception(res.get("errors"))
        

        

    if module == "get_pipe":

        pipe_id = GetParams("pipe_id")
        result = GetParams("result")

        options = "{start_form_fields{id,label},phases{name,id,fields{type,id,label}},labels{id,name}}"
        pipe = mod_pipefy_sessions[session]["pipe"]
        
        if "pipe" not in mod_pipefy_sessions[session]:
            raise Exception("Execute connect command")
        
        res = pipe.get_pipe_by_id(pipe_id, options)
        SetVar(result, res)

        if res.get("errors"):
            raise Exception(res.get("errors"))


    if module == "upload_file":
        attached_file = GetParams("attached_file")
        result = GetParams("result")

        pipe = mod_pipefy_sessions[session]["pipe"]
        
        if "pipe" not in mod_pipefy_sessions[session]:
            raise Exception("Execute connect command")
        
        res = pipe.upload_file_direct(attached_file)
        SetVar(result, res)

        if res.get("errors"):
            raise Exception(res.get("errors"))
        
    if module == "move_card":
        card_id = GetParams("card_id")
        destination_phase_id = GetParams("phase_id")
        result = GetParams("result")
        
        pipe = mod_pipefy_sessions[session]["pipe"]
        
        if "pipe" not in mod_pipefy_sessions[session]:
            raise Exception("Execute connect command")
        
        res = pipe.move_card_to_phase(card_id, destination_phase_id)


        try:
            if res.get("errors"):
                raise Exception(res.get("errors"))
            else:
                SetVar(result, res.get("data").get("moveCardToPhase").get("card"))

        except Exception as e:
            SetVar(result, False)
            PrintException()
            raise e

    if module == "delete_card":
        card_id = GetParams("card_id")
        result = GetParams("result")

        pipe = mod_pipefy_sessions[session]["pipe"]
        
        if "pipe" not in mod_pipefy_sessions[session]:
            raise Exception("Execute connect command")
        
        res = pipe.delete_card(card_id)
        try:
            if res.get("errors"):
                raise Exception(res.get("errors"))
            else:
                SetVar(result, res.get("data").get("deleteCard").get("success"))
        except Exception as e:
            SetVar(result, False)
            PrintException()
            raise e

    if module == "update_card":
        card_id = GetParams("card_id")
        title = GetParams("title")
        asignee_ids = GetParams("asignee_id")
        due_date = GetParams("due_date")
        label_ids = GetParams("label_ids")
        result = GetParams("result")

        pipe = mod_pipefy_sessions[session]["pipe"]
        
        if "pipe" not in mod_pipefy_sessions[session]:
            raise Exception("Execute connect command")
        
        res = pipe.update_card(card_id, title, due_date, asignee_ids, label_ids)


        try:
            if res.get("errors"):
                raise Exception(res.get("errors"))
            else:
                SetVar(result, res)

        except Exception as e:
            SetVar(result, False)
            PrintException()
            raise e



except Exception as e:
    traceback.print_exc()
    PrintException()
    raise e