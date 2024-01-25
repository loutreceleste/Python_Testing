# Güdlift light application

## Why ?

 This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

## Getting Started !

 This project uses the following technologies:

 * Python v3.x+
 * [Flask](https://flask.palletsprojects.com/en/1.1.x/)
 * Pytest
* Locust

 Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     
## [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

This ensures you'll be able to install the correct packages without interfering with Python on your machine.
Before you begin, please ensure you have this installed globally. 


1. Installation

    - After cloning, change into the directory and type:
      ```bash
      virtualenv .
      ```
      This will then set up a virtual python environment within that directory.
    - Next, type:
      ```bash
       source bin/activate
      ```
      You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside.
      
      To deactivate, type:
      ```bash
       source bin/deactivate
      ```
    - Rather than hunting around for the packages you need, you can install in one step by typing:
      ```bash
      pip install -r requirements.txt
      ```
      This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is by typing:
      ```bash
      pip freeze > requirements.txt
      ```
    - Flask requires that you set an environmental variable to the python file. To do that type:
      ```bash
      export FLASK_APP=app/server.py
      ```
    - You should now be ready to test the application. In the directory, type either:
      ```bash
      flask run
      ```
      or 
      ```bash
      python -m flask run
      ```
      The app should respond with an address you should be able to go to using your browser.


2. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

## Unit and integration tests

### Run Tests:

Execute the following command to run all tests:

```bash
pytest
```
### For a more detailed output, use:

```bash
pytest -v
```
This will display each test case with its outcome.

### [Coverage Report](https://coverage.readthedocs.io/en/coverage-5.1/):

To generate a coverage report type:
```bash
pytest --cov=app
```
To generate an HTML coverage report for the project type:
```bash
pytest --cov=. --cov-report html
```

## Performance test whith locust
Please before lauching the performance test ensure that the application is corectly runing.

Then go to a terminal (other than the application terminal) and reach the main directory of the application.
Then type:
```bash
locust -f tests/performance_tests/locustfile.py
```
This will start the Locust web interface on http://localhost:8089. Open this URL in your web browser to configure and start your load test.

Configure and Start Load Test:
- Set the number of users to simulate.
- Set the hatch rate (users spawned per second).
- Specify the host (base URL) of your application.
- Click the "Start swarming" button.

Once the load test is running, you can monitor the results in real-time through the Locust web interface.
