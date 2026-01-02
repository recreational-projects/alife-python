import pytest

from library import MapGrid, Squad


def test_grid_logger(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr('library.grid.SHOW_GRID', True)

    grid = MapGrid()
    grid.add_log_msg("INFO", "test")

    assert len(grid._msg_log) == 1, "Message should be added to the message log"
    assert grid._msg_log.pop() == "\x1b[37m[INFO]\x1b[39m TEST", "Message in the log should be correctly formatted"

    grid.add_log_msg("CMBT", "test combat", (1, 3))
    assert len(grid._msg_log) == 1, "Message should be added to the message log"
    assert grid._msg_log.pop() == "\x1b[31m[CMBT]\x1b[39m [SQUARE=(1, 3)] TEST COMBAT", "Message should be correctly formatted"


def test_grid_spawner() -> None:
    grid = MapGrid()
    grid.spawn("stalker", (5, 33))

    assert len(grid.squares.keys()) == 1, "Only one square should be populated"
    assert (5, 33) in grid.squares, "Entity should be spawned at the expected square"

    entities = grid.squares[(5, 33)]
    assert len(entities[0]) == 1, "Only one entity should spawn"

    squad = entities[0][0]
    assert isinstance(squad, Squad), "Should be correct entity object"
    assert squad.faction == "stalker", "Entity should have correct faction set"
    assert squad.location == (5, 33), "Entity should have correct location set"


def test_grid_remove() -> None:
    grid = MapGrid()
    grid.spawn("stalker", (4, 22))

    squad = grid.squares[(4, 22)][0][0]
    grid.remove(squad)
    grid.cleanup()

    assert (4, 22) not in grid.squares, "Square should be removed from the grid"


def test_grid_place() -> None:
    grid = MapGrid()
    squad = Squad(faction="stalker", location=(0, 0))
    grid.place(squad, (3, 26))

    assert (3, 26) in grid.squares, "Square should be added to the grid"
    assert grid.squares[(3, 26)][0][0] is squad, "Square should contain correct entity"
