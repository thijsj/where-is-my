import json
import hashlib


class Location:
    def __init__(self, url):
        self.name = ""
        self.url = url
        self.type = ""
        self.tags = []
        self.description = ""

    def store(self, path):
        id = hashlib.sha1(self.url.encode("utf-8")).hexdigest()
        with (path / f"{id}.json").open("w") as f:
            json.dump(self.__dict__, f)

    @classmethod
    def load_all(cls, path):
        for p in path.glob("*.json"):
            with p.open() as f:
                d = json.load(f)
                r = cls(d["url"])
                r.__dict__.update(d)
                yield r
