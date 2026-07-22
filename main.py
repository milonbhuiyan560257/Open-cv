from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=20
        )

        title = Label(
            text="Hello Android APK",
            font_size='24sp'
        )

        button = Button(
            text="Click Me"
        )

        result = Label(
            text="Ready"
        )

        def on_button_press(instance):
            result.text = "Button Clicked!"

        button.bind(on_press=on_button_press)

        layout.add_widget(title)
        layout.add_widget(button)
        layout.add_widget(result)

        return layout


if __name__ == "__main__":
    MyApp().run()
