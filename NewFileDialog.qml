import Qt.labs.platform 1.0

FileDialog {
    id: root
    visible: false
    property var output: {}

    onAccepted: {
        var sizeToRemove = root.folder.toString().length - root.currentFile.toString().length + 1
        // 1 (File) : File (remove file://) : format
        var finalString
        var urlString = root.currentFile.toString()
        if (urlString.startsWith("file:///")) {
            // Check if is a windows string (8) or linux (7)
            var sliceValue = urlString.charAt(9) === ':' ? 8 : 7
            finalString = urlString.substring(sliceValue)
        } else {
            finalString = urlString
        }
        output = finalString
    }
}
