
from orm import Model, StringField, IntegerField

class User(Model):
	__table__='user'
	id=IntegerField()
