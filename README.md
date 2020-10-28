#Text API

The following instructions assume that you've got Python 3 installed and that you've activated your virtual environment.


###Install the dependencies

pip install -r fiona_requirements.txt


pip install -r local_requirements.txt --no-index --find-links wheels


pip install -r requirements.txt 

###Running the script

cd home_project

python main.py


Sources for spatial join:
https://geopandas.org/mergingdata.html
https://towardsdatascience.com/how-to-easily-join-data-by-location-in-python-spatial-join-197490ff3544