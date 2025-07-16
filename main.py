from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QFormLayout, QPushButton
from PySide6.QtCore import Qt
import os, json

DATA_FILE = 'users.json'

def main():
    def add_form():
        def handle_submit():
            login = login_input.text()
            pwd = pwd_input.text()
            user = {'id': gen_id(), 'login': login, 'password': pwd}
            
            users.append(user)
            show_users()
            save_users()

        def handle_delete():
            item = get_selected()
            id = item.data(ID)
            user = next((u for u in users if u['id'] == id), None)

            if user in users:
                users.remove(user)
                show_users()
                save_users()

        form = QFormLayout()
        login_input = QLineEdit()
        pwd_input = QLineEdit()
        btn_layout = QHBoxLayout()
        add_btn = QPushButton('Add')
        del_btn = QPushButton('Delete')
        
        form.addRow('Login: ', login_input)
        form.addRow('Password: ', pwd_input)
        form.addRow(btn_layout)

        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(del_btn)

        add_btn.clicked.connect(handle_submit)
        del_btn.clicked.connect(handle_delete)

        layout.addLayout(form)
    
    def add_list():
        def show_users():
            user_list.clear()
            for user in users:
                item = QListWidgetItem(user['login'])
                item.setData(ID, user['id']) 
                item.setToolTip('password: ' + user['password'])                                          
                user_list.addItem(item)
        
        def get_selected():
            item = user_list.currentItem()
            return item
                        
        user_list = QListWidget()
                        
        user_list.itemDoubleClicked.connect(show_user_details)

        layout.addWidget(user_list) 
        show_users()
                
        return show_users, get_selected
        
    def add_window():
        def update_user():
            current['user']['login'] = login_input.text()
            current['user']['password'] = pwd_input.text()
            child_window.close()
            show_users()
            save_users()
                        
        def show_user_details(item):
            child_window.show()
            id = item.data(ID)
            user = next((u for u in users if u['id'] == id), None)
            login_input.setText(user['login'])
            pwd_input.setText(user['password'])
            current['user'] = user
            
        child_window = QWidget()
        form = QFormLayout()
        login_input = QLineEdit()
        pwd_input = QLineEdit()
        btn_layout = QHBoxLayout()
        save_btn = QPushButton('Save')
        close_btn = QPushButton('Close')
        current = {'user': None}
        
        form.addRow('Login', login_input)
        form.addRow('Password', pwd_input)
        form.addRow(btn_layout)
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(close_btn)
                       
        child_window.setLayout(form)        
        child_window.setWindowTitle('User info')
        child_window.resize(350, 100)

        save_btn.clicked.connect(update_user)
        close_btn.clicked.connect(lambda: child_window.close())

        return show_user_details
        
    def gen_id():
        id = next_gen['id']
        next_gen['id'] += 1
        return id
    
    def load_users():
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding = 'utf-8') as file:
                return json.load(file)
        return []

    def save_users():
        with open(DATA_FILE, 'w', encoding = 'utf-8') as file:
            json.dump(users, file, ensure_ascii = False, indent = 4)

    next_gen = {'id': 1}     
    
    ID = Qt.UserRole

    users = load_users()
     
    app =  QApplication()
    window = QWidget()
    layout = QVBoxLayout()

    window.setLayout(layout)    
    window.setWindowTitle('Users CRUD')
    window.resize(900, 750)
    
    add_form()

    show_user_details = add_window()
    show_users, get_selected = add_list()
        

    window.show()
    # show_user_details()      

    app.exec()

main()