install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest -vv *.py

format:
	black *.py

lint:
	pylint --disable=R,C *.py

all: install lint test
