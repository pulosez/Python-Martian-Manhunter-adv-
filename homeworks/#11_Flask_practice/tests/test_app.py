from config import Config


class MockResponse:
    def __init__(self, *args, **kwargs):
        self.ok = True
        self.status_code = 200
        self.json_data = {"message": "accurate", "cod": "200", "count": 1, "list": [
            {"id": 702550, "name": "Lviv", "coord": {"lat": 49.8383, "lon": 24.0232},
             "main": {"temp": 284.95, "feels_like": 284.8, "temp_min": 283.71, "temp_max": 285.93, "pressure": 1015,
                      "humidity": 100}, "dt": 1623452950, "wind": {"speed": 1, "deg": 160},
             "sys": {"country": "UA"}, "rain": None, "snow": None, "clouds": {"all": 24},
             "weather": [{"id": 801, "main": "Clouds", "description": "few clouds", "icon": "02n"}]}]}

    def json(self):
        return self.json_data


def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200


def test_search_weather(client):
    Config.WEATHER_API_KEY = "53493f042amsh58b54fe3ed83e24p195f98jsnf109acbc59d2"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    response = client.post("/search", data={"cities": "london"})
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for London" in response.data


def test_mock_search_weather(client, mocker):
    mocker.patch('requests.request', side_effect=MockResponse)
    response = client.post("/search", data={"cities": "london"})
    print(response)
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for Lviv" in response.data
