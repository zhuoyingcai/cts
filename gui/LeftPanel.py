""" Left Panel for CTS """

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QToolButton, QMenu, QFormLayout, QAction
from PyQt5.QtGui import QPixmap, QPalette, QIcon, QColor
from PyQt5.QtCore import Qt, QSize, QObjectCleanupHandler


class LeftPanel(QWidget):
    def __init__(self, width, hight, parent=None):
        super(LeftPanel, self).__init__(parent)

        # set width and hight
        self.width = width
        self.hight = hight

        # declare path string
        self.unknownUser = "../img/unknown-user.png"
        self.menuIcon = "../img/menu-icon.png"

        # declare user picture label
        self.pic = QLabel(self)
        self.pic.setScaledContents(True)

        # declare control panel
        self.controlPanel = QWidget(self)
        # declare control button
        self.homeB0 = QPushButton("Home")
        self.homeB1 = QPushButton("Home")
        self.homeB2 = QPushButton("Home")
        self.searchB = QPushButton("Search")
        self.currentProjectB = QPushButton("Current Project")
        self.submitProjectB = QPushButton("Submit Project")
        self.postProjectB = QPushButton("Post New Project")
        self.messageB = QPushButton("Message")
        self.historyB = QPushButton("History")
        self.manageTeam = QPushButton("Team Manager")
        # TODO: super user buttons
        # declare button list
        self.vblist = [self.homeB0, self.searchB]
        self.dblistNoTranaction = [self.homeB1, self.searchB, self.currentProjectB, self.submitProjectB, self.messageB,
                       self.historyB, self.manageTeam]
        self.dblistHasTranaction = [self.homeB2, self.searchB, self.currentProjectB, self.submitProjectB, self.messageB,
                       self.historyB, self.manageTeam]
        self.cblistNoTranaction = [self.homeB1, self.searchB, self.currentProjectB, self.postProjectB, self.messageB,
                       self.historyB]
        self.cblistHasTranaction = [self.homeB2, self.searchB, self.currentProjectB, self.postProjectB, self.messageB,
                       self.historyB]
        self.sublist = []

        # declare function button
        self.funcbutt = QToolButton(self)
        # declare action
        self.personalInfo = QAction("Personal Information")
        self.grandStat = QAction("Grand Statistic")
        self.out = QAction("Sign Out")

        # start initUI
        self.initUI()

    def initUI(self):
        # set LeftPanel size
        self.setFixedSize(self.width, self.hight)

        # set LeftPanel background color
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(self.backgroundRole(), QColor(40, 42, 45))
        self.setPalette(palette)

        # set pic
        self.setpic(self.unknownUser)
        # set pic size
        self.pic.setFixedSize(self.width - 20, self.width - 20)
        # add pic to LeftPanel
        self.pic.move(10, 10)

        # set stackWidget size
        self.controlPanel.setFixedSize(self.width, self.hight - 250)
        # add controlPanel to LeftPanel
        self.setControlPanel(0)
        self.controlPanel.move(0, 180)

        # set funcbutt menu
        self.setFuncMenu(False)
        self.funcbutt.setPopupMode(QToolButton.InstantPopup)
        # set image for funcbutt
        self.funcbutt.setIcon(QIcon(self.menuIcon))
        self.funcbutt.setIconSize(QSize(60, 30))
        # add funcbutt to LeftPanel
        self.funcbutt.setFixedSize(61, 31)
        self.funcbutt.move(39, self.hight - 43)
        # connect menu event


    def setpic(self, path):
        """ set pic to the path image"""
        pixmap = QPixmap(path)
        # when path not found
        if (pixmap.isNull()):
            pixmap = QPixmap(self.unknownUser)
        # scaled and set
        pixmap.scaled(60, 60, Qt.KeepAspectRatio)
        self.pic.setPixmap(pixmap)

    def setControlPanel(self, i):
        """set controlPanle widget index"""
        layout = QFormLayout()

        if (i == 0):
            for button in self.vblist:
                layout.addRow(button)
        if (i == 1):
            for button in self.dblistNoTranaction:
                layout.addRow(button)
        if (i == 2):
            for button in self.dblistHasTranaction:
                layout.addRow(button)
        if (i == 3):
            for button in self.cblistNoTranaction:
                layout.addRow(button)
        if (i == 4):
            for button in self.cblistHasTranaction:
                layout.addRow(button)
        if (i == 5):
            for button in self.sublist:
                layout.addRow(button)

        # delete and add layout to controlPanel
        QObjectCleanupHandler().add(self.controlPanel.layout())
        self.controlPanel.setLayout(layout)

    def setFuncMenu(self, login):
        if (login):
            mu = QMenu()
            mu.addAction(self.personalInfo)
            mu.addAction(self.grandStat)
            mu.addAction(self.out)
            self.funcbutt.setMenu(mu)
        else:
            mu = QMenu()
            mu.addAction(self.grandStat)
            self.funcbutt.setMenu(mu)
