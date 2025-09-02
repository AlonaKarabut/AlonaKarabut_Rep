from app import get_connection

class UserPage:
    def create_table(self):
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

    def insert_user(self, name):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        conn.commit()
        cur.close()
        conn.close()

    def update_user(self, user_id, new_name):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE users SET name=%s WHERE id=%s", (new_name, user_id))
        conn.commit()
        cur.close()
        conn.close()

    def delete_user(self, user_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
        conn.commit()
        cur.close()
        conn.close()

    def select_users(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
