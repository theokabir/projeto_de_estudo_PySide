# IMPORTANDO MODULOS DE SISTEMA
import sys
import os

# IMPORTAÇÕES DO PySide6
from qt_core import *

# IMPORTANDO MAIN WINDOW
from gui.windows.main_window.ui_main_window import *

# CLASSE DA PRIMEIRA JANELA HERDANDO QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Curso de PySide6")
        
        self.ui = UI_Main_Window()
        self.ui.setup_ui(self)
        
        self.ui.toggle_button.clicked.connect(self.toggle_button)
        
        self.ui.button_1.clicked.connect(self.show_page_1)
        self.ui.button_2.clicked.connect(self.show_page_2)
        self.ui.settings_btn.clicked.connect(self.show_page_3)
        
        self.ui.ui_pages.pushButton.clicked.connect(self.change_text)
        
        self.show()
        
    def reset_selection(self):
        for btn in self.ui.left_box.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass
        
    def show_page_1(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.reset_selection()
        self.ui.button_1.set_active(True)
        
    def show_page_2(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page__2)
        self.reset_selection()
        self.ui.button_2.set_active(True)
        
    def show_page_3(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.reset_selection()
        self.ui.settings_btn.set_active(True)
    
    def toggle_button(self):
        menu_width = self.ui.left_box.width()
        
        width = 50
        if menu_width == 50:
            width = 240
            
        self.animation = QPropertyAnimation(self.ui.left_box, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()
        
    def change_text(self):
        nome = self.ui.ui_pages.lineEdit.text()
        if not nome or nome == "":
            nome = "..."
        self.ui.ui_pages.texto_nome.setText(f"Olá, {nome}")
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())