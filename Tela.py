from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from ModuloCadastro import inserir
from Data import converterData

class TelaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        carregador = QUiLoader()
        self.tela = carregador.load("Tela.ui")
        self.componentes()
    
    def componentes(self):
        self.ho = self.tela.findChild(QtWidgets.QSpinBox, "ho")
        self.pi = self.tela.findChild(QtWidgets.QComboBox, "pi")
        self.de = self.tela.findChild(QtWidgets.QDateEdit, "de")
        self.dt = self.tela.findChild(QtWidgets.QDateEdit, "dt")
        self.pe = self.tela.findChild(QtWidgets.QComboBox, "pe")
        self.ds = self.tela.findChild(QtWidgets.QLineEdit, "ds")
        self.ob = self.tela.findChild(QtWidgets.QLineEdit, "ob")
        self.btnCadastrar = self.tela.findChild(QtWidgets.QPushButton, "btnCadastrar")
        self.btnCadastrar.clicked.connect(self.cadastrarInventario)

    def cadastrarInventario(self):
                  
        dx = self.ds.text()        
        pr = self.pe.currentText()
        di = self.de.text()
        dat = self.dt.text()
        qp = self.ho.text()
        ti = self.pi.currentText()
        ob = self.ob.text()
        inserir(dx,pr,converterData(di),converterData(dat),qp,ti,ob)
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    interface = TelaPrincipal()
    interface.tela.show()
    app.exec()