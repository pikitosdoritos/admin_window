from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QVBoxLayout, QLabel, QListWidget, QFormLayout, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor


def main():     
    def add_form():
        def handle_submit():
            login = login_input.text()
            pwd = pwd_input.text()
            user = {'id': gen_id(), 'login': login, 'password': pwd}
            
            users.append(user)
            show_users()

        form = QFormLayout()
        login_input = QLineEdit()
        pwd_input = QLineEdit()
        btn = QPushButton('Add')

        form.addRow('Login: ', login_input)
        form.addRow('Password: ', pwd_input)
        form.addRow(btn)
        btn.clicked.connect(handle_submit)

        layout.addLayout(form)
    
    def add_list():
        def show_users():
            logins = [user['login'] for user in users]
            list.clear()
            list.addItems(logins)

        list = QListWidget()
        
        show_users()
        layout.addWidget(list) 

        return show_users


    def gen_id():
        id = next['id']
        next['id'] += 1
        return id

    next = {'id': 1}     
    
    users = [
        {'id': gen_id(), 'login': 'Bob', 'password': '84308459'}, 
        {'id': gen_id(), 'login': 'Alex', 'password': '1234567'}, 
        {'id': gen_id(), 'login': 'Steve', 'password': '0987654321'}
    ]
     
    app =  QApplication()
    window = QMainWindow()
    wrapper = QWidget()
    layout = QVBoxLayout()

    layout.setAlignment(Qt.AlignCenter)
    wrapper.setLayout(layout)

    window.setCentralWidget(wrapper)
    window.setWindowTitle('Users CRUD')
    window.resize(900, 750)

    add_form()
    show_users = add_list()
        
    window.show()

    app.exec()

main()