# The parentheses around a named expression used as a with item can't be removed,
# even when it has more than one pair.
with ((item := 10)):
    pass
with (((item := 10))):
    pass
with ((a := b)), c:
    pass
with c, ((a := b)):
    pass
with ((a := b)) as c:
    pass
with ((a := open(f))) as b, ((c := open(g))) as d:
    pass


async def f():
    async with ((a := b)):
        pass

# output
# The parentheses around a named expression used as a with item can't be removed,
# even when it has more than one pair.
with (item := 10):
    pass
with (item := 10):
    pass
with (a := b), c:
    pass
with c, (a := b):
    pass
with ((a := b)) as c:
    pass
with ((a := open(f))) as b, ((c := open(g))) as d:
    pass


async def f():
    async with (a := b):
        pass
