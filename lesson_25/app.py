import psycopg2

def get_connection():
    return psycopg2.connect(
        host="mydb",          # замість "localhost"
        database="testdb",
        user="user",
        password="pass"
    )


def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_user(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    cur.close()
    conn.close()

def update_user(user_id, new_name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET name=%s WHERE id=%s", (new_name, user_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()

def select_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

if __name__ == "__main__":
    create_table()
    insert_user("Alice")
    print(select_users())
