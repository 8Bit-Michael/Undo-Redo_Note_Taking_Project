Hello, this repository consists of a Python project I was developing using undo and redo stacks, simulating a note taking app. Each action the user causes can be redone and undone
into the main notes stack using these two stacks. The user can interactively manage the note taking app using a simple command line interface, and text files to import and export 
notes.

The following is an example of how the application can be used:

Enter a command:
1. Add note
2. Delete last note
3. Undo
4. Redo
5. Show notes
6. Save notes
7. Load notes
0. Exit
add
Enter your note: Buy groceries
"Buy groceries" added to notes
1: Buy groceries

Enter a command:
1. Add note
2. Delete last note
3. Undo
4. Redo
5. Show notes
6. Save notes
7. Load notes
0. Exit
1
Enter your note: Finish project report
"Finish project report" added to notes
1: Buy groceries
2: Finish project report

Enter a command:
2
Last note ("Finish project report") deleted
1: Buy groceries

Enter a command:
3
Undid action: delete
1: Buy groceries
2: Finish project report

Enter a command:
4
Redid action: delete
1: Buy groceries

Enter a command:
5
1: Buy groceries

Enter a command:
6
Enter filename to save notes: notes.txt
Notes saved successfully

Enter a command:
7
Enter filename to load notes: notes.txt
Notes successfully loaded
1: Buy groceries

Enter a command:
0
Exiting the application.
