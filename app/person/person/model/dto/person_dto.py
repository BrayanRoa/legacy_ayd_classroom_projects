
class PersonDTO():
    def __init__(self, institutional_mail,names,lastnames,code,document_type_id, role_id, img):
        self.institutional_mail= institutional_mail
        self.names= names
        self.lastnames= lastnames
        self.code =  code
        self.document_type_id = document_type_id 
        self.role_id=role_id
        self.img = img
        
    def __str__(self):
        return {
            "institutional_mail":self.institutional_mail,
            "names":self.names,
            "lastnames":self.lastnames,
            "code":self.code,
            "document_type_id":self.document_type_id,
            "role_id":self.role_id,
            "img":self.img
        }