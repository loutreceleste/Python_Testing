from app.server import app

def test_point_diplay():
    # Create a test request context for the '/pointsDisplay' endpoint
    with app.test_request_context('/pointsDisplay'):

        # Simulate the GET request to '/pointsDisplay'
        response = app.test_client().get('/pointsDisplay')

    # Assert that the expected message is present in the response
    assert 'All clubs and their remaining points' in response.get_data(as_text=True)

