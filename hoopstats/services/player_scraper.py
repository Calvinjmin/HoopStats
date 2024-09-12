import pandas as pd

from typing import Optional
from ..utils.request_utils import get_wrapper
from ..utils.players_utils import create_player_suffix
from ..utils.pandas_utils import create_pd_data_frame_from_html


class PlayerScraper:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.suffix = create_player_suffix(first_name, last_name, "01")
        self.url = f"https://www.basketball-reference.com/players/{self.suffix}"

    def get_stats_by_year(self, stat_type: str = "per_game") -> Optional[pd.DataFrame]:
        """
        This function web scraps a player's aggregate stats group by the year

        Args:
            stat_type (str, optional): 'per_game' 'totals' and 'advanced' are viable options. Defaults to "per_game".

        Returns:
            Optional[pd.DataFrame]: Pandas Data Frame
        """
        if stat_type not in ["per_game", "totals", "advanced"]:
            print(f"Invalid stat type: {stat_type}")
            return None

        try:
            r = get_wrapper(self.url + ".html")
            if r:
                return create_pd_data_frame_from_html(r.content, stat_type)
        except Exception as e:
            print(f"Error fetching stats: {e}")
            return None

    def get_game_log_by_year(self, year: int) -> Optional[pd.DataFrame]:
        """
        This function web scraps a player's game log based on the year

        Args:
            year (int): numerical value that represents a year

        Returns:
            Optional[pd.DataFrame]: Pandas Data Frame
        """
        try:
            r = get_wrapper(f"{self.url}/gamelog/{year}")
            if r:
                return create_pd_data_frame_from_html(r.content, "pgl_basic")
            else:
                print(f"Failed to retrieve game log for {year}")
                return None
        except Exception as e:
            print(f"Error fetching game log: {e} - Maybe an invalid year - {year}")
            return None
