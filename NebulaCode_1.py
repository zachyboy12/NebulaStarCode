# Reminder: Continue commenting. Left out at: def _run():
import tkinter, os, subprocess, tkinter.messagebox as filedialog  # Importing modules (see what each of them does below)
"""
tkinter - Creating GUI (Graphical User Interface)
os - Doing commands; Deleting files; Running code
subprocess - Shows terminal output of code
"""


def editandrun():  # Editing code and running it
    
    
    def run(filler):  # Main run function for running program
        
        
        def check(theroot, thefilename):  # Checks if extension is .py, .htm, or .html
            if thefilename.split('.')[1] == 'py':
                os.system('python3 ' + thefilename)
                cmd = ['python3', thefilename]
                output = subprocess.Popen( cmd, stdout = subprocess.PIPE ).communicate()[0]
                myoutput = tkinter.Label(theroot, text = output)
                myoutput.configure(background=str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
                myoutput.pack()
            elif thefilename.split('.')[1] == 'html' or thefilename.split('.')[1] == 'htm' or thefilename.split('.')[1] == 'ps':
                os.system('open ' + thefilename)
                output = ''
                cmd = ['open', thefilename]
                output = subprocess.Popen( cmd, stdout = subprocess.PIPE ).communicate()[0]
                myoutput = tkinter.Label(theroot, text = output)
                myoutput.configure(background=str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
                myoutput.pack()
            
            
        myroot = tkinter.Toplevel()
        myroot.title('Run file')
        filedialog.showwarning('ALERT', 'WARNING: INPUT FUNCTION AND TKINTER MODULE MIGHT NOT WORK')
        myroot.configure(background = str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
        myfile = tkinter.Entry(myroot)
        myget = tkinter.Button(myroot, text = 'Run', command = lambda: check(myroot, myfile.get()))
        mylabel = tkinter.Label(myroot, text = 'Output:')
        myfile.pack()
        myget.pack()
        mylabel.pack()
        myroot.mainloop()
            
            
            
    def openfile(toplevel, name):  # Root of savefile function
        open(name, 'w').write(str(tb.get("1.0", "end-1c")))
        toplevel.destroy()
        
        
    def savefile(filler):  # Saves file for shortcut key
        nextroot = tkinter.Toplevel()
        nextroot.title('Save file')
        nextroot.configure(background = str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
        myentry = tkinter.Entry(nextroot)
        mybutton = tkinter.Button(nextroot, text = "Save file", command = lambda: openfile(nextroot, myentry.get()))
        myentry.pack()
        mybutton.pack()
        nextroot.mainloop()
        
        
    def kill(filler):  # Destroys window for shortcut key
        root.destroy()
        
        
    def destroyfile(filler):  # Deletes file for shortcut key
        
        
        def dfroot(value, aroot):
            os.remove(value)
            aroot.destroy()
            
            
        mamaroot = tkinter.Tk()
        mamaroot.configure(background = str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
        mamaroot.title('Delete a file')
        mamaentry = tkinter.Entry(mamaroot)
        mamabutton = tkinter.Button(mamaroot, text = 'Delete file', command = lambda: dfroot(mamaentry.get(), mamaroot))
        mamaentry.pack()
        mamabutton.pack()
        mamaroot.mainloop()
            
            
            
    def _run():
        
        
        def check(theroot, thefilename):
            if thefilename.split('.')[1] == 'py':
                os.system('python3 ' + thefilename)
                cmd = ['python3', thefilename]
                output = subprocess.Popen(cmd, stdout = subprocess.PIPE).communicate()[0]
                myoutput = tkinter.Label(theroot, text = output)
                myoutput.configure(background=str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
                myoutput.pack()
            elif thefilename.split('.')[1] == 'html' or thefilename.split('.')[1] == 'htm':
                os.system('open ' + thefilename)
                output = ''
                cmd = ['open', thefilename]
                output = subprocess.Popen( cmd, stdout = subprocess.PIPE ).communicate()[0]
                myoutput = tkinter.Label(theroot, text = output)
                myoutput.configure(background=str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
                myoutput.pack()
            
            
        myroot = tkinter.Toplevel()
        myroot.title('Run file')
        filedialog.showwarning('ALERT', 'WARNING: INPUT FUNCTION AND TKINTER MODULE MIGHT NOT WORK')
        myroot.configure(background = str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
        myfile = tkinter.Entry(myroot)
        myget = tkinter.Button(myroot, text = 'Run', command = lambda: check(myroot, myfile.get()))
        mylabel = tkinter.Label(myroot, text = 'Output:')
        myfile.pack()
        myget.pack()
        mylabel.pack()
        myroot.mainloop()
        
        
    def _savefile():
        nextroot = tkinter.Toplevel()
        nextroot.title('Save file')
        nextroot.configure(background = str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
        myentry = tkinter.Entry(nextroot)
        mybutton = tkinter.Button(nextroot, text = "Save file", command = lambda: openfile(nextroot, myentry.get()))
        myentry.pack()
        mybutton.pack()
        nextroot.mainloop()
        
        
    def _kill():
        root.destroy()
        
        
    def _destroyfile():
        
        
        def dfroot(value, aroot):
            os.remove(value)
            aroot.destroy()
            
            
        mamaroot = tkinter.Tk()
        mamaroot.configure(background = str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
        mamaroot.title('Delete a file')
        mamaentry = tkinter.Entry(mamaroot)
        mamabutton = tkinter.Button(mamaroot, text = 'Delete file', command = lambda: dfroot(mamaentry.get(), mamaroot))
        mamaentry.pack()
        mamabutton.pack()
        mamaroot.mainloop()
        
        
        
    def _getfile():
        
        
        def mainfunc(rootname, name):
            tb.insert('1.0', open(name.get()).read())
            rootname.destroy()
        
        
        paparoot = tkinter.Toplevel()
        paparoot.title('Open file')
        paparoot.configure(background = str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
        filename = tkinter.Entry(paparoot)
        tb.delete('1.0', tkinter.END)
        getbutton = tkinter.Button(paparoot, text='Open file', command=lambda: mainfunc(paparoot, filename))
        filename.pack()
        getbutton.pack()
        paparoot.mainloop()
        
        
    root = tkinter.Tk()
    mytop = tkinter.Toplevel()
    mytop.title('File manager')
    mytop.geometry('400x150')
    mytop.configure(background =  str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
    savebutton = tkinter.Button(mytop, text='Save file', command=_savefile)
    runbutton = tkinter.Button(mytop, text='Run file', command=_run)
    deletebutton = tkinter.Button(mytop, text='Delete file', command=_destroyfile)
    openbutton = tkinter.Button(mytop, text='Open file', command=_getfile)
    destroywindow = tkinter.Button(mytop, text='Exit', command=_kill)
    savebutton.pack()
    runbutton.pack()
    deletebutton.pack()
    openbutton.pack()
    destroywindow.pack()
    root.title('NebulaCode: Edit and run!')
    tb = tkinter.Text(root)
    tb.configure(background = str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
    if str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', '').lower() == 'black':
        tb.configure(fg='white', insertbackground='white')
    else:
        pass
    
    
    def getfile(filler):
        
        
        def mainfunc(rootname, name):
            tb.insert('1.0', open(name.get()).read())
            rootname.destroy()
        
        
        paparoot = tkinter.Toplevel()
        paparoot.title('Open file')
        paparoot.configure(background = str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
        filename = tkinter.Entry(paparoot)
        tb.delete('1.0', tkinter.END)
        getbutton = tkinter.Button(paparoot, text='Open file', command=lambda: mainfunc(paparoot, filename))
        filename.pack()
        getbutton.pack()
        paparoot.mainloop()
        
 
    root.bind('<Control-s>', savefile)
    root.bind('<Control-r>', run)
    root.bind('<Control-k>', kill)
    root.bind('<Control-d>', destroyfile)
    root.bind('<Control-o>', getfile)
    tb.pack(expand=True, fill='both')
    root.mainloop()
    
    

def customize():
    
    
    def donecustomizing(theroot, colorname):
        theroot.destroy()
        open('NCcolor.txt', 'w').write(colorname)
    
    
    root = tkinter.Tk()
    root.configure(background = str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
    root.title('Customize NebulaCode')
    l1 = tkinter.Label(root, text='Background color:')
    color = tkinter.Entry(root)
    donebutton = tkinter.Button(root, text = 'Done customizing', command = lambda: donecustomizing(root, color.get()))
    l1.pack()
    color.pack()
    donebutton.pack()
    root.mainloop()    
    
    
def helpwindow():
    root = tkinter.Tk()
    mylabel = tkinter.Label(root, text = """About:
Copyright @ zachyboy12
Used with permission from the MIT License and command git clone https://github.com/zachyboy12/NebulaCode/
Shortcuts (for edit and run window only):
CTRL+r - Runs file
CTRL+o - Opens file""")
    
    
    

root = tkinter.Tk()


def killroot(filler): 
    root.destroy()
    
    
root.title('NebulaCode')
root.attributes('-topmost', True)
root.focus_force()
root.geometry('400x150')
root.configure(background = str(open('NCcolor.txt').read()).replace('[', '').replace("'", '').replace(']', ''))
mainbutton = tkinter.Button(root, text='Edit files and run them!', command = editandrun)
customizebutton = tkinter.Button(root, text = 'Customize NebulaCode!', command = customize)
mainbutton.pack()
customizebutton.pack()
root.mainloop()
