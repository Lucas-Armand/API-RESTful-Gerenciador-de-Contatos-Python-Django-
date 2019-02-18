from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from head.models import Contato
import json

def serializer(contatos):
    # Funcao transforma lista de queries em lista de dicionarios (jsonlike)
    result= []
    keys = ["id","nome","canal","valor","obs"]
    for c in contatos:
        contato_dict = {}
        for k in keys:
            contato_dict[k] = c.serializable_value(k)
        result.append(contato_dict)
    return result

def index(request):
    if request.method == "GET":
        # Testando se os parametros foram passados
        try :
            size = int(request.GET["size"])
            page = int(request.GET["page"])
                        
        except:
            # Caso os parametros nao sejam validos usar size=10 e page=0
            return redirect("http://127.0.0.1:8000/?size=10&page=0")
        
        #Calculando offset:
        offset = page*size
     
        # Query:
        contatos = Contato.objects.all()[offset:offset+size]
        
        # Construindo resultado json:
        result= serializer(contatos)
        
        # Retornando resultado HTML json utf8
        return HttpResponse(json.dumps(result,
                                       sort_keys=True, 
                                       indent=2, 
                                       ensure_ascii=False).encode('utf8'),
                            content_type="application/json")
    
    if request.method == "POST":
        # No caso de receber um POST devemos tentar criar um novo contato
        dataJson = dict(request.POST)
        
        # contatoCreate salva e retonra um novo contato ou "ERROR" caso n haja parametros validos
        contatoResult = Contato.contatoCreate(contatoJson = dataJson)
        if contatoResult == "ERROR":
            return Http404("Erro! Informações de contato não foram passados!")
        else:
            result = serializer([contatoResult])
            
            return HttpResponse(json.dumps(result,
                                           sort_keys=True, 
                                           indent=2, 
                                           ensure_ascii=False).encode('utf8'),
                                content_type="application/json",
                                status=201)
        
    
    

def contact(request,contato_id):

    if request.method == "GET":
        contato = Contato.objects.all()[contato_id-1]
        result= serializer([contato])
        return HttpResponse(json.dumps(result,
                                       sort_keys=True, 
                                       indent=2, 
                                       ensure_ascii=False).encode('utf8'),
                            content_type="application/json")
    
    if request.method == "PUT":
        contato = Contato.objects.all()[contato_id-1]
        result= serializer([contato])
        dataJson = dict(request.PUT)
        contato = Contato.contatoUpdate(contatoJson = dataJson)
        result = serializer([contato])
            
        return HttpResponse(json.dumps(result,
                                       sort_keys=True, 
                                       indent=2, 
                                       ensure_ascii=False).encode('utf8'),
                            content_type="application/json",
                            status=204)
    
    if request.method == "POST":    
        contato = Contato.objects.all()[contato_id-1]
        result= serializer([contato])
        dataJson = dict(request.POST)
        contato = Contato.contatoUpdate(contato,contatoJson = dataJson)
        result = serializer([contato])
            
        return HttpResponse(json.dumps(result,
                                       sort_keys=True, 
                                       indent=2, 
                                       ensure_ascii=False).encode('utf8'),
                            content_type="application/json",
                            status=204)
    
    if request.method == "DELETE":
        contato = Contato.objects.all()[contato_id-1]
        result= serializer([contato])
        Contato.contatoDelete(contato)
        return HttpResponse("Deleted",
                            status=204)
        