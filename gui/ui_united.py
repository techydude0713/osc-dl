# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'united.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 425)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 425))
        MainWindow.setStyleSheet(u"")
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.actionAbout_OSC_DL = QAction(MainWindow)
        self.actionAbout_OSC_DL.setObjectName(u"actionAbout_OSC_DL")
        self.actionEnable_Log_File = QAction(MainWindow)
        self.actionEnable_Log_File.setObjectName(u"actionEnable_Log_File")
        self.actionEnable_Log_File.setCheckable(True)
        self.actionClear_Log = QAction(MainWindow)
        self.actionClear_Log.setObjectName(u"actionClear_Log")
        self.actionClear_Log.setEnabled(False)
        self.actionDownload_HBB_Client_Latest = QAction(MainWindow)
        self.actionDownload_HBB_Client_Latest.setObjectName(u"actionDownload_HBB_Client_Latest")
        self.actionCheck_for_Updates = QAction(MainWindow)
        self.actionCheck_for_Updates.setObjectName(u"actionCheck_for_Updates")
        self.actionClose_the_shop = QAction(MainWindow)
        self.actionClose_the_shop.setObjectName(u"actionClose_the_shop")
        self.actionDisplay_Banner = QAction(MainWindow)
        self.actionDisplay_Banner.setObjectName(u"actionDisplay_Banner")
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        self.actionSelect_Theme = QAction(MainWindow)
        self.actionSelect_Theme.setObjectName(u"actionSelect_Theme")
        self.actionIcons_provided_by = QAction(MainWindow)
        self.actionIcons_provided_by.setObjectName(u"actionIcons_provided_by")
        self.actionIcons_provided_by.setEnabled(False)
        self.actionCopy_Direct_Link = QAction(MainWindow)
        self.actionCopy_Direct_Link.setObjectName(u"actionCopy_Direct_Link")
        self.actionDeveloper_Profile = QAction(MainWindow)
        self.actionDeveloper_Profile.setObjectName(u"actionDeveloper_Profile")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.AppsLibraryBox = QGroupBox(self.centralwidget)
        self.AppsLibraryBox.setObjectName(u"AppsLibraryBox")
        self.verticalLayout = QVBoxLayout(self.AppsLibraryBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 4, -1, -1)
        self.LibraryTopFrameTop = QFrame(self.AppsLibraryBox)
        self.LibraryTopFrameTop.setObjectName(u"LibraryTopFrameTop")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LibraryTopFrameTop.sizePolicy().hasHeightForWidth())
        self.LibraryTopFrameTop.setSizePolicy(sizePolicy1)
        self.LibraryTopFrameTop.setFrameShape(QFrame.NoFrame)
        self.LibraryTopFrameTop.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.LibraryTopFrameTop)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ViewDevWebsite = QLabel(self.LibraryTopFrameTop)
        self.ViewDevWebsite.setObjectName(u"ViewDevWebsite")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ViewDevWebsite.sizePolicy().hasHeightForWidth())
        self.ViewDevWebsite.setSizePolicy(sizePolicy2)
        self.ViewDevWebsite.setVisible(False)
        self.ViewDevWebsite.setTextFormat(Qt.RichText)
        self.ViewDevWebsite.setOpenExternalLinks(True)

        self.horizontalLayout_3.addWidget(self.ViewDevWebsite)

        self.ReposComboBox = QComboBox(self.LibraryTopFrameTop)
        self.ReposComboBox.setObjectName(u"ReposComboBox")
        self.ReposComboBox.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.ReposComboBox)

        self.AppsAmountLabel = QLabel(self.LibraryTopFrameTop)
        self.AppsAmountLabel.setObjectName(u"AppsAmountLabel")
        self.AppsAmountLabel.setMaximumSize(QSize(60, 16777215))
        self.AppsAmountLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.AppsAmountLabel)

        self.ReturnToMainBtn = QPushButton(self.LibraryTopFrameTop)
        self.ReturnToMainBtn.setObjectName(u"ReturnToMainBtn")
        self.ReturnToMainBtn.setMaximumSize(QSize(161, 16777215))
        self.ReturnToMainBtn.setVisible(False)

        self.horizontalLayout_3.addWidget(self.ReturnToMainBtn)


        self.verticalLayout.addWidget(self.LibraryTopFrameTop)

        self.LibraryContentFrame = QFrame(self.AppsLibraryBox)
        self.LibraryContentFrame.setObjectName(u"LibraryContentFrame")
        self.verticalLayout_2 = QVBoxLayout(self.LibraryContentFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SearchFrame = QFrame(self.LibraryContentFrame)
        self.SearchFrame.setObjectName(u"SearchFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.SearchFrame.sizePolicy().hasHeightForWidth())
        self.SearchFrame.setSizePolicy(sizePolicy3)
        self.SearchFrame.setMaximumSize(QSize(16777215, 20))
        self.SearchFrame.setFrameShape(QFrame.NoFrame)
        self.SearchFrame.setFrameShadow(QFrame.Plain)
        self.SearchFrame.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.SearchFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.SearchBar = QLineEdit(self.SearchFrame)
        self.SearchBar.setObjectName(u"SearchBar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.SearchBar.sizePolicy().hasHeightForWidth())
        self.SearchBar.setSizePolicy(sizePolicy4)

        self.horizontalLayout_5.addWidget(self.SearchBar)

        self.CategoriesComboBox = QComboBox(self.SearchFrame)
        self.CategoriesComboBox.addItem("")
        self.CategoriesComboBox.addItem("")
        self.CategoriesComboBox.addItem("")
        self.CategoriesComboBox.addItem("")
        self.CategoriesComboBox.addItem("")
        self.CategoriesComboBox.addItem("")
        self.CategoriesComboBox.setObjectName(u"CategoriesComboBox")
        self.CategoriesComboBox.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.CategoriesComboBox)


        self.verticalLayout_2.addWidget(self.SearchFrame)

        self.listAppsWidget = QListWidget(self.LibraryContentFrame)
        self.listAppsWidget.setObjectName(u"listAppsWidget")
        sizePolicy4.setHeightForWidth(self.listAppsWidget.sizePolicy().hasHeightForWidth())
        self.listAppsWidget.setSizePolicy(sizePolicy4)
        self.listAppsWidget.setBaseSize(QSize(581, 281))
        self.listAppsWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_2.addWidget(self.listAppsWidget)


        self.verticalLayout.addWidget(self.LibraryContentFrame)

        self.announcement = QFrame(self.AppsLibraryBox)
        self.announcement.setObjectName(u"announcement")
        self.announcement.setMaximumSize(QSize(16777215, 21))
        self.announcement.setVisible(False)
        self.announcement.setStyleSheet(u"QFrame {\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.announcement.setFrameShape(QFrame.StyledPanel)
        self.announcement.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.announcement)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, 0, 3, 0)
        self.announcementLabel = QLabel(self.announcement)
        self.announcementLabel.setObjectName(u"announcementLabel")
        self.announcementLabel.setOpenExternalLinks(True)

        self.horizontalLayout_4.addWidget(self.announcementLabel)

        self.announcementURLLabel = QLabel(self.announcement)
        self.announcementURLLabel.setObjectName(u"announcementURLLabel")
        self.announcementURLLabel.setStyleSheet(u"QLabel {\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.announcementURLLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.announcementURLLabel.setOpenExternalLinks(True)

        self.horizontalLayout_4.addWidget(self.announcementURLLabel)


        self.verticalLayout.addWidget(self.announcement)


        self.horizontalLayout_2.addWidget(self.AppsLibraryBox)

        self.SelectionInfoBox = QGroupBox(self.centralwidget)
        self.SelectionInfoBox.setObjectName(u"SelectionInfoBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.SelectionInfoBox.sizePolicy().hasHeightForWidth())
        self.SelectionInfoBox.setSizePolicy(sizePolicy5)
        self.SelectionInfoBox.setMaximumSize(QSize(271, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.SelectionInfoBox)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 4, 0, -1)
        self.MetadataTabsFrame = QFrame(self.SelectionInfoBox)
        self.MetadataTabsFrame.setObjectName(u"MetadataTabsFrame")
        self.MetadataTabsFrame.setFrameShape(QFrame.NoFrame)
        self.MetadataTabsFrame.setLineWidth(0)
        self.tabMetadata = QTabWidget(self.MetadataTabsFrame)
        self.tabMetadata.setObjectName(u"tabMetadata")
        self.tabMetadata.setGeometry(QRect(10, 0, 251, 271))
        self.GeneralTab = QWidget()
        self.GeneralTab.setObjectName(u"GeneralTab")
        self.label_description = QLabel(self.GeneralTab)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(10, 80, 221, 16))
        self.label_description.setMaximumSize(QSize(221, 16777215))
        self.label_description.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.label_displayname = QLabel(self.GeneralTab)
        self.label_displayname.setObjectName(u"label_displayname")
        self.label_displayname.setGeometry(QRect(10, 60, 221, 16))
        self.label_displayname.setMaximumSize(QSize(221, 16777215))
        font = QFont()
        font.setBold(True)
        self.label_displayname.setFont(font)
        self.label_displayname.setWordWrap(True)
        self.label_displayname.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.progressBar = QProgressBar(self.GeneralTab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(150, 0, 91, 23))
        self.progressBar.setVisible(False)
        self.progressBar.setValue(0)
        self.HomebrewIconLabel = QLabel(self.GeneralTab)
        self.HomebrewIconLabel.setObjectName(u"HomebrewIconLabel")
        self.HomebrewIconLabel.setGeometry(QRect(10, 10, 128, 48))
        self.HomebrewIconLabel.setAlignment(Qt.AlignCenter)
        self.HomebrewCategoryLabel = QLabel(self.GeneralTab)
        self.HomebrewCategoryLabel.setObjectName(u"HomebrewCategoryLabel")
        self.HomebrewCategoryLabel.setGeometry(QRect(147, 10, 81, 48))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.HomebrewCategoryLabel.setFont(font1)
        self.HomebrewCategoryLabel.setAlignment(Qt.AlignCenter)
        self.statusIcon = QLabel(self.GeneralTab)
        self.statusIcon.setObjectName(u"statusIcon")
        self.statusIcon.setGeometry(QRect(120, 0, 16, 16))
        self.statusIcon.setMaximumSize(QSize(30, 30))
        self.statusIcon.setScaledContents(True)
        self.statusIcon.setMargin(3)
        self.gridLayoutWidget = QWidget(self.GeneralTab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 100, 223, 136))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_releasedate = QLabel(self.gridLayoutWidget)
        self.label_releasedate.setObjectName(u"label_releasedate")

        self.gridLayout.addWidget(self.label_releasedate, 3, 0, 1, 1)

        self.label_filesize = QLabel(self.gridLayoutWidget)
        self.label_filesize.setObjectName(u"label_filesize")

        self.gridLayout.addWidget(self.label_filesize, 4, 0, 1, 1)

        self.label_version = QLabel(self.gridLayoutWidget)
        self.label_version.setObjectName(u"label_version")

        self.gridLayout.addWidget(self.label_version, 1, 0, 1, 1)

        self.label_developer = QLabel(self.gridLayoutWidget)
        self.label_developer.setObjectName(u"label_developer")

        self.gridLayout.addWidget(self.label_developer, 2, 0, 1, 1)

        self.label_appname = QLabel(self.gridLayoutWidget)
        self.label_appname.setObjectName(u"label_appname")

        self.gridLayout.addWidget(self.label_appname, 0, 0, 1, 1)

        self.appname = QLineEdit(self.gridLayoutWidget)
        self.appname.setObjectName(u"appname")
        self.appname.setEchoMode(QLineEdit.Normal)
        self.appname.setReadOnly(True)

        self.gridLayout.addWidget(self.appname, 0, 1, 1, 1)

        self.version = QLineEdit(self.gridLayoutWidget)
        self.version.setObjectName(u"version")
        self.version.setEchoMode(QLineEdit.Normal)
        self.version.setReadOnly(True)

        self.gridLayout.addWidget(self.version, 1, 1, 1, 1)

        self.developer = QLineEdit(self.gridLayoutWidget)
        self.developer.setObjectName(u"developer")
        self.developer.setEchoMode(QLineEdit.Normal)
        self.developer.setReadOnly(True)

        self.gridLayout.addWidget(self.developer, 2, 1, 1, 1)

        self.releasedate = QLineEdit(self.gridLayoutWidget)
        self.releasedate.setObjectName(u"releasedate")
        self.releasedate.setEchoMode(QLineEdit.Normal)
        self.releasedate.setReadOnly(True)

        self.gridLayout.addWidget(self.releasedate, 3, 1, 1, 1)

        self.filesize = QLineEdit(self.gridLayoutWidget)
        self.filesize.setObjectName(u"filesize")
        self.filesize.setEchoMode(QLineEdit.Normal)
        self.filesize.setReadOnly(True)

        self.gridLayout.addWidget(self.filesize, 4, 1, 1, 1)

        self.tabMetadata.addTab(self.GeneralTab, "")
        self.statusIcon.raise_()
        self.label_description.raise_()
        self.label_displayname.raise_()
        self.progressBar.raise_()
        self.HomebrewIconLabel.raise_()
        self.HomebrewCategoryLabel.raise_()
        self.gridLayoutWidget.raise_()
        self.Description = QWidget()
        self.Description.setObjectName(u"Description")
        self.longDescriptionBrowser = QTextBrowser(self.Description)
        self.longDescriptionBrowser.setObjectName(u"longDescriptionBrowser")
        self.longDescriptionBrowser.setGeometry(QRect(-1, -1, 247, 244))
        self.longDescriptionBrowser.setStyleSheet(u"QTextBrowser {\n"
"	border-style: hidden;\n"
"}")
        self.longDescriptionBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.longDescriptionLoadingSpinner = QLabel(self.Description)
        self.longDescriptionLoadingSpinner.setObjectName(u"longDescriptionLoadingSpinner")
        self.longDescriptionLoadingSpinner.setGeometry(QRect(210, 210, 32, 32))
        self.tabMetadata.addTab(self.Description, "")
        self.RawTab = QWidget()
        self.RawTab.setObjectName(u"RawTab")
        self.SupportedControllersListWidget = QListWidget(self.RawTab)
        self.SupportedControllersListWidget.setObjectName(u"SupportedControllersListWidget")
        self.SupportedControllersListWidget.setGeometry(QRect(0, 0, 245, 244))
        self.SupportedControllersListWidget.setStyleSheet(u"QListWidget {\n"
"	border: unset;\n"
"}")
        self.SupportedControllersListWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.SupportedControllersListWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.SupportedControllersListWidget.setIconSize(QSize(30, 30))
        self.SupportedControllersListWidget.setMovement(QListView.Static)
        self.SupportedControllersListWidget.setViewMode(QListView.ListMode)
        self.SupportedControllersListWidget.setWordWrap(True)
        self.tabMetadata.addTab(self.RawTab, "")

        self.verticalLayout_3.addWidget(self.MetadataTabsFrame)

        self.MetadataBottomFrame = QFrame(self.SelectionInfoBox)
        self.MetadataBottomFrame.setObjectName(u"MetadataBottomFrame")
        self.MetadataBottomFrame.setMaximumSize(QSize(16777215, 34))
        self.MetadataBottomFrame.setFrameShape(QFrame.NoFrame)
        self.MetadataBottomFrame.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.MetadataBottomFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.ViewMetadataBtn = QPushButton(self.MetadataBottomFrame)
        self.ViewMetadataBtn.setObjectName(u"ViewMetadataBtn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.ViewMetadataBtn.sizePolicy().hasHeightForWidth())
        self.ViewMetadataBtn.setSizePolicy(sizePolicy6)

        self.horizontalLayout_6.addWidget(self.ViewMetadataBtn)

        self.WiiLoadButton = QPushButton(self.MetadataBottomFrame)
        self.WiiLoadButton.setObjectName(u"WiiLoadButton")
        sizePolicy6.setHeightForWidth(self.WiiLoadButton.sizePolicy().hasHeightForWidth())
        self.WiiLoadButton.setSizePolicy(sizePolicy6)

        self.horizontalLayout_6.addWidget(self.WiiLoadButton)


        self.verticalLayout_3.addWidget(self.MetadataBottomFrame)

        self.MetadataBottomFrame.raise_()
        self.MetadataTabsFrame.raise_()

        self.horizontalLayout_2.addWidget(self.SelectionInfoBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuDebug = QMenu(self.menubar)
        self.menuDebug.setObjectName(u"menuDebug")
        self.menuExperimental = QMenu(self.menuDebug)
        self.menuExperimental.setObjectName(u"menuExperimental")
        self.menuAnnouncement_Banner = QMenu(self.menuExperimental)
        self.menuAnnouncement_Banner.setObjectName(u"menuAnnouncement_Banner")
        self.menuClients = QMenu(self.menubar)
        self.menuClients.setObjectName(u"menuClients")
        self.menuHomebrew_Browser = QMenu(self.menuClients)
        self.menuHomebrew_Browser.setObjectName(u"menuHomebrew_Browser")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuClients.menuAction())
        self.menubar.addAction(self.menuDebug.menuAction())
        self.menuAbout.addAction(self.actionAbout_OSC_DL)
        self.menuAbout.addAction(self.actionIcons_provided_by)
        self.menuDebug.addAction(self.actionCopy_Direct_Link)
        self.menuDebug.addSeparator()
        self.menuDebug.addAction(self.actionEnable_Log_File)
        self.menuDebug.addAction(self.actionClear_Log)
        self.menuDebug.addSeparator()
        self.menuDebug.addAction(self.menuExperimental.menuAction())
        self.menuExperimental.addAction(self.menuAnnouncement_Banner.menuAction())
        self.menuExperimental.addAction(self.actionSelect_Theme)
        self.menuAnnouncement_Banner.addAction(self.actionDisplay_Banner)
        self.menuClients.addAction(self.menuHomebrew_Browser.menuAction())
        self.menuClients.addSeparator()
        self.menuClients.addAction(self.actionCheck_for_Updates)
        self.menuClients.addAction(self.actionRefresh)
        self.menuHomebrew_Browser.addAction(self.actionDownload_HBB_Client_Latest)

        self.retranslateUi(MainWindow)

        self.listAppsWidget.setCurrentRow(-1)
        self.tabMetadata.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Open Shop Channel Downloader - Library", None))
        self.actionAbout_OSC_DL.setText(QCoreApplication.translate("MainWindow", u"About OSC-DL", None))
        self.actionEnable_Log_File.setText(QCoreApplication.translate("MainWindow", u"Enable GUI Log File", None))
#if QT_CONFIG(shortcut)
        self.actionEnable_Log_File.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionClear_Log.setText(QCoreApplication.translate("MainWindow", u"Clear GUI Log", None))
        self.actionDownload_HBB_Client_Latest.setText(QCoreApplication.translate("MainWindow", u"Download Homebrew Browser", None))
        self.actionCheck_for_Updates.setText(QCoreApplication.translate("MainWindow", u"Check for Updates", None))
        self.actionClose_the_shop.setText(QCoreApplication.translate("MainWindow", u"Close the shop", None))
        self.actionDisplay_Banner.setText(QCoreApplication.translate("MainWindow", u"Reload Announcement Banner", None))
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh List", None))
#if QT_CONFIG(shortcut)
        self.actionRefresh.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.actionSelect_Theme.setText(QCoreApplication.translate("MainWindow", u"Select Theme", None))
        self.actionIcons_provided_by.setText(QCoreApplication.translate("MainWindow", u"Icons provided by https://icons8.com", None))
        self.actionCopy_Direct_Link.setText(QCoreApplication.translate("MainWindow", u"Copy Direct Link to App", None))
        self.actionDeveloper_Profile.setText(QCoreApplication.translate("MainWindow", u"Developer Profile", None))
#if QT_CONFIG(tooltip)
        self.actionDeveloper_Profile.setToolTip(QCoreApplication.translate("MainWindow", u"View Profile", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.centralwidget.setAccessibleName(QCoreApplication.translate("MainWindow", u"centralcontainer", None))
#endif // QT_CONFIG(accessibility)
        self.AppsLibraryBox.setTitle(QCoreApplication.translate("MainWindow", u"Apps Library", None))
        self.ViewDevWebsite.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://oscwii.org/library?coder=\"><span style=\" text-decoration: underline; color:#0000ff;\">Profile on Website</span></a></p></body></html>", None))
        self.AppsAmountLabel.setText(QCoreApplication.translate("MainWindow", u"0 Apps", None))
        self.ReturnToMainBtn.setText(QCoreApplication.translate("MainWindow", u"Return to All Apps", None))
        self.SearchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Applications..", None))
        self.CategoriesComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All Apps", None))
        self.CategoriesComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Utilities", None))
        self.CategoriesComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Emulators", None))
        self.CategoriesComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Games", None))
        self.CategoriesComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Media", None))
        self.CategoriesComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Demos", None))

        self.announcementLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Announcement Header: </span>Announcement Content.</p></body></html>", None))
        self.announcementURLLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://google.com\"><span style=\" text-decoration: underline; color:#ffff00;\">Announcement URL</span></a></p></body></html>", None))
        self.SelectionInfoBox.setTitle(QCoreApplication.translate("MainWindow", u"Application Metadata", None))
#if QT_CONFIG(accessibility)
        self.GeneralTab.setAccessibleName(QCoreApplication.translate("MainWindow", u"tabcontent", None))
#endif // QT_CONFIG(accessibility)
        self.label_description.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_displayname.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.HomebrewIconLabel.setText(QCoreApplication.translate("MainWindow", u"No homebrew icon. Aw.", None))
        self.HomebrewCategoryLabel.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.statusIcon.setText("")
        self.label_releasedate.setText(QCoreApplication.translate("MainWindow", u"Release Date", None))
        self.label_filesize.setText(QCoreApplication.translate("MainWindow", u"File Size", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_developer.setText(QCoreApplication.translate("MainWindow", u"Developer", None))
        self.label_appname.setText(QCoreApplication.translate("MainWindow", u"App Name", None))
        self.appname.setText("")
        self.appname.setPlaceholderText("")
        self.tabMetadata.setTabText(self.tabMetadata.indexOf(self.GeneralTab), QCoreApplication.translate("MainWindow", u"General", None))
#if QT_CONFIG(accessibility)
        self.Description.setAccessibleName(QCoreApplication.translate("MainWindow", u"tabcontent", None))
#endif // QT_CONFIG(accessibility)
        self.longDescriptionBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.longDescriptionLoadingSpinner.setText("")
        self.tabMetadata.setTabText(self.tabMetadata.indexOf(self.Description), QCoreApplication.translate("MainWindow", u"Description", None))
#if QT_CONFIG(accessibility)
        self.RawTab.setAccessibleName(QCoreApplication.translate("MainWindow", u"tabcontent", None))
#endif // QT_CONFIG(accessibility)
        self.tabMetadata.setTabText(self.tabMetadata.indexOf(self.RawTab), QCoreApplication.translate("MainWindow", u"Peripherals", None))
        self.ViewMetadataBtn.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.WiiLoadButton.setText(QCoreApplication.translate("MainWindow", u"Send to Wii", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuDebug.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuExperimental.setTitle(QCoreApplication.translate("MainWindow", u"Experimental", None))
        self.menuAnnouncement_Banner.setTitle(QCoreApplication.translate("MainWindow", u"Announcement Banner", None))
        self.menuClients.setTitle(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.menuHomebrew_Browser.setTitle(QCoreApplication.translate("MainWindow", u"Homebrew Browser", None))
    # retranslateUi

