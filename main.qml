import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Controls.Material 2.1

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
        text: magic.foo
        onClicked: {
            magic.print_it()
            print(magic.foo)
            magic.foo = !magic.foo
        }
    }
}
