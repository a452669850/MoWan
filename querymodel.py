import typing

import qtawesome
from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant, QSize

from magicPillWindow import *
from PyQt5.QtWidgets import QItemDelegate, QHBoxLayout, QWidget, QTableView


class QPushButton(QtWidgets.QPushButton):
    def __init__(self, *__args: any,clicked = None):
        super(QPushButton,self).__init__(*__args)
        self.setCursor(Qt.PointingHandCursor)
        self.setIconSize(QSize(14, 14))




class myTableModel(QAbstractTableModel):
    def __init__(self, header, data: list):
        QAbstractTableModel.__init__(self, parent=None)
        self.header = header
        self.datas = data

    def append_data(self, x):
        self.datas.append(x)
        self.layoutChanged.emit()

    def remove_row(self, row):
        self.datas.pop(row)
        self.layoutChanged.emit()

    def rowCount(self, parent: QModelIndex = ...) -> int:
        if len(self.datas) > 0:
            return len(self.datas)
        return 0

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return len(self.header)

    def data(self, QModelIndex, role=None):
        # print(Qt.__dict__.items())
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        if not QModelIndex.isValid():
            print("行或者列有问题")
            return QVariant()
        # if role == Qt.BackgroundColorRole:
        #     if QModelIndex.column() == 3:
        #         return QtGui.QColor('black')
        if role == Qt.TextColorRole:
            if QModelIndex.column() == 6:
                return QtGui.QColor('#1fbb6f')
            return QtGui.QColor('#ffffff')
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.datas[QModelIndex.row()][QModelIndex.column()]);

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return self.header[section]


