# -*- decoding=utf-8 -*-
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import FocusBehavior


class ButtonFocus(MDRaisedButton, FocusBehavior):
    ...


class SenhaCard(MDCard):
    def fechar_card(self):
        self.parent.remove_widget(self)


class LoginScreen(FloatLayout):
    def abrir_card(self):
        self.add_widget(SenhaCard())


class BarberShop(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Brown'
        self.theme_cls.primary_hue = '300'
        self.theme_cls.accent_palette = 'Orange'
        self.theme_cls.accent_hue = '300'
        return Builder.load_file('app.kv', 'utf-8')


BarberShop().run()
