from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt, Slot, Property, Signal, QTimer
from PySide2.QtQml import qmlRegisterType

import copy
import pickle

class Map(QAbstractListModel):
    ROLES = [
        "cell",
    ]

    def __init__(self, parent=None):
        super(Map, self).__init__(parent)
        self._timer = QTimer()
        self._timer.setInterval(1000)
        self._timer.timeout.connect(self.run)
        self.start()

    @Slot(int)
    def start(self, size=10):
        self._size = size
        self._cells = [0]*(self._size**2)
        self._roles = dict(enumerate(Map.ROLES))
        self.endResetModel()
        self.sizeChanged.emit()

    def size(self):
        return self._size

    sizeChanged = Signal()
    size = Property(int, size, notify=sizeChanged)

    def running(self):
        return self._timer.isActive()

    def setRunning(self, state):
        if state:
            self._timer.start()
        else:
            self._timer.stop()
        self.runningChanged.emit()

    runningChanged = Signal()
    running = Property(bool, running, setRunning, notify=runningChanged)

    def rowCount(self, parent=QModelIndex()):
        return len(self._cells)

    @Slot()
    def run(self):
        temp_cells = copy.deepcopy(self._cells)
        for i in range(self._size):
            for u in range(self._size):
                total = self.countNeighbors(i, u)
                # underpopulation
                if total < 2 and self.at(i, u):
                    self.setCell(i, u, temp_cells, 0)
                # overpopulation
                elif total > 3 and self.at(i, u):
                    self.setCell(i, u, temp_cells, 0)
                # reproduction
                elif total == 3 and not self.at(i, u):
                    self.setCell(i, u, temp_cells, 1)

        self._cells = temp_cells
        self.endResetModel()

    def setCell(self, x, y, cells=None, value=0):
        if cells == None:
            cells = self._cells
        if x < 0 or y < 0 or x >= self._size or y >= self._size:
            return
        cells[y*self._size + x] = value

    def at(self, x, y, cells=None):
        if cells == None:
            cells = self._cells
        if x < 0 or y < 0 or x >= self._size or y >= self._size:
            return 0
        return cells[y*self._size + x]

    #debug function
    @Slot(int, result='int')
    def countNeighborsFromIndex(self, index):
        y = 0
        x = index
        while x > self._size:
            y += 1
            x -= self._size
        return self.countNeighbors(x, y)

    def countNeighbors(self, x, y, n=1):
        total = 0
        for i in range(-n + x, x + n + 1):
            for u in range(-n + y, y + n + 1):
                if i == x and u == y:
                    continue
                if self.at(i, u) == 1:
                    total = total + 1
        return total

    def data(self, index, role=Qt.DisplayRole):
        return self._cells[index.row()]

    def setData(self, index, value, role):
        self._cells[index.row()] = value
        self.dataChanged.emit(index, index, self._roles)
        self.endResetModel()
        return True

    def roleNames(self):
        return self._roles

    @Slot(str)
    def loadMap(self, path):
        try:
            with open(path) as f:
                self._cells = pickle.load(f)
                self._size = int(len(self._cells)**0.5)
                self._roles = dict(enumerate(Map.ROLES))
                self.endResetModel()
                self.sizeChanged.emit()
        except Exception as e:
            print(e)

    @Slot(str)
    def saveMap(self, path):
        try:
            with open(path, 'w') as f:
                pickle.dump(self._cells, f)
        except Exception as e:
            print(e)

qmlRegisterType(Map, 'Map', 1, 0, 'Map')
