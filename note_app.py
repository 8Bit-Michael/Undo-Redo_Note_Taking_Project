class NoteApp:
    
    def __init__(self, notes, undo_stack, redo_stack):
        self.notes = [] # The stack/list of notes
        self.undo_stack = undo_stack # For undo operations
        self.redo_stack = redo_stack # Redo operations

    def add_note(self, text):
        pass

    def delete_last_note(self):
        pass

    def undo(self):
        pass

    def redo(self):
        pass

    def save_to_file(filename):
        pass

    def load_from_file(filename):
        pass

    def show_notes(self):
        pass