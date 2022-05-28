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
    code.edit_redo()
    
    
def undo(filler):
    code.edit_undo()
    
    
def execute():
    output, error = subprocess.Popen(myentry.get().split(' '), stdout = subprocess.PIPE).communicate()  # Getting the output and the error
    os.system(myentry.get())
    theoutput.delete('1.0', tkinter.END)  # Deleting last output tezt
    theoutput.insert('1.0', output)  # Inserting output
