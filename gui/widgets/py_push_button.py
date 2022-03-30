from qt_core import *
import os

class pyPushButton(QPushButton):
    def __init__(
        self,
        text="",
        height=40,
        minimun_width=50,
        text_padding=55,
        text_color="#c3ccdf",
        icon_path="",
        icon_color="#c3ccdf",
        btn_color="#44475a",
        btn_hover="#4f5368",
        btn_pressed="#282a36",
        is_active=False
    ):
        super().__init__()
        
        #self.setObjectName("QPushButton")
        
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.minimun_width = minimun_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color  
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active
        
        self.set_style(is_active=self.is_active)
        
    def set_style(
        self,
        text_padding=55,
        text_color="#c3ccdf",
        btn_color="#44475a",
        btn_hover="#4f5368",
        btn_pressed="#282a36",
        is_active=False
    ):
        
        style = f"""
            QPushButton {{
                color: {text_color};
                background-color: {btn_color};
                padding-left: {text_padding};
                text-align: left;
                border: none;
            }}
            
            QPushButton:hover{{
                background-color: {btn_hover};
            }}
            
            QPushButton:pressed{{
                background-color: {btn_pressed};
            }}
        """
        
        active_style = f"""
            QPushButton{{
                border-right: 5px solid #282a36;
                background-color: {btn_hover};
            }}
        """
        
        if is_active:
            style += active_style 
        
        self.setStyleSheet(style)
    
    def set_active(self, is_active):
        self.is_active = is_active
        self.set_style(is_active=is_active)
        
    def paintEvent(self, event):
        QPushButton.paintEvent(self, event)
        
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)
        
        rect = QRect(0,0, self.minimun_width, self.height())
        
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)
        
        qp.end()
        
    def draw_icon(self, qp, image, rect, color):
        path = os.path.join(os.path.abspath(os.getcwd()), "gui/images/icons/")
        icon_path = os.path.normpath(os.path.join(path, image))
        
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width())/2,
            (rect.height() - icon.height())/2,
            icon
        )
        
        painter.end()
        