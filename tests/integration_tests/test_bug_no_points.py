from unittest.mock import patch
from app.server import app

def test_not_allowed_use_more_points():
    # Create a test request context for the '/purchasePlaces' endpoint
    with app.test_request_context('/purchasePlaces'):

        # Mock the 'clubs' data to simulate a club with zero points
        with patch('app.server.clubs', [{'name': 'Simply Lift', 'points': '0'}]):

            # Mock the request form data with a booking attempt for more places than available points
            with patch('app.server.request') as mock_request:
                mock_request.form = {'points': '0', 'competition': 'Spring Festival', 'club': 'Simply Lift',
                                     'places': '25'}

                # Simulate the POST request to '/purchasePlaces'
                response = app.test_client().post('/purchasePlaces', data={'points': mock_request.form['points'],
                                                                           'competition': mock_request.form[
                                                                               'competition'],
                                                                           'club': mock_request.form['club'],
                                                                           'places': mock_request.form['places']})

    # Assert that the expected error message is present in the response
    assert "You can&#39;t book more places than you have!" in response.get_data(as_text=True)

