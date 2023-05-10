from PyQt5 import QtCore, QtGui, QtWidgets
import mongo

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.currentWidgets = []
        self.activeWindow = 'topMovies'
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(375, 491)
        MainWindow.setStyleSheet("#MainWindow {background-color:#202020;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 400, 381, 80))
        self.groupBox.setStyleSheet(".QGroupBox {background-color:#323232;border:none;}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.pushButton = QtWidgets.QPushButton(self.groupBox, clicked = lambda: self.listWindow())
        self.pushButton.setGeometry(QtCore.QRect(50, 20, 51, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("#pushButton{border:none;background-color:none;}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/rank2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(64, 64))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox, clicked = lambda: self.savedWindow())
        self.pushButton_2.setGeometry(QtCore.QRect(280, 20, 61, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("#pushButton_2 {border:none;background-color:none;}")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/bookmark2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox, clicked = lambda: self.filterWindow())
        self.pushButton_3.setGeometry(QtCore.QRect(160, 10, 71, 51))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("#pushButton_3 {border:none;background-color:none;}")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/review2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_3.setObjectName("pushButton_3")

        self.listWindow()
        self.searchMovies()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.enterEvent = self.on_enter_button
        self.pushButton.leaveEvent = self.on_leave_button

        self.pushButton_2.enterEvent = self.on_enter_button_2
        self.pushButton_2.leaveEvent = self.on_leave_button_2

        self.pushButton_3.enterEvent = self.on_enter_button_3
        self.pushButton_3.leaveEvent = self.on_leave_button_3

    def on_enter_button(self, event):
        self.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/rank2.png')))
    def on_leave_button(self, event):
        if self.activeWindow != 'topMovies':
            self.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/quality3.png')))
    
    def on_enter_button_2(self, event):
        self.pushButton_2.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/bookmark.png')))
    def on_leave_button_2(self, event):
        if self.activeWindow != 'savedMovies':
            self.pushButton_2.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/bookmark2.png')))
    
    def on_enter_button_3(self, event):
        self.pushButton_3.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/review.png')))
    def on_leave_button_3(self, event):
        if self.activeWindow != 'filterMovies':
            self.pushButton_3.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/review2.png')))


    def clearCentralWidget(self):
        for widget in self.currentWidgets:
            widget.setParent(None)
            widget.hide()
            widget.deleteLater()
            self.currentWidgets.remove(widget)

    def listView(self):
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 25, 295, 31))
        self.lineEdit.setStyleSheet("#lineEdit {border:none;border-radius:6px;font-size:16px;padding-left:10px;}")
        self.lineEdit.setObjectName("lineEdit")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.searchMovies())
        self.pushButton_4.setGeometry(QtCore.QRect(295, 29, 24, 24))
        self.pushButton_4.setText("")
        self.pushButton_4.setStyleSheet("#pushButton_4 {border:none;background-color:none;}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        self.currentWidgets.append(self.lineEdit)
        self.currentWidgets.append(self.pushButton_4)

        self.scroll = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll.setWidgetResizable(True)
        self.scroll.setGeometry(QtCore.QRect(0, 70, 375, 320))
        scrollContent = QtWidgets.QWidget(self.scroll)
        self.scrollLayout = QtWidgets.QVBoxLayout(scrollContent)
        scrollContent.setLayout(self.scrollLayout)
        self.scroll.setWidget(scrollContent)
        self.scrollLayout.setAlignment(QtCore.Qt.AlignTop)
        self.currentWidgets.append(self.scroll)
        self.scroll.setStyleSheet("""
        QWidget {
            background-color: transparent;
            border:none;
        }""")
        scrollContent.setStyleSheet("""
        QWidget {
            background-color: transparent;
        }""")

        self.scroll.verticalScrollBar().setStyleSheet("""
        QScrollBar:vertical {
            background-color: transparent;
            width: 7px;
            margin: 0px 0px 0px 0px;
        }
        QScrollBar::handle:vertical {
            background-color: #57595a;
            min-height: 20px;
            border-radius: 3px;
        }
        QScrollBar::add-line:vertical {
            background-color: transparent;
            height: 10px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            background-color: transparent;
            height: 10px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background-color: none;
            border-radius: 10px;
        }
        """)
        self.lineEdit.show()
        self.pushButton_4.show()
        self.scroll.show()

    def searchMovies(self):
        for i in reversed(range(self.scrollLayout.count())): 
            self.scrollLayout.itemAt(i).widget().deleteLater()
        names = mongo.getByName(self.lineEdit.text())
        for movie in names:
            box = QtWidgets.QGroupBox()
            buttonName = QtWidgets.QPushButton(movie['name'], box)
            buttonName.clicked.connect(lambda _, m=movie: self.movieWindow(m))
            buttonName.setGeometry(QtCore.QRect(10, 5, 325, 24))
            buttonName.setStyleSheet("QPushButton{text-align:left;color:#fffffd;font-size:16px;font-weight:bold;}")
            buttonName.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            
            labelLength = QtWidgets.QLabel(f"{movie['length']}", box)
            labelLength.setGeometry(QtCore.QRect(10, 30, 335, 24))
            labelLength.setStyleSheet("QLabel{text-align:left;color:#c6c6c6;font-size:11px;font-weight:bold;}")
            
            labelRating = QtWidgets.QLabel(f"{movie['rating']}/10", box)
            labelRating.setGeometry(QtCore.QRect(60, 30, 335, 24))
            labelRating.setStyleSheet("QLabel{text-align:left;color:#c6c6c6;font-size:11px;font-weight:bold;}")


            labelStar1 = QtWidgets.QLabel(f"{movie['stars'][0]}   -", box)
            labelStar1.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            labelStar1_Size = labelStar1.sizeHint()
            labelStar1.setGeometry(QtCore.QRect(10, 55, labelStar1_Size.width()+5, labelStar1_Size.height()))
            labelStar1.setStyleSheet("QLabel {color: #c6c6c6; font-size: 10px; font-weight: bold;}")
            # ---
            labelStar2 = QtWidgets.QLabel(f"{movie['stars'][1]}   -", box)
            labelStar2.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            labelStar2_Size = labelStar2.sizeHint()
            labelStar2.setGeometry(QtCore.QRect(labelStar1.geometry().right() + 10, 55, labelStar2_Size.width()+5, labelStar2_Size.height()))
            labelStar2.setStyleSheet("QLabel {color: #c6c6c6; font-size: 10px; font-weight: bold;}")
            # ---
            labelStar3 = QtWidgets.QLabel(f"{movie['stars'][2]}", box)
            labelStar3.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            labelStar3_Size = labelStar3.sizeHint()
            labelStar3.setGeometry(QtCore.QRect(labelStar2.geometry().right() + 10, 55, labelStar3_Size.width()+5, labelStar3_Size.height()))
            labelStar3.setStyleSheet("QLabel {color: #c6c6c6; font-size: 10px; font-weight: bold;}")
            
            box.setMaximumHeight(80)
            box.setMaximumWidth(350)
            box.setMinimumHeight(80)
            box.setMinimumWidth(350)
            box.setStyleSheet(".QGroupBox {background-color:#323232;border:none;border-radius:10px;}")
            
            self.scrollLayout.insertWidget(300, box)
    
    def listWindow(self):
        self.clearCentralWidget()
        self.clearCentralWidget()
        self.clearCentralWidget()
        self.clearCentralWidget()
        self.listView()
        self.activeWindow = 'topMovies'
        self.switchWindows()

    def movieView(self, movie):
        movieWidgets = []
        
        backButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.listWindow())
        backButton.setGeometry(QtCore.QRect(20, 83, 40, 40))
        backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        backButton.setStyleSheet("QPushButton{border:none;background-color:none;}")
        backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        backButton.setIcon(icon)
        def on_enter_backButton(event):
            backButton.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/back2.png')))
        def on_leave_backButton(event):
            backButton.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/back.png')))
        backButton.setIconSize(QtCore.QSize(40, 40))
        backButton.enterEvent = on_enter_backButton
        backButton.leaveEvent = on_leave_backButton
        movieWidgets.append(backButton)
        self.currentWidgets.append(backButton)
        
        boxTitle = QtWidgets.QGroupBox(self.centralwidget)
        boxTitle.setStyleSheet(".QGroupBox {background-color:#323232;border:none;border-radius:10px;}")
        boxTitle.setGeometry(QtCore.QRect(70, 70, 290, 70))
        movieWidgets.append(boxTitle)
        self.currentWidgets.append(boxTitle)
        title = QtWidgets.QLabel(movie['name'], boxTitle)
        title.setGeometry(QtCore.QRect(15, 0, 260, 36))
        title.setStyleSheet("QLabel{text-align:left;color:#fffffd;font-size:14px;font-weight:bold;}")
        movieWidgets.append(title)
        self.currentWidgets.append(title)
        rating = QtWidgets.QLabel(f"{movie['rating']}/10", boxTitle)
        rating.setGeometry(QtCore.QRect(15, 25, 285, 36))
        rating.setStyleSheet("QLabel{text-align:left;color:#c6c6c6;font-size:12px;font-weight:bold;}")
        movieWidgets.append(rating)
        self.currentWidgets.append(rating)
        year = QtWidgets.QLabel(f"{movie['year']}", boxTitle)
        year.setGeometry(QtCore.QRect(75, 25, 285, 36))
        year.setStyleSheet("QLabel{text-align:left;color:#c6c6c6;font-size:12px;font-weight:bold;}")
        movieWidgets.append(year)
        self.currentWidgets.append(year)
        length = QtWidgets.QLabel(f"{movie['length']}", boxTitle)
        length.setGeometry(QtCore.QRect(125, 25, 285, 36))
        length.setStyleSheet("QLabel{text-align:left;color:#c6c6c6;font-size:12px;font-weight:bold;}")
        movieWidgets.append(length)
        self.currentWidgets.append(length)

        boxInfo = QtWidgets.QGroupBox(self.centralwidget)
        boxInfo.setStyleSheet(".QGroupBox {background-color:#323232;border:none;border-radius:10px;}")
        boxInfo.setGeometry(QtCore.QRect(15, 150, 345, 150))
        movieWidgets.append(boxInfo)
        self.currentWidgets.append(boxInfo)
        if len(movie['categories']) >= 1:
            labelCategory1 = QtWidgets.QLabel(movie['categories'][0], boxInfo)
            labelCategory1_Size = labelCategory1.sizeHint()
            labelCategory1.setAlignment(QtCore.Qt.AlignCenter)
            labelCategory1.setGeometry(QtCore.QRect(15, 10, labelCategory1.width(), labelCategory1_Size.height()+25))
            labelCategory1.setStyleSheet("QLabel{text-align:center;color:#c6c6c6;font-size:11px;font-weight:bold;border:2px solid #c6c6c6;border-radius:19px;padding:8px}")
            movieWidgets.append(labelCategory1)
            self.currentWidgets.append(labelCategory1)
            if len(movie['categories']) >= 2:
                labelCategory2 = QtWidgets.QLabel(movie['categories'][1], boxInfo)
                labelCategory2_Size = labelCategory2.sizeHint()
                labelCategory2.setAlignment(QtCore.Qt.AlignCenter)
                labelCategory2.setGeometry(QtCore.QRect(labelCategory1.geometry().right() + 10, 10, labelCategory2.width(), labelCategory2_Size.height()+25))
                labelCategory2.setStyleSheet("QLabel{text-align:center;color:#c6c6c6;font-size:11px;font-weight:bold;border:2px solid #c6c6c6;border-radius:19px;padding:8px}")
                movieWidgets.append(labelCategory2)
                self.currentWidgets.append(labelCategory2)
                if len(movie['categories']) >= 3:
                    labelCategory3 = QtWidgets.QLabel(movie['categories'][2], boxInfo)
                    labelCategory3_Size = labelCategory3.sizeHint()
                    labelCategory3.setAlignment(QtCore.Qt.AlignCenter)
                    labelCategory3.setGeometry(QtCore.QRect(labelCategory2.geometry().right() + 10, 10, labelCategory3.width(), labelCategory3_Size.height()+25))
                    labelCategory3.setStyleSheet("QLabel{color:#c6c6c6;font-size:11px;font-weight:bold;border:2px solid #c6c6c6;border-radius:19px;padding:8px}")
                    movieWidgets.append(labelCategory3)
                    self.currentWidgets.append(labelCategory3)
        description = QtWidgets.QLabel(f"{movie['description']}.", boxInfo)
        description.setGeometry(QtCore.QRect(15, 50, 320, 100))
        description.setWordWrap(True)
        description.setStyleSheet("QLabel{text-align:left;color:#c6c6c6;font-size:13px;font-weight:bold;}")
        movieWidgets.append(description)
        self.currentWidgets.append(description)

        boxRate = QtWidgets.QGroupBox(self.centralwidget)
        boxRate.setStyleSheet(".QGroupBox {background-color:#323232;border:none;border-radius:10px;}")
        boxRate.setGeometry(QtCore.QRect(15, 310, 130, 70))
        movieWidgets.append(boxRate)
        self.currentWidgets.append(boxRate)

        boxSave = QtWidgets.QGroupBox(self.centralwidget)
        boxSave.setStyleSheet(".QGroupBox {background-color:#323232;border:none;border-radius:10px;}")
        boxSave.setGeometry(QtCore.QRect(160, 310, 130, 70))
        movieWidgets.append(boxSave)
        self.currentWidgets.append(boxSave)
        save = QtWidgets.QPushButton(boxSave, clicked = lambda: saveSwitch(movie))
        save.setGeometry(QtCore.QRect(round((boxSave.width()/2)-(48/2)), round((boxSave.height()/2)-(48/2)), 48, 48))
        icon = QtGui.QIcon()
        if movie['savedState'] == 'not saved':
            icon.addPixmap(QtGui.QPixmap("assets/addBookmark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif movie['savedState'] == 'saved':
            icon.addPixmap(QtGui.QPixmap("assets/addBookmark2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        save.setIconSize(QtCore.QSize(45, 45))
        save.setIcon(icon)
        save.setStyleSheet("QPushButton{border:none;background-color:none;}")
        save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        movieWidgets.append(save)
        self.currentWidgets.append(save)

        def saveSwitch(movie):
            if movie['savedState'] == 'not saved':
                mongo.updateField(movie['name'], 'savedState', 'saved')
                icon.addPixmap(QtGui.QPixmap("assets/addBookmark2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                save.setIconSize(QtCore.QSize(45, 45))
                save.setIcon(icon)
            elif movie['savedState'] == 'saved':
                mongo.updateField(movie['name'], 'savedState', 'not saved')
                icon.addPixmap(QtGui.QPixmap("assets/addBookmark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                save.setIconSize(QtCore.QSize(45, 45))
                save.setIcon(icon)


        for widget in movieWidgets:
            widget.show()
    
    def movieWindow(self, movie):
        self.clearCentralWidget()
        self.clearCentralWidget()
        self.clearCentralWidget()
        self.movieView(movie)

    def switchWindows(self):
        if self.activeWindow == 'topMovies':
            self.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/rank2.png')))
            self.pushButton_2.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/bookmark2.png')))
            self.pushButton_3.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/review2.png')))
        elif self.activeWindow == 'savedMovies':
            self.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/quality3.png')))
            self.pushButton_2.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/bookmark.png')))
            self.pushButton_3.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/review2.png')))
        elif self.activeWindow == 'filterMovies':
            self.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/quality3.png')))
            self.pushButton_2.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/bookmark2.png')))
            self.pushButton_3.setIcon(QtGui.QIcon(QtGui.QPixmap('assets/review.png')))
    
    def savedView(self):
        self.scroll = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll.setWidgetResizable(True)
        self.scroll.setGeometry(QtCore.QRect(0, 70, 375, 320))
        scrollContent = QtWidgets.QWidget(self.scroll)
        self.scrollLayout = QtWidgets.QVBoxLayout(scrollContent)
        scrollContent.setLayout(self.scrollLayout)
        self.scroll.setWidget(scrollContent)
        self.scrollLayout.setAlignment(QtCore.Qt.AlignTop)
        self.currentWidgets.append(self.scroll)
        self.scroll.setStyleSheet("""
        QWidget {
            background-color: transparent;
            border:none;
        }""")
        scrollContent.setStyleSheet("""
        QWidget {
            background-color: transparent;
        }""")

        self.scroll.verticalScrollBar().setStyleSheet("""
        QScrollBar:vertical {
            background-color: transparent;
            width: 7px;
            margin: 0px 0px 0px 0px;
        }
        QScrollBar::handle:vertical {
            background-color: #57595a;
            min-height: 20px;
            border-radius: 3px;
        }
        QScrollBar::add-line:vertical {
            background-color: transparent;
            height: 10px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            background-color: transparent;
            height: 10px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background-color: none;
            border-radius: 10px;
        }
        """)
        self.scroll.show()

        names = mongo.getByName(self.lineEdit.text())
        for movie in names:
            box = QtWidgets.QGroupBox()
            buttonName = QtWidgets.QPushButton(movie['name'], box)
            buttonName.clicked.connect(lambda _, m=movie: self.movieWindow(m))
            buttonName.setGeometry(QtCore.QRect(10, 5, 325, 24))
            buttonName.setStyleSheet("QPushButton{text-align:left;color:#fffffd;font-size:16px;font-weight:bold;}")
            buttonName.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            
            labelLength = QtWidgets.QLabel(f"{movie['length']}", box)
            labelLength.setGeometry(QtCore.QRect(10, 30, 335, 24))
            labelLength.setStyleSheet("QLabel{text-align:left;color:#c6c6c6;font-size:11px;font-weight:bold;}")
            
            labelRating = QtWidgets.QLabel(f"{movie['rating']}/10", box)
            labelRating.setGeometry(QtCore.QRect(60, 30, 335, 24))
            labelRating.setStyleSheet("QLabel{text-align:left;color:#c6c6c6;font-size:11px;font-weight:bold;}")


            labelStar1 = QtWidgets.QLabel(f"{movie['stars'][0]}   -", box)
            labelStar1.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            labelStar1_Size = labelStar1.sizeHint()
            labelStar1.setGeometry(QtCore.QRect(10, 55, labelStar1_Size.width()+5, labelStar1_Size.height()))
            labelStar1.setStyleSheet("QLabel {color: #c6c6c6; font-size: 10px; font-weight: bold;}")
            # ---
            labelStar2 = QtWidgets.QLabel(f"{movie['stars'][1]}   -", box)
            labelStar2.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            labelStar2_Size = labelStar2.sizeHint()
            labelStar2.setGeometry(QtCore.QRect(labelStar1.geometry().right() + 10, 55, labelStar2_Size.width()+5, labelStar2_Size.height()))
            labelStar2.setStyleSheet("QLabel {color: #c6c6c6; font-size: 10px; font-weight: bold;}")
            # ---
            labelStar3 = QtWidgets.QLabel(f"{movie['stars'][2]}", box)
            labelStar3.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            labelStar3_Size = labelStar3.sizeHint()
            labelStar3.setGeometry(QtCore.QRect(labelStar2.geometry().right() + 10, 55, labelStar3_Size.width()+5, labelStar3_Size.height()))
            labelStar3.setStyleSheet("QLabel {color: #c6c6c6; font-size: 10px; font-weight: bold;}")
            
            box.setMaximumHeight(80)
            box.setMaximumWidth(350)
            box.setMinimumHeight(80)
            box.setMinimumWidth(350)
            box.setStyleSheet(".QGroupBox {background-color:#323232;border:none;border-radius:10px;}")
            
            self.scrollLayout.insertWidget(300, box)
    
    def savedWindow(self):
        self.clearCentralWidget()
        self.clearCentralWidget()
        self.activeWindow = 'savedMovies'
        self.switchWindows()
        self.savedView()

    def filterView(self):
        ...
    
    def filterWindow(self):
        self.clearCentralWidget()
        self.activeWindow = 'filterMovies'
        self.switchWindows()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
