import cv2
import numpy as np

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics.texture import Texture


class ImageClassifierApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10,
        )

        title = Label(
            text="OpenCV Image Demo",
            font_size=24,
            size_hint=(1, 0.1),
        )

        self.image_widget = Image(
            size_hint=(1, 0.7),
        )

        self.result = Label(
            text="Press the button",
            size_hint=(1, 0.1),
        )

        button = Button(
            text="Process Image",
            size_hint=(1, 0.1),
        )

        button.bind(on_press=self.process_image)

        layout.add_widget(title)
        layout.add_widget(self.image_widget)
        layout.add_widget(self.result)
        layout.add_widget(button)

        return layout

    def process_image(self, instance):

        image = np.zeros((300, 300, 3), dtype=np.uint8)

        cv2.circle(
            image,
            (150, 150),
            80,
            (0, 255, 0),
            -1,
        )

        image = cv2.flip(image, 0)

        texture = Texture.create(
            size=(300, 300),
            colorfmt="bgr",
        )

        texture.blit_buffer(
            image.tobytes(),
            colorfmt="bgr",
            bufferfmt="ubyte",
        )

        self.image_widget.texture = texture

        self.result.text = (
            "Class: Green Circle\n"
            "Confidence: 98.5%"
        )


if __name__ == "__main__":
    ImageClassifierApp().run()
