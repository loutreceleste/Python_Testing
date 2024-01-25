from app.server import app

def test_index():
    # Create a test request context for the '/' endpoint
    with app.test_request_context('/'):

        # Simulate the GET request to '/'
        response = app.test_client().get('/')

    # Assert that the expected message is present in the response
    assert '<h1>Welcome to the GUDLFT Registration Portal!</h1>' in response.get_data(as_text=True)
