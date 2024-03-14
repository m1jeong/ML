from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog
from PyQt5.uic import loadUi

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI 파일 로드
        loadUi('version1.ui', self)
        self.setGeometry(100, 100, 400, 200)

        # 버튼 클릭 시 이벤트 연결
        self.openButton.clicked.connect(self.openPath)

    def openPath(self):
        # 파일 대화상자 열기
        path = QFileDialog.getExistingDirectory(self, '경로 선택')

        # 선택된 경로를 레이블에 표시
        self.pathLabel.setText('선택된 경로: ' + path)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()