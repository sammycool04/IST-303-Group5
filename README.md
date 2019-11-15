# IST-303-Group5


### PROJECT DESCRIPTION
FinalList is a web application that enables users to identify their ideal housing option. Users can generate their personalized housing lists based on their inputed parameters such as
* crime rate risk levels and proximity to area amenities (schools based on performance rankings, grocery stores,
gas stations, banks, restauarants, etc.)
* recreation space (hiking and biking trails, parks, etc.) that
coincide with selected rental or sales ranges
*bedroom/bathroom combinations and other housing-related 
specifications.

### GROUP NAME: 
Team FinalLists

### GROUP MEMBERS: 
The members of this group are Sam Feng, Alex Jin, Kieu Lara, Rutuja Ganesh Limaye, and Phillip Wang.

### ROLES
* Sam - Web Developer
* Alex - UI Designer
* Kieu - Product Owner/Project Manager
* Rutuja - Database Developer
* Phillip - Web Developer

### STAKEHOLDERS
* People who are looking for a place to live
* Landloards and proerty owners
* Real estate agents/professionals

### USER STORIES
* Any user should be able to search by location and property features only
* Any user would be able to input their preference parameters when they open the web app as an added feature 
* A registered user is able to save listings, contact housing hosts and access other web features on the web pages
* A user can make a change to their preferences without starting over
* A user can see both a map view and text listings of search results
* A user should be able to sort the listings based on their personalized rankings preference
   
### TECHNOLOGY
* Frontend: HTML, CSS, JavaScript
* Backend: Python, Django
* Database: SQL
 
### PROJECT MANAGEMENT/COLLABORATION TOOLS
* GitHub
* Google Doc/Slides
* Trello https://trello.com/b/PzPFRTuv/ist303-finalists)
 
### PARAMETERS WE COLLECT FROM USERS
* Distance to certain places, areas, etc...
* Price Preference
* Safety Level Preference
* Purpose: Sell, rent, or buy?
* Location

### PROJECT REQUIREMENTS:
User stories will be drafted and appropriately scheduled in order to organize related activities throughout
this project time-frame.  The user stories will center around requirements for what the user interface will 
include, what the web application ranking options will include, as well as accessiblity to the web application.
Data sources will be identified, validated, and documented to ensure that the web application is held up by 
by realistic data or inferred by real data.

### PROJECT CONCEPT PRESENTATION PART A FEEDBACK AND NEXT STEPS:
* Stakeholder feedback via survey responses from classmates will be sought. A survey will be drafted and distributed to 
  refine preference categories.
* propertyfinder.ae was suggested for review for ideas.
* Looking beyond API sources was suggested for data sources to ensure un-biased data is used.
* Query on what indexes will be used was brought up to offset implied or direct bias.
* Further exploration on how ranking (1 through 5 versus most importnat to least important, etc.) should be set to ensure
  the recommendations provided by the search is not too restrictive.

### PROJECT STATUS TRACKING (W/ BURNDOWN CHART)
See https://github.com/sammycool04/IST-303-Group5/blob/master/Project%20Hours%20Tracking.xlsx
  
### TEAM MEETING NOTES
Agenda Link: https://drive.google.com/open?id=1zvve-Ctsv2qc7kWy-xecymomQILijSlj

### To Run the Application:
* Git clone the project
* CD to the project folder
* Since we are using Postgresql at this moment, you will also have to set up your local database first:
   - Download Postgres from https://www.postgresql.org/
   - Open Postgres app and click “initialize” to create the first database
   - The first database should be selected automatically on the app, and double click it to open a terminal 
   - In the terminal, type ‘password postgres’ to create your own password
   - Type CREATE DATABASE (a name you want), for example, CREATE DATABASE finalLists 
   - Go to settings.py file under Worksample:
   - Find the DATABASE setting, and change it  to something like:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': ‘(the database name you just created)’,
        'USER':'postgres',
        'PASSWORD’:’(the password you just created)’,
        'HOST':'localhost',
        'PORT’:’(open postgres, click Server Setting to check your port number)’,
    }
}
```

* Save the change
* In the terminal, type “python manage.py runserver”

### TESTING:
* We use pytest-django and mixer for our testing
- In your terminal, type:
```
pip install pytest-django
pip install mixer
```
* Remember to keep your Postgres database running. In your terminal, type:
```
pytest
```

