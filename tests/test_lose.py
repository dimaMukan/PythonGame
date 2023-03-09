from lab_1.lab_1 import lose, is_win, win_mes

def test_lose_message():
    assert lose() == "YOU LOSE!"

def test_is_win():
    assert is_win(3, 3) == False

def test_win_mes():
    assert win_mes(1, 3) == "You WIN!"
