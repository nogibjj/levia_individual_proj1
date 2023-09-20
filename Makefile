install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	nbqa ruff *.ipynb
	ruff check *.py

format:	
	black *.py 
	nbqa black *.ipynb 

test:
	python -m pytest -vv --cov=main test_*.py
	python -m pytest -vv --cov=lib test_*.py
	python -m pytest -vv --cov=script test_*.py
	pytest --nbval descriptive.ipynb

deploy:

		
all: install lint format test 
