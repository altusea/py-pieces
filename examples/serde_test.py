import orjson
from utils.model import Point

p1 = Point(1, 2)
json_str = orjson.dumps(p1)
print(json_str)
p2 = orjson.loads(json_str)
print(p2)
