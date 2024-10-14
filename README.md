# Late-Show
Late-Show is a Flask API for managing episodes and guest appearances on a fictional late-night show.

## Features
- Retrieve all episodes
- Retrieve details of a specific episode
- Retrieve all guests
- Create new appearances for guests in episodes
- Delete episodes

## Technologies Used
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite (or any SQL database)
- Pipenv for dependency management

## Setup and Installation
1. **Clone the repository**:
   
   git clone git@github.com:brendan544/Late-Show.git
   cd Late-Show

2. **Install dependencies**
     pipenv install

3. Set the environment variable for Flask:
         export FLASK_APP=app:create_app
  
  To run the applicstion type "python app.py" in the 
