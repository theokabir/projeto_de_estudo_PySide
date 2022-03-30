from qt_core import *
from gui.pages.ui_pages import Ui_application
from gui.widgets.py_push_button import pyPushButton

class UI_Main_Window:
    def setup_ui(self, parent):
        if not parent.objectName:
            parent.setObjectName("Main Window")
            
        # SETTANDO TAMANHO DA JANELA
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)
        
        # CRINANDO WIDGET CENTRAL
        self.central_frame = QFrame()
        
        # LAYOUT HORIZONTAL PRINCIPAL
        self.layout = QHBoxLayout(self.central_frame)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        
        # BARRA ESQUERDA
        self.left_box = QFrame()
        self.left_box.setStyleSheet("background-color: #44475a")
        self.left_box.setMaximumWidth(50)
        self.left_box.setMinimumWidth(50)
        self.left_box_layout = QVBoxLayout(self.left_box)
        self.left_box_layout.setContentsMargins(0,0,0,0)
        self.left_box_layout.setSpacing(0)
        
        # ICONES LATERAIS
        # ICONES DE CIMA
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        self.left_menu_top_frame.setStyleSheet("""
        #left_menu_top_frame{
            background-color: red;
        }
        """)
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)
        
        # BOTÕES DE CIMA
        self.toggle_button = pyPushButton("Menu", icon_path="icon_menu.svg")
        self.button_1 = pyPushButton("Home", is_active=True, icon_path="icon_home.svg")
        self.button_2 = pyPushButton("Widgets", icon_path="icon_widgets.svg")
        
        # ADIÇÕES DOS BOTÕES
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.button_1)
        self.left_menu_top_layout.addWidget(self.button_2)
        
        # ESPAÇADOR
        self.left_menu_spacer = QSpacerItem(20,20,QSizePolicy.Minimum,QSizePolicy.Expanding)
        
        # BOTÕES DE BAIXO
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(40)
        self.left_menu_bottom_frame.setMaximumHeight(40)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0,0,0,0)
        self.left_menu_bottom_layout.setSpacing(0)
        
        # BOTÃO DA PARTE DE BAIXO
        self.settings_btn = pyPushButton("Settings", icon_path="icon_settings.svg")
        
        # ADICIONANDO O BOTÃO INFERIOR
        self.left_menu_bottom_layout.addWidget(self.settings_btn)
        
        # LABEL DE VERSIONAMENTO
        self.left_menu_version = QLabel("v1.0.0")
        self.left_menu_version.setAlignment(Qt.AlignCenter)
        self.left_menu_version.setMinimumHeight(30)
        self.left_menu_version.setMaximumHeight(30)
        self.left_menu_version.setStyleSheet("color: #c3ccdf")
        
        # ADICIONANDO ICONES LATERAIS
        self.left_box_layout.addWidget(self.left_menu_top_frame)
        self.left_box_layout.addItem(self.left_menu_spacer)
        self.left_box_layout.addWidget(self.left_menu_bottom_frame)
        self.left_box_layout.addWidget(self.left_menu_version)
        
        # WIDGET DE CONTEUDO
        self.right_box = QFrame()
        self.right_box.setStyleSheet("background-color: #282a36")
        
        # LAYOUT VERTICAL DA ABA DE CONTEUDO
        self.content_layout = QVBoxLayout(self.right_box)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)
        
        # TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #44475a")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)
        
        # LEFT LABEL
        self.top_label_left = QLabel("Está é minha primeira aplicação PySide6")
        
        # SPACING
        self.top_spacing = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        
        # RIGHT LABEL
        self.top_label_right = QLabel("| PÁGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")
        
        # ADICIONANDO WIDGGETS AO TOP BAR
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacing)
        self.top_bar_layout.addWidget(self.top_label_right)
        
        # APPLICATION PAGES
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: white")
        self.ui_pages = Ui_application()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_1)
        
        # BOTTOM BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #44475a")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10,0,10,0)
        
        # LEFT LABEL
        self.bottom_label_left = QLabel("Criado por: Théo Kabir")
        
        # BOTTOM SPACING
        self.bottom_spacing = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        
        # RIGHT LABEL
        self.bottom_label_right = QLabel("\xa9 2022")
        
        # ADICIONANDO WIDGETS À BOTTOM BAR
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacing)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)
        
        # ADICIONANDO WIDGET AO LAYOUT DA ABA DE CONTEUDO
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)
        
        # ADICIONANDO WIDGETS AO LAYOUT PRINCIPAL
        self.layout.addWidget(self.left_box)
        self.layout.addWidget(self.right_box)
        
        # DEFININDO CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)