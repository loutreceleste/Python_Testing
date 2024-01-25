from locust import HttpUser, task, between

class ProjectPerfTest(HttpUser):
    # Set the wait time between requests (1 to 3 seconds)
    wait_time = between(1, 3)

    # Task to simulate a user accessing the index page
    @task
    def index(self):
        self.client.get('/')

    # Task to simulate a user submitting a summary request via POST
    @task
    def show_summary(self):
        self.client.post('/showSummary', data={"email": "john@simplylift.co"})

    # Task to simulate a user accessing the book page
    @task
    def book(self):
        self.client.get('/book/Spring Festival/Simply Lift')

    # Task to simulate a user purchasing places via POST
    @task
    def purchase_places(self):
        data ={
            'competition': "Spring Festival",
            'club': "Simply Lift",
            'places': 5
        }
        self.client.post('/purchasePlaces', data=data)

    # Task to simulate a user accessing the points display page
    @task
    def points_display(self):
        self.client.get('/pointsDisplay')

    # Task to simulate a user logging out
    @task
    def logout(self):
        self.client.get('/logout')
