# 🧠 Makefile de control para Validador Semántico Jurídico

.PHONY: test analyze docker serve deploy mkvenv install all

test:
	@python manage.py test

analyze:
	@python manage.py analyze

docker:
	@python manage.py docker

serve:
	@python manage.py serve

deploy:
	@python manage.py deploy

mkvenv:
	@python manage.py mkvenv

install:
	@python manage.py install

all: install test analyze serve