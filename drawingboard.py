from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyPaintWidget(Widget):
    def __init__(self, label, **kwargs):
        super(MyPaintWidget, self).__init__(**kwargs)
        self.label = label

    def update_label_text(self, text):
        self.label.text = text

    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 25
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            self.update_label_text(f"{touch.ud['line'].points}")

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
        self.update_label_text(f"{[touch.x, touch.y]}")


class MyPaintApp(App):
    def build(self):
        parent = Widget()
        label = Label(text=' ')
        self.painter = MyPaintWidget(label)
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)

        # Add the widgets to the BoxLayout in the desired order
        parent.add_widget(label)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

if __name__ == '__main__':
    MyPaintApp().run()
