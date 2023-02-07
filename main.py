from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLabel, QVBoxLayout, QPushButton)
import aspose.words as aw

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('PDF converter')

my_win.move(700, 100)
my_win.resize(600, 500)
my_win.show()

title = QLabel("Для генерации index.html в PDF нажмите кнопку ниже!")
button = QPushButton("Конвертировать")

line_v = QVBoxLayout()

line_v.addWidget(title, alignment=Qt.AlignCenter)
line_v.addWidget(button, alignment=Qt.AlignCenter)

my_win.setLayout(line_v)


def generate_label():
    new_title = 'Html успешно сгенерирован в PDF'
    # doc = aw.Document("index.html")
    # doc.save("file.pdf")
    title.setText(str(new_title))
    my_win.setLayout(line_v)


button.clicked.connect(generate_label)

app.exec()
