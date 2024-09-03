import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QStackedWidget)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
class StartPage(QWidget):  def __init__(self, stacked_widget):
 super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # ur welcome
        welcome = QLabel("We have come to save you. (sort of.)", self)
        welcome.setAlignment(Qt.AlignCenter)
        layout.addWidget(welcome)

        welcome.setStyleSheet("""
                    QLabel {
                    font-family: 'Arial';  /* Set the font family */
                    font-size: 24px;       /* Set the font size */
                    font-weight: bold;     /* Set the font weight */
                    font-size: 16px;
                    padding: 12px;
                    min-width: 250px;
                    min-height: 60px;
                    color: black;
                    border-radius: 10px;
                    }
                """)

        # Load and display image
        logo_label = QLabel(self)
        pixmap = QPixmap('resources/logo.png')  # Ensure 'logo.png' is in the same directory
        logo_label.setPixmap(pixmap.scaled(400, 200, Qt.KeepAspectRatio))  # Resize image to fit label
        logo_label.setAlignment(Qt.AlignCenter)  # Center align the image
        layout.addWidget(logo_label)

        # Button to navigate to the settings page
        here_button = QPushButton('SAVE MWEH', self)
        here_button.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                padding: 12px;
                min-width: 250px;
                min-height: 60px;
                background-color: #cb9f7d;
                color: white;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #bfaa9a;
            }
        """)
        here_button.clicked.connect(self.goToSettingsPage)
        layout.addWidget(here_button)

        self.setLayout(layout)
        self.setWindowTitle('Start Page')
        self.setGeometry(100, 100, 600, 400)


    def goToSettingsPage(self):
        self.stacked_widget.setCurrentIndex(1)  # Switch to the SettingsPage


class SettingsPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Buttons for each test page
        mic_button = QPushButton('Mic Test', self)
        mic_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        layout.addWidget(mic_button)

        camera_button = QPushButton('Camera Test', self)
        camera_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        layout.addWidget(camera_button)

        speaker_button = QPushButton('Speaker Test', self)
        speaker_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))
        layout.addWidget(speaker_button)

        internet_button = QPushButton('Internet Test', self)
        internet_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))
        layout.addWidget(internet_button)

        self.setLayout(layout)
        self.setWindowTitle('Testing...')
        self.setGeometry(100, 100, 400, 600)


class TestPage(QWidget):
    def __init__(self, title):
        super().__init__()
        self.initUI(title)

    def initUI(self, title):
        layout = QVBoxLayout()

        instructions = QLabel(f"Welcome to {title}, but i legit havent added anything to this page yet rip", self)
        instructions.setAlignment(Qt.AlignCenter)
        layout.addWidget(instructions)

        self.setLayout(layout)
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 400, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('resources/logo.png'))  # Ensure 'app_icon.png' is in the same directory

    stacked_widget = QStackedWidget()

    start_page = StartPage(stacked_widget)
    settings_page = SettingsPage(stacked_widget)
    mic_page = TestPage('Microphone Test Page')
    camera_page = TestPage('Camera Test Page')
    speaker_page = TestPage('Speaker Test Page')
    internet_page = TestPage('Internet Test Page')

    stacked_widget.addWidget(start_page)
    stacked_widget.addWidget(settings_page)
    stacked_widget.addWidget(mic_page)
    stacked_widget.addWidget(camera_page)
    stacked_widget.addWidget(speaker_page)
    stacked_widget.addWidget(internet_page)

    stacked_widget.setWindowTitle('Dove Adobe Connect Troubleshooter')
    stacked_widget.setGeometry(200, 100, 600, 400)
    stacked_widget.show()

    sys.exit(app.exec_())
