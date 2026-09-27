from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Calculator(App):

    def build(self):
        self.expression = ""

        main = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=8
        )

        # Строка с примером
        self.example = Label(
            text="",
            font_size=28,
            halign="right",
            valign="middle",
            size_hint_y=0.18
        )

        # Строка с ответом
        self.result = Label(
            text="0",
            font_size=42,
            halign="right",
            valign="middle",
            size_hint_y=0.18
        )

        main.add_widget(self.example)
        main.add_widget(self.result)

        buttons = [
            "(", ")", "C", "⌫",
            "7", "8", "9", "÷",
            "4", "5", "6", "×",
            "1", "2", "3", "−",
            "0", ".", "=", "+"
        ]

        grid = GridLayout(
            cols=4,
            spacing=5
        )

        for text in buttons:
            button = Button(
                text=text,
                font_size=27
            )

            button.bind(on_press=self.press_button)
            grid.add_widget(button)

        main.add_widget(grid)

        return main

    def press_button(self, button):
        value = button.text

        if value == "C":
            self.expression = ""
            self.example.text = ""
            self.result.text = "0"

        elif value == "⌫":
            self.expression = self.expression[:-1]
            self.update_screen()

        elif value == "=":
            self.calculate()

        else:
            conversions = {
                "×": "*",
                "÷": "/",
                "−": "-"
            }

            self.expression += conversions.get(value, value)
            self.update_screen()

    def update_screen(self):
        visible = self.expression

        visible = visible.replace("*", " × ")
        visible = visible.replace("/", " ÷ ")
        visible = visible.replace("-", " − ")
        visible = visible.replace("+", " + ")

        self.example.text = visible

    def calculate(self):
        if not self.expression:
            return

        try:
            # Разрешаем только цифры и математические символы
            allowed = "0123456789+-*/(). "

            if any(char not in allowed for char in self.expression):
                self.result.text = "Ошибка"
                return

            answer = eval(self.expression, {"__builtins__": None}, {})

            if isinstance(answer, float) and answer.is_integer():
                answer = int(answer)

            self.result.text = str(answer)

        except:
            self.result.text = "Ошибка"


Calculator().run()