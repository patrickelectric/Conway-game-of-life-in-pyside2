import QtQuick 2.11
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.4
import QtQuick.Controls.Material 2.1
import Qt.labs.platform 1.0 as QLP

import Magic 1.0

ApplicationWindow {
    id: window
    height: 480
    width: 480
    visible: true
    Material.theme: Material.Dark
    Material.accent: Material.Blue

    Magic {
        id: magic
    }

    Button {
        anchors.fill: parent
        text: magic.foo ? "T" : "F"
        onClicked: {
            magic.print_it()
            print(magic.foo)
            magic.foo = !magic.foo
        }
    }
}
