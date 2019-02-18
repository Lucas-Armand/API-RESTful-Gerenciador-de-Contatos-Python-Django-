from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=200)
    canal = models.CharField(max_length=200)
    valor = models.CharField(max_length=200)
    obs = models.CharField(max_length=200)
    
    def contatoCreate(contatoJson):
        #Test if json has some contact infomation
        basic_keys = ['nome','canal','valor','obs']
        contato_keys = contatoJson.keys()
        absent_keys = basic_keys-contato_keys
        
        if len(absent_keys)==3:
            # If not, alert ERROR
            return("ERROR")
        else:
            # If yes, complet miss information and save
            for k in absent_keys:
                contatoJson[k]=''
                
        newContato = Contato(nome = contatoJson["nome"][0],
                             canal = contatoJson["canal"][0],
                             valor = contatoJson["valor"][0],
                             obs = contatoJson["obs"][0])
        newContato.save()
        return(newContato)

        
    def contatoUpdate(contato,contatoJson):
        # Acessando contato correto:
        update_keys = contatoJson.keys()
        if 'nome' in update_keys:
            contato.nome = contatoJson['nome'][0]
        if 'canal' in update_keys:
            contato.canal = contatoJson['canal'][0]
        if 'valor' in update_keys:
            contato.valor = contatoJson['valor'][0]
        if 'obs' in update_keys:
            contato.obs = contatoJson['obs'][0]
        contato.save()
        
        return(contato)
        
    def contatoDelete(contato):
        contato.delete()
        
        return(contato)
        
        
