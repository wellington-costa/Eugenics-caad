import os

from kaki.app import App
from kivy.factory import Factory
from kivymd.app import MDApp






class CaadApp(MDApp, App):
    DEBUG = 1  # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "screenmanager.kv")
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "screenmanager"

    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self):
     return Factory.MainScreenManager()

if __name__ == '__main__':
 CaadApp().run()


