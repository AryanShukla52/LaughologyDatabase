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
            Date TEXT NOT NULL,
            Quarter TEXT NOT NULL,
            Venue TEXT NOT NULL,
            Headliner TEXT NOT NULL,
            Host TEXT NOT NULL,
            Feature TEXT NOT NULL,
            Appearances TEXT NOT NULL
        )
    '''
    c.execute(create_shows_table_query)

    # Insert the initial data point into the comedy_show table
    show_data = ('29', '5/20/23','Spring 2023', 'Embarcadero Hall',
                 'Student Standup Show', 'Mateen Stewart', 'None', """Aryan Shukla,
                  Benny Lamp, Caroline Murphy, Danny Pogue, Evan Sayer, Lucy Jones,
                  Mark Asch, Rahul Sankar, Raj Oberoi, Raul Reynaga, Rick T Zhang""")

    insert_show_query = '''
        INSERT INTO shows (Show, Date, Quarter, Venue, 
        Headliner, Host, Feature, Appearances)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    '''
    c.execute(insert_show_query, show_data)

    # Print the shows table
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

def fill_data():
    conn = sqlite3.connect("MyArchive.sqlite")
    c = conn.cursor()

    # Insert the initial data point into the comedy_show table
    insert_show_details_query = '''
        INSERT INTO shows (Show, Date, Quarter, Venue, Headliner, Host, Feature, Appearances)
        VALUES 
            ('28', '5/13/23', 'Spring 2023', 'Embarcadero Hall', 'Asif Ali', 
            'Raj Oberoi', 'Milan Patel', 'Aryan Shukla, Raaghav Thatte, Rahul Sankar'),
            ('27', '5/06/23', 'Spring 2023', 'Embarcadero Hall', 'Brandon Wardell', 
            'Jack Scotti', 'Rick Storer', 'Benny Lamp, Danny Pogue'),
            ('26', '4/29/23' ,'Spring 2023','Embarcadero Hall','Andrew Michaan',
            'Adam Elder','Mikey Kampmann', 'Lucy Jones, Rick T Zhang'),
            ('25','4/22/23','Spring 2023','Embarcadero Hall','Brent Pella',
            'David Uhlfelder','Key Lewis','Jamal Ogans, Raul Reynaga'),
            ('24','4/15/23','Spring 2023','IV Theater','Steph Tolev',
            'Jake Ciccone','Mateen Stewart','Aryan Shukla, Mark Asch'),
            ('23','3/11/23','Winter 2023','Embarcadero Hall','Joe Mande',
            'Jack Scotti','Michael Schirtzer','Benny Lamp, David Zingher'),
            ('22','3/4/23','Winter 2023','Embarcadero Hall', 'California College Comedy 
            Club Contest','Benny Lamp','None','SLO, UCLA, UCR, UCSB'),
            ('21','2/25/23','Winter 2023','Embarcadero Hall','Chase O Donnell',
            'Joe Yuke','Isak Allen','Rahul Sankar, Rick T Zhang'),
            ('20','2/11/23','Winter 2023','Embarcadero Hall','Brent Weinbach',
            'Courtney Rainwater','Paige Weldon','Caroline Murphy, Danny Pogue'),
            ('19','1/28/23','Winter 2023','Embarcadero Hall','Jamie Wolf & Lucas Zelnick',
            'Jake Ciccone','None','Jamal Ogans, Raj Oberoi'),
            ('18','11/19/22','Fall 2022','Embarcadero Hall','Jeremy Rocha',
            'Caroline Murphy','Daniel Lewis','Benny Lamp, Raj Oberoi'),
            ('17','11/5/22','Fall 2022','Embarcadero Hall','Tre Lamb',
            'Jack Scotti','Corde Snell','Caroline Murphy, David Zingher'),
            ('16','10/29/22','Fall 2022','Embarcadero Hall','Amy Silverberg',
            'Evan Sayer','Matt Curry','Aiden Brent, Rahul Sankar'),
            ('15','10/22/22','Fall 2022','Embarcadero Hall','Sean Grant',
            'Jake Ciccone','Chris Flail','Danny Pogue, Jamal Ogans'),
            ('14','10/15/22','Fall 2022','Embarcadero Hall','Kiry Shabazz',
            'Lauren Nicole Clark','Rick Storer','Unknown'),
            ('13','5/21/22','Spring 2022','Embarcadero Hall','Martin Morrow',
            'Jack Scotti','Paul Clay','Unknown'),
            ('12','5/14/22','Spring 2022','Embarcadero Hall','Roberto Omoto',
            'Courtney Rainwater','Xander Beltran','Uriah Wesman'),
            ('11','4/23/22','Spring 2022','Embarcadero Hall','Nicki Fuchs',
            'Chris Williams','Cat Alvarado','Benny Lamp, David Zingher'),
            ('10','4/16/22','Spring 2022','Embarcadero Hall','Orion Levine',
            'Lauren Nicole Clark','David Samuel','Unknown'),
            ('9','4/9/22','Spring 2022','Embarcadero Hall','Sean Grant',
            'Corde Snell','Clay Newman','Alexis Bradby'),
            ('8','2/29/20','Winter 2020','Embarcadero Hall','CA Comedy Carnival',
            'Unknown','None','SLO, UCLA, UCSB, USC'),
            ('7','2/22/20','Winter 2020','Embarcadero Hall','Chris Cope',
            'Unknown','Unknown','Unknown'),
            ('6','2/15/20','Winter 2020','Embarcadero Hall','Asif Ali',
            'Unknown','Unknown','Unknown'),
            ('5','2/8/20','Winter 2020','Embarcadero Hall','Andrew Michaan',
            'Unknown','Unknown','Unknown'),
            ('4','2/1/20','Winter 2020','Embarcadero Hall','Chase Bernstein',
            'Unknown','Unknown','Unknown'),
            ('3','1/25/20','Winter 2020','Embarcadero Hall','Amy Silverberg',
            'Unknown','Unknown','Unknown'),
            ('2','1/18/20','Winter 2020','Embarcadero Hall','Jeremiah Watkins',
            'Unknown','Unknown','Unknown'),
            ('1','1/11/20','Winter 2020','Embarcadero Hall','Kiry Shabazz',
            'Unknown','Unknown','Unknown')
            '''
    c.execute(insert_show_details_query)

    # Print the shows table
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
    fill_data()
    #look up crud


