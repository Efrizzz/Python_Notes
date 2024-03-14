from core.note_manager import NoteManager

def main():
    note_manager = NoteManager()

    while True:
        command = input("Введите команду (add, list, edit, delete, filter, exit): ")
        if command == "add":
            note_manager.create_note()
        elif command == "list":
            note_manager.list_notes()
        elif command == "edit":
            note_manager.edit_note()
        elif command == "delete":
            note_manager.delete_note()
        elif command == "filter":
            note_manager.filter_notes_by_date()
        elif command == "exit":
            break
        else:
            print("Некорректная команда, попробуйте еще раз")

if __name__ == "__main__":
    main()
