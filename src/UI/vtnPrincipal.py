# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(740, 521)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblNombre = QLabel(self.centralwidget)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(180, 100, 91, 41))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblNombre.setFont(font)
        self.lblApellido = QLabel(self.centralwidget)
        self.lblApellido.setObjectName(u"lblApellido")
        self.lblApellido.setGeometry(QRect(180, 150, 91, 41))
        self.lblApellido.setFont(font)
        self.lblCedula = QLabel(self.centralwidget)
        self.lblCedula.setObjectName(u"lblCedula")
        self.lblCedula.setGeometry(QRect(180, 200, 91, 41))
        self.lblCedula.setFont(font)
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(290, 110, 261, 21))
        self.txtNombre.setMaxLength(50)
        self.txtCedula = QLineEdit(self.centralwidget)
        self.txtCedula.setObjectName(u"txtCedula")
        self.txtCedula.setGeometry(QRect(290, 210, 131, 21))
        self.txtCedula.setMaxLength(10)
        self.txtApellido = QLineEdit(self.centralwidget)
        self.txtApellido.setObjectName(u"txtApellido")
        self.txtApellido.setGeometry(QRect(290, 160, 261, 21))
        self.txtApellido.setMaxLength(50)
        self.btnNuevo = QPushButton(self.centralwidget)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setGeometry(QRect(200, 370, 75, 34))
        font1 = QFont()
        font1.setPointSize(14)
        self.btnNuevo.setFont(font1)
        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(460, 370, 75, 34))
        self.btnLimpiar.setFont(font1)
        self.lblSexo = QLabel(self.centralwidget)
        self.lblSexo.setObjectName(u"lblSexo")
        self.lblSexo.setGeometry(QRect(180, 240, 91, 41))
        self.lblSexo.setFont(font)
        self.lblEmail = QLabel(self.centralwidget)
        self.lblEmail.setObjectName(u"lblEmail")
        self.lblEmail.setGeometry(QRect(180, 290, 91, 41))
        self.lblEmail.setFont(font)
        self.txtEmail = QLineEdit(self.centralwidget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(290, 300, 251, 22))
        self.txtEmail.setMaxLength(100)
        self.cbSexo = QComboBox(self.centralwidget)
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.setObjectName(u"cbSexo")
        self.cbSexo.setGeometry(QRect(290, 250, 131, 24))
        self.txtBuscarCedula = QLineEdit(self.centralwidget)
        self.txtBuscarCedula.setObjectName(u"txtBuscarCedula")
        self.txtBuscarCedula.setGeometry(QRect(290, 40, 131, 21))
        self.txtBuscarCedula.setMaxLength(10)
        self.lblCedulaBuscar = QLabel(self.centralwidget)
        self.lblCedulaBuscar.setObjectName(u"lblCedulaBuscar")
        self.lblCedulaBuscar.setGeometry(QRect(90, 30, 171, 41))
        self.lblCedulaBuscar.setFont(font)
        self.btnActualizar = QPushButton(self.centralwidget)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setGeometry(QRect(280, 370, 92, 34))
        self.btnActualizar.setFont(font1)
        self.btnBorrarRegistro = QPushButton(self.centralwidget)
        self.btnBorrarRegistro.setObjectName(u"btnBorrarRegistro")
        self.btnBorrarRegistro.setGeometry(QRect(380, 370, 75, 34))
        self.btnBorrarRegistro.setFont(font1)
        self.btnBuscar = QPushButton(self.centralwidget)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setGeometry(QRect(450, 30, 101, 41))
        self.btnBuscar.setFont(font1)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemSearch))
        self.btnBuscar.setIcon(icon)
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 740, 33))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txtNombre, self.txtApellido)
        QWidget.setTabOrder(self.txtApellido, self.txtCedula)
        QWidget.setTabOrder(self.txtCedula, self.cbSexo)
        QWidget.setTabOrder(self.cbSexo, self.txtEmail)
        QWidget.setTabOrder(self.txtEmail, self.btnNuevo)
        QWidget.setTabOrder(self.btnNuevo, self.btnLimpiar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"Sistema de Gesti\u00f3n de Personas", None))
        self.lblNombre.setText(QCoreApplication.translate("vtnPrincipal", u"Nombre:", None))
        self.lblApellido.setText(QCoreApplication.translate("vtnPrincipal", u"Apellido:", None))
        self.lblCedula.setText(QCoreApplication.translate("vtnPrincipal", u"C\u00e9dula:", None))
        self.btnNuevo.setText(QCoreApplication.translate("vtnPrincipal", u"Nuevo", None))
        self.btnLimpiar.setText(QCoreApplication.translate("vtnPrincipal", u"Limpiar", None))
        self.lblSexo.setText(QCoreApplication.translate("vtnPrincipal", u"Sexo:", None))
        self.lblEmail.setText(QCoreApplication.translate("vtnPrincipal", u"Email:", None))
        self.cbSexo.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"Seleccionar", None))
        self.cbSexo.setItemText(1, QCoreApplication.translate("vtnPrincipal", u"Hombre", None))
        self.cbSexo.setItemText(2, QCoreApplication.translate("vtnPrincipal", u"Mujer", None))

        self.lblCedulaBuscar.setText(QCoreApplication.translate("vtnPrincipal", u"Buscar por Cedula:", None))
        self.btnActualizar.setText(QCoreApplication.translate("vtnPrincipal", u"Actualizar", None))
        self.btnBorrarRegistro.setText(QCoreApplication.translate("vtnPrincipal", u"Borrar", None))
        self.btnBuscar.setText("")
    # retranslateUi

