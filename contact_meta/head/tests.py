from django.test import TestCase
import requests
import json

# Create your tests here.

class ViewTests(TestCase):
    def test_first_page_is_ok(self):
        r = requests.get("http://127.0.0.1:8000/")
        self.assertIs(r.status_code, 200)

    def test_first_page_have_ten_results(self):
        result = json.loads(requests.get("http://127.0.0.1:8000/").text)
        self.assertIs(len(result), 10)
        
    def test_first_page_start_from_begining(self):
        result = json.loads(requests.get("http://127.0.0.1:8000/").text)
        self.assertIs(result[0]["id"], 1)

    
    def test_acess_firt_contato(self):
        result = json.loads(requests.get("http://127.0.0.1:8000/1").text)
        self.assertIs(result[0]['nome'] == 'Lucas Armand',True)

        
    def Test_create_new_contact_is_ok(self):
        testdata = {'nome':'teste',
                    'canal':'testefone',
                    'obs':"it's a test",
                    'valor':'(21) 3243-5465'}
        r = requests.post("http://127.0.0.1:8000/",
                  data=testdata)
        self.assertIs(r.status_code,201)
    
    def Test_last_contact_is_the_contact_created(self):
        result = json.loads(requests.get("http://127.0.0.1:8000/?size=1000&page=0").text)
        self.assertIs(result[-1]['nome']=='teste',True)
    

    def Test_delet_contact_is_ok(self):
        # delete the lastone
        result = json.loads(requests.get("http://127.0.0.1:8000/?size=1000&page=0").text)
        n = len(result)
        r = requests.delete("http://127.0.0.1:8000/"+str(n)+"/")
        self.assertIs(r.status_code,204)
        
    def Test_last_contact_is_not_the_contact_created(self):
        result = json.loads(requests.get("http://127.0.0.1:8000/?size=1000&page=0").text)
        self.assertIs(result[-1]['nome']=='teste',False)
        
    def test_create_and_delete_contact(self):
        self.Test_create_new_contact_is_ok()
        self.Test_last_contact_is_the_contact_created()
        self.Test_delet_contact_is_ok()
        self.Test_last_contact_is_not_the_contact_created()
        
    def test_update_contact_is_ok(self):
        updata = {'obs':1}#'Seu futuro desenvolvedor python!'}
        r = requests.post("http://127.0.0.1:8000/1/",
                  data=updata)
        self.assertIs(r.status_code,204)
        
                                
                          