import os

POEM = """Spare Key

I asked to borrow it.
You pressed it in my palm,
still warm from your pocket.

All night I kept a door
I was allowed to open
and didn't.

That is what you gave me:
not the house.
The choice
to leave it yours."""

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(POEM)
