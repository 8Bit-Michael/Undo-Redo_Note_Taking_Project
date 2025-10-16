class NoteApp:
    
    def __init__(self, undo_stack, redo_stack, notes):
        self.redo_stack = [] # Redo operations
        self.undo_stack = [] # Undo operations
        self.notes = [] # The current notes

    def add_note(self, text):
        self.notes.append(text)
        self.undo_stack.append(('add', text))
        self.redo_stack.clear()

    def delete_last_note(self):
        self.undo_stack.append(('delete', len(self.notes) - 1)) 
        # Storing the index of the deleted node(coming from the top of the stack)
        self.notes.pop() # Pops the top block
        self.redo_stack.clear()

    # The undo stack takes in an action you would like to undo, like deleting a note
    # from the note stack. The redo stack takes in an action like adding a note back to the
    # note stack.
    def undo(self):
        node = self.undo_stack.pop() # Assign the popped node to a variable
        # If the first value in the parameter if you undo that and push it into the redo stack:
        if node[0] == 'add':
            self.notes.remove(node[1]) # Remove from the notes list the node index itself.
            self.redo_stack.append(node) # Append the node to the redo_stack
        # If the first value is 'delete' you want to add it back to the notes list
        elif node[0] == 'delete':
            self.notes.append(node[1]) # Adding it back into the note list
            self.redo_stack.append(node) # Append the node to the redo_stack  

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

def add_note_test():
    print("=== Test: Note Initialization ===")
    app.add_note("First note") # Create the first note
    app.show_notes()

def undo_note_test():
    print("=== Test: Undo Note ===")
    app.undo() # Undo the last note added
    app.show_notes()
