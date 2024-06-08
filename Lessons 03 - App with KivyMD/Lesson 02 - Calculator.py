"""
Link to GitHub:
https://github.com/mnrclab/Build_Mobile_App_With_Python_Kivy_Framework
"""


from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.utils import platform
if platform == "android":
    from jnius import autoclass


# ## ### True ## False ### ## #
set_window_size = True
if platform == "android":
    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    ActivityInfo = autoclass("android.content.pm.ActivityInfo")
    activity = PythonActivity.mActivity
    activity.setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_USER)  # set orientation according to user's preference
elif set_window_size:
                                       
    Window.size = (540, 720)



class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=55)
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        h_layout = BoxLayout()
        equals_button = Button(text="=")
        equals_button.bind(on_press=self.on_solution)
        h_layout.add_widget(equals_button)

        edebug_button = Button(text="Debug", size_hint=(0.333333, 1))
        edebug_button.bind(on_press=self.print_debug)
        h_layout.add_widget(edebug_button)
        main_layout.add_widget(h_layout)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":      # Clear the solution widget
            self.solution.text = ""
        else:
            if self.solution.text == "ERROR":
                current = ""
            if current == "" and button_text in self.operators:
                return  # First character cannot be an operator
            elif current and (self.last_was_operator and button_text in self.operators):
                new_text = current[:-1] + button_text
            else:
                new_text = current + button_text
            self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                solution = str(eval(self.solution.text))
            except:
                solution = "ERROR"
            self.solution.text = solution

    def print_debug(self, instance):
        self.solution.text = f'x = {Window.size[0]}, y = {Window.size[1]}'


if __name__ == "__main__":
    app = MainApp()
    app.run()
