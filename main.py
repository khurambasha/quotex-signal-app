from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class SignalApp(App):
def build(self):
Window.clearcolor = (0.08, 0.10, 0.15, 1)

    layout = BoxLayout(
        orientation="vertical",
        padding=20,
        spacing=15
    )

    title = Label(
        text="QUOTEX SIGNAL BOT",
        font_size="25sp",
        bold=True,
        size_hint_y=0.2
    )
    layout.add_widget(title)

    self.status = Label(
        text="Signal app ready\nLive market data not connected",
        font_size="17sp"
    )
    layout.add_widget(self.status)

    info = Label(
        text="EMA 9 / EMA 21 / RSI 14\nTesting mode only",
        font_size="16sp"
    )
    layout.add_widget(info)

    button = Button(
        text="CHECK SIGNAL",
        font_size="18sp",
        size_hint_y=0.2
    )
    button.bind(on_press=self.check_signal)
    layout.add_widget(button)

    return layout

def check_signal(self, instance):
    self.status.text = (
        "WAITING FOR MARKET DATA\n"
        "No live signal available yet"
    )

if name == "main":
SignalApp().run()
