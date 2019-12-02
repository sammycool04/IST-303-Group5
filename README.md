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
1. Install Python 3
    - On macOS using Homebrew:
    ```shell script
     /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
     brew install python
    ```
    - On Linux:
    ```shell script
     sudo apt-get install python3
    ```
    - On Windows, download & install from link:
    https://www.python.org/downloads/windows/
    

2. Install Microsoft ODBC driver for SQL Server ( for project's database)
    - macOS:
    ```shell script
     brew install msodbcsql17 mssql-tools
    ```
    - Linux (Ubuntu 19 as example)
    ```shell script
     #Ubuntu 19.04
     curl https://packages.microsoft.com/config/ubuntu/19.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
     exit
     sudo apt-get update
     sudo ACCEPT_EULA=Y apt-get install msodbcsql17
     # optional: for bcp and sqlcmd
     sudo ACCEPT_EULA=Y apt-get install mssql-tools
     echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
     echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
     source ~/.bashrc
     
    ```
    
    - Windows, download & install from link:
	https://www.microsoft.com/en-us/download/details.aspx?id=56567

3. Install Python Virtual Environment
    - Windows:
    ```shell script
     python3 -m pip install virtualenv
    ```
    - non-Windows:
    ```shell script
     python3 -m pip install --user virtualenv
    ```

4. Create & activate virtual environment (named env)
    ```shell script
     python3 -m venv /path/to/new/virtual/environment/env
     source env/bin/activate
    ```

5. Clone the project inside virtual environment
	git clone git@github.com:sammycool04/IST-303-Group5.git

6. cd to the project folder & install required python packages
    ```shell script
     cd IST-303-Group5
     python -m pip install -r requirements.txt
    ```

7. Start the project
    ```shell script
     python manage.py runserver
    ```
8. To access the web app, open your web browser, enter: 
    [127.0.0.1:8000](127.0.0.1:8000 "Finalists")
	



### TESTING:
* We use pytest-django and mixer for our testing
- If you haven't installed the packages, in your terminal, type:
```shell script
pip install pytest-django
pip install mixer
```
* Remember to keep your Postgres database running. In your terminal, type:
```
pytest
```

