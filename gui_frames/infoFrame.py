from   tkinter  import ttk
import tkinter  as tk
from cv2 import line

from pyrsistent import v

class InfoFrame(tk.Frame) :

    def __init__(self, parent, root, *args, **kwargs) :
        super().__init__(parent, *args, **kwargs)

        self.root = root

        self.configure(background="gray74")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.lineNumber = tk.StringVar(value="Line Number  :  ")
        self.currentInstruction = tk.StringVar(value="Current Instruction  : ")
        self.CI_BIN = tk.StringVar(value="BIN  :  ")
        self.CI_HEX = tk.StringVar(value="HEX  :  ")
        self.CI_DEC = tk.StringVar(value="DEC  :  ")
        self.accumulator = tk.StringVar(value="Accumulator  :  ")
        self.AC_BIN = tk.StringVar(value="BIN  :  ")
        self.AC_HEX = tk.StringVar(value="HEX  :  ")
        self.AC_DEC = tk.StringVar(value="DEC  :  ")

        lineNumberLabel = ttk.Label(self, textvariable=self.lineNumber)
        currentInstructionLabel = ttk.Label(self, textvariable=self.currentInstruction)
        CI_BINLabel = ttk.Label(self, textvariable=self.CI_BIN)
        CI_HEXLabel = ttk.Label(self, textvariable=self.CI_HEX)
        CI_DECLabel = ttk.Label(self, textvariable=self.CI_DEC)
        accumulatorLabel = ttk.Label(self, textvariable=self.accumulator)
        AC_BINLabel = ttk.Label(self, textvariable=self.AC_BIN)
        AC_HEXLabel = ttk.Label(self, textvariable=self.AC_HEX)
        AC_DECLabel = ttk.Label(self, textvariable=self.AC_DEC)

        lineNumberLabel.grid(row=0, column=0)
        currentInstructionLabel.grid(row=1, column=0)
        CI_BINLabel.grid(row=2, column=0)
        CI_HEXLabel.grid(row=3, column=0)
        CI_DECLabel.grid(row=4, column=0)
        ttk.Label(self, text="").grid(row=5, column=0)
        accumulatorLabel.grid(row=6, column=0)
        AC_BINLabel.grid(row=7, column=0)
        AC_HEXLabel.grid(row=8, column=0)
        AC_DECLabel.grid(row=9, column=0)
        ttk.Label(self, text="").grid(row=10, column=0)

        for label in self.winfo_children() :
            label.configure(font=("Cambiria", 11, "bold"), anchor="center", justify="center", background="gray74")

    def updateInfoScreen(self, lineNumber, currentInstruction, CI_BIN, CI_HEX, CI_DEC, AC_BIN, AC_HEX, AC_DEC) :

        self.lineNumber.set(f"Line Number  :  {lineNumber}")
        self.currentInstruction.set(f"Current Instruction  : {currentInstruction}")
        self.CI_BIN.set(f"BIN  :  {CI_BIN}")
        self.CI_HEX.set(f"HEX  :  {CI_HEX}")
        self.CI_DEC.set(f"DEC  :  {CI_DEC}")
        self.accumulator.set("Accumulator  :  ")
        self.AC_BIN.set(f"BIN  :  {AC_BIN}")
        self.AC_HEX.set(f"HEX  :  {AC_HEX}")
        self.AC_DEC.set(f"DEC  :  {AC_DEC}")