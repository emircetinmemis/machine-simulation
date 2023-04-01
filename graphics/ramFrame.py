from   utilities    import (
    reverse_sign_op, 
    RAM
)
from   tkinter      import ttk
import tkinter      as tk

class RamFrame(tk.Frame) :

    def __init__(self, parent, root, *args, **kwargs) :
        """
        I'm trying to create a frame within a frame, and then I'm trying to configure the inner frame
        
        :param parent: The parent widget
        :param root: The root window
        """
        super().__init__(parent, *args, **kwargs)

        self.configure(background="gray74")

        self.root = root

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.ramContainerFrame = ttk.Frame(self, relief="solid", borderwidth=1)
        self.ramContainerFrame.grid(row=0, column=0)

        #self.ramContainerFrame.configure(background="gray74")
        self.resetRamScreen()
        
    def loadRamLabels(self) :
        """
        It takes a list of RAM values, and creates a list of labels for each RAM value
        """
        self.ramLabels = []

        for i in range(len(self.ramValues)) :
            if reverse_sign_op(self.ramValues[i].value) != "0x0" :
                self.ramLabels.append([str(self.ramValues[i].address +" "+ reverse_sign_op(self.ramValues[i].value)), True])
            else :
                self.ramLabels.append([str(self.ramValues[i].address +" "+ reverse_sign_op(self.ramValues[i].value)), False])

    def resetRamScreen(self) :
        """
        It creates a new RAM object, assigns the RAM object's registers to a variable, and then calls
        two functions to load the RAM labels and grid the RAM labels
        """
        self.ramObj = RAM()
        self.ramValues = self.ramObj.registers
        self.loadRamLabels()
        self.gridRamLabels()

    def updateRamScreen(self) :
        """
        It takes the values from the RAM object and puts them into the labels on the GUI
        """
        self.ramObj = self.root.ram
        self.ramValues = self.ramObj.registers
        self.loadRamLabels()
        self.clearContainer()
        self.gridRamLabels()

    def gridRamLabels(self) :
        """
        It creates a grid of labels and places them in a frame
        """
        matrixSize = 16
        fontSize = 11
        currentColumn = 0
        currentRow = 0

        for i in range(len(self.ramLabels)) :
            if self.ramLabels[i][1] :
                self.ramLabels[i][0] = tk.Label(self.ramContainerFrame, text=" "+self.ramLabels[i][0].upper().replace("X","x")+" ", font=("Cambiria Math", fontSize, "bold"), bg="black", fg="yellow")
            else :
                self.ramLabels[i][0] = tk.Label(self.ramContainerFrame, text=" "+self.ramLabels[i][0].upper().replace("X","x")+" ", font=("Cambiria Math", fontSize, "bold"), bg="white", fg="black")

            self.ramLabels[i][0].grid(row=currentRow, column=currentColumn, sticky="nsew", padx=7, pady=7)
            self.ramLabels[i][0].configure(borderwidth=1, relief="solid")

            currentColumn += 1

            if currentColumn == matrixSize :
                currentColumn = 0
                currentRow += 1

    def clearContainer(self) :
        """
        It destroys all the widgets in the ramContainerFrame.
        """
        for child in self.ramContainerFrame.winfo_children() :
            child.destroy()