import json
import datetime

class NoteManager:
    def create_note(self):
        notes = self.read_notes()
        note_id = len(notes) + 1
        title = input("Введите заголовок заметки: ")
        message = input("Введите тело заметки: ")
        created_at = datetime.datetime.now().strftime('%d-%m-%Y')
        new_note = {"id": note_id, "title": title, "message": message, "created_at": created_at}
        notes.append(new_note)
        self.save_notes(notes)
        print("Заметка успешно сохранена")

    def read_notes(self):
        try:
            with open("notes.json", "r") as file:
                notes = json.load(file)
        except FileNotFoundError:
            notes = []
        return notes

    def save_notes(self, notes):
        with open("notes.json", "w") as file:
            json.dump(notes, file)

    def list_notes(self):
            notes = self.read_notes()
            if notes:
                for note in notes:
                    print(f"ID: {note['id']} | Заголовок: {note['title']} | Тело заметки: {note['message']} | Создано: {note['created_at']}")
            else:
                print("Список заметок пуст")


    def edit_note(self):
        notes = self.read_notes()
        note_id = int(input("Введите ID заметки для редактирования: "))
        for note in notes:
            if note['id'] == note_id:
                new_title = input("Введите новый заголовок заметки: ")
                new_message = input("Введите новое тело заметки: ")
                note['title'] = new_title
                note['message'] = new_message
                self.save_notes(notes)
                print("Заметка успешно отредактирована")
                return
        print("Заметка с указанным ID не найдена")

    def delete_note(self):
        notes = self.read_notes()
        note_id = int(input("Введите ID заметки для удаления: "))
        for note in notes:
            if note['id'] == note_id:
                notes.remove(note)
                self.save_notes(notes)
                print("Заметка успешно удалена")
                return
        print("Заметка с указанным ID не найдена")

    def filter_notes_by_date(self):
        notes = self.read_notes()
        date = input("Введите дату в формате ДД-ММ-ГГГГ: ")
        filtered_notes = [note for note in notes if note['created_at'].split()[0] == date]

        if not filtered_notes:
            print("В указанную дату не было создано заметок")
        else:
            for note in filtered_notes:
                print(f"ID: {note['id']} | Заголовок: {note['title']} | Тело заметки: {note['message']} | Создано: {note['created_at']}")