class MyButtonDelegate(QItemDelegate):
    """该类用于向单元格中添加按钮  任务表格"""

    def __init__(self, parent=None):
        super(MyButtonDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        if not self.parent().indexWidget(index):
            self.button1 = QPushButton(
                qtawesome.icon('fa.play', color='#1fbb6f'),
                "",
                self.parent(),
                clicked=self.start_action
            )
            # self.button1.setIconSize(QSize(15, 15))
            self.button1.setStyleSheet("border:none;")
            self.button2 = QPushButton(
                qtawesome.icon('fa.pencil', color='white'),
                "",
                self.parent(),
                clicked=self.edit_action
            )
            self.button2.setStyleSheet("border:none;")
            self.button3 = QPushButton(
                qtawesome.icon('fa.trash', color='#ff6d6d'),
                "",
                self.parent(),
                clicked=self.delete_action
            )
            self.button3.setStyleSheet("border:none;")
            self.button4 = QPushButton(
                qtawesome.icon('fa.clone', color='#393c4e'),
                "",
                self.parent(),
                clicked=self.copy_action
            )

            self.button1.clicked.connect(self.start_action)
            self.button2.clicked.connect(self.edit_action)
            self.button3.clicked.connect(self.delete_action)
            self.button4.clicked.connect(self.copy_action)

            self.button4.setStyleSheet("border:none;")
            self.button1.index = [index.row(), index.column()]
            self.button2.index = [index.row(), index.column()]
            self.button3.index = [index.row(), index.column()]
            self.button4.index = [index.row(), index.column()]
            h_box_layout = QHBoxLayout()
            h_box_layout.addWidget(self.button1)
            h_box_layout.addWidget(self.button2)
            h_box_layout.addWidget(self.button3)
            h_box_layout.addWidget(self.button4)
            h_box_layout.setContentsMargins(0, 0, 0, 0)
            h_box_layout.setAlignment(Qt.AlignCenter)
            widget = QWidget()
            widget.setLayout(h_box_layout)
            self.parent().setIndexWidget(
                index,
                widget
            )
            widget.setStyleSheet('''
            QWidget{background : #1c1e28;
            margin-bottom:4px;
            margin-top:4px;}''')

    def start_action(self):
        TaskFunc.item_start_action(self)

    def edit_action(self):
        print(1)
        self.win = addTaskWindow()
        self.win.setWindowModality(Qt.ApplicationModal)
        self.win.show()

    def delete_action(self):
        TaskFunc.item_delete_action(self)

    def copy_action(self):
        TaskFunc.item_copy_action(self)


class MyButtonDelegate1(QItemDelegate):
    def __init__(self, parent=None):
        super(MyButtonDelegate1, self).__init__(parent)

    def paint(self, painter, option, index):
        if not self.parent().indexWidget(index):
            self.button1 = QPushButton(
                qtawesome.icon('fa.pencil', color='white'),
                "",
                self.parent(),
                clicked=self.edit_action
            )
            self.button1.setStyleSheet("border:none;")
            self.button2 = QPushButton(
                qtawesome.icon('fa.trash', color='#ff6d6d'),
                "",
                self.parent(),
                clicked=self.delete_action
            )
            self.button2.setStyleSheet("border:none;")
            self.button1.index = [index.row(), index.column()]
            self.button2.index = [index.row(), index.column()]
            h_box_layout = QHBoxLayout()
            h_box_layout.addWidget(self.button1)
            h_box_layout.addWidget(self.button2)
            h_box_layout.setContentsMargins(0, 0, 0, 0)
            h_box_layout.setAlignment(Qt.AlignCenter)
            widget = QWidget()
            widget.setLayout(h_box_layout)
            self.parent().setIndexWidget(
                index,
                widget
            )
            widget.setStyleSheet('''
            QWidget{background : #1c1e28;
            margin-bottom:5px;
            margin-top:5px;}''')

            self.button1.clicked.connect(self.edit_action)
            self.button2.clicked.connect(self.delete_action)

    def edit_action(self):
        self.win = addAgentWindow()        
        self.win.setWindowModality(Qt.ApplicationModal)
        self.win.show()

    def delete_action(self):
        AgentFunc.item_delete_action(self)

    def copy_action(self):
        AgentFunc.item_copy_action(self)


class MyButtonDelegate2(QItemDelegate):
    def __init__(self, parent=None):
        super(MyButtonDelegate2, self).__init__(parent)

    def paint(self, painter, option, index):
        if not self.parent().indexWidget(index):
            self.button1 = QPushButton(
                qtawesome.icon('fa.play', color='#1fbb6f'),
                "",
                self.parent(),
                clicked=self.start_action
            )
            self.button1.setStyleSheet("border:none;")
            self.button2 = QPushButton(
                qtawesome.icon('fa.pencil', color='white'),
                "",
                self.parent(),
                clicked=self.edit_action
            )
            self.button2.setStyleSheet("border:none;")
            self.button3 = QPushButton(
                qtawesome.icon('fa.trash', color='#ff6d6d'),
                "",
                self.parent(),
                clicked=self.delete_action
            )
            self.button3.setStyleSheet("border:none;")
            self.button1.index = [index.row(), index.column()]
            self.button2.index = [index.row(), index.column()]
            self.button3.index = [index.row(), index.column()]
            h_box_layout = QHBoxLayout()
            h_box_layout.addWidget(self.button1)
            h_box_layout.addWidget(self.button2)
            h_box_layout.addWidget(self.button3)
            h_box_layout.setContentsMargins(0, 0, 0, 0)
            h_box_layout.setAlignment(Qt.AlignCenter)
            widget = QWidget()
            widget.setLayout(h_box_layout)
            self.parent().setIndexWidget(
                index,
                widget
            )
            widget.setStyleSheet('''
            QWidget{background : #1c1e28;
            margin-bottom:4px;
            margin-top:4px;}''')

            self.button1.clicked.connect(self.start_action)
            self.button2.clicked.connect(self.edit_action)
            self.button3.clicked.connect(self.delete_action)


    def start_action(self):
        AccountFunc.item_start_action(self)

    def edit_action(self):
        self.win = addUserWindow()
        self.win.setWindowModality(Qt.ApplicationModal)
        self.win.show()

    def delete_action(self):
        AccountFunc.item_delete_action(self)



class MyButtonDelegate3(QItemDelegate):
    def __init__(self, parent=None):
        super(MyButtonDelegate3, self).__init__(parent)
        self.paren = parent

    def paint(self, painter, option, index):
        if not self.parent().indexWidget(index):
            self.button1 = QPushButton(
                qtawesome.icon('fa.repeat', color='#1fbb6f'),
                "",
                self.parent(),
                clicked=self.repeat_action
            )
            self.button1.setStyleSheet("border:none;")
            self.button2 = QPushButton(
                qtawesome.icon('fa.pencil', color='white'),
                "",
                self.parent(),
                clicked=self.edit_action
            )
            self.button2.setStyleSheet("border:none;")
            self.button3 = QPushButton(
                qtawesome.icon('fa.trash', color='#ff6d6d'),
                "",
                self.parent(),
                clicked=self.delete_action
            )
            self.button3.setStyleSheet("border:none;")
            self.button1.index = [index.row(), index.column()]
            self.button2.index = [index.row(), index.column()]
            self.button3.index = [index.row(), index.column()]
            h_box_layout = QHBoxLayout()
            h_box_layout.addWidget(self.button1)
            h_box_layout.addWidget(self.button2)
            h_box_layout.addWidget(self.button3)
            h_box_layout.setContentsMargins(0, 0, 0, 0)
            h_box_layout.setAlignment(Qt.AlignCenter)
            widget = QWidget()
            widget.setLayout(h_box_layout)
            self.parent().setIndexWidget(
                index,
                widget
            )
            widget.setStyleSheet('''
            QWidget{background : #1c1e28;
            margin-bottom:4px;
            margin-top:4px;}''')

            self.button1.clicked.connect(self.repeat_action)
            self.button2.clicked.connect(self.edit_action)
            self.button3.clicked.connect(self.delete_action)

    def repeat_action(self):
        if self.parent().__class__.__name__ == 'MyTableView3':
            DiscountFunc.item_repeat_action(self)
        elif self.parent().__class__.__name__ == 'MyTableView4':
            GiftFunc.item_repeat_action(self)

    def edit_action(self):
        if self.paren.__class__.__name__ == 'MyTableView4':
            self.win = addGiftWindow()
            self.win.setWindowModality(Qt.ApplicationModal)
            self.win.show()
        elif self.paren.__class__.__name__ == 'MyTableView3':
            self.win = addDiscountWindow()
            self.win.setWindowModality(Qt.ApplicationModal)
            self.win.show()

    def delete_action(self):
        if self.parent().__class__.__name__ == 'MyTableView3':
            DiscountFunc.item_delete_action(self)
        elif self.parent().__class__.__name__ == 'MyTableView4':
            GiftFunc.item_delete_action(self)


class MyButtonDelegate4(QItemDelegate):
    def __init__(self, parent=None):
        super(MyButtonDelegate4, self).__init__(parent)

    def paint(self, painter, option, index):
        if not self.parent().indexWidget(index):
            self.button1 = QPushButton(
                qtawesome.icon('fa.pencil', color='white'),
                "",
                self.parent(),
                clicked=self.edit_action
            )
            self.button1.setStyleSheet("border:none;")
            self.button2 = QPushButton(
                qtawesome.icon('fa.trash', color='#ff6d6d'),
                "",
                self.parent(),
                clicked=self.delete_action
            )
            self.button2.setStyleSheet("border:none;")
            self.button3 = QPushButton(
                qtawesome.icon('fa.clone', color='#393c4e'),
                "",
                self.parent(),
                clicked=self.copy_action
            )
            self.button3.setStyleSheet("border:none;")
            self.button1.index = [index.row(), index.column()]
            self.button2.index = [index.row(), index.column()]
            self.button3.index = [index.row(), index.column()]
            h_box_layout = QHBoxLayout()
            h_box_layout.addWidget(self.button1)
            h_box_layout.addWidget(self.button2)
            h_box_layout.addWidget(self.button3)
            h_box_layout.setContentsMargins(0, 0, 0, 0)
            h_box_layout.setAlignment(Qt.AlignCenter)
            widget = QWidget()
            widget.setLayout(h_box_layout)
            self.parent().setIndexWidget(
                index,
                widget
            )
            widget.setStyleSheet('''
            QWidget{background : #1c1e28;
            margin-bottom:4px;
            margin-top:4px;}''')

            self.button1.clicked.connect(self.edit_action)
            self.button2.clicked.connect(self.delete_action)
            self.button3.clicked.connect(self.copy_action)

    def copy_action(self):
        AddressFunc.item_copy_action(self)

    def edit_action(self):
        self.win = addAddressWindow()
        self.win.setWindowModality(Qt.ApplicationModal)
        self.win.show()

    def delete_action(self):
        AddressFunc.item_delete_action(self)


class MyTableView(QTableView):
    """重写的tableview"""

    def __init__(self, parent=None):
        super(MyTableView, self).__init__(parent)
        self.setItemDelegateForColumn(8, MyButtonDelegate(self))
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff) 

    def cellButtonClicked(self):
        print(1)


