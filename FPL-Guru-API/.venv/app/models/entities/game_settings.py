from pydantic import BaseModel
from typing import List, Optional

class GameSettings(BaseModel):
    league_join_private_max: int
    league_join_public_max: int
    league_max_size_public_classic: int
    league_max_size_public_h2h: int
    league_max_size_private_h2h: int
    league_max_ko_rounds_private_h2h: int
    league_prefix_public: str
    league_points_h2h_win: int
    league_points_h2h_lose: int
    league_points_h2h_draw: int
    league_ko_first_instead_of_random: bool
    cup_start_event_id: Optional[int]
    cup_stop_event_id: Optional[int]
    cup_qualifying_method: Optional[str]
    cup_type: Optional[str]
    featured_entries: List[str]  # Assuming it's a list of strings, adjust if needed
    percentile_ranks: List[int]
    squad_squadplay: int
    squad_squadsize: int
    squad_team_limit: int
    squad_total_spend: int
    ui_currency_multiplier: int
    ui_use_special_shirts: bool
    ui_special_shirt_exclusions: List[str]  # Adjust if necessary
    stats_form_days: int
    sys_vice_captain_enabled: bool
    transfers_cap: int
    transfers_sell_on_fee: float
    max_extra_free_transfers: int
    league_h2h_tiebreak_stats: List[str]
    timezone: str
