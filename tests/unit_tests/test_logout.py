from app.server import app

def test_logout():
    # Create a test request context for the '/logout' endpoint
    with app.test_request_context('/logout'):

        # Simulate the GET request to '/logout'
        response = app.test_client().get('/logout')

    # Assert that the expected message is present in the response
    assert '<a href="/">/</a>' in response.get_data(as_text=True)
