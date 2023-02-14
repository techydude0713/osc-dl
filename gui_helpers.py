from PySide6 import QtCore
from PySide6.QtCore import QObject, QSettings

settings = QSettings("Open Shop Channel", "OSCDL")

DATASENT = False
CURRENTLY_SENDING = False
CURRENTLY_LOADING_ICONS = False
IN_DOWNLOAD_DIALOG = False
IN_WIILOAD_DIALOG = False
WINDOW_IS_READY = False

class URLR(QObject):
    data = QtCore.Signal(str)
    download = QtCore.Signal(bool)
    send = QtCore.Signal(bool)
    
INCOMING_REQUEST = URLR()
INCOMING_REQUEST_BUCKET = None
WAIT_FOR_REPOPULATION=False
URL_LOCK = False
        


