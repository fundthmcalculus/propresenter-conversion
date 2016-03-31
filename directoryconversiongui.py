from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from os.path import expanduser
from propresenterconverter import propresenterconverter


class directoryconversiongui:
    def __init__(self):

        # Create the gui.
        self.window = Tk()
        self.window.title("Directory Converter")

        # Set the variables.
        self.inputdirectory = StringVar(value="")
        self.outputdirectory = StringVar(value="")

        # Add the variables.
        self.mainframe = ttk.Frame(self.window, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        self.inputdirbutton = ttk.Button(self.mainframe, text="Input Directory", command=self.inputdirbutton_click).\
            grid(column=1, row=1, sticky=(W, E))
        self.outputdirbutton = ttk.Button(self.mainframe, text="Output Directory", command=self.outputdirbutton_click).\
            grid(column=1, row=2, sticky=(W, E))
        self.processbutton = ttk.Button(self.mainframe, text="Convert!", command=self.processbutton_click).\
            grid(column=1, row=3, sticky=(W, E))

        self.inputdirlabel = ttk.Label(self.mainframe, textvariable=self.inputdirectory).grid(column=2, columnspan=2,
                                                                                              row=1, sticky=(W, E))
        self.outputdirlabel = ttk.Label(self.mainframe, textvariable=self.outputdirectory).grid(column=2, columnspan=2,
                                                                                                row=2, sticky=(W, E))

        # Minimum width for the label.
        self.mainframe.columnconfigure(2, minsize=200)

        # Options for opening a directory.
        self.dir_opt = options = {}
        options['initialdir'] = expanduser("~")
        options['mustexist'] = False
        options['parent'] = self.mainframe
        options['title'] = 'Choose Folder'

    def inputdirbutton_click(self):
        # Show the folder choice dialog.
        self.dir_opt['title'] = 'Choose Input Directory'
        inputdir = filedialog.askdirectory(**self.dir_opt)
        if inputdir is None:
            inputdir = ""

        self.inputdirectory.set(inputdir)

        self.mainframe.update_idletasks()

    def outputdirbutton_click(self):
        # Show the folder choice dialog.
        self.dir_opt['title'] = 'Choose Input Directory'
        outputdir = filedialog.askdirectory(**self.dir_opt)
        if outputdir is None:
            outputdir = ""

        self.outputdirectory.set(outputdir)

        self.mainframe.update_idletasks()

    def processbutton_click(self):
        # TODO - Run the conversion code with the appropriate arguments.
        ppconv = propresenterconverter(arglist=['-inputdir', self.inputdirectory.get(), '-outputdir',
                                                self.outputdirectory.get()])
        ppconv.convert()
        return

    def show(self):
        # Start running the main loop.
        self.window.mainloop()
