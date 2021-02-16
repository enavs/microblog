# Step 1. create the name of your main/root folder
# Step 2. create a virtual environment.  note that the 'venv "venv"' part looks the same but the last venv can be whatever name you want
    python3 -m venv venv
# Step 3. activate your virutal environment
    . venv/bin/activate
# Step 4. install flask
    # if you need to install a newer version type:
    pip3 install --upgrade pip
    # install flask
    pip install flask
# Step 5. import flask
    import flask
# Step 6. create the flask environment by selecting the file to run
    export FLASK_APP=microblog.py
# Step 7. run the files by doing:
    flask run
    # to quit type:
    Press CTRL+C to quit)
# Step 8. to make your changes dynamic and to move to the development server type this:
    export FLASK_ENV=development
# Step 9. install extra packages
    pip install flask-wtf
    pip install flask-sqlalchemy
    pip install flask-migrate
# Step 10. let's create a migration repository for our database
    flask db init
# Step 11. this generates the automatic migrations.  You can add in "-m" to give a short description of what you migrated
    flask db migrate
# Step 12. you need to push or upgrade to make changes to your database
    flask db upgrade
# Step 13. flask login information that saves login details across webpages
    pip install flask-login
# Step 14. validator - email
    pip install email-validator
