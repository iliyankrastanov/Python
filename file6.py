# %%
s1 = 'Hello'
s2 = 'Hello'

id(s1) == id (s2)
# %%
s1 = 'Hello'
s2 = 'hello'

id(s1) == id (s2)
# %%
class Point:

    def __init__(self,x):
        self.x = x
# %%
p1 = Point(x = 10)
p2 = Point(x = 10)

id(p1) == id(p2)


# %%
type(p1)
type(p2)
# %%
id(p1.x) == id(p2.x)
# %%
s1 = 'Hello' * 1000
s2 = 'Hello' * 1000

id(s1) == id (s2)
# %%
