# import psycopg2
# from psycopg2 import Error
# from config import DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT
# import logging

# async def insert_word(word, transcription, translation, definition, table):
#     try:
#         db_connection = connect_db()
#         cursor = db_connection.cursor()
#     except(Error):
#         print("[Error]: ", Error)
    
#     cursor.execute(f'''
#                     INSERT INTO {table} (word, transcription, translation, definition)
#                     VALUES ('{word}', '{transcription}', '{translation}', '{definition}');
#                     ''')
    
#     db_connection.commit()
#     db_connection.close()

# async def insert_user(user_id, first_name, last_name):
#     db_connection = connect_db()
#     db_cursor = db_connection.cursor()

#     try:
#         db_cursor.execute(f'''
#                         INSERT INTO users (userid, first_name, last_name)
#                         VALUES ({user_id}, '{first_name}', '{last_name}')
#                         ON CONFLICT (userid) DO UPDATE SET
#                         userid={user_id}, first_name='{first_name}', last_name='{last_name}';
#                         ''')
#     except psycopg2.errors.UniqueViolation:
#         logging.error(f"Failed to insert user {first_name} {last_name} with id {user_id} into database users.")
        
#     db_connection.commit()
#     db_connection.close()

# async def get_user(id):
#     db_connection = connect_db()
#     db_cursor = db_connection.cursor()
 
#     try:
#         db_cursor.execute(f"SELECT * FROM users WHERE userid = {id};")
#     except psycopg2.errors.UndefinedColumn:
#         print("Failed to get data from database. Error: psycopg2.errors.UndefinedColumn")

#     if db_cursor.fetchall() == []:
#         return False

# async def create_table(level, kind):
#     try:
#         db_connection = connect_db()
#         cursor = db_connection.cursor()
#     except(Error):
#         print("[Error]: ", Error)
#         return 1

#     table = f"{level}_{kind}_words"
    
#     cursor.execute(f'''
#                     CREATE TABLE IF NOT EXISTS {table} (
#                     id serial PRIMARY KEY,
#                     word VARCHAR(64) UNIQUE NOT NULL,
#                     transcription VARCHAR(64),
#                     translation VARCHAR(64) NOT NULL,
#                     definition TEXT(4096));
#                     ''')
    
#     db_connection.commit()
#     db_connection.close()

# async def get_list_of_user_wordlists(id):
#     db_connection = connect_db()
#     db_cursor = db_connection.cursor()
 
#     try:
#         db_cursor.execute(f"SELECT name, wordlist_id FROM user_wordlists WHERE userid = {id};")
#     except psycopg2.errors.UndefinedColumn:
#         print("Failed to get data from database. Error: psycopg2.errors.UndefinedColumn")

#     data = db_cursor.fetchall()

#     if data == []:
#         return False
    
#     print(data)
    
    
    

# def connect_db():
#     return psycopg2.connect(database=DATABASE_NAME, user=DATABASE_USERNAME, 
#                             password=DATABASE_PASSWORD, host=DATABASE_HOST, 
#                             port=DATABASE_PORT)
