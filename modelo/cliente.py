class Cliente:
    def __init__(self,cliente:str, email:str, telefone:str):
        self._cliente = cliente.strip() 
        self._email = email.strip()
        self._telefone = telefone.strip()

    def __str__(self):
        return self._cliente    
        
