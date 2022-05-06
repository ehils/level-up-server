from django.db import models
from django.contrib.auth.models import User

# After creating your models, and importing them into init.py,
# create a migration to create database tables:
    # python3 manage.py makemigrations levelupapi (in the terminal)
# once they are created, execute migrations with:
    # python3 manage.py migrate
# seed the database by creating fixtures, json formatted data for each table
    # Django reads this as an INSERT INTO SQL statement  
# load data into database using the following:
    # python3 manage.py loaddata game_types


# by specifying the field type and parameters in the model class,
# you effectively create a SQL statement that creates the table
class Gamer(models.Model):
    # the Django User model is built in, with specific properties, anything additional (in this case "bio"),
    # create a separate model with a one to one relationship with user
    # this is called "extending the user model"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)