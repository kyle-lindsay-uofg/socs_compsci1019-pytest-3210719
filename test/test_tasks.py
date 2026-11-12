import pytest
from card_game.card.entity.PlayerType import USER, COMPUTER
from card_game.Player import create_player, HAND, SCORE, WINNER
from card_game.Game import clear_players, add_player, determine_winner, show_players
from card_game.card.game.TwentyOne.TwentyOne import score_hand, calculate_bust_probability
from card_game.LoadCSV import create_csv_reader


# Sub-task 1
def test_calculate_bust_probability():
    deck = ["H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK"]
    hand = ["H10", "D6"]

    assert calculate_bust_probability(hand, deck) == pytest.approx(0.667, abs=0.01)


# Sub-task 2
def test_create_csv_reader_invalid_path():
    with pytest.raises(IOError):
        create_csv_reader("does_not_exist.csv")

# Sub-task 3
@pytest.mark.parametrize("hand,expected_score", [(["H7", "D8"], 15), (["HJ", "SQ"], 20), (["HA", "D9"], 20), (["HA", "HJ", "D5"], 16), (["H10", "D8", "S5"], 0)])
def test_score_hand_combinations(hand, expected_score):
    assert score_hand(hand) == expected_score

# Sub-task 4
def test_display_player_console_output(capsys):
    clear_players()
    player = create_player(COMPUTER, "Bob")
    player[HAND] = ["H10", "S7"]
    player[SCORE] = 17
    add_player(player)
    show_players()
    output = capsys.readouterr()
    assert "Bob with score: 17" in output.out

# Sub-task 5
def test_create_csv_reader_valid_data(tmp_path):
    pass