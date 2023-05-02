from src.features.build_features import hello_members


def test_hello_member():
    assert hello_members() is None
