from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(
            orientation="vertical",
            padding=30,
            spacing=20,
            **kwargs,
        )

        self.label = Label(
            text="Hello from Buildozer!",
            font_size="24sp",
        )
        self.add_widget(self.label)

        button = Button(
            text="Click me",
            size_hint=(1, 0.3),
        )
        button.bind(on_press=self.on_click)
        self.add_widget(button)

    def on_click(self, instance):
        self.label.text = "Your Android app is running!"


class MyApp(App):
    def build(self):
        return MainLayout()


if __name__ == "__main__":
    MyApp().run()
