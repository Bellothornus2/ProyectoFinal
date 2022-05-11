#SELECT MingredientUserAX(ID) AS LastID FROM Persons
from peewee import SqliteDatabase,CharField,BooleanField,Model,IntegerField,fn

db = SqliteDatabase('ImpetuYam.sqlite')

class User(Model):
	name = CharField()
	surname = CharField()
	age =IntegerField()
	dni = CharField()
	username = CharField()
	password = CharField()
	sex = CharField()
	phone_number = CharField()
	email = CharField()
	verified_user = IntegerField()
	class Meta:
		database = db

def get_user_last_id():
	db.connect()
	query = User.select(fn.MAX(User.id)) ##para obtener SELECT MAX(id) AS LastID FROM Item
	last_id = query.scalar() ##para tener un registro
	db.close()
	return last_id

def get_all_user():
	db.connect()
	list_user = User.select()
	data = {}
	data["data"] = []
	for item in list_user:
		data["data"].append({
			"id":item.id,
			"name":item.name,
			"surname":item.surname,
			"age":item.age,
			"dni":item.dni,
			"username":item.username,
			"password":item.password,
			"sex":item.sex,
			"phone_number":item.phone_number,
			"email":item.email,
			"verified_user":item.verified_user
		})
	db.close()
	return data

def get_user_id(user_id):
	try:
		db.connect()
		user_db = User.get(User.id == user_id)
		answer = {
			"data":{
				"id":user_db.id,
				"name":user_db.name,
				"surname":user_db.surname,
				"age":user_db.age,
				"dni":user_db.dni,
				"username":user_db.username,
				"password":user_db.password,
				"sex":user_db.sex,
				"phone_number":user_db.phone_number,
				"email":user_db.email,
				"verified_user":user_db.verified_user
			}
		}
		db.close()
	except User.DoesNotExist:
		answer = {"error": "the record can't be retrieved"}
	return answer

def create_user(name,surname,age,dni,username,password,sex,phone_number,email,verified_user):
	db.connect()
	user = User.create(
		name=name, 
		surname=surname,
		age=age,
		dni=dni,
		username=username,
		password=password,
		sex=sex,
		phone_number=phone_number,
		email=email,
		verified_user=verified_user)
	print(user)
	user.save()
	db.commit()
	db.close()

def update_user(id, name,surname,age,dni,username,password,sex,phone_number,email,verified_user):
	db.connect()
	try:
		user = User.get(User.id==id)
		user.name = name
		user.surname = surname
		user.age = age
		user.dni = dni
		user.username = username
		user.password = password
		user.sex = sex
		user.phone_number = phone_number
		user.email = email
		user.verified_user = verified_user
		user.save()
		db.commit()
	except User.DoesNotExist:
		pass
	db.close()

def delete_user(id):
	db.connect()
	try:
		user = User.get(User.id==id)
		user.delete_instance()
	except User.DoesNotExist:
		pass
	db.close()
