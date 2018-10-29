mypy:
	mypy --config-file=mypy.ini $(f)

kaggle_1:
	python3.6 kaggle_mushrooms_1.py -l='$(l)'

kaggle_2:
	python3.6 kaggle_mushrooms_2.py -l='$(l)' -o='$(o)'
