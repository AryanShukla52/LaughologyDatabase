# Laughology Database

### Background

I joined Laughology, UCSB's premier stand-up comedy club, in the Winter Quarter of my Sophomore year (2023). 
After weeks of helping promote our biweekly shows, attending our open mics, and even performing in several shows, I was appointed Treasurer of Laughology. Sifting through all the archival Google documents I gained access to, I realized the club did not have any proper records of the shows we had hosted this year or the years before. I sought to change that by creating a database featuring all the information about the shows we hosted and the comedians that performed at them that I could find.

### My Process

First, I needed to collect my data. In this case, that was the Date, Venue, Host, Headlining Comedian, Featured Comedian, and Student Appearances at all of the shows we had hosted in the past. Since we had no way of keeping track of this information, my only method of collection was to scour through Laughology's numerous Instagram posts and copy down whatever was available on our announcement graphics onto a Google sheet. For example, an announcement graphic leading up to a show typically looks like this:   

<br> 
<img src="https://github.com/AryanShukla52/LaughologyDatabase/assets/102696882/d54972f2-547e-4ff0-83cb-249962d8a8f4" width="500" />  <br> 
<br> 
While our graphics have become more sleek and informative, for older shows dating back to before the pandemic, most of the information available is just the Headliner, the Date, and the Venue.  <br> 
<br> 
<img src="https://github.com/AryanShukla52/LaughologyDatabase/assets/102696882/8445ee8d-1fb5-4573-b3aa-ab5249792dde" width="500" />   

Thus, whatever I could not find in Instagram captions, I had to mark it as unknown. Going as far back as the Winter Quarter of 2020, this is the information I was able to collect onto the Google Sheet

<img src="https://github.com/AryanShukla52/LaughologyDatabase/assets/102696882/b9818964-fe99-45cf-924a-1b8e441f1903" width="1000" />

I then exported the data into a .CSV file for easier entry into my SQL database.

## Creating the Database

For this project, I used Python and imported the SQLite3 library. I chose to utilize the lightweight SQLite database over something like MySQL server because this is a personal project, so I opted for efficiency and simplicity over multi-user capabilities.

#### create_database()

My first function, create_database(), establishes a connection to a SQLite file. After that, I create my shows table, add an initializing set of data points to it, and then print the items in the table. I set my primary key as the show number, as no two shows would ever have the same show number. During this process, I also learned I needed to add a drop table query to the start of the function so I could override any existing tables from a previous save. 

<img src="https://github.com/AryanShukla52/LaughologyDatabase/assets/102696882/b17d19dc-d4ad-476e-a0ce-11ca1a4c927f" width="800" />   

#### fill_data()

My second function, fill_data(), was created to add the rest of the data points to the shows table I initialized in the create_database() function.   

<img src="https://github.com/AryanShukla52/LaughologyDatabase/assets/102696882/fd81f619-edc5-460a-afd9-90a50d82b90c" width="800" />   


#### Output

The resulting database looks like this:

<img src="https://github.com/AryanShukla52/LaughologyDatabase/assets/102696882/a08190be-0002-4492-81ff-ed2cd1f793f5" width="800" />   













