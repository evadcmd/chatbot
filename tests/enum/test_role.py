from chatbot.enum.role import Role


def test_role():
    assert Role.ROOT > Role.ADMIN
