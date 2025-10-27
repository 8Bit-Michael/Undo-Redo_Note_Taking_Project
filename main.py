while __name__ == '__main__':
    from note_app import NoteApp
    from difflib import get_close_matches

    def match_input(user_input, options, cutoff=0.6):
        return get_close_matches(user_input.lower(), options, n=1, cutoff=cutoff)
    
    app = NoteApp([], [], [])

    while True:
        command = input("""Enter a command:
        1. Add note
        2. Delete last note
        3. Undo
        4. Redo
        5. Show notes
        6. Save notes
        7. Load notes
        0. Exit
        """)

        if match_input(command, ['add', '1']):
            note = input("Enter your note: ")
            result = app.add_note(note)
            print(result)
            app.show_notes()
        
        elif match_input(command, ['delete', '2']):
            result = app.delete_last_note()
            print(result)
            app.show_notes()

        elif match_input(command, ['undo', '3']):
            result = app.undo()
            print(result)
            app.show_notes()
        
        elif match_input(command, ['redo', '4']):
            result = app.redo()
            print(result)
            app.show_notes()

        elif match_input(command, ['show', '5']):
            app.show_notes()
        
        elif match_input(command, ['save', '6']):
            filename = input("Enter filename to save notes: ")
            result = app.save_to_file(filename)
            print(result)

        elif match_input(command, ['load', '7']):
            filename = input("Enter filename to load notes: ")
            result = app.load_from_file(filename)
            print(result)

        elif match_input(command, ['exit', '0']):
            print("Exiting the application.")
            exit(0)

        else:
            matches = match_input(command, 
            ['add', 'delete', 'undo', 'redo', 'show', 'save', 
             'load', 'exit', '1', '2', '3', '4', '5', '6', '7', '0'])
            if matches:
                command = input(f"Did you mean '{matches[0]}'?")
                print("Returning to menu...")
                return
            else:
                print("Unknown command. Please try again.")
                return

