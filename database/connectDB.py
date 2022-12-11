import sqlite3

conn = sqlite3.connect("ideabank.db")
c = conn.cursor()


# create Table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS ideatable(title TEXT, detail TEXT, status TEXT)')


# Add Data
def add_data(title, detail, status):
    c.execute('INSERT INTO ideatable(title, detail, status) VALUES (?, ?, ?)', (title, detail, status))
    conn.commit()


# View Data
def view_data():
    c.execute('SELECT * FROM ideatable')
    data = c.fetchall()
    return data


# function get a single idea
def get_single_idea_by_title(title):
    c.execute(f"SELECT * FROM ideatable WHERE TITLE = '{title}'")
    data = c.fetchall()
    return data


def get_single_idea_by_detail(detail):
    c.execute(f"SELECT * FROM ideatable WHERE DETAIL = '{detail}'")
    data = c.fetchall()
    return data


def get_single_idea_by_status(status):
    c.execute(f"SELECT * FROM ideatable WHERE STATUS = '{status}'")
    data = c.fetchall()
    return data
