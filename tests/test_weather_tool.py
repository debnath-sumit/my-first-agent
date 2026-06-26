from src.tools.weather_tool import get_weather

def test_get_weather_returns_expected_fields():
    weather = get_weather("Dallas")

    assert weather is not None
    assert "temperature" in weather
    assert "condition" in weather
    assert "humidity" in weather