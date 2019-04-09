from PySide2.QtCore import QObject, Slot, Property, Signal
from PySide2.QtQml import qmlRegisterType

import copy
import pickle

class Magic(QObject):
    _signals = {}
    _attributes = {}

    def __init__(self, parent=None):
        super(Magic, self).__init__(parent)
        self._foo = False

    def foo(self):
        return self._foo

    def setFoo(self, value):
        self._foo = value
        self.fooChanged.emit()

    fooChanged = Signal()
    foo = Property(bool, foo, setFoo, notify=fooChanged)

    @Slot()
    def print_it(self):
        print('python:', self._foo)

qmlRegisterType(Magic, 'Magic', 1, 0, 'Magic')
