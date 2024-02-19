import NoteView as v
import Note
import datetime

my_Notes = dict()
quit = True

while(quit):
    action = v.chooseComand 
    if(action == 1):
        head = v.inputHead
        body = v.inpuBody
        addingNote = Note(head,body,datetime.datetime.now())
        
        my_Notes[]
    elif(action==2):
        id = v.chooseID
        change = v.chooseChanging
        if(change==1):
            listOfNotes[]v.inputHead