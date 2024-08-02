from src.model import db

class User:
  def __init__(self, name, chat_id):
    self.name = name
    self.chat_id = chat_id

  def add(self):
    ### Проверка на существование юзера
    db.cursor.execute(f'SELECT * FROM users WHERE chat_id={self.chat_id}')
    u = db.cursor.fetchone()
    if u is None:
      db.cursor.execute(f'INSERT INTO users (name, chat_id) VALUES ("{self.name}", {self.chat_id})')
      # Commit the changes to the database
      db.conn.commit()
    else:
      print(f'User with chat_id {self.chat_id} already exists')


  def get(self, chat_id):
    # Create a cursor object to perform database operations
    cursor = db.conn.cursor()
    cursor.execute(f'SELECT * FROM users WHERE chat_id={chat_id}')
    u = cursor.fetchone()
    if u is not None:
        user = User(u[1], u[2])
    else:
        user = None
    # Close the cursor and the connection to the database
    cursor.close()
    return user


def get_all():
    db.cursor.execute(f'SELECT * FROM users')
    users = []
    for row in db.cursor.fetchall():
        user = User(row[1], row[2])
        users.append(user)
    # Close the cursor and the connection to the database
    db.cursor.close()
    return users