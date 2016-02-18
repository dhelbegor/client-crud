run:
	./manage.py runserver

migrate:
	./manage.py makemigrations
	./manage.py migrate

user:
	./manage.py createsuperuser --username='admin' --email=''

dump:
	./manage.py dumpdata > database.json

load:
	./manage.py loaddata database.json

clients:
	./manage.py shell < fixture/client.py