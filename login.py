# Student Manager User Login Module
# Author  : C14147@github.com
#
# Copyright (c) 2024-2025 by C14147 <ffffasddd@163.com>.
# Annotations Wrote By DouBao AI
# Licensed in Apache 2.0
import sys, os
import pydbclib
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from qfluentwidgets import *

# Check Windows Version(>=11) and Import Window Lib
isWin11 = sys.platform == "win32" and sys.getwindowsversion().build >= 22000
if isWin11:
    from qframelesswindow import AcrylicWindow as Window
else:
    from qframelesswindow import FramelessWindow as Window

import constants


# Create a QApplication instance
app = QApplication(sys.argv)

# Reurn Variables
UUID = ""
DATA_PATH = ""


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        # If the object name of LoginWindow is not set, set it to "LoginWindow"
        if not LoginWindow.objectName():
            LoginWindow.setObjectName("LoginWindow")
        # Resize the LoginWindow
        LoginWindow.resize(540, 400)
        # Set the minimum size of LoginWindow based on whether LOGIN_BGI is set
        if not constants.LOGIN_BGI:
            LoginWindow.setMinimumSize(QSize(300, 200))
        else:
            LoginWindow.setMinimumSize(QSize(450, 400))
        # Set the maximum size of LoginWindow
        LoginWindow.setMaximumSize(QSize(700, 800))
        # Create a vertical layout for LoginWindow
        self.verticalLayout_2 = QVBoxLayout(LoginWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Create a size policy
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        # If LOGIN_BGI is set, create an image label
        if constants.LOGIN_BGI:
            self.imgLabel = QLabel(LoginWindow)
            self.imgLabel.setObjectName("imgLabel")
            sizePolicy.setHeightForWidth(self.imgLabel.sizePolicy().hasHeightForWidth())
            self.imgLabel.setSizePolicy(sizePolicy)
            self.imgLabel.setMinimumSize(QSize(0, 40))
            self.imgLabel.setMaximumSize(QSize(16777215, 400))

            self.verticalLayout_2.addWidget(self.imgLabel)

        # Create another vertical layout
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        # Create a horizontal layout
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # Create a body label
        self.label_4 = BodyLabel(LoginWindow)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        # Create an editable combo box for database path
        self.DatabasePath = EditableComboBox(LoginWindow)
        self.DatabasePath.setObjectName("DatabasePath")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.DatabasePath.sizePolicy().hasHeightForWidth()
        )
        self.DatabasePath.setSizePolicy(sizePolicy1)
        self.DatabasePath.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_3.addWidget(self.DatabasePath)

        # Create a primary push button for selecting from path
        self.FromPath = PrimaryPushButton(LoginWindow)
        self.FromPath.setObjectName("FromPath")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.FromPath.sizePolicy().hasHeightForWidth())
        self.FromPath.setSizePolicy(sizePolicy2)
        self.FromPath.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_3.addWidget(self.FromPath)

        # If RCT_AVAILABLE is set, create a button for remote toolkit
        if constants.RCT_AVAILABLE:
            self.FromCemoteToolkit = PrimaryPushButton(LoginWindow)
            self.FromCemoteToolkit.setObjectName("FromCemoteToolkit")
            sizePolicy2.setHeightForWidth(
                self.FromCemoteToolkit.sizePolicy().hasHeightForWidth()
            )
            self.FromCemoteToolkit.setSizePolicy(sizePolicy2)
            self.FromCemoteToolkit.setMaximumSize(QSize(16777215, 35))

            self.horizontalLayout_3.addWidget(self.FromCemoteToolkit)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        # Create another horizontal layout
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        # Create a body label for accountant
        self.label_2 = BodyLabel(LoginWindow)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout.addWidget(self.label_2)

        # Create a line edit for accountant
        self.Accountant = LineEdit(LoginWindow)
        self.Accountant.setObjectName("Accountant")
        sizePolicy1.setHeightForWidth(self.Accountant.sizePolicy().hasHeightForWidth())
        self.Accountant.setSizePolicy(sizePolicy1)
        self.Accountant.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout.addWidget(self.Accountant)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # Create another horizontal layout
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # Create a body label for password
        self.label_3 = BodyLabel(LoginWindow)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        # Create a line edit for password
        self.Password = LineEdit(LoginWindow)
        self.Password.setObjectName("Password")
        sizePolicy1.setHeightForWidth(self.Password.sizePolicy().hasHeightForWidth())
        self.Password.setSizePolicy(sizePolicy1)
        self.Password.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_2.addWidget(self.Password)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # Create a primary push button for login
        self.Login = PrimaryPushButton(LoginWindow)
        self.Login.setObjectName("Login")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Login.sizePolicy().hasHeightForWidth())
        self.Login.setSizePolicy(sizePolicy3)
        self.Login.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.Login)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        # Set the text and connect slots by name
        self.retranslateUi(LoginWindow)
        QMetaObject.connectSlotsByName(LoginWindow)

    # setupUi

    def retranslateUi(self, LoginWindow):
        # Set the window title
        LoginWindow.setWindowTitle(
            QCoreApplication.translate("LoginWindow", "Form", None)
        )
        # Set the text of imgLabel if LOGIN_BGI is set
        if constants.LOGIN_BGI:
            self.imgLabel.setText(
                QCoreApplication.translate("LoginWindow", "TextLabel", None)
            )
        # Set the text of label_4
        self.label_4.setText(
            QCoreApplication.translate("LoginWindow", "Database: ", None)
        )
        # Set the tooltip and text of FromPath button
        self.FromPath.setToolTip(
            QCoreApplication.translate(
                "LoginWindow",
                "<html><head/><body><p>Select database from path</p></body></html>",
                None,
            )
        )
        self.FromPath.setText(
            QCoreApplication.translate("LoginWindow", "From Path", None)
        )
        # Set the tooltip and text of FromCemoteToolkit button if RCT_AVAILABLE is set
        if constants.RCT_AVAILABLE:
            self.FromCemoteToolkit.setToolTip(
                QCoreApplication.translate(
                    "LoginWindow",
                    "<html><head/><body><p>Select database on C4147\u2122 Remote Connection Toolkit</p></body></html>",
                    None,
                )
            )
            self.FromCemoteToolkit.setText(
                QCoreApplication.translate("LoginWindow", "From C14147\u2122 RCT", None)
            )
        # Set the text of label_2
        self.label_2.setText(
            QCoreApplication.translate("LoginWindow", "Accountant: ", None)
        )
        # Set the text of label_3
        self.label_3.setText(
            QCoreApplication.translate("LoginWindow", "Password: ", None)
        )
        # Set the text of Login button
        self.Login.setText(QCoreApplication.translate("LoginWindow", "Login", None))
        # retranslateUi
        


