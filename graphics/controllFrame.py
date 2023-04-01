from    tkinter     import  ttk
import  tkinter     as      tk

class ControllFrame(tk.Frame) :

    def __init__(self, parent, root, *args, **kwargs) :
        """
        It creates a frame with 5 buttons, each with a different function
        
        :param parent: The parent widget
        :param root: the root window
        """
        super().__init__(parent, *args, **kwargs)

        self.configure(background="gray74")

        self.root = root

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Cambiria", 11, "bold"), background="gray83", foreground="black")

        self.columnconfigure(1, weight=4)
        self.rowconfigure(0, weight=1)

        self.startButton = ttk.Button(self, text="Start", command=self.startMachine, cursor="hand2")
        self.startButton.grid(row=0, column=0, sticky="nsew")

        self.nextButton = ttk.Button(self, text="Next", state="disabled", command=self.root.runCompiler, cursor="hand2")
        self.nextButton.grid(row=0, column=1, sticky="nsew")

        self.photoButton = ttk.Button(self, text="Open Sheet", command=self.root.showPhoto, cursor="hand2")
        self.photoButton.grid(row=0, column=2, sticky="nsew")

        self.resetButton = ttk.Button(self, text="Reset", state="disabled", command=self.resetMachine, cursor="hand2")
        self.resetButton.grid(row=0, column=3, sticky="nsew")

        self.exitButton = ttk.Button(self, text="Exit", command=self.root.destroy, cursor="hand2")
        self.exitButton.grid(row=0, column=4, sticky="nsew")

        for button in self.winfo_children() :
            button.grid_configure(padx=20, pady=5, ipadx=5, ipady=5)

    def startMachine(self) :
        """
        It disables the start button, enables the reset and next buttons, saves the text content, loads
        the machine, and runs the compiler
        """
        self.startButton.config(state="disabled")
        self.resetButton.config(state="normal")
        self.nextButton.config(state="normal")

        self.root.inputSection.saveAndCloseTextContent()
        self.root.loadMachine()
        self.root.runCompiler()

    def resetMachine(self) :
        """
        It resets the GUI to its initial state.
        """
        self.resetButton.config(state="disabled")
        self.nextButton.config(state="disabled", text="Next")
        self.startButton.config(state="normal")

        self.root.ramSection.resetRamScreen()
        self.root.infoSection.updateInfoScreen("","","","","","","","")

        self.root.inputSection.inputArea.config(state="normal")
        self.root.inputSection.inputArea.delete("1.0", tk.END)
        self.root.inputSection.inputArea.insert(tk.END, "Enter the assembly code here")
        self.root.inputSection.inputArea.bind("<Button-1>", self.root.inputSection.clearTextContent)
