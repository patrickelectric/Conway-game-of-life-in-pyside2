import QtQuick 2.11
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.4
import Qt.labs.platform 1.0 as QLP

import Map 1.0

ApplicationWindow {
    id: window
    height: 480
    width: 480
    visible: true

    menuBar: MenuBar {
        Menu {
            title: "File"
            MenuItem {
                text: "Open..."
                onTriggered: loadMap.visible = true
            }
            MenuItem {
                text: "Save..."
                onTriggered: saveMap.visible = true
            }
        }

        Menu {
            title: "Map size"
            MenuItem {
                text: "10"
                onTriggered: map.start(10)
            }
            MenuItem {
                text: "20"
                onTriggered: map.start(20)
            }
            MenuItem {
                text: "50"
                onTriggered: map.start(50)
            }
            MenuItem {
                text: "100"
                onTriggered: map.start(100)
            }
        }
    }
    ColumnLayout {
        anchors.fill: parent

        GridLayout {
            id: tableView
            Layout.fillHeight: true
            Layout.fillWidth: true

            columns: map.size
            rowSpacing: 1
            columnSpacing: 1

            Repeater {
                model: Map {
                    id: map
                }

                Rectangle {
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    color: {
                        if(map.countNeighborsFromIndex(index) < 2 && modelData && colorCB.checked) {
                            return "#440000"
                        } else if(map.countNeighborsFromIndex(index) > 3 && modelData && colorCB.checked) {
                            return "#440000"
                        } else if(map.countNeighborsFromIndex(index) == 3 && !modelData && colorCB.checked) {
                            return "#004400"
                        } else if(modelData) {
                            return "#f3f3f4"
                        } else {
                            return "#b5b7bf"
                        }
                    }
                    MouseArea {
                        anchors.fill: parent
                        onClicked: cell = !cell
                    }
                    Text {
                        text: map.countNeighborsFromIndex(index)
                    }
                }
            }
        }

        RowLayout {
            Button {
                text: "Clear"
                Layout.fillWidth: true
                onClicked: {print(window.loadMap);map.start(map.size);}
            }
            Button {
                text: map.running ? "Stop" : "Start"
                Layout.fillWidth: true
                onClicked: map.running = !map.running
            }
            CheckBox {
                id: colorCB
                text: "Enable colors"
            }
        }
    }

    NewFileDialog {
        id: loadMap
        title: "Please choose a Map file"
        nameFilters: ["Map files (*.map)"]
        fileMode: QLP.FileDialog.OpenFile
        onOutputChanged: {
            print('Load from >', output)
            map.loadMap(output)
        }
    }

    NewFileDialog {
        id: saveMap
        title: "Please select a folder"
        nameFilters: ["Map files (*.map)"]
        fileMode: QLP.FileDialog.SaveFile
        onOutputChanged: {
            print('Save in >', output)
            map.saveMap(output)
        }
    }
}
