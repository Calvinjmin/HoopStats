import pandas as pd

from ..utils.request_utils import get_wrapper
from ..utils.pandas_utils import create_pd_data_frame_from_html
from ..utils.team_utils import TEAM_ABBREVIATIONS


class TeamScraper:
    def __init__(self, team_name) -> None:
        self.team_name = team_name
        self.abbreviation = TEAM_ABBREVIATIONS[self.team_name]
        self.url = f"https://www.basketball-reference.com/teams/{self.abbreviation}"

    def team_stats_by_year(self, table_type: str, year: int) -> pd.DataFrame:
        """
        Given a dynamic variable, compute a pandas Data Frame for a given team

        Args:
            table_type (str): table type associated on the website 
            year (int): year 

        Returns:
            pd.DataFrame: Pandas DataFrame 
        """
        
        # Valid Stat Options
        valid_stats = ["roster"]
        if table_type not in valid_stats:
            print(f"Input was an invalid stat. Try one of these: {valid_stats}")
            return None

        try:
            r = get_wrapper(f"{self.url}/{year}.html")
            if r:
                return create_pd_data_frame_from_html(r.content, table_type)
            else:
                print(f"Failed to retrieve game log for {year}")
                return None
        except Exception as e:
            print(f"Error fetching game log: {e}")
            return None
