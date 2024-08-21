from .location import Location
import json


def test_location(tmp_path):
    l = Location("https://www.google.com")
    l.name = "Google"
    l.type = "website"
    l.tags = ["search", "engine"]
    l.store(tmp_path)
    assert json.loads(
        (tmp_path / "ef7efc9839c3ee036f023e9635bc3b056d6ee2db.json").read_text()
    ) == {
        "description": "",
        "name": "Google",
        "tags": [
            "search",
            "engine",
        ],
        "type": "website",
        "url": "https://www.google.com",
    }

    assert l.__dict__ == list(Location.load_all(tmp_path))[0].__dict__
