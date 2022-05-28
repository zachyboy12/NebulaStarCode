import tkinter, os, subprocess, tkinter.messagebox  # tkinter - Creates GUI; os - Runs files and helps delete files; subprocess - Gets output; tkinter.messagebox (optional) - For help button


root = tkinter.Tk()  # Creating main window
root.title('NebulaCode: Edit, save, run, delete, and open!')  # The title of the window
root.geometry('800x900')  # Making the Geometry
myentry = tkinter.Entry(root)  # The file name to enter
code = tkinter.Text(root, undo=True)  # Code to be run
theoutput = tkinter.Text(root)  # Output of the code
theoutput.insert('1.0', 'Terminal loaded.')
code.configure(highlightcolor='light gray')  # Configuring border color of code widget
theoutput.configure(highlightcolor='light gray')  # Confinguring border color of theoutput widget


def run(file):  # Making the run function
    e = file.split('.')[1]  # The extension of the file name
    if e == 'py':
        os.system(f'python3 {file}')  # Running fhe file with `python3`
        output, error = subprocess.Popen(['python3', file], stdout = subprocess.PIPE).communicate()  # Getting the output and the error
        theoutput.delete('1.0', tkinter.END)  # Deleting last output text
        theoutput.insert('1.0', output)  # Inserting output
    elif e == 'htm' or e == 'html' or e == 'ps':
        output, error = subprocess.Popen(['open', file], stdout = subprocess.PIPE).communicate()  # Getting the output and the error
        os.system(f'open {file}')  # Opening file to run the program
        theoutput.delete('1.0', tkinter.END)  # Deleting last output tezt
        theoutput.insert('1.0', output)  # Inserting output
        
        
def savefile(file):
    open(file, 'w').write(code.get('1.0', 'end-1c'))  # Opening the file and getting code to write


def deletefile(file):
    os.remove(file)  # Deletes given file
        
        
def openfile(file):
    code.insert('1.0', open(file).read())  # Inserts file contents to code widget
    
    
def redo(filler):
    code.edit_redo()  # Redos last edit
    
    
def undo(filler):
    code.edit_undo()  # Undos last edit
    
    
def execute():
    output, error = subprocess.Popen(myentry.get().split(' '), stdout = subprocess.PIPE).communicate()  # Getting the output and the error
    os.system(myentry.get())
    theoutput.delete('1.0', tkinter.END)  # Deleting last output tezt
    theoutput.insert('1.0', output)  # Inserting output
        


runbutton = tkinter.Button(root, text='Run', command=lambda: run(myentry.get()))  # Making run button to run code
savebutton = tkinter.Button(root, text='Save / make given file', command=lambda: savefile(myentry.get()))  # Making save button to save or make the entered file / filename
deletebutton = tkinter.Button(root, text='Delete file', command=lambda: deletefile(myentry.get()))  # Making delete button to delete the file
openbutton = tkinter.Button(root, text='Open file', command=lambda: openfile(myentry.get()))  # Making open button to insert contents of file
executebutton = tkinter.Button(root, text='Execute command', command=execute)  # Making execute button to execute entered command
helpbutton = tkinter.Button(root, text='Help', command=lambda: tkinter.messagebox.showinfo('About\n', """Copyright @ zachyboy12
Used with educational purposes.
No copyright intended.
Cannot be used for anything other than education.
To undo, Press CTRL+u. To redo, Press CTRL+r."""))  # Making help button to be informitive
root.bind('<Control-u>', undo)  # Binding CTRL+u to undo function
root.bind('<Control-r>', redo)  # Binding CTRL+r to redo function
exitbutton = tkinter.Button(root, text='Exit', command=root.destroy)  # Making exit button (just in case you are running on trinket.io)
myentry.pack()  # Packing everything on the screen
runbutton.pack()
savebutton.pack()
deletebutton.pack()
openbutton.pack()
executebutton.pack()
helpbutton.pack()
exitbutton.pack()
code.pack()
theoutput.pack()
root.mainloop()  # Looping everything all over again
