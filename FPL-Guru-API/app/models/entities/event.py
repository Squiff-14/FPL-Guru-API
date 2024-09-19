from typing import List, Optional
from pydantic import BaseModel
from .chip_play import ChipPlay
from .top_element_info import TopElementInfo

class Event(BaseModel):
    id: int
    name: str
    deadline_time: str
    average_entry_score: int
    finished: bool
    data_checked: bool
    highest_scoring_entry: Optional[int]
    deadline_time_epoch: int
    deadline_time_game_offset: int
    highest_score: Optional[int]
    is_previous: bool
    is_current: bool
    is_next: bool
    chip_plays: List[ChipPlay]
    most_selected: Optional[int]
    most_transferred_in: Optional[int]
    top_element: Optional[int]
    top_element_info: Optional[TopElementInfo]
    transfers_made: int
    most_captained: Optional[int]
    most_vice_captained: Optional[int]
