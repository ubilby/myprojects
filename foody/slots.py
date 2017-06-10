"""
Пользовательские слоты для виджетов.
"""

# Импортируем класс интерфейса из созданного конвертером модуля
from ui import Ui_Form


# Создаём собственный класс, наследуясь от автоматически сгенерированного
class MainWindowSlots(Ui_Form):

    def view_dish(self):
        pass


    def check_the_box(self):       
        if self.comboBox.currentText() == "Борщ":
            self.label.setText("Fuck YEAH!")
        
        elif self.comboBox.currentText() == "Плов":
            self.label.setText("Shock sheet")
