if __name__ == "__main__":
    # defaultdict demo
    from collections import defaultdict

    dd1 = defaultdict()
    try:
        dd1["a"]
    except Exception as e:
        print(repr(e))

    dd2 = defaultdict(int)
    print(dd2["hello"])
