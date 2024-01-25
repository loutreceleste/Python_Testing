from unittest.mock import patch
from app.server import app

def test_show_summary_with_incorrect_email():
    # Create a test request context for the '/showSummary' endpoint with incorrect email data
    with app.test_request_context('/showSummary', data={'email': 'incorrect@example.com'}):

        # Mock the request form data with an incorrect email
        with patch('app.server.request') as mock_request:
            mock_request.form = {'email': 'incorrect@example.com'}

            # Simulate the POST request to '/showSummary'
            response = app.test_client().post('/showSummary', data={'email': mock_request.form['email']})

    # Assert that the expected error message is present in the response
    assert 'No club associated with this email, please try again.' in response.get_data(as_text=True)

