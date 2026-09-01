"""Calculator logic independent from the Tkinter user interface."""


class Calculator:
    """Evaluate the expression currently being entered by the user."""

    def __init__(self):
        self.expression = ""

    def press(self, value):
        if value == "C":
            self.expression = ""
        elif value == "backspace":
            self.expression = self.expression[:-1]
        elif value == "=":
            self.expression = self._calculate()
        else:
            if self.expression == "Error":
                self.expression = ""
            self.expression += value
        return self.expression

    def _calculate(self):
        try:
            result = eval(self.expression, {"__builtins__": {}}, {})
            return str(result)
        except Exception:
            return "Error"
