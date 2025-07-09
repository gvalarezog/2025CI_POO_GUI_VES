class Persona:
    def __init__(self, nombre, apellido, cedula, sexo, email):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._sexo = sexo
        self._email = email

    # Encapsulamiento con property y setter para cada atributo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = valor

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        self._cedula = valor

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, valor):
        self._sexo = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

    def __str__(self):
        return f'Persona: {self.__dict__.__str__()}'

if __name__ == '__main__':
    p1 = Persona('Luis', 'Paz', '0123456789', 'M', 'lpaz@mail.com')
    print(p1)