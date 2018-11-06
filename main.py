import sys

from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine

# Register Map and use it in QML
from map import Map

def main():
    sys.argv += ['--style', 'material']
    app = QApplication(sys.argv)

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    engine = QQmlApplicationEngine('main.qml')

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