class MyTableView1(QTableView):
    def __init__(self, parent=None):
        super(MyTableView1, self).__init__(parent)
        self.setItemDelegateForColumn(3, MyButtonDelegate1(self))
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.verticalScrollBar().setStyleSheet('''QScrollBar:vertical{
                                                  margin-left:5px;
                                                  margin-top:25px;
                                                  width: 10px;
                                                  background:#181922;  
                                                  }
                                                  QScrollBar::handle:vertical{
                                                  background:#5c5858;}   
                                                  QScrollBar::handle:vertical:hover{
                                                  background:#5c5858;} 
                                                  QScrollBar::add-line:vertical{
                                                  background:#181922;}  
                                                  QScrollBar::sub-line:vertical{ 
                                                  background:#181922;}

                                                  QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
                                                  {background:#181922;;}''')

    def cellButtonClicked(self):
        print(1)


class MyTableView2(QTableView):
    def __init__(self, parent=None):
        super(MyTableView2, self).__init__(parent)
        self.setItemDelegateForColumn(4, MyButtonDelegate2(self))
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.verticalScrollBar().setStyleSheet('''QScrollBar:vertical{
                                                  margin-left:5px;
                                                  margin-top:25px;
                                                  width: 10px;
                                                  background:#181922;  
                                                  }
                                                  QScrollBar::handle:vertical{
                                                  background:#5c5858;}   
                                                  QScrollBar::handle:vertical:hover{
                                                  background:#5c5858;} 
                                                  QScrollBar::add-line:vertical{
                                                  background:#181922;}  
                                                  QScrollBar::sub-line:vertical{ 
                                                  background:#181922;}

                                                  QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
                                                  {background:#181922;;}''')

    def cellButtonClicked(self):
        print(1)


