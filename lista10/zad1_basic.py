import tkinter as tk
 

class Calculator(tk.Frame):
    def __init__(self, master=None):
        self.result = tk.StringVar()
        self.base = tk.StringVar()
        self.base.set("dec")

        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="First no:").grid(column=0, row=0, columnspan=2)
        self.first = tk.Entry(
            self,
            justify='right',
        )
        self.first.grid(column=2, row=0, columnspan=2)

        tk.Label(self, text="Second no:").grid(column=0, row=1, columnspan=2)
        self.second = tk.Entry(
            self,
            justify='right',
        )
        self.second.grid(column=2, row=1, columnspan=2)

        tk.Button(
            self,
            text="+",
            command=self.add
        ).grid(column=0, row=2, ipadx=25)

        tk.Button(
            self,
            text="-",
            command=self.sub
        ).grid(column=1, row=2, ipadx=25)

        tk.Button(
            self,
            text="*",
            command=self.mul
        ).grid(column=2, row=2, ipadx=25)

        tk.Button(
            self,
            text="/",
            command=self.div
        ).grid(column=3, row=2, ipadx=25)

        tk.Label(self, text="Output base:").grid(column=0, row=3, columnspan=2)
        tk.Radiobutton(self, text="Decimal", variable=self.base, value="dec").grid(column=2, row=3)
        tk.Radiobutton(self, text="Binary", variable=self.base, value="bin").grid(column=3, row=3)

        self.output = tk.Entry(self,  justify='right')
        self.output["state"] = "readonly"
        self.output["textvariable"] = self.result
        self.output.grid(columnspan=4, ipadx=100)

    def op(self, op):
        # use int() to prevent evil action in eval :P
        operation = f"{int(self.first.get())}{op}{int(self.second.get())}"

        if self.base.get() == "bin":
            operation = f"bin({operation})"

        self.result.set(eval(operation))

    def mul(self):
        self.op("*")

    def div(self):
        self.op("/")

    def add(self):
        self.op("+")

    def sub(self):
        self.op("-")


root = tk.Tk()
root.title("My Dumb Calc")

app = Calculator(master=root)
app.mainloop()
