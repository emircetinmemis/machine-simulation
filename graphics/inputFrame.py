from   tkinter  import ttk
import tkinter  as tk
from constants import INPUT_TXT_PATH

class InputFrame(tk.Frame) :
    def __init__(self, parent, root, *args, **kwargs) :
        super().__init__(parent, *args, **kwargs)

        self.root = root

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.isFirst = True

        self.style = ttk.Style()

        self.inputArea = tk.Text(self, height=10, width=25, wrap="word", font=("Cambiria", 12, "bold"), foreground="black", background="gray86", selectbackground="black", selectforeground="yellow")
        self.inputArea.grid(row=0, column=0, sticky="nsew")
        self.inputArea.focus_force()

        areaScrollBarY = ttk.Scrollbar(self, orient="vertical", command=self.inputArea.yview)
        areaScrollBarY.grid(row=0, column=1, sticky="nsew")

        self.inputArea.config(yscrollcommand=areaScrollBarY.set)

        self.inputArea.insert(tk.END, "Enter the assembly code here")
        self.inputArea.bind("<Button-1>", self.clearTextContent)

        self.inputArea.bind("<Delete>", self.clearTextContent)
    
    def clearTextContent(self, *event) :
        self.inputArea.delete("1.0", tk.END)
        self.inputArea.unbind("<Button-1>")

    def saveAndCloseTextContent(self) :
        self.inputArea.config(state="disabled")

        with open(INPUT_TXT_PATH, 'w') as f:
            f.write(self.inputArea.get("1.0", tk.END).rstrip())

