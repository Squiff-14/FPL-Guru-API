from typing import List, Optional

from pydantic import BaseModel

class PlayerComparison(BaseModel):
    player_name: str
    cost_comparison: Optional[str]
    cost_difference: Optional[float]
    points_per_game_comparison: Optional[str]
    points_per_game_difference: Optional[float]
    goals_scored_comparison: Optional[str]
    goals_scored_difference: Optional[int]
    assists_comparison: Optional[str]
    assists_difference: Optional[int]
    influence_comparison: Optional[str]
    influence_difference: Optional[float]
    creativity_comparison: Optional[str]
    creativity_difference: Optional[float]
    threat_comparison: Optional[str]
    threat_difference: Optional[float]
    total_points_comparison: Optional[str]
    total_points_difference: Optional[int]
    value_for_money_comparison: Optional[str]
    value_for_money_difference: Optional[float]
    
class ComparisonSummary(BaseModel):
    better_player: str
    reasoning: str
    
class PlayerComparisonResult(BaseModel):
    comparison_summary: ComparisonSummary
    detailed_comparison: List[PlayerComparison]