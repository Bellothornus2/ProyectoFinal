from peewee import SqliteDatabase,ForeignKeyField,Model,CharField,fn

from services.user import User

db = SqliteDatabase('ImpetuYam.sqlite')

class CreditCard(Model):
	card_number = CharField()
	expire_date = CharField()
	cvv = CharField()
	owner_name = CharField()
	user_id = ForeignKeyField(User)
	class Meta:
		database = db

def get_credit_card_last_id():
	db.connect()
	query = CreditCard.select(fn.MAX(CreditCard.id))
	last_id = query.scalar() ##para tener un registro
	db.close()
	return last_id

def get_all_credit_card():
	db.connect()
	list_credit_card = CreditCard.select()
	data = {}
	data["data"] = []
	for item in list_credit_card:
		data["data"].append({
			"id":item.id,
			"card_number":item.card_number,
			"expire_date":item.expire_date,
			"cvv":item.cvv,
			"owner_name":item.owner_name,
			"user_id":item.user_id.id,
		})
	db.close()
	return data

def get_credit_card_id(credit_card_id):
	try:
		db.connect()
		credit_card_db = CreditCard.get(CreditCard.id == credit_card_id)
		answer = {
			"data":{
				"id":credit_card_db.id,
				"card_number":credit_card_db.card_number,
				"expire_date":credit_card_db.expire_date,
				"cvv":credit_card_db.cvv,
				"owner_name":credit_card_db.owner_name,
				"user_id":credit_card_db.user_id.id,
			}
		}
		db.close()
	except CreditCard.DoesNotExist:
		answer = {"error": "the record can't be retrieved"}
	return answer

def create_credit_card(card_number,expire_date,cvv,owner_name,user_id):
	db.connect()
	try:
		credit_card = CreditCard.create(
			card_number = card_number,
			expire_date = expire_date,
			cvv = cvv,
			owner_name = owner_name,
			user_id = user_id
		)
		credit_card.save()
		db.commit()
	except:
		pass
	db.close()

def update_credit_card(id, card_number,expire_date,cvv,owner_name,user_id):
	db.connect()
	try:
		credit_card = CreditCard.get(CreditCard.id==id)
		credit_card.card_number = card_number
		credit_card.expire_date = expire_date
		credit_card.cvv = cvv
		credit_card.owner_name = owner_name
		credit_card.user_id = user_id
		credit_card.save()
		db.commit()
	except CreditCard.DoesNotExist:
		pass
	db.close()

def delete_credit_card(id):
	db.connect()
	try:
		credit_card = CreditCard.get(CreditCard.id==id)
		credit_card.delete_instance()
	except CreditCard.DoesNotExist:
		pass
	db.close()


