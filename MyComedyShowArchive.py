import sqlite3

# Function to generate fake data for comedy shows
def generate_fake_data():
    comedy_shows = [
        ("The Comedy Club", "John Doe", "2022-05-15", "8:00 PM"),
        ("Laugh Factory", "Jane Smith", "2022-06-20", "7:30 PM"),
        ("Stand-Up Spectacular", "Mike Johnson", "2022-07-10", "9:00 PM"),
        ("Comedy Central Live", "Emily Williams", "2022-08-05", "8:30 PM"),
        ("Funny Frenzy", "David Lee", "2022-09-12", "7:00 PM")
    ]
    return comedy_shows

# Create the database and table
def create_database():
    conn = sqlite3.connect("MyArchive.sqlite")
    c = conn.cursor()

    # Create the comedy_show table
    create_shows_table_query = '''
        CREATE TABLE IF NOT EXISTS shows (
            show_id INTEGER PRIMARY KEY,
            show_date DATE NOT NULL,
            comedian_name TEXT NOT NULL,
            audience_count INTEGER
        )
    '''
    c.execute(create_shows_table_query)

    # Insert the fake data into the comedy_show table
    show_data = ('2023-08-24', 'John Smith', 150)

    insert_show_query = '''
        INSERT INTO shows (show_date, comedian_name, audience_count)
        VALUES (?, ?, ?)
    '''
    c.execute(insert_show_query, show_data)

    select_all_shows_query = '''
        SELECT * FROM shows
    '''
    c.execute(select_all_shows_query)
    all_shows = c.fetchall()
    for show in all_shows:
        print(show)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("MyArchive.sqlite database created with the comedy_show table and fake data.")
    print("hi there")
    #how does this even work
    #what is this fr bruh
    #please work


