from PyQt5 import QtCore, QtGui, QtWidgets
import mongo

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.currentWidgets = []
        self.activeWindow = 'topMovies'
        self.searchText = ''
        
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
        if self.currentWidgets != []:
            for widget in self.currentWidgets:
                try: 
                    widget.setParent(None)
                    widget.hide()
                    widget.deleteLater()
                    self.currentWidgets.remove(widget)
                except RuntimeError:
                    pass

    def listView(self):
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setText(self.searchText)
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
        self.searchMovies()

    def searchMovies(self, *args):
        for i in reversed(range(self.scrollLayout.count())): 
            self.scrollLayout.itemAt(i).widget().deleteLater()
        if args:
            names = mongo.getSaved()
            self.searchText = self.lineEdit.text()
            names = mongo.filterSavedByName(self.searchText)
        else:
            self.searchText = self.lineEdit.text()
            names = mongo.getByName(self.searchText)
        for movie in names:
            box = QtWidgets.QGroupBox()
            buttonName = QtWidgets.QPushButton(movie['name'], box)
            buttonName.clicked.connect(lambda _, m=movie: self.movieWindow(m, 'top'))
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
        self.activeWindow = 'topMovies'
        self.switchWindows()
        self.listView()

    def movieView(self, movie, window):
        movieWidgets = []
        
        if window == 'top':  
            backButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.listWindow())
        elif window == 'saved':
            backButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.savedWindow())
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
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setText(self.searchText)
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
        movieWidgets.append(self.lineEdit)
        movieWidgets.append(self.pushButton_4)
        self.currentWidgets.append(self.lineEdit)
        self.currentWidgets.append(self.pushButton_4)

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
        fullStarIcon = QtGui.QIcon()
        halfStarIcon = QtGui.QIcon()
        emptyStarIcon = QtGui.QIcon()
        fullStarIcon.addPixmap(QtGui.QPixmap("assets/star.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        halfStarIcon.addPixmap(QtGui.QPixmap("assets/half-star.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        emptyStarIcon.addPixmap(QtGui.QPixmap("assets/empty-star.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        star1 = QtWidgets.QPushButton(boxRate)
        star2 = QtWidgets.QPushButton(boxRate)
        star3 = QtWidgets.QPushButton(boxRate)
        star4 = QtWidgets.QPushButton(boxRate)
        star5 = QtWidgets.QPushButton(boxRate)
       
        rateBox = QtWidgets.QDoubleSpinBox(boxRate)
        rateBox.setStyleSheet(
            """
            QDoubleSpinBox {
                background-color: #232323;
                border: 2px solid #2a2a2a;
                border-radius: 5px;
                color: #ffffff;
                padding: 5px;
                font-size: 16px;
            }
            QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {
                background-color: #2a2a2a;
                color: #ffffff;
                padding: 5px;
                width: 20px;
                height: 8px;
            }
            QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover {
                background-color: #444444;
            }
            QDoubleSpinBox::up-arrow, QDoubleSpinBox::down-arrow {
                width: 10px;
                height: 10px;
            }
            QDoubleSpinBox::up-arrow {
                image: url('assets/caret-arrow-up.png');
            }
            QDoubleSpinBox::down-arrow {
                image: url('assets/down-filled-triangular-arrow.png');
            }
            """
        )
        rateBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        rateBox.setSingleStep(1)
        rateBox.setDecimals(0)
        rateBox.setMaximum(10)
        rateBox.setValue(float(movie['userRating']))
        rateBox.setGeometry(QtCore.QRect(15, 30, 70, 40))
        self.currentWidgets.append(rateBox)

        star1.setStyleSheet("QPushButton{border:none;background-color:none;}")
        star2.setStyleSheet("QPushButton{border:none;background-color:none;}")
        star3.setStyleSheet("QPushButton{border:none;background-color:none;}")
        star4.setStyleSheet("QPushButton{border:none;background-color:none;}")
        star5.setStyleSheet("QPushButton{border:none;background-color:none;}")
        star1.setGeometry(QtCore.QRect(25, 10, 16, 16))
        star2.setGeometry(QtCore.QRect(40, 10, 16, 16))
        star3.setGeometry(QtCore.QRect(55, 10, 16, 16))
        star4.setGeometry(QtCore.QRect(70, 10, 16, 16))
        star5.setGeometry(QtCore.QRect(85, 10, 16, 16))
        check = QtWidgets.QPushButton(boxRate, clicked = lambda: rate(rateBox.value()))
        check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        check.setGeometry(QtCore.QRect(90, 32, 32, 32))
        check.setStyleSheet("QPushButton{border:none;background-color:none;}")
        checkIcon = QtGui.QIcon()
        checkIcon.addPixmap(QtGui.QPixmap("assets/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        check.setIcon(checkIcon)
        stars = [star1, star2, star3, star4, star5]

        def updateStars():
            if movie['userRating'] == '0.0':
                for i in range(5):
                    stars[i].setIcon(emptyStarIcon)
            if movie['userRating'] == '1.0':
                star1.setIcon(halfStarIcon)
                for i in range(1, 5):
                    stars[i].setIcon(emptyStarIcon)
            if movie['userRating'] == '2.0':
                star1.setIcon(fullStarIcon)
                for i in range(1, 5):
                    stars[i].setIcon(emptyStarIcon)
            if movie['userRating'] == '3.0':
                star1.setIcon(fullStarIcon)
                star2.setIcon(halfStarIcon)
                for i in range(2, 5):
                    stars[i].setIcon(emptyStarIcon)
            if movie['userRating'] == '4.0':
                star1.setIcon(fullStarIcon)
                star2.setIcon(fullStarIcon)
                for i in range(2, 5):
                    stars[i].setIcon(emptyStarIcon)
            if movie['userRating'] == '5.0':
                star1.setIcon(fullStarIcon)
                star2.setIcon(fullStarIcon)
                star3.setIcon(halfStarIcon)
                for i in range(3, 5):
                    stars[i].setIcon(emptyStarIcon)
            if movie['userRating'] == '6.0':
                star1.setIcon(fullStarIcon)
                star2.setIcon(fullStarIcon)
                star3.setIcon(fullStarIcon)
                for i in range(3, 5):
                    stars[i].setIcon(emptyStarIcon)
            if movie['userRating'] == '7.0':
                star1.setIcon(fullStarIcon)
                star2.setIcon(fullStarIcon)
                star3.setIcon(fullStarIcon)
                star4.setIcon(halfStarIcon)
                star5.setIcon(emptyStarIcon)
            if movie['userRating'] == '8.0':
                star1.setIcon(fullStarIcon)
                star2.setIcon(fullStarIcon)
                star3.setIcon(fullStarIcon)
                star4.setIcon(fullStarIcon)
                star5.setIcon(emptyStarIcon)
            if movie['userRating'] == '9.0':
                star1.setIcon(fullStarIcon)
                star2.setIcon(fullStarIcon)
                star3.setIcon(fullStarIcon)
                star4.setIcon(fullStarIcon)
                star4.setIcon(halfStarIcon)
            if movie['userRating'] == '10.0':
                star1.setIcon(fullStarIcon)
                star2.setIcon(fullStarIcon)
                star3.setIcon(fullStarIcon)
                star4.setIcon(fullStarIcon)
                star5.setIcon(fullStarIcon)

        updateStars()
 
        
        def rate(userRating):
            mongo.updateField(movie['name'], 'userRating', userRating)
            updateStars()

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
    
    def movieWindow(self, movie, window):
        self.clearCentralWidget()
        self.clearCentralWidget()
        self.clearCentralWidget()
        self.movieView(movie, window)

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
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setText(self.searchText)
        self.lineEdit.setGeometry(QtCore.QRect(40, 25, 295, 31))
        self.lineEdit.setStyleSheet("#lineEdit {border:none;border-radius:6px;font-size:16px;padding-left:10px;}")
        self.lineEdit.setObjectName("lineEdit")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.searchMovies('saved'))
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

        names = mongo.getSaved()
        for movie in names:
            box = QtWidgets.QGroupBox()
            saved_buttonName = QtWidgets.QPushButton(movie['name'], box)
            saved_buttonName.clicked.connect(lambda _, m=movie: self.movieWindow(m, 'saved'))
            saved_buttonName.setGeometry(QtCore.QRect(10, 5, 325, 24))
            saved_buttonName.setStyleSheet("QPushButton{text-align:left;color:#fffffd;font-size:16px;font-weight:bold;}")
            saved_buttonName.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            
            saved_labelLength = QtWidgets.QLabel(f"{movie['length']}", box)
            saved_labelLength.setGeometry(QtCore.QRect(10, 30, 335, 24))
            saved_labelLength.setStyleSheet("QLabel{text-align:left;color:#c6c6c6;font-size:11px;font-weight:bold;}")
            
            saved_labelRating = QtWidgets.QLabel(f"{movie['rating']}/10", box)
            saved_labelRating.setGeometry(QtCore.QRect(60, 30, 335, 24))
            saved_labelRating.setStyleSheet("QLabel{text-align:left;color:#c6c6c6;font-size:11px;font-weight:bold;}")


            saved_labelStar1 = QtWidgets.QLabel(f"{movie['stars'][0]}   -", box)
            saved_labelStar1.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            saved_labelStar1_Size = saved_labelStar1.sizeHint()
            saved_labelStar1.setGeometry(QtCore.QRect(10, 55, saved_labelStar1_Size.width()+5, saved_labelStar1_Size.height()))
            saved_labelStar1.setStyleSheet("QLabel {color: #c6c6c6; font-size: 10px; font-weight: bold;}")
            # ---
            saved_labelStar2 = QtWidgets.QLabel(f"{movie['stars'][1]}   -", box)
            saved_labelStar2.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            saved_labelStar2_Size = saved_labelStar2.sizeHint()
            saved_labelStar2.setGeometry(QtCore.QRect(saved_labelStar1.geometry().right() + 10, 55, saved_labelStar2_Size.width()+5, saved_labelStar2_Size.height()))
            saved_labelStar2.setStyleSheet("QLabel {color: #c6c6c6; font-size: 10px; font-weight: bold;}")
            # ---
            saved_labelStar3 = QtWidgets.QLabel(f"{movie['stars'][2]}", box)
            saved_labelStar3.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            saved_labelStar3_Size = saved_labelStar3.sizeHint()
            saved_labelStar3.setGeometry(QtCore.QRect(saved_labelStar2.geometry().right() + 10, 55, saved_labelStar3_Size.width()+5, saved_labelStar3_Size.height()))
            saved_labelStar3.setStyleSheet("QLabel {color: #c6c6c6; font-size: 10px; font-weight: bold;}")
            
            box.setMaximumHeight(80)
            box.setMaximumWidth(350)
            box.setMinimumHeight(80)
            box.setMinimumWidth(350)
            box.setStyleSheet(".QGroupBox {background-color:#323232;border:none;border-radius:10px;}")
            
            self.scrollLayout.insertWidget(300, box)
    
    def savedWindow(self):
        self.clearCentralWidget()
        self.clearCentralWidget()
        self.clearCentralWidget()
        self.clearCentralWidget()
        self.activeWindow = 'savedMovies'
        self.switchWindows()
        self.savedView()

    def filterView(self):
        mixSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        mixSpinBox.setStyleSheet(
            """
            QDoubleSpinBox {
                background-color: #232323;
                border: 2px solid #2a2a2a;
                border-radius: 5px;
                color: #ffffff;
                padding: 5px;
                font-size: 16px;
            }
            QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {
                background-color: #2a2a2a;
                color: #ffffff;
                padding: 5px;
                width: 20px;
                height: 8px;
            }
            QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover {
                background-color: #444444;
            }
            QDoubleSpinBox::up-arrow, QDoubleSpinBox::down-arrow {
                width: 10px;
                height: 10px;
            }
            QDoubleSpinBox::up-arrow {
                image: url('assets/caret-arrow-up.png');
            }
            QDoubleSpinBox::down-arrow {
                image: url('assets/down-filled-triangular-arrow.png');
            }
            """
        )
        mixSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        mixSpinBox.setSingleStep(0.1)
        mixSpinBox.setDecimals(1)
        mixSpinBox.setMaximum(10)
        mixSpinBox.setValue(7.5)
        mixSpinBox.setGeometry(QtCore.QRect(30, 30, 70, 40))
        self.currentWidgets.append(mixSpinBox)
        mixSpinBox.show()

        maxSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        maxSpinBox.setStyleSheet("""
            QDoubleSpinBox {
                background-color: #232323;
                border: 2px solid #2a2a2a;
                border-radius: 5px;
                color: #ffffff;
                padding: 5px;
                font-size: 16px;
            }
            QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {
                background-color: #2a2a2a;
                color: #ffffff;
                padding: 5px;
                width: 20px;
                height: 8px;
            }
            QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover {
                background-color: #444444;
            }
            QDoubleSpinBox::up-arrow, QDoubleSpinBox::down-arrow {
                width: 10px;
                height: 10px;
            }
            QDoubleSpinBox::up-arrow {
                image: url('assets/caret-arrow-up.png');
            }
            QDoubleSpinBox::down-arrow {
                image: url('assets/down-filled-triangular-arrow.png');
            }
            """)
        maxSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        maxSpinBox.setSingleStep(0.1)
        maxSpinBox.setDecimals(1)
        maxSpinBox.setMaximum(10)
        maxSpinBox.setValue(7.5)
        maxSpinBox.setGeometry(QtCore.QRect(115, 30, 70, 40))
        self.currentWidgets.append(maxSpinBox)
        maxSpinBox.show()

        combo_box = QtWidgets.QComboBox(self.centralwidget)
        combo_box.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        combo_box.addItem(' ')
        combo_box.addItems(mongo.getAllCategories())
        combo_box.setStyleSheet(
            """
            QComboBox {
                background-color: #232323;
                border: 2px solid #2a2a2a;
                border-radius: 5px;
                color: #ffffff;
                padding: 5px;
                font-size: 13px;
            }
            QComboBox::drop-down {
                width: 25px;
                height: 25px;
                subcontrol-origin: padding;
                subcontrol-position: center right;
                border: none;
                background-color: #2a2a2a;
            }
            QComboBox::down-arrow {
                image: url('assets/down-filled-triangular-arrow.png');
                width: 10px;
                height: 40px;
            }
            QComboBox QAbstractItemView {
                background-color: #232323;
                border: 2px solid #2a2a2a;
                border-radius: 5px;
                color: #ffffff;
                padding: 5px;
                font-size: 13px;
            }
            QComboBox QAbstractItemView::item {
                height: 25px;
                padding: 5px;
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: #444444;
            }
            QScrollBar:vertical {
                border: none;
                background-color: #2a2a2a;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background-color: #444444;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical {
                height: 0px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line:vertical {
                height: 0px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
            """
        )
        combo_box.setGeometry(QtCore.QRect(200, 35, 100, 25))
        self.currentWidgets.append(combo_box)
        combo_box.show()

        filterButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: filterByRatingOrCategory())
        filterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        filterButton.setGeometry(QtCore.QRect(320, 33, 32, 32))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/search3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        filterButton.setIconSize(QtCore.QSize(32, 32))
        filterButton.setIcon(icon)
        filterButton.setStyleSheet("QPushButton{border:none;background-color:none;}")
        self.currentWidgets.append(filterButton)
        filterButton.show()

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
        self.currentWidgets.append(self.scroll)
        self.scroll.show()
        
        def filterByRatingOrCategory():
            for i in reversed(range(self.scrollLayout.count())):
                self.scrollLayout.itemAt(i).widget().deleteLater()
            names = mongo.getByRatingAndCategory(mixSpinBox.value(), maxSpinBox.value(), combo_box.currentText())
            for movie in names:
                box = QtWidgets.QGroupBox()
                buttonName = QtWidgets.QPushButton(movie['name'], box)
                buttonName.clicked.connect(lambda _, m=movie: self.movieWindow(m, 'top'))
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
    
    def filterWindow(self):
        self.clearCentralWidget()
        self.clearCentralWidget()
        self.activeWindow = 'filterMovies'
        self.switchWindows()
        self.filterView()

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
