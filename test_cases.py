import pytest
import requests
from sort_list import bubble_sort
from stack import CustomStack
from weather_fetcher import fetch_weather_data
from unittest.mock import patch, mock_open, call
from title_scraper import save_titles_to_file, read_from_file

# Bubble Sort Testing
def test_bubble_sort():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]
    assert bubble_sort([1]) == [1]
    assert bubble_sort([]) == []

# CustomStack Testing
def test_custom_stack():
    stack = CustomStack()
    assert stack.is_empty() == True
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.peek() == 30
    
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.pop() == None
    
    assert stack.is_empty() == True

# Weather Fetcher Testing
def test_fetch_weather_data(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data):
                self.json_data = json_data
            def raise_for_status(self):
                pass
            def json(self):
                return self.json_data
        return MockResponse({"main": {"temp": 20, "humidity": 50}, "weather": [{"description": "clear sky"}], "cod": 200})
    
    monkeypatch.setattr(requests, "get", mock_get)
    data = fetch_weather_data("http://api.openweathermap.org/data/2.5/weather?", "Lahore", "1517ed8b6e93dae5197a90c3e4754de1")
    assert data == {'temperature': 20, 'humidity': 50, 'weather_description': 'clear sky'}

# Test save_titles_to_file function
def test_save_titles_to_file():
    mock_titles = ["Title 1", "Title 2", "Title 3", "Title 4"]
    mock_file = mock_open()
    
    with patch("builtins.open", mock_file):
        save_titles_to_file(mock_titles, "titles.txt")
    
    mock_file.assert_called_once_with("titles.txt", "w")
    mock_file().write.assert_has_calls([call("Title 1\n"), call("Title 2\n"), call("Title 3\n"), call("Title 4\n")])

# Test read_from_file function
def test_read_from_file():
    mock_file_content = "Title 1\nTitle 2\nTitle 3\nTitle 4\n"
    mock_file = mock_open(read_data=mock_file_content)
    
    with patch("builtins.open", mock_file):
        titles = read_from_file()
    
    mock_file.assert_called_once_with("titles.txt", "r")
    assert titles == ["Title 1", "Title 2", "Title 3", "Title 4"]

# Additional tests for error handling and edge cases
def test_bubble_sort_edge_cases():
    assert bubble_sort([-1, -3, -2, -5]) == [-5, -3, -2, -1]
    assert bubble_sort([1, 2, 2, 1]) == [1, 1, 2, 2]

def test_custom_stack_edge_cases():
    stack = CustomStack()
    assert stack.pop() == None
    stack.push(None)
    assert stack.pop() == None

def test_fetch_weather_data_error_handling(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code):
                self.status_code = status_code
            def raise_for_status(self):
                if self.status_code != 200:
                    raise requests.exceptions.HTTPError(f"{self.status_code} Error")
            def json(self):
                return {}
        return MockResponse(404)
    
    monkeypatch.setattr(requests, "get", mock_get)
    data = fetch_weather_data("http://api.openweathermap.org/data/2.5/weather?", "InvalidCity", "invalidapikey")
    assert data == {"error": "HTTP Error: 404 Error"}
