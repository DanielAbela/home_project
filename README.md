#Text API

The following instructions assume that you've got Python 3 installed and that you've activated your virtual environment.


###Install the dependencies

pip install -r fiona_requirements.txt 


pip install -r local_requirements.txt --no-index --find-links wheels (see NB below)


pip install -r requirements.txt 

###Running the script

cd home_project

python main.py


###Running tests

cd home_project

pytest --cov=. --cov-config=../.coveragerc

Sources for spatial join:
https://geopandas.org/mergingdata.html
https://towardsdatascience.com/how-to-easily-join-data-by-location-in-python-spatial-join-197490ff3544

Source for wheels:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#rtree
https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona
https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal

NB: The wheels used are for a 32-bit version of Python 3.6.5