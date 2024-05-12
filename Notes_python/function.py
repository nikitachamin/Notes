from Notes_python import ui, file_operation
from Notes_python.Note import Note


def add():
    note = ui.create_note()
    array = file_operation.read_file()
    for notes in array:
        if Note.get_id(note) == Note.get_id(notes):
           Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('Заметка добавлена...')

def show(text):
    array = file_operation.read_file()
    if text == 'date':
        date = input("Введите число в формате dd.mm.yyyy: ")
    for notes in array:
        if text == 'all':
           print(Note.map_note(notes))
        if text == 'id':
           print(Note.get_id(notes))
        if text == 'date':
           if date in Note.get_date(notes):
               print(Note.map_note(notes))

def id_edit_del_show(text):
    id = input("Введите желаемый id: ")
    array = file_operation.read_file()
    for notes in array:
        if id == Note.get_id(notes):
            if text == 'edit':
                note = ui.create_note()
                Note.set_title(notes, note.get_title())
                Note.set_body(notes, note.get_body())
                Note.set_date(notes, note.get_date())
                print("Заметка изменина...")
            if text == 'del':
                array.remove(notes)
                print("Запись удалена...")
            if text == 'show':
                print(Note.map_note(notes))
    file_operation.write_file(array, 'a')

