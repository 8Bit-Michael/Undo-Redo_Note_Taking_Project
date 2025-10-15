class NoteApp:
    
    def __init__(self, undo_stack, redo_stack, notes):
        self.redo_stack = [] # Redo operations
        self.undo_stack = [] # Undo operations
        self.notes = [] # The current notes

    def add_note(self, text):
        self.notes.append(text)
        self.undo_stack.append(('add', text))
        self.redo_stack.clear()

    def delete_last_note(self, text): # Text or an index which would lead you to the note.
        self.undo_stack.append(('delete', len(self.notes) - 1)) 
        # Storing the index of the deleted node(coming from the top of the stack)
        self.notes.pop() # Pops the top block
        self.redo_stack.clear()

    def undo(self):
        pass

    def redo(self):
        pass

    def save_to_file(filename):
        pass

    def load_from_file(filename):
        pass

    def show_notes(self):
        for idx, note in enumerate(self.notes): # Loops through the notes with their indexes
            print(f"{idx + 1}: {note}") # Print the numbered notes

app = NoteApp() # Initalize the app
app.add_note("First note") # Create the first note
app.show_notes()
app.undo_stack("First note")
app.show_notes()
