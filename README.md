# To run follow this steps
1.Clone respository 
2.Setup virtual environment
3. isntall django(python3 -m pip install Django) and djangorestframework (python3 -m pip install Djangorestframework)



# Then run these commands
you have to do it in this order becuase gym_app depends on the models of customuser
1.  python3 manage.py makemigrations customuser
2. python3 manage.py migrate
3. python3 manage.py makemigrations gym_app
4. python3 manage.py migrate
5. python3 manage.py runserver



