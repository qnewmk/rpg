from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from itens import *
nome_item = input('adaga, espada media, espada grande, escudo ')
class Game(App):
    def build(self):
        self.item = pega_item(nome_item)
        texto_item = f'item : {self.item["nome"]}\nmãos : {self.item["maos"]}\ndano : {self.item["dano"]}'
        box = BoxLayout(orientation='vertical')
        self.label = Label(text='coisas sobre o jogo',font_size = 10)
        box.add_widget(self.label)
        self.label = Label(text=f'{texto_item}',font_size = 30)
        box.add_widget(self.label)
        return box


Game().run()

#print(f'item : {item["nome"]}\nmãos : {item["maos"]}\ndano : {item["dano"]}')
