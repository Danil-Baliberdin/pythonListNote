class Note:
    head = ""
    body = ""
    id = 0
    dateOfCreationOtChanging = ""

    def __init__(self,texthead,textbody,date):
        self.head = texthead
        self.body = textbody
        self.dateOfCreationOtChanging = date
        Note.id =+ 1
        self.id = Note.id
    
    def changeHead(self,text):
        self.head = text

    def changeBody(self,text):
        self.body = text
    
    def toString():
        print("id = {id}, head = {head}, body = {body}, date = {dateOfCreationOtChanging}")

    def getiD(self):
        return self.id 