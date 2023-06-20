from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


# Представление для получения всех пользователей
@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    users = []
    for row in rows:
        user = {
            'id': row[0],
            'name': row[1],
            'email': row[2]
        }
        users.append(user)

    conn.close()

    return jsonify(users)


# Представление для получения пользователя по идентификатору
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    row = cursor.fetchone()

    if row is None:
        conn.close()
        return jsonify({'error': 'User not found'}), 404

    user = {
        'id': row[0],
        'name': row[1],
        'email': row[2]
    }

    conn.close()

    return jsonify(user)


# Представление для создания пользователя
@app.route('/users', methods=['POST'])
def create_user():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    user_data = request.get_json()

    if 'name' not in user_data or 'email' not in user_data or 'password' not in user_data:
        conn.close()
        return jsonify({'error': 'Missing required fields'}), 400

    cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)',
                   (user_data['name'], user_data['email'], user_data['password']))
    conn.commit()

    user_id = cursor.lastrowid

    conn.close()

    return jsonify({'id': user_id}), 201


# Представление для обновления пользователя
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    user_data = request.get_json()

    if 'name' not in user_data or 'email' not in user_data or 'password' not in user_data:
        conn.close()
        return jsonify({'error': 'Missing required fields'}), 400

    cursor.execute('UPDATE users SET name = ?, email = ?, password = ? WHERE id = ?',
                   (user_data['name'], user_data['email'], user_data['password'], user_id))
    conn.commit()

    conn.close()

    return jsonify({'message': 'User updated successfully'})


# Представление для удаления пользователя
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()

    conn.close()

    return jsonify({'message': 'User deleted successfully'})


if __name__ == '__main__':
    app.run()
