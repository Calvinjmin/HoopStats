import pytest
import pandas as pd
from bs4 import BeautifulSoup
from hoopstats import create_pd_data_frame_from_html

# Sample HTML content for testing
mock_html_content = """
<html>
    <body>
        <table id="test_table">
            <tr><th>Column1</th><th>Column2</th></tr>
            <tr><td>1</td><td>2</td></tr>
            <tr><td>3</td><td>4</td></tr>
        </table>
    </body>
</html>
"""

mock_html_empty_content = "<html><body>No table here</body></html>"


def mock_read_html(*args, **kwargs):
    return [pd.DataFrame({"Column1": [1, 3], "Column2": [2, 4]})]


class MockBeautifulSoup:
    def __init__(self, html_content, parser):
        self.html_content = html_content
        self.parser = parser

    def find(self, tag, attrs):
        if tag == "table" and attrs.get("id") == "test_table":
            return BeautifulSoup(mock_html_content, "html.parser").find(
                "table", {"id": "test_table"}
            )
        return None


def test_create_pd_data_frame_from_html(monkeypatch):
    # Patch BeautifulSoup in the hoopstats module
    monkeypatch.setattr("hoopstats.utils.pandas_utils.BeautifulSoup", MockBeautifulSoup)
    monkeypatch.setattr(pd, "read_html", mock_read_html)

    # Call the function with mock data
    df = create_pd_data_frame_from_html(mock_html_content, "test_table")

    # Expected DataFrame
    expected_df = pd.DataFrame({"Column1": [1, 3], "Column2": [2, 4]})
    pd.testing.assert_frame_equal(df, expected_df)


def test_create_pd_data_frame_from_html_no_table(monkeypatch):
    # Mock BeautifulSoup to return no table
    class MockBeautifulSoupNoTable:
        def __init__(self, html_content, parser):
            self.html_content = html_content
            self.parser = parser

        def find(self, tag, attrs):
            return None

    # Patch BeautifulSoup in the hoopstats module
    monkeypatch.setattr(
        "hoopstats.utils.pandas_utils.BeautifulSoup", MockBeautifulSoupNoTable
    )
    monkeypatch.setattr(pd, "read_html", mock_read_html)

    # Call the function and expect it to raise a ValueError
    with pytest.raises(ValueError):
        create_pd_data_frame_from_html(mock_html_empty_content, "test_table")
