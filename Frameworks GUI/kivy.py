from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Criação de um rótulo
        label = Label(text="Olá, Kivy!")
        layout.add_widget(label)

        # Criação de um botão
        button = Button(text="Clique em mim")
        button.bind(on_press=self.on_button_click)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        print("Botão clicado!")

if _name_ == "_main_":
    MyApp().run()
