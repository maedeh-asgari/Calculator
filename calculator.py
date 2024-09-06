import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalculatorGridLayout(GridLayout):
    def calculate(self, event):
        if event:
            try:
                self.display.text = str(eval(event))
            except:
                self.display.text = "Error!"

class Calculator(App):
    def build(self):
        return CalculatorGridLayout()
    
    def display_color(self, text):
        if text == "Error!":
            return (1, 0, 0, 1)
        return (0, 0, 0, 1)

if __name__ == '__main__':
    Calculator().run()