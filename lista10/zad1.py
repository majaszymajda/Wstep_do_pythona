import tkinter as tk


class Calculator(tk.Frame):
    def __init__(self, master=None):
        self.last_op_was_num = None
        self.last_op = None
        self.last_result = 0

        self.result = tk.StringVar()
        super().__init__(master)
        self.master = master
        self.grid()

        self.buttons = [
            [("7", self.btn_7), ("8", self.btn_8), ("9", self.btn_9), ("*", self.mul)],
            [("4", self.btn_4), ("5", self.btn_5), ("6", self.btn_6), ("/", self.div)],
            [("1", self.btn_1), ("2", self.btn_2), ("3", self.btn_3), ("-", self.sub)],
            [("C", self.clear), ("0", self.btn_0), ("=", self.equal), ("+", self.add)],
        ]
        self.create_widgets()

    def create_widgets(self):
        self.output = tk.Entry(self,  justify='right')
        self.output["state"] = "readonly"
        self.output["textvariable"] = self.result
        self.output.grid(columnspan=4, ipadx=100)

        for r in range(4):
            for c in range(4):
                tk.Button(
                    self,
                    text=self.buttons[r][c][0],
                    command=self.buttons[r][c][1],
                ).grid(row=r+2, column=c, ipadx=25)

    def btn_0(self):
        self.btn_no(0)

    def btn_1(self):
        self.btn_no(1)

    def btn_2(self):
        self.btn_no(2)

    def btn_3(self):
        self.btn_no(3)

    def btn_4(self):
        self.btn_no(4)

    def btn_5(self):
        self.btn_no(5)

    def btn_6(self):
        self.btn_no(6)

    def btn_7(self):
        self.btn_no(7)

    def btn_8(self):
        self.btn_no(8)

    def btn_9(self):
        self.btn_no(9)

    def btn_no(self, no):
        if self.last_op_was_num:
            res = self.result.get() + str(no)
            self.result.set(res)
        else:
            self.result.set(no)
            self.last_op_was_num = True

    def clear(self):
        self.result.set(0)
        self.last_op_was_num = False
        self.last_op = None

    def op(self, op):
        if not self.last_op_was_num:
            # We only changeing operation
            self.last_op = op
            return

        self.evaluate()
        self.last_result = self.result.get()
        self.last_op = op
        self.last_op_was_num = False

    def mul(self):
        self.op("*")

    def div(self):
        self.op("/")

    def add(self):
        self.op("+")

    def sub(self):
        self.op("-")

    def equal(self):
        self.evaluate()
        self.last_result = self.result.get()
        self.last_op = None

    def evaluate(self):
        if self.last_op is None:
            # There was no operation to evaluate
            return

        operation = f"{self.last_result}{self.last_op}{self.result.get()}"

        try:
            self.result.set(eval(operation))
        except ZeroDivisionError:
            self.result.set("ERROR - dividing by 0")
            self.last_op_was_num = False
            self.last_op = None


root = tk.Tk()
root.title("My Super Calc")

app = Calculator(master=root)
app.mainloop()
