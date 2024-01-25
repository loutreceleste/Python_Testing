from datetime import timedelta, datetime
from unittest.mock import patch
from app.server import app

def test_book_in_a_past_competition():
    # Generate a past date to simulate a competition in the past
    past_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')

    # Create a test request context for the '/showSummary' endpoint
    with app.test_request_context('/showSummary', data={'email': 'john@simplylift.co'}):

        # Mock the 'competitions' data to simulate a competition in the past
        with patch('app.server.competitions', [{"name": "Spring Festival", "date": past_date,
                                                "numberOfPlaces": "25"}]):

            # Mock the request form data with a valid email
            with patch('app.server.request') as mock_request:
                mock_request.form = {'email': 'john@simplylift.co'}

                # Simulate the POST request to '/showSummary'
                response = app.test_client().post('/showSummary', data={'email': mock_request.form['email']})

    # Assert that the "Book Places" link is not present in the response
    assert "Book Places" not in response.get_data(as_text=True)
