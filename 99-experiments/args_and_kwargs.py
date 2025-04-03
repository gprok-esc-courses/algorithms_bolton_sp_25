
def test(a, *args, **kwargs):
    print("A:", a)
    print("ARGS:", args)
    print("KWARGS:", kwargs)


print("Just fixed params")
test(5)
print("With args")
test(5, 6, 7, 8)

print("With kwargs")
test(5, user="mary", amount=800)
print("With all")
test(5, 8, 6, "xyx", False, user="john", amount=1000, product="Mouse")