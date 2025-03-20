
def test(a, *args, **kwargs):
    print("A:", a)
    print("ARGS:", args)
    print("KWARGS:", kwargs)


test(5, 8, 6, "xyx", False, user="john", amount=1000, product="Mouse")