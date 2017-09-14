from PyQt4 import QtCore, QtGui
import rersource_rc

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1921, 1080))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.widget = QtGui.QWidget(self.page)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1920, 150))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(310, 10, 300, 140))
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(169, 166, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(610, 10, 225, 140))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(169, 166, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(845, 10, 310, 140))
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgb(15, 255, 95);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(1155, 10, 225, 140))
        self.label_4.setStyleSheet(_fromUtf8("background-color: rgb(15, 255, 95);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(1390, 10, 240, 140))
        self.label_5.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(160, 10, 140, 140))
        self.label_6.setStyleSheet(_fromUtf8("background-color: rgb(255, 185, 237);"))
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(1630, 10, 50, 140))
        self.label_7.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 140, 140))
        self.label_9.setStyleSheet(_fromUtf8(""))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Sewing.png")))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(1680, 40, 230, 40))
        self.label_8.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(1680, 80, 230, 40))
        self.label_10.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.frame = QtGui.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(1620, 10, 290, 140))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.frame_2 = QtGui.QFrame(self.page)
        self.frame_2.setGeometry(QtCore.QRect(0, 150, 1390, 930))
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))

        self.gridLayout_2 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(9)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.frame_3 = QtGui.QFrame(self.page)
        self.frame_3.setGeometry(QtCore.QRect(1390, 150, 520, 930))
        self.frame_3.setStyleSheet(_fromUtf8("background-color: rgb(225, 148, 255);"))
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_11 = QtGui.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(50, 30, 221, 41))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(50, 190, 221, 41))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(40, 550, 221, 41))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.frame_4 = QtGui.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(170, 70, 2, 75))
        self.frame_4.setStyleSheet(_fromUtf8("background-color: rgb(118, 118, 118);"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.frame_5 = QtGui.QFrame(self.frame_3)
        self.frame_5.setGeometry(QtCore.QRect(170, 230, 2, 275))
        self.frame_5.setStyleSheet(_fromUtf8("background-color: rgb(118, 118, 118);"))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.frame_6 = QtGui.QFrame(self.frame_3)
        self.frame_6.setGeometry(QtCore.QRect(170, 600, 2, 210))
        self.frame_6.setStyleSheet(_fromUtf8("background-color: rgb(118, 118, 118);"))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.label_16 = QtGui.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(190, 450, 101, 31))
        self.label_16.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(190, 250, 111, 31))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.frame_3)
        self.label_18.setGeometry(QtCore.QRect(190, 320, 101, 31))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.frame_3)
        self.label_19.setGeometry(QtCore.QRect(190, 390, 101, 31))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.frame_3)
        self.label_20.setGeometry(QtCore.QRect(190, 620, 111, 31))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.frame_3)
        self.label_21.setGeometry(QtCore.QRect(190, 690, 101, 31))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.frame_3)
        self.label_22.setGeometry(QtCore.QRect(190, 760, 101, 31))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.frame_3)
        self.label_23.setGeometry(QtCore.QRect(330, 450, 101, 31))
        self.label_23.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.frame_3)
        self.label_24.setGeometry(QtCore.QRect(330, 250, 101, 31))
        self.label_24.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.frame_3)
        self.label_25.setGeometry(QtCore.QRect(330, 320, 101, 31))
        self.label_25.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(self.frame_3)
        self.label_26.setGeometry(QtCore.QRect(330, 390, 101, 31))
        self.label_26.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.frame_3)
        self.label_27.setGeometry(QtCore.QRect(330, 620, 101, 31))
        self.label_27.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(self.frame_3)
        self.label_28.setGeometry(QtCore.QRect(330, 690, 101, 31))
        self.label_28.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_29 = QtGui.QLabel(self.frame_3)
        self.label_29.setGeometry(QtCore.QRect(330, 760, 101, 31))
        self.label_29.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_30 = QtGui.QLabel(self.frame_3)
        self.label_30.setGeometry(QtCore.QRect(190, 90, 101, 31))
        self.label_30.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtGui.QLabel(self.frame_3)
        self.label_31.setGeometry(QtCore.QRect(330, 90, 101, 31))
        self.label_31.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.stackedWidget.addWidget(self.page)

        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.widget_2 = QtGui.QWidget(self.page_2)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 1931, 150))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_51 = QtGui.QLabel(self.widget_2)
        self.label_51.setGeometry(QtCore.QRect(310, 10, 300, 140))
        self.label_51.setStyleSheet(_fromUtf8("background-color: rgb(169, 166, 255);"))
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.label_52 = QtGui.QLabel(self.widget_2)
        self.label_52.setGeometry(QtCore.QRect(610, 10, 225, 140))
        self.label_52.setStyleSheet(_fromUtf8("background-color: rgb(169, 166, 255);"))
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.label_53 = QtGui.QLabel(self.widget_2)
        self.label_53.setGeometry(QtCore.QRect(845, 10, 310, 140))
        self.label_53.setStyleSheet(_fromUtf8("background-color: rgb(15, 255, 95);"))
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.label_54 = QtGui.QLabel(self.widget_2)
        self.label_54.setGeometry(QtCore.QRect(1155, 10, 225, 140))
        self.label_54.setStyleSheet(_fromUtf8("background-color: rgb(15, 255, 95);"))
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.label_55 = QtGui.QLabel(self.widget_2)
        self.label_55.setGeometry(QtCore.QRect(1390, 10, 240, 140))
        self.label_55.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.label_56 = QtGui.QLabel(self.widget_2)
        self.label_56.setGeometry(QtCore.QRect(160, 10, 140, 140))
        self.label_56.setStyleSheet(_fromUtf8("background-color: rgb(255, 185, 237);"))
        self.label_56.setScaledContents(False)
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.label_57 = QtGui.QLabel(self.widget_2)
        self.label_57.setGeometry(QtCore.QRect(1630, 10, 50, 140))
        self.label_57.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.label_58 = QtGui.QLabel(self.widget_2)
        self.label_58.setGeometry(QtCore.QRect(10, 10, 140, 140))
        self.label_58.setStyleSheet(_fromUtf8(""))
        self.label_58.setText(_fromUtf8(""))
        self.label_58.setPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Sewing.png")))
        self.label_58.setScaledContents(True)
        self.label_58.setObjectName(_fromUtf8("label_58"))
        self.label_59 = QtGui.QLabel(self.widget_2)
        self.label_59.setGeometry(QtCore.QRect(1680, 40, 230, 40))
        self.label_59.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.label_60 = QtGui.QLabel(self.widget_2)
        self.label_60.setGeometry(QtCore.QRect(1680, 80, 230, 40))
        self.label_60.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.frame_8 = QtGui.QFrame(self.widget_2)
        self.frame_8.setGeometry(QtCore.QRect(1620, 10, 290, 140))
        self.frame_8.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.frame_8.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.frame_8.raise_()
        self.label_51.raise_()
        self.label_52.raise_()
        self.label_53.raise_()
        self.label_54.raise_()
        self.label_55.raise_()
        self.label_56.raise_()
        self.label_57.raise_()
        self.label_58.raise_()
        self.label_59.raise_()
        self.label_60.raise_()
        self.frame_9 = QtGui.QFrame(self.page_2)
        self.frame_9.setGeometry(QtCore.QRect(0, 150, 1390, 930))
        self.frame_9.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_9.setObjectName(_fromUtf8("frame_9"))

        self.gridLayout_3 = QtGui.QGridLayout(self.frame_9)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setMargin(9)
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.frame_10 = QtGui.QFrame(self.page_2)
        self.frame_10.setGeometry(QtCore.QRect(1390, 150, 520, 930))
        self.frame_10.setStyleSheet(_fromUtf8("background-color: rgb(225, 148, 255);"))
        self.frame_10.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_10.setObjectName(_fromUtf8("frame_10"))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.widget_3 = QtGui.QWidget(self.page_3)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 1931, 150))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.label_61 = QtGui.QLabel(self.widget_3)
        self.label_61.setGeometry(QtCore.QRect(310, 10, 300, 140))
        self.label_61.setStyleSheet(_fromUtf8("background-color: rgb(169, 166, 255);"))
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.label_62 = QtGui.QLabel(self.widget_3)
        self.label_62.setGeometry(QtCore.QRect(610, 10, 225, 140))
        self.label_62.setStyleSheet(_fromUtf8("background-color: rgb(169, 166, 255);"))
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.label_63 = QtGui.QLabel(self.widget_3)
        self.label_63.setGeometry(QtCore.QRect(845, 10, 310, 140))
        self.label_63.setStyleSheet(_fromUtf8("background-color: rgb(15, 255, 95);"))
        self.label_63.setObjectName(_fromUtf8("label_63"))
        self.label_64 = QtGui.QLabel(self.widget_3)
        self.label_64.setGeometry(QtCore.QRect(1155, 10, 225, 140))
        self.label_64.setStyleSheet(_fromUtf8("background-color: rgb(15, 255, 95);"))
        self.label_64.setObjectName(_fromUtf8("label_64"))
        self.label_65 = QtGui.QLabel(self.widget_3)
        self.label_65.setGeometry(QtCore.QRect(1390, 10, 240, 140))
        self.label_65.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_65.setObjectName(_fromUtf8("label_65"))
        self.label_66 = QtGui.QLabel(self.widget_3)
        self.label_66.setGeometry(QtCore.QRect(160, 10, 140, 140))
        self.label_66.setStyleSheet(_fromUtf8("background-color: rgb(255, 185, 237);"))
        self.label_66.setScaledContents(False)
        self.label_66.setObjectName(_fromUtf8("label_66"))
        self.label_67 = QtGui.QLabel(self.widget_3)
        self.label_67.setGeometry(QtCore.QRect(1630, 10, 50, 140))
        self.label_67.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_67.setObjectName(_fromUtf8("label_67"))
        self.label_68 = QtGui.QLabel(self.widget_3)
        self.label_68.setGeometry(QtCore.QRect(10, 10, 140, 140))
        self.label_68.setStyleSheet(_fromUtf8(""))
        self.label_68.setText(_fromUtf8(""))
        self.label_68.setPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Sewing.png")))
        self.label_68.setScaledContents(True)
        self.label_68.setObjectName(_fromUtf8("label_68"))
        self.label_69 = QtGui.QLabel(self.widget_3)
        self.label_69.setGeometry(QtCore.QRect(1680, 40, 230, 40))
        self.label_69.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_69.setObjectName(_fromUtf8("label_69"))
        self.label_70 = QtGui.QLabel(self.widget_3)
        self.label_70.setGeometry(QtCore.QRect(1680, 80, 230, 40))
        self.label_70.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_70.setObjectName(_fromUtf8("label_70"))
        self.frame_11 = QtGui.QFrame(self.widget_3)
        self.frame_11.setGeometry(QtCore.QRect(1620, 10, 290, 140))
        self.frame_11.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.frame_11.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_11.setObjectName(_fromUtf8("frame_11"))
        self.frame_11.raise_()
        self.label_61.raise_()
        self.label_62.raise_()
        self.label_63.raise_()
        self.label_64.raise_()
        self.label_65.raise_()
        self.label_66.raise_()
        self.label_67.raise_()
        self.label_68.raise_()
        self.label_69.raise_()
        self.label_70.raise_()
        self.frame_12 = QtGui.QFrame(self.page_3)
        self.frame_12.setGeometry(QtCore.QRect(0, 150, 1390, 930))
        self.frame_12.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_12.setObjectName(_fromUtf8("frame_12"))

        self.gridLayout_5 = QtGui.QGridLayout(self.frame_12)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setMargin(9)
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_5.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.frame_13 = QtGui.QFrame(self.page_3)
        self.frame_13.setGeometry(QtCore.QRect(1390, 150, 520, 930))
        self.frame_13.setStyleSheet(_fromUtf8("background-color: rgb(225, 148, 255);"))
        self.frame_13.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_13.setObjectName(_fromUtf8("frame_13"))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.widget_4 = QtGui.QWidget(self.page_4)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 1931, 150))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.label_71 = QtGui.QLabel(self.widget_4)
        self.label_71.setGeometry(QtCore.QRect(310, 10, 300, 140))
        self.label_71.setStyleSheet(_fromUtf8("background-color: rgb(169, 166, 255);"))
        self.label_71.setObjectName(_fromUtf8("label_71"))
        self.label_72 = QtGui.QLabel(self.widget_4)
        self.label_72.setGeometry(QtCore.QRect(610, 10, 225, 140))
        self.label_72.setStyleSheet(_fromUtf8("background-color: rgb(169, 166, 255);"))
        self.label_72.setObjectName(_fromUtf8("label_72"))
        self.label_73 = QtGui.QLabel(self.widget_4)
        self.label_73.setGeometry(QtCore.QRect(845, 10, 310, 140))
        self.label_73.setStyleSheet(_fromUtf8("background-color: rgb(15, 255, 95);"))
        self.label_73.setObjectName(_fromUtf8("label_73"))
        self.label_74 = QtGui.QLabel(self.widget_4)
        self.label_74.setGeometry(QtCore.QRect(1155, 10, 225, 140))
        self.label_74.setStyleSheet(_fromUtf8("background-color: rgb(15, 255, 95);"))
        self.label_74.setObjectName(_fromUtf8("label_74"))
        self.label_75 = QtGui.QLabel(self.widget_4)
        self.label_75.setGeometry(QtCore.QRect(1390, 10, 240, 140))
        self.label_75.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_75.setObjectName(_fromUtf8("label_75"))
        self.label_76 = QtGui.QLabel(self.widget_4)
        self.label_76.setGeometry(QtCore.QRect(160, 10, 140, 140))
        self.label_76.setStyleSheet(_fromUtf8("background-color: rgb(255, 185, 237);"))
        self.label_76.setScaledContents(False)
        self.label_76.setObjectName(_fromUtf8("label_76"))
        self.label_77 = QtGui.QLabel(self.widget_4)
        self.label_77.setGeometry(QtCore.QRect(1630, 10, 50, 140))
        self.label_77.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_77.setObjectName(_fromUtf8("label_77"))
        self.label_78 = QtGui.QLabel(self.widget_4)
        self.label_78.setGeometry(QtCore.QRect(10, 10, 140, 140))
        self.label_78.setStyleSheet(_fromUtf8(""))
        self.label_78.setText(_fromUtf8(""))
        self.label_78.setPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Sewing.png")))
        self.label_78.setScaledContents(True)
        self.label_78.setObjectName(_fromUtf8("label_78"))
        self.label_79 = QtGui.QLabel(self.widget_4)
        self.label_79.setGeometry(QtCore.QRect(1680, 40, 230, 40))
        self.label_79.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_79.setObjectName(_fromUtf8("label_79"))
        self.label_80 = QtGui.QLabel(self.widget_4)
        self.label_80.setGeometry(QtCore.QRect(1680, 80, 230, 40))
        self.label_80.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.label_80.setObjectName(_fromUtf8("label_80"))
        self.frame_14 = QtGui.QFrame(self.widget_4)
        self.frame_14.setGeometry(QtCore.QRect(1620, 10, 290, 140))
        self.frame_14.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);"))
        self.frame_14.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_14.setObjectName(_fromUtf8("frame_14"))
        self.frame_14.raise_()
        self.label_71.raise_()
        self.label_72.raise_()
        self.label_73.raise_()
        self.label_74.raise_()
        self.label_75.raise_()
        self.label_76.raise_()
        self.label_77.raise_()
        self.label_78.raise_()
        self.label_79.raise_()
        self.label_80.raise_()
        self.frame_15 = QtGui.QFrame(self.page_4)
        self.frame_15.setGeometry(QtCore.QRect(0, 150, 1390, 930))
        self.frame_15.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_15.setObjectName(_fromUtf8("frame_15"))

        self.gridLayout_7 = QtGui.QGridLayout(self.frame_15)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setMargin(9)
        self.gridLayout_8.setHorizontalSpacing(6)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.frame_16 = QtGui.QFrame(self.page_4)
        self.frame_16.setGeometry(QtCore.QRect(1390, 150, 520, 930))
        self.frame_16.setStyleSheet(_fromUtf8("background-color: rgb(225, 148, 255);"))
        self.frame_16.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_16.setObjectName(_fromUtf8("frame_16"))
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.StackWidTimer = QtCore.QTimer()
        self.StackWidTimer.timeout.connect(self.stackchange)
        self.StackWidTimer.start(10000)

        self.StackWidTimer1 = QtCore.QTimer()
        self.StackWidTimer1.timeout.connect(self.graph_draw)
        self.StackWidTimer1.start(1000)




    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DSI - SP Production Monitoring System", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">Target</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">100</span></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">Actual</span></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">95</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:48pt; color:#ffffff;\">12:00</span></p></body></html>", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">A</span></p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">PM</span></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Wednesday</span></p></body></html>", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">September</span></p></body></html>", None))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Hourly</span></p></body></html>", None))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Daily</span></p></body></html>", None))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Monthly</span></p></body></html>", None))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Loss</span></p></body></html>", None))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Target</span></p></body></html>", None))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Actual</span></p></body></html>", None))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Required</span></p></body></html>", None))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Target</span></p></body></html>", None))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Actual</span></p></body></html>", None))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Required</span></p></body></html>", None))

        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">05</span></p></body></html>", None))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">10000</span></p></body></html>", None))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">9500</span></p></body></html>", None))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">500</span></p></body></html>", None))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">30000</span></p></body></html>", None))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">25000</span></p></body></html>", None))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">5000</span></p></body></html>", None))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Loss</span></p></body></html>", None))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">205</span></p></body></html>", None))
        self.label_51.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">Target</span></p></body></html>", None))
        self.label_52.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">110</span></p></body></html>", None))
        self.label_53.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">Actual</span></p></body></html>", None))
        self.label_54.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">97</span></p></body></html>", None))
        self.label_55.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:48pt; color:#ffffff;\">12:00</span></p></body></html>", None))
        self.label_56.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">B</span></p></body></html>", None))
        self.label_57.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">PM</span></p></body></html>", None))
        self.label_59.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Wednesday</span></p></body></html>", None))
        self.label_60.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">September</span></p></body></html>", None))
        self.label_61.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">Target</span></p></body></html>", None))
        self.label_62.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">115</span></p></body></html>", None))
        self.label_63.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">Actual</span></p></body></html>", None))
        self.label_64.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">100</span></p></body></html>", None))
        self.label_65.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:48pt; color:#ffffff;\">12:00</span></p></body></html>", None))
        self.label_66.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">C</span></p></body></html>", None))
        self.label_67.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">PM</span></p></body></html>", None))
        self.label_69.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Wednesday</span></p></body></html>", None))
        self.label_70.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">September</span></p></body></html>", None))
        self.label_71.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">Target</span></p></body></html>", None))
        self.label_72.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">115</span></p></body></html>", None))
        self.label_73.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">Actual</span></p></body></html>", None))
        self.label_74.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; color:#ffffff;\">100</span></p></body></html>", None))
        self.label_75.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:48pt; color:#ffffff;\">12:00</span></p></body></html>", None))
        self.label_76.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">D</span></p></body></html>", None))
        self.label_77.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">PM</span></p></body></html>", None))
        self.label_79.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Wednesday</span></p></body></html>", None))
        self.label_80.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">September</span></p></body></html>", None))
