import sqlite3 as sqlite3
import streamlit as st
import json


def retreiveKey(username):

    connection = sqlite3.connect('streamlitBase')
    connect = connection.cursor()

    connect.execute('''SELECT key FROM users WHERE username = ?''', (username,))
    testToken = connect.fetchone()
    return testToken[0]



def insertUserTokenIntoDatabase(token, username):
     
    connection = sqlite3.connect('streamlitBase')
    connect = connection.cursor()




    connect.execute('''UPDATE users SET key = ? WHERE username = ? ''', (token, username))
    connection.commit()
    connect.execute('''SELECT key FROM users WHERE username = ?''', (username,))
    testToken = connect.fetchone()
    return testToken[0]

def registerUser(username, password, key):
       
    connection = sqlite3.connect('streamlitBase')
    connect = connection.cursor()


    #create the database if there are no users yet
    connect.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT, key TEXT, assignment_estimates TEXT, DaysAvailableToWork TEXT)''')
    connection.commit()

    try:
        connect.execute("INSERT INTO users (username, password, key) VALUES (?, ?, ?)", (username, password, key))
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        st.error("username already exists please try another one")
        return False

def loginUser(username, password):

    connection = sqlite3.connect('streamlitBase')
    connect = connection.cursor()


    connect.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
    return connect.fetchone()



def checkForAndInitializeAssignmentTimeEstimates():

    connection = sqlite3.connect('streamlitBase')
    cursor = connection.cursor()
    try:
        cursor.execute('''ALTER TABLE users ADD COLUMN assignment_estimates TEXT''')
    except sqlite3.OperationalError:
        pass
    
    connection.commit()
    connection.close()


def save_time_estimates_to_db(username, time_estimates):
    connection = sqlite3.connect('streamlitBase')
    cursor = connection.cursor()
    
    time_estimates_json = json.dumps(time_estimates)
    cursor.execute("UPDATE users SET assignment_estimates = ? WHERE username = ?", 
                   (time_estimates_json, username))
    connection.commit()
    connection.close()

def retrieve_time_estimates_from_db(username):
    connection = sqlite3.connect('streamlitBase')
    cursor = connection.cursor()
    
    cursor.execute("SELECT assignment_estimates FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    connection.close()
    
    if result and result[0]:
        return json.loads(result[0])
    return {}
    
def checkForAndInitializeDaysAvailableToWork():
    connection = sqlite3.connect('streamlitBase')
    cursor = connection.cursor()
    try:
        cursor.execute('''ALTER TABLE users ADD COLUMN DaysAvailableToWork TEXT''')
    except sqlite3.OperationalError:
        pass
    
    connection.commit()
    connection.close()

def saveDaysAvailableToDB(username, daysAvailable):
    connection = sqlite3.connect('streamlitBase')
    cursor = connection.cursor()
    
    
    daysAvailableJSON = json.dumps(daysAvailable)
    cursor.execute("UPDATE users SET DaysAvailableToWork = ? WHERE username = ?", 
                   (daysAvailableJSON, username))
    connection.commit()
    connection.close()

def retrieveDaysAvailableFromDB(username):
    connection = sqlite3.connect('streamlitBase')
    cursor = connection.cursor()

    cursor.execute("SELECT DaysAvailableToWork FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    connection.close()
    
    if result and result[0]:
        return json.loads(result[0])
    return []


def loadGradesFromDB(username):
    table_name = f"grades_{username}"
    connection = sqlite3.connect("grades.db")
    cursor = connection.cursor()


    cursor.execute(f'''
        SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'
    ''')
    if not cursor.fetchone():
        return []

    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()

    connection.close()

    grade_information = []
    for row in rows:
        grade_information.append({
            "class_name": row[0],
            "assignment_name": row[1],
            "score": row[2],
            "points_possible": row[3],
        })

    return grade_information

def saveGradesToDB(grade_information, username):
    table_name = f"grades_{username}"
    connection = sqlite3.connect("grades.db")
    cursor = connection.cursor()

    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            class_name TEXT,
            assignment_name TEXT,
            score REAL,
            points_possible REAL
        )
    ''')


    cursor.execute(f'DELETE FROM {table_name}')


    for grade in grade_information:
        cursor.execute(f'''
            INSERT INTO {table_name} (class_name, assignment_name, score, points_possible)
            VALUES (?, ?, ?, ?)
        ''', (grade["class_name"], grade["assignment_name"], grade["score"], grade["points_possible"]))

    connection.commit()
    connection.close()




def createSubtaskDB():
    conn = sqlite3.connect("assignments.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS subtasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    assignment_name TEXT,
                    name TEXT,
                    completed BOOLEAN)''')
    
    conn.commit()
    conn.close()


def addSubTaskToDB(assignment_name, individualSubTask):
    conn = sqlite3.connect("assignments.db")
    c = conn.cursor()
    c.execute("INSERT INTO subtasks (assignment_name, name, completed) VALUES (?, ?, ?)",
              (assignment_name, individualSubTask, False))
    conn.commit()
    conn.close()


def getSubTasksFromDB(assignment_name):
    conn = sqlite3.connect("assignments.db")
    c = conn.cursor()
    c.execute("SELECT id, name, completed FROM subtasks WHERE assignment_name = ?", (assignment_name,))
    subtasks = c.fetchall()
    conn.close()
    return subtasks

def updateSubTaskstatus(assignment_name, individualSubTask, completed):
    conn = sqlite3.connect("assignments.db")
    c = conn.cursor()
    c.execute('''UPDATE subtasks
                 SET completed = ?
                 WHERE name = ? AND assignment_name = ?''',
              (completed, individualSubTask, assignment_name))
    conn.commit()
    conn.close()

def deleteSubtask(subtask_id):
    conn = sqlite3.connect("assignments.db")
    c = conn.cursor()
    c.execute("DELETE FROM subtasks WHERE id = ?", (subtask_id,))
    conn.commit()
    conn.close()