class LoginWindow(Window, Ui_LoginWindow):

    def __init__(self):
        # Call the superclass constructor
        super().__init__()
        # Set up the UI
        self.setupUi(self)
        # Create a file dialog and an error dialog
        self.fileDialog = QFileDialog()
        self.errorDialog = QErrorMessage()
        # Set the window title of the error dialog
        self.errorDialog.setWindowTitle(
            QCoreApplication.translate("LoginWindow", "Error", None)
        )
        # Set the theme color
        setThemeColor("#28afe9")

        # Set the title bar
        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()

        # Set the window title
        self.setWindowTitle(
            QCoreApplication.translate("LoginWindow", "Student Manager", None)
        )
        # Set the window effect
        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=isDarkTheme())
        # Set the background color if not Win11
        if not isWin11:
            color = QColor(25, 33, 42) if isDarkTheme() else QColor(240, 244, 249)
            self.setStyleSheet(f"LoginWindow{{background: {color.name()}}}")

        # Get the desktop geometry and move the window to the center
        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        # Connect the button click signals to the corresponding slots
        self.FromPath.clicked.connect(self.askDataFile_Local)
        self.Login.clicked.connect(self.checkPassword)

    def resizeEvent(self, e):
        # Call the superclass resize event
        super().resizeEvent(e)
        # If LOGIN_BGI is set, set the pixmap of imgLabel
        if constants.LOGIN_BGI:
            pixmap = QPixmap(":/images/background.jpg").scaled(
                self.imgLabel.size(),
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation,
            )
            self.imgLabel.setPixmap(pixmap)

    def systemTitleBarRect(self, size):
        """Returns the system title bar rect, only works for macOS"""
        return QRect(size.width() - 75, 0, 75, size.height())

    def askDataFile_Local(self):
        # Declare asked_path as global
        global asked_path
        # Set the file mode of the file dialog
        self.fileDialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        # Get the selected file path
        asked_path, _ = self.fileDialog.getOpenFileName(
            self,
            QCoreApplication.translate("LoginWindow", "Open Database File", None),
            os.getcwd(),
            constants.SQLite,
        )
        # If the selected path is a string, add it to the combo box and set it as the current text
        if type(asked_path) == str:
            self.DatabasePath.addItem(asked_path)
            self.DatabasePath.setCurrentText(asked_path)
            self.DatabasePath.update()

    def checkPassword(self):
        # Get the current database path
        db_path = self.DatabasePath.currentText()
        # Get the SQL type of the database
        sql_type = constants.sql_looker(db_path)
        # If the SQL type is None, show an error message
        if sql_type is None:
            MessageBox(
                QCoreApplication.translate(
                    "LoginWindow", "Invalid database file.", None
                ),
                QCoreApplication.translate(
                    "LoginWindow",
                    "This file may be damaged or occupied by another program.",
                    None,
                ),
                self,
            ).exec()
            return False
        # Show a state tooltip
        stateTooltip = StateToolTip(
            QCoreApplication.translate("LoginWindow", "Logging in...", None),
            QCoreApplication.translate("LoginWindow", "Connecting database...", None),
            self,
        )
        stateTooltip.show()
        try:
            # Connect to the database
            with pydbclib.connect(db_path, driver=sql_type) as db:
                # Update the state tooltip
                stateTooltip.setContent(
                    QCoreApplication.translate(
                        "LoginWindow", "Verifying identity...", None
                    )
                )
                # Execute the SQL query to get the password
                cursor = db.execute(
                    f"SELECT Users.Password FROM Users WHERE Users.UserName = '{self.Accountant.text()}'",
                )
                # Fetch the result
                result = cursor.fetchone()
                # Set the state of the state tooltip
                stateTooltip.setState(True)
                # If the result is not None, check the password
                if result is not None:
                    passwd = result[0]
                    if passwd == self.Password.text():
                        # Execute the SQL query to get the UUID
                        cursor = db.execute(
                            f"SELECT Users.ID FROM Users WHERE Users.UserName = '{self.Accountant.text()}'",
                        )
                        # Fetch the result
                        global UUID,DATA_PATH
                        UUID = str(cursor.fetchone())
                        DATA_PATH = self.DatabasePath.currentText()
                        # Close The Window
                        self.close()
                        self.destroy()
                        app.exit(0)
                        return True
                # If the password is incorrect, show an error message
                MessageBox(
                    QCoreApplication.translate("LoginWindow", "Password Error", None),
                    QCoreApplication.translate(
                        "LoginWindow",
                        "Please check if the account name and password you entered are correct.",
                        None,
                    ),
                    self,
                ).exec()
                return False
        except Exception as e:
            # Set the state of the state tooltip
            stateTooltip.setState(True)
            # Show an error message
            MessageBox(
                QCoreApplication.translate("LoginWindow", "Database Error", None),
                QCoreApplication.translate(
                    "LoginWindow",
                    "This is an unrecorded exception. The following is the detailed information of the error:",
                    None,
                )
                + "\n"
                + str(e),
                self,
            ).exec()
            return False


def runLogin() -> dict:
    # Create a translator for internationalization
    translator = FluentTranslator(QLocale())
    # Install the translator
    app.installTranslator(translator)

    # Create a LoginWindow instance and show it
    w = LoginWindow()
    w.show()
    # Start the application event loop
    app.exec()
    # Return a Tuple(UUID: str, DATA_PATH: str)
    return (UUID[2:].split(',')[0][:-1],DATA_PATH)


if __name__ == "__main__":
    print(runLogin())
