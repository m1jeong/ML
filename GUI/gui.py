# 필요한 PyQt 모듈 가져오기
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 창의 크기 및 제목 설정
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('경로 열기 예제')

        # 버튼 생성 및 위치 설정
        self.openButton = QPushButton('경로 열기', self)
        self.openButton.setGeometry(50, 50, 100, 30)
        self.openButton.clicked.connect(self.openPath)

        # 레이블 생성 및 위치 설정
        self.pathLabel = QLabel('선택된 경로: ', self)
        self.pathLabel.setGeometry(50, 100, 300, 30)

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
