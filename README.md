# Django Tutorial: Polls App
An attempt to strengthen my Django skills.

The tutorial being followed are the lecture slides for [Web App Development](https://www.gla.ac.uk/coursecatalogue/course/?code=COMPSCI2021) that are nearly the same as [Django Tutorial](https://docs.djangoproject.com/en/2.2/intro/).

## Using this Repository
Since this repository uses a virtual environment with specific packages, it is essential to activate it specifically.

### Virtual Environment
If you haven't already created a virtual environment, you can do so using either of the following:
* Anaconda Prompt

    `$ conda create -n polls python=3.8.0`

* Python (Windows)

    `$ python -m venv polls`

* Python (macOS / Linux)

    `$ python3 -m venv polls`


You can then activate the environment once created.
* Anaconda Prompt

    `$ conda activate polls`

* Python (Windows)

     `$ .\polls\Scripts\activate`

* Python (macOS / Linux)

     `$ source polls/bin/activate`


This project uses Anaconda Prompt specifically as instructed.

### Installing packages
A `requirements.txt` file mentions all the packages along with their versions used for this project. You can install them using:

`$ pip install -r requirements.txt`


### Running the App
The main Python file is `manage.py`. The app can be run using

`$ python manage.py runserver`

and then use a browser to go to http://127.0.0.1:8000/polls/