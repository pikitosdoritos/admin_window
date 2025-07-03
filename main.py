from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QFormLayout, QPushButton
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
            list.clear()
            for user in users:
                item = QListWidgetItem(user['login'])
                item.setData(ID, user['id'])                                           
                list.addItem(item)

        def show_user_details(item):
            print(item.data(ID))
            
                        
        ID = Qt.UserRole
        list = QListWidget()        
        
        list.itemDoubleClicked.connect(show_user_details)

        layout.addWidget(list) 
        show_users()
        
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
    window = QWidget()
    layout = QVBoxLayout()

    window.setLayout(layout)    
    window.setWindowTitle('Users CRUD')
    window.resize(900, 750)

    add_form()
    show_users = add_list()
        
    window.show()

    app.exec()

main()