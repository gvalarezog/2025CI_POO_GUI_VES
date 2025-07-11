
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from src.UI.vtnPrincipal import Ui_vtnPrincipal
from src.datos.personaDao import PersonaDao
from src.dominio.persona import Persona


class PersonaServicio(QMainWindow):
    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.btnNuevo.clicked.connect(self.nuevo)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnBuscar.clicked.connect(self.buscar)
        self.ui.btnActualizar.clicked.connect(self.actualizar)
        self.ui.btnBorrarRegistro.clicked.connect(self.borrar)
        self.ui.txtCedula.setValidator(QIntValidator())
        self.ui.txtBuscarCedula.setValidator(QIntValidator())

    def nuevo(self):
        if self.ui.txtNombre.text() == "" or self.ui.txtApellido.text() == ""\
                or len(self.ui.txtCedula.text()) < 10 or self.ui.txtEmail.text()==""\
                or self.ui.cbSexo.currentText()=='Seleccionar':
            QMessageBox.warning(self, "Advertencia", "Completar todos los datos.")

        else:
            persona = Persona(nombre=self.ui.txtNombre.text(),
                              apellido = self.ui.txtApellido.text(),
                              cedula = self.ui.txtCedula.text(),
                              sexo = self.ui.cbSexo.currentText()[00],
                              email = self.ui.txtEmail.text())
            # print(persona)
            if PersonaDao.insertar_persona(persona) == -1:
                QMessageBox.critical(self, "Error", "No se pudo guardar.")
            else:
                self.ui.statusbar.showMessage("Se guardo correctamente", 3000)
                self.limpiar()

    def limpiar(self):
        self.ui.txtNombre.setText("")
        self.ui.txtApellido.setText("")
        self.ui.txtCedula.setText("")
        self.ui.txtEmail.setText("")
        self.ui.cbSexo.setCurrentText('Seleccionar')

    def buscar(self):
        if len(self.ui.txtBuscarCedula.text()) < 10:
            QMessageBox.warning(self, "Advertencia", "Ingrese la cedula a buscar.")
        else:
            persona = PersonaDao.seleccionar_persona(self.ui.txtBuscarCedula.text())
            if persona:
                self.ui.txtNombre.setText(persona.nombre)
                self.ui.txtApellido.setText(persona.apellido)
                self.ui.txtCedula.setText(persona.cedula)
                self.ui.txtEmail.setText(persona.email)
                self.ui.cbSexo.setCurrentText(persona.sexo)
            else:
                print("No se encontro la persona con la cedula.")
                QMessageBox.information(self, "Advertencia", "No se encontro la persona con la cedula.")

    def actualizar(self):
        if QMessageBox.question(self,'Confirmación', "Desea actualizar el registro?") == QMessageBox.Yes:
            if self.ui.txtNombre.text() == "" or self.ui.txtApellido.text() == "" \
                    or len(self.ui.txtCedula.text()) < 10 or self.ui.txtEmail.text() == "" \
                    or self.ui.cbSexo.currentText() == 'Seleccionar':
                QMessageBox.warning(self, "Advertencia", "Completar todos los datos.")
            else:
                persona = Persona(nombre=self.ui.txtNombre.text(),
                                  apellido=self.ui.txtApellido.text(),
                                  cedula=self.ui.txtCedula.text(),
                                  sexo=self.ui.cbSexo.currentText()[00],
                                  email=self.ui.txtEmail.text())
                # print(persona)
                if PersonaDao.actualizar_persona(persona) == -1:
                    QMessageBox.critical(self, "Error", "No se pudo guardar.")
                else:
                    self.ui.statusbar.showMessage("Se actualizó correctamente", 3000)
                    self.limpiar()

    def borrar(self):
        if QMessageBox.question(self, "Confirmación", "Desea borrar el registro.") == QMessageBox.Yes:
            retorno = PersonaDao.eliminar_persona(self.ui.txtCedula.text())
            if retorno != -1:
                self.ui.statusbar.showMessage("Registro eliminado con éxito",3000)
                self.limpiar()
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar.")
