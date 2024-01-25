from unittest.mock import patch
from app.server import app

def test_point_update_not_reflected():
    # Create a test request context for the '/purchasePlaces' endpoint
    with app.test_request_context('/purchasePlaces'):

        # Mock the 'clubs' data to simulate a club with initial points
        with patch('app.server.clubs', [{'name': 'Simply Lift', 'points': '10'}]):

            # Mock the 'competitions' data to simulate a competition with available places
            with patch('app.server.competitions', [{"name": "Spring Festival", "date": "2020-03-27 10:00:00",
                                                    "numberOfPlaces": "25"}]):

                # Mock the request form data with a valid booking attempt
                with patch('app.server.request') as mock_request:
                    mock_request.form = {'points': '0', 'competition': 'Spring Festival', 'club': 'Simply Lift',
                                         'places': '4'}

                    # Simulate the POST request to '/purchasePlaces'
                    response = app.test_client().post('/purchasePlaces', data={'points': mock_request.form['points'],
                                                                               'competition': mock_request.form[
                                                                                   'competition'],
                                                                               'club': mock_request.form['club'],
                                                                               'places': mock_request.form['places']})

    # Assert that the expected updated points message is present in the response
    assert "Points available: 6" in response.get_data(as_text=True)
