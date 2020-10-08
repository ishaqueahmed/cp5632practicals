"""
CP5632 Practical 7

GUI program to display values from list as labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Initialise the app"""
        super().__init__(**kwargs)
        self.names_list = ["Alice", "Bob", "Charles"]

    def build(self):
        """Build the app from the .kv file"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from items in list"""
        for name in self.names_list:
            label_name = Label(text=name, id=name)
            self.root.ids.entries.add_widget(label_name)


DynamicLabelsApp().run()
