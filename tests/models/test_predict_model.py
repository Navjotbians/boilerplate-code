from src.models.predict_model import load_data


def test_load_data():
    data = load_data()
    assert load_data() is not None
