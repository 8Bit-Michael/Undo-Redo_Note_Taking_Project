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
        node = self.undo_stack.pop() # Assign the popped node from the undo stack to a variable
        # If the second value in the parameter is 'add':
        if node[0] == 'add': # Undo that and push it into the redo stack
            self.notes.remove(node[1]) # Remove from the notes list the node index itself.
            self.redo_stack.append(node) # Append the node to the redo_stack
        # If the first value is 'delete' you want to add it back to the notes list
        elif node[0] == 'delete':
            self.notes.append(node[1]) # Adding it back into the note list
            self.redo_stack.append(node) # Append the node to the redo_stack  

    def redo(self):
        node = self.redo_stack.pop() # Erase this node from the redo stack
        if node[0] == 'add': # If you want to redo adding a node
            self.notes.append(node) # Add it back to the notes list
        elif node[0] == 'delete': # if you change your mind and decide to delete something
            self.undo_stack.append(node) # push the action back onto undo stack

    def save_to_file(filename):
        pass

    def load_from_file(filename):
        pass

    def show_notes(self):
        for idx, note in enumerate(self.notes): # Loops through the notes with their indexes
            print(f"{idx + 1}: {note}") # Print the numbered notes
        if not self.notes:
            print("No notes available")

app = NoteApp([], [], []) # Initalize the app, though it's not like your adding features of an object

def add_note_test():
    print("=== Test: Note Initialization ===")
    app.add_note("First note") # Create the first note
    app.show_notes()

def undo_note_test():
    print("=== Test: Undo Note ===")
    app.undo() # Undo the last note added
    # Inserting an index is not necessary, since stacks just push and pop starting at the top
    app.show_notes()

def redo_note_test():
    print("=== Test: Redo Note ===")
    app.redo() # Redo the last undone note
    app.show_notes()

add_note_test() # Node created should appear
undo_note_test() # Node should disappear
redo_note_test() # Node should reappear
