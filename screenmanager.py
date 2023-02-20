from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.pickers import MDDatePicker

from core import *


class Departamentos(Screen):
    pass
class Escalas(Screen):
    pass
class AgendaEventos(Screen):
    pass
class CadastroAluno(Screen):
    pass
class CadastroMembro(Screen):


    def cadastrar_membro(self,nome,cpf,data_nasc,data_membro,endereco,congregacao,departamento,cargo):
       membro={'nome':nome,
               'cpf':cpf,
               'data_nascimento':data_nasc,
               'data_membro':data_membro,
               'endereco':endereco,
               'congregacao':congregacao,
               'departamento':departamento,
               'cargo':cargo
               }
    def on_cancel_since(self,instance, value):
        self.manager.get_screen('cad_membro').ids.data_membro.text = ""

    def on_save_since(self,instance, value, date_range):
        data = converte_utc(value)
        self.manager.get_screen('cad_membro').ids.data_membro.text=data
    def showDatePickerSince(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save_since, on_cancel=self.on_cancel_since)
        date_dialog.open()
    def on_cancel(self,instance, value):
        self.manager.get_screen('cad_membro').ids.data_nasc.text = ""

    def on_save(self,instance, value, date_range):
        data = converte_utc(value)

        self.manager.get_screen('cad_membro').ids.data_nasc.text=data
    def showDatePicker(self):
        date_dialog = MDDatePicker()

        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

class AcaoSocial(Screen):
    pass
class EBD(Screen):
    pass
class Dashboard(Screen):
    pass
class Login(Screen):
    pass

class MainScreenManager(ScreenManager):
    pass