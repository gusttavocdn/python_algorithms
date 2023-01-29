from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("33231", "dasdsa")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 2321)

    assert encrypt_message("Naruto", 9) == "oturaN"
    assert encrypt_message("Naruto", 5) == "turaN_o"
    assert encrypt_message("Naruto", 4) == "ot_uraN"
