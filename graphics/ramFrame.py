from utilities import RAM
from    utilities import reverse_sign_op
from   tkinter  import ttk
import tkinter  as tk

class RamFrame(tk.Frame) :
    def __init__(self, parent, root, *args, **kwargs) :
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
        self.ramLabels = []

        for i in range(len(self.ramValues)) :
            if reverse_sign_op(self.ramValues[i].value) != "0x0" :
                self.ramLabels.append([str(self.ramValues[i].address +" "+ reverse_sign_op(self.ramValues[i].value)), True])
            else :
                self.ramLabels.append([str(self.ramValues[i].address +" "+ reverse_sign_op(self.ramValues[i].value)), False])

    def resetRamScreen(self) :
        self.ramObj = RAM()
        self.ramValues = self.ramObj.registers
        self.loadRamLabels()
        self.gridRamLabels()

    def updateRamScreen(self) :
        self.ramObj = self.root.ram
        self.ramValues = self.ramObj.registers
        self.loadRamLabels()
        self.clearContainer()
        self.gridRamLabels()

    def gridRamLabels(self) :
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
        for child in self.ramContainerFrame.winfo_children() :
            child.destroy()