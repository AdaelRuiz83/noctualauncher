from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.uic import loadUi
import sys
class NoctuaLauncher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Noctua Launcher")
        self.resize(1024, 768)

        #Creo los contenedores de las paginas
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stack)

        #Cargo las paginas hechas en Qt Designer
        self.login_view = loadUi("login_window.ui")
        self.main_view = loadUi("main_dashboard.ui")

        # Añadir al Stack
        self.stack.addWidget(self.login_view)   Índice 0
        self.stack.addWidget(self.main_view)   # Índice 1
        
        # Conectar señal de login para cambiar de vista
        # Asumiendo que tu botón en el .ui se llama 'btn_login'
        self.login_view.btn_login.clicked.connect(self.ir_al_sistema)

    def ir_al_sistema(self):
        # Aquí puedes validar credenciales antes de cambiar
        self.stack.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Cargar tu QSS global aquí
    with open("estilos.qss", "r") as f:
        app.setStyleSheet(f.read())
        
    window = NoctuaLauncher()
    window.show()
    sys.exit(app.exec())
Consejos de QSS para un Launcher Oscuro