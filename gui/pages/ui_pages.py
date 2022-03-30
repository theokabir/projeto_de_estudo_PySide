# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesCZbudA.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_application(object):
    def setupUi(self, application):
        if not application.objectName():
            application.setObjectName(u"application")
        application.resize(812, 636)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        application.addWidget(self.page_1)
        self.page__2 = QWidget()
        self.page__2.setObjectName(u"page__2")
        self.verticalLayout_3 = QVBoxLayout(self.page__2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.page__2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 70))
        self.frame.setMaximumSize(QSize(500, 70))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.texto_nome = QLabel(self.frame)
        self.texto_nome.setObjectName(u"texto_nome")
        self.texto_nome.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: #fff")

        self.verticalLayout_4.addWidget(self.texto_nome)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #44475a;\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: white;\n"
"	border-radius: 10px\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 36))
        self.pushButton.setMaximumSize(QSize(120, 36))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(57, 133, 200);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: white;\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170,  255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 0 , 127	);\n"
"}")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        application.addWidget(self.page__2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_2 = QVBoxLayout(self.page_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        application.addWidget(self.page_3)

        self.retranslateUi(application)

        QMetaObject.connectSlotsByName(application)
    # setupUi

    def retranslateUi(self, application):
        application.setWindowTitle(QCoreApplication.translate("application", u"StackedWidget", None))
        self.label.setText(QCoreApplication.translate("application", u"P\u00e1gina Inicial", None))
        self.texto_nome.setText(QCoreApplication.translate("application", u"Ol\u00e1, ...", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("application", u"Digite seu nome", None))
        self.pushButton.setText(QCoreApplication.translate("application", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("application", u"Pagina 3", None))
    # retranslateUi

