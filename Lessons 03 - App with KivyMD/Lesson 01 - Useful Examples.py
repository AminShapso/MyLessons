from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class Main01App(App):
    def on_press_button(self, instance):
        self.on_press_button_2()

    def on_press_button_2(self):
        print('You pressed the button!')

    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        btn = Button(text="Button", background_color="red")
        btn.bind(on_release=self.on_press_button)   # on_press is in main01 constructor
        layout.add_widget(btn)
        label = Label(text='Hello from Kivy', size_hint=(1, 1), pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(label)
        img = Image(source=r"C:\Users\USER\Pictures\Snuba Diving Eilat 13-09-2016\AMBA0009.jpg", size_hint=(1, .5), pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(img)
        layout.add_widget(Button())
        return layout


if __name__ == '__main__':
    app = Main01App()
    app.run()
