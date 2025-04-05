from uuid import UUID
import psycopg2
from psycopg2 import Error
from config import DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT
import logging

async def add_user(first_name, last_name, telegram_id) -> UUID:
    try:
        db_connection = connect_db()
        cursor = db_connection.cursor()
        cursor.execute("""
            INSERT INTO users (first_name, last_name, telegram_id)
            VALUES (%s, %s, %s)
            RETURNING id;
        """, (first_name, last_name, telegram_id))
        user_id = cursor.fetchone()[0]
        db_connection.commit()
        return user_id
    except Error as e:
        logging.error(f"[Error adding user]: {e}")
        raise
    finally:
        if db_connection:
            db_connection.close()

async def get_user(uuid: UUID, tid: int) -> list:
    if not uuid and not tid:
        raise ValueError("Either uuid or tid must be provided.")
    try:
        db_connection = connect_db()
        cursor = db_connection.cursor()
        if uuid:
            cursor.execute("""
                SELECT * FROM users WHERE id = %s;
            """, (uuid,))
        else:
            cursor.execute("""
                SELECT * FROM users WHERE telegram_id = %s;
            """, (tid,))
        return cursor.fetchone()
    except Error as e:
        logging.error(f"[Error getting user]: {e}")
        raise
    finally:
        if db_connection:
            db_connection.close()
            
# async def get_problems()

def connect_db():
    return psycopg2.connect(database=DATABASE_NAME, user=DATABASE_USERNAME, 
                            password=DATABASE_PASSWORD, host=DATABASE_HOST, 
                            port=DATABASE_PORT)
