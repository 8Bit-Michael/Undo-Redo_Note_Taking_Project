import os

class NoteApp:
    def __init__(self, undo_stack=None, redo_stack=None, notes=None):
        self.undo_stack = undo_stack or []  # Stack for undo actions
        self.redo_stack = redo_stack or []  # Stack for redo actions
        self.notes = notes or []            # List of notes

    def add_note(self, text):
        """Add a note to the list."""
        self.notes.append(text)
        self.undo_stack.append(('add', text))
        self.redo_stack.clear()
        return f'"{text}" added to notes'

    def delete_last_note(self):
        """Delete the most recent note."""
        if not self.notes:
            return "No notes to delete"
        deleted_note = self.notes.pop()
        self.undo_stack.append(('delete', deleted_note))
        self.redo_stack.clear()
        return f'Last note ("{deleted_note}") deleted'

    def undo(self):
        """Undo the last action."""
        if not self.undo_stack:
            return "No actions to undo"

        action, value = self.undo_stack.pop()
        if action == 'add':
            # Remove the note that was last added
            if value in self.notes:
                self.notes.remove(value)
            self.redo_stack.append(('add', value))
        elif action == 'delete':
            # Re-add the note that was deleted
            self.notes.append(value)
            self.redo_stack.append(('delete', value))

        return f"Undid action: {action}"

    def redo(self):
        """Redo the last undone action."""
        if not self.redo_stack:
            return "No actions to redo"

        action, value = self.redo_stack.pop()
        if action == 'add':
            self.notes.append(value)
            self.undo_stack.append(('add', value))
        elif action == 'delete':
            if value in self.notes:
                self.notes.remove(value)
            self.undo_stack.append(('delete', value))

        return f"Redid action: {action}"

    def save_to_file(self, filename):
        """Save notes to a text file."""
        with open(filename, 'w') as f:
            for note in self.notes:
                f.write(f"{note}\n")
        return "Notes saved successfully"

    def load_from_file(self, filename):
        """Load notes from a text file."""
        if not os.path.exists(filename):
            return f"{filename} does not exist"
        with open(filename, 'r') as f:
            self.notes = [line.strip() for line in f.readlines()]
        self.undo_stack.clear()
        self.redo_stack.clear()
        return "Notes successfully loaded"

    def show_notes(self):
        """Display all notes."""
        if not self.notes:
            print("No notes available")
        else:
            for i, note in enumerate(self.notes, start=1):
                print(f"{i}: {note}")
