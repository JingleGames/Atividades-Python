from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

def on_button_click():
    print("Botão clicado!")

# Criação da aplicação
app = QApplication([])

# Criação da janela principal
window = QWidget()
window.setWindowTitle("Exemplo PyQt")

# Criação do layout
layout = QVBoxLayout()

# Criação de um rótulo
label = QLabel("Olá, PyQt!")
layout.addWidget(label)

# Criação de um botão
button = QPushButton("Clique em mim")
button.clicked.connect(on_button_click)
layout.addWidget(button)

# Definição do layout na janela
window.setLayout(layout)
window.show()

# Início do loop principal
app.exec_()
