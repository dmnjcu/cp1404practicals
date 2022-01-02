"""
CP1404/CP5632 Practical
Kivy GUI program to convert Miles to Kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesKmApp(App):
    """
    ConvertMilesKmApp is a Kivy App for converting Miles to Kilometres
    """
    def build(self):
        """
        Build the Kivy app from the kv file
        """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        """
        Handle convert (could be button press or other call), output result to label widget
        """
        m = int(self.root.ids.input_number.text)
        km = round(m*1.609344, 3)
        self.root.ids.output_number.text = str(km)

    def handle_up_down(self, value):
        """
        Handle event when press up or down button (could be button press or other call), output result to label widget
        """
        self.root.ids.input_number.text = str(int(self.root.ids.input_number.text) + value)


ConvertMilesKmApp().run()
