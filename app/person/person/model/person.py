
class Person():
    def __init__(self, institutional_mail,names,lastnames,code,document_type_id) -> None:
        self.institutional_mail= institutional_mail
        # self.password = password
        self.names= names
        self.lastnames= lastnames
        self.code =  code
        self.document_type_id = document_type_id 
        
    def __str__(self):
        return {
            "institutional_mail":self.institutional_mail,
            # "password":self.password,
            "names":self.names,
            "lastnames":self.lastnames,
            "code":self.code,
            "role_code":self.role_code,
            "document_type_id":self.document_type_id,
        }