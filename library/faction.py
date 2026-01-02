from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Faction:
    """Defines a faction."""

    hostile: set[str] = field(default_factory=set)
    """Factions hostile to this faction."""
    spawn_bias: tuple[float, float] | None = None
    """Spawn bias on the grid, for example (0.5, 0.8) being lower-center.
    If None, can spawn anywhere."""
    relative_firepower: float = 1.0
    """Relative firepower of the faction squad. 1.0 is baseline and default."""
    can_loot: bool = False
    """Determines if this faction can loot bodies."""
    can_gain_exp: bool = False
    """Determines if actors of this faction can gain exp."""
    can_trade: bool = False
    """Determines if actors of this faction will visit traders."""
    can_hunt_artifacts: bool = False
    """Determines if actors of this faction will hunt for artifacts."""
    can_hunt_squads: bool = False
    """Determines if actors of this faction will take bounties on other squads."""
