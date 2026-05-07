Step 1:- Run This Command For Installing Virtual Enviroment (python -m venv myenv)
Step 2:- Run THis COmmand For Activation 
         For Windows (myenv\Scripts\activate)
         For Mac/Linux(source myenv/bin/activate)
Step 3:- Now HAve To INstall Django (pip install django)
Step 4:- Now Run (pip install pscopyg2)
Step 5:- Now Run Two Command 
         (python manage.py makemigrations)
         (python manage.py migrate)
Step 6:- Run This Command For Image Storage 
         (pip install pillow)
Step 7:- Create Super User
         (python manage.py createsuperuser)
Step 8:- Create A Model Of Students
Step 9:- Create URLS And VIEWS File 
Step 10:- Create HTML Pages For Froontend To Represent All The Data And Performe CRUD Operation  
Step 11:- Create a Seed File 
                  students/
                  │
                  ├── management/
                  │   ├── __init__.py
                  │   └── commands/
                  │       ├── __init__.py
                  │       └── seed_students.py

         students/management/commands/seed_students.py

         Enter Student Seeded data

Step 12:- Run Migrations First
            python manage.py makemigrations
            python manage.py migrate

Step 13:- Run Seeder Command
            python manage.py seed_students

Step 14:- Add a serching where we can search using name , rool no , city , class 
            Updating View.py and HTML File

Step 15:- Adding Filter And Paginator
         Updating View.py and HTML File