# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy_garden.webview import WebView


class BrowserApp(App):
    def build(self):
        self.title = "Kivy Browser"
        layout = BoxLayout(orientation='vertical')

        nav = BoxLayout(size_hint_y=0.1, spacing=5, padding=5)
        self.url = TextInput(text='https://www.google.com', multiline=False)
        go = Button(text='Git', size_hint_x=0.2)
        go.bind(on_press=self.navigate)
        nav.add_widget(self.url)
        nav.add_widget(go)
        layout.add_widget(nav)

        self.webview = WebView(url='https://www.google.com')
        layout.add_widget(self.webview)
        return layout

    def navigate(self, *args):
        url = self.url.text.strip()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        self.webview.url = url


if __name__ == '__main__':
    BrowserApp().run()
