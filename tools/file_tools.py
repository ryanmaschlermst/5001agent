import os


def read_files():

    contents = []

    for root, _, files in os.walk("."):

        for f in files:

            if f.endswith(".py"):

                path = os.path.join(root, f)

                try:
                    with open(path, "r", encoding="utf8") as fh:
                        contents.append(fh.read()[:200])
                except Exception:
                    pass

    return contents
