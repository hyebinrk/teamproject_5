import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtWidgets,uic

# # Oracle 모듈
# import cx_Oracle as oci

## DB연결 설정
sid = 'XE'
host = 'localhost'
port = 1521
username = 'attendance'
password = '12345'
basic_msg = '출결관리앱'

# 교사/학생 로그인 선택    
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
    
    def initUI(self):
        uic.loadUi('./sel_login.ui', self)
        self.setWindowTitle('출결체크')
        self.setWindowIcon(QIcon('./image/kitty.png'))

        # 버튼 아이콘 추가
        self.btnTeacherSelect.setIcon(QIcon('./image/teacher.png'))
        self.btnStudentSelect.setIcon(QIcon('./image/student.png'))
        
        # 버튼 이벤트 추가
        self.btnTeacherSelect.clicked.connect(self.btnTeacherClick)
        self.btnStudentSelect.clicked.connect(self.btnStudentClick)
        

    def btnTeacherClick(self):
        self.teacherlogin_window = TLoginWindow()
        self.teacherlogin_window.show()
        self.close()

    def btnStudentClick(self):
        self.studentlogin_window = SLoginWindow()
        self.studentlogin_window.show()
        self.close()

    
    def TLoginWindow(self):
        from t_login import MainWindow as TLoginWindow
        self.my_page = TLoginWindow()  
        self.my_page.show() 

    def SLoginWindow(self):
        from TAtd_chk import TAtdMainWindow as CheckWindow  # check.py에서 MainWindow 가져오기
        self.check_window = CheckWindow(t_id)  # T_ID 전달
        self.check_window.show()  # 출결 체크 창 열기
        self.close()  # 현재 창 닫기

# class TeacherloginWindow(QMainWindow):
#     def __init__(self):
#         super(TeacherloginWindow, self).__init__()
#         self.initUI()
#         # self.loadData()
    
#     def initUI(self):
#         uic.loadUi('./t_login.ui', self)
#         self.setWindowTitle('교사 로그인')

# class StudentloginWindow(QMainWindow):
#     def __init__(self):
#         super(StudentloginWindow, self).__init__()
#         self.initUI()
#         # self.loadData()
    
#     def initUI(self):
#         uic.loadUi('./학생 로그인 화면.ui', self)
#         self.setWindowTitle('학생 로그인')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()