# -*- coding: utf-8 -*-
"""Small sample Kivy app used to smoke-test the Android workflow."""
from kivy.app import App
from kivy.lang import Builder

KV = """
BoxLayout:
    orientation: "vertical"
    padding: "24dp"
    spacing: "16dp"
    canvas.before:
        Color:
            rgba: 0.06, 0.09, 0.16, 1
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: "Kivy APK Sample"
        font_size: "28sp"
        bold: True
        color: 0.35, 0.78, 1, 1
    Label:
        id: status
        text: "Built with the Android Integration workflow"
        halign: "center"
        valign: "middle"
        text_size: self.width, None
    Button:
        text: "Tap to test"
        size_hint_y: None
        height: "52dp"
        on_release:
            app.tap_count += 1
            status.text = "It works! Taps: " + str(app.tap_count)
"""

class SampleApp(App):
    title = "Kivy APK Sample"
    tap_count = 0

    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    SampleApp().run()