class MyTableView3(QTableView):
    def __init__(self, parent=None):
        super(MyTableView3, self).__init__(parent)
        self.setItemDelegateForColumn(3, MyButtonDelegate3(self))
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff) 
        self.verticalScrollBar().setStyleSheet('''QScrollBar:vertical{
                                                  margin-left:5px;
                                                  margin-top:25px;
                                                  width: 10px;
                                                  background:#181922;  
                                                  }
                                                  QScrollBar::handle:vertical{
                                                  background:#5c5858;}   
                                                  QScrollBar::handle:vertical:hover{
                                                  background:#5c5858;} 
                                                  QScrollBar::add-line:vertical{
                                                  background:#181922;}  
                                                  QScrollBar::sub-line:vertical{ 
                                                  background:#181922;}

                                                  QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
                                                  {background:#181922;;}''')

    def cellButtonClicked(self):
        print(1)


class MyTableView4(QTableView):
    def __init__(self, parent=None):
        super(MyTableView4, self).__init__(parent)
        self.setItemDelegateForColumn(6, MyButtonDelegate3(self))
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff) 
        self.verticalScrollBar().setStyleSheet('''QScrollBar:vertical{
                                                  margin-left:5px;
                                                  margin-top:25px;
                                                  width: 10px;
                                                  background:#181922;  
                                                  }
                                                  QScrollBar::handle:vertical{
                                                  background:#5c5858;}   
                                                  QScrollBar::handle:vertical:hover{
                                                  background:#5c5858;} 
                                                  QScrollBar::add-line:vertical{
                                                  background:#181922;}  
                                                  QScrollBar::sub-line:vertical{ 
                                                  background:#181922;}

                                                  QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
                                                  {background:#181922;;}''')

    def cellButtonClicked(self):
        print(1)


class MyTableView5(QTableView):
    def __init__(self, parent=None):
        super(MyTableView5, self).__init__(parent)
        self.setItemDelegateForColumn(5, MyButtonDelegate4(self))
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff) 
        self.verticalScrollBar().setStyleSheet('''QScrollBar:vertical{
                                                  margin-left:5px;
                                                  margin-top:25px;
                                                  width: 10px;
                                                  background:#181922;  
                                                  }
                                                  QScrollBar::handle:vertical{
                                                  background:#5c5858;}   
                                                  QScrollBar::handle:vertical:hover{
                                                  background:#5c5858;} 
                                                  QScrollBar::add-line:vertical{
                                                  background:#181922;}  
                                                  QScrollBar::sub-line:vertical{ 
                                                  background:#181922;}

                                                  QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
                                                  {background:#181922;;}''')

    def cellButtonClicked(self):
        print(1)

class MyTableView6(QTableView):
    def __init__(self, parent=None):
        super(MyTableView6, self).__init__(parent)
        self.setItemDelegateForColumn(5, MyButtonDelegate4(self))
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff) 
        self.verticalScrollBar().setStyleSheet('''QScrollBar:vertical{
                                                  margin-left:5px;
                                                  margin-top:25px;
                                                  width: 10px;
                                                  background:#181922;  
                                                  }
                                                  QScrollBar::handle:vertical{
                                                  background:#5c5858;}   
                                                  QScrollBar::handle:vertical:hover{
                                                  background:#5c5858;} 
                                                  QScrollBar::add-line:vertical{
                                                  background:#181922;}  
                                                  QScrollBar::sub-line:vertical{ 
                                                  background:#181922;}

                                                  QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
                                                  {background:#181922;;}''')

    def cellButtonClicked(self):
        print(1)