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

    drop_shows_table_query = '''
        DROP TABLE IF EXISTS shows
    '''
    c.execute(drop_shows_table_query)

    # Create the comedy_show table
    create_shows_table_query = '''
        CREATE TABLE IF NOT EXISTS shows (
            Show INTEGER PRIMARY KEY,
            Date DATE NOT NULL,
            Year TEXT NOT NULL,
            Quarter TEXT NOT NULL,
            Venue TEXT NOT NULL,
            Headliner TEXT NOT NULL,
            Host TEXT NOT NULL,
            Feature TEXT NOT NULL,
            Appearances TEXT NOT NULL
        )
    '''
    c.execute(create_shows_table_query)

    # Insert the fake data into the comedy_show table
    show_data = ('31', '05/20/2023','2022/2023', 'Spring', 'Embarcadero Hall',
                 'Student Standup Show', 'Mateen Stewart', 'None', """Aryan Shukla,
                  Benny Lamp, Caroline Murphy, Danny Pogue, Evan Sayer, Lucy Jones,
                  Mark Asch, Rahul Sankar, Raj Oberoi, Raul Reynaga, Rick T. Zhang""")

    insert_show_query = '''
        INSERT INTO shows (Show, Date, Year, Quarter, Venue, 
        Headliner, Host, Feature, Appearances)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
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
    #newest version
    #trying something


