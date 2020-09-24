import sys

from Interface import *
from png import *
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QAbstractItemView, QTableView, QVBoxLayout, QSplitter, \
    QApplication, QGroupBox, QLabel, QGridLayout, QLineEdit, QComboBox, QTextEdit, QCheckBox,QVBoxLayout,QListView
from PyQt5.QtWidgets import QListWidget, QStackedWidget, QFrame
from PyQt5.QtWidgets import QListWidgetItem, QSizePolicy
from PyQt5.QtWidgets import QWidget, QSpacerItem, QHeaderView
from top import Top
from magicPillWindow import magicPillWindow, Version
import qtawesome

from PyQt5 import QtCore, QtGui, QtWidgets





class Bin(QWidget):
    def __init__(self):
        super(Bin, self).__init__()
        self.resize(960, 640)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 81, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout.setSpacing(12)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 39, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.confirm_btn = QPushButton(self)
        self.confirm_btn.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.confirm_btn)
        self.cancel_btn = QPushButton(self)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_3.setSpacing(15)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 81, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 2)
        self.verticalLayout_2.setStretch(5, 2)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.verticalLayout_2.setContentsMargins(0, 0, 0, 15)

        self.setWindowTitle("Form")
        # self.label.setText("TextLabel")

        pix = QtGui.QPixmap(':/static/logo.png')
        self.label.setPixmap(pix)
        self.label.setScaledContents(True)
        self.label.setMaximumSize(QSize(110,40))

        self.label_2.setText("key:")
        self.label_3.setText(Version)
        self.confirm_btn.setText("确定")
        self.cancel_btn.setText("取消")

        self.confirm_btn.clicked.connect(self.confirm_action)
        self.cancel_btn.clicked.connect(self.close)

        self.setStyleSheet('''QWidget{background : #181922;}
                            QLineEdit{

                            width: 360px;

                            height: 38px;

                            border-radius: 8px;

                            background: #21232f;

                            color: #5b5d6a;

                            font-family: "PingFangSC-Regular";

                            font-size: 18px;

                            font-weight: 400;

                            line-height: 13px;

                            }

                            QLabel{

                            width: 308px;

                            height: 16px;

                            color: #5b5d6a;

                            font-family: "PingFangSC-Regular";

                            font-size: 13px;

                            font-weight: 400;

                            line-height: 16px;

                            text-align: center;

                            }''')

        self.label_2.setStyleSheet('''

            width: 36px;

            height: 19px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 15px;

            font-weight: 400;

            line-height: 19px;

            ''')

        self.confirm_btn.setStyleSheet('''width: 100px;

                height: 30px; 

                border-radius: 6px;

                color: #ffffff;

                font-family: "PingFangSC-Medium";

                font-size: 12px;

                font-weight: 400;

                line-height: 16px;

                background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.cancel_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: #5c5858;''')
        # self.label.setStyleSheet('''border-image:url(:/static/logo.png)''')

    def mouseMoveEvent(self, e: QtGui.QMouseEvent):  # 重写移动事件
        try:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)
        except:
            pass

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = True
            self._startPos = QtCore.QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def confirm_action(self):
        key = self.lineEdit.text()
        win = magicPillWindow()
        win.show()
        self.close()


class QPushButton(QPushButton):
    def __init__(self, *__args: any,clicked = None):
        super(QPushButton,self).__init__(*__args)
        self.setCursor(Qt.PointingHandCursor)
        self.setIconSize(QSize(14, 14))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Bin()
    # ex = settingWindow()
    ex.show()
    sys.exit(app.exec_())