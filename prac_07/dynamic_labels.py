"""
CP1404/CP5632 Practical
Kivy GUI program to create dynamic labels
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelApp(App):
    """Main program - Kivy app to create dynamic label."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.users = ["Harry James Potter", "Ronald Bilius Weasley", "Hermione Jean Granger",\
            "Albus Percival Wulfric Brian Dumbledore", "Severus Tobias Snape", "Rubeus Hagrid",\
                "George Weasley", "Fred Weasley", "Tom Marvolo Riddle"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from list user name and add them to the GUI."""
        for name in self.users:
            # create a label for each data in the list
            temp_label = Label(text=name, size_hint_y=0.1)
            # add the label to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_label)


DynamicLabelApp().run()
