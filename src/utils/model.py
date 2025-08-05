from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


if __name__ == "__main__":
    p = Point(1, 2)
    print(p)
