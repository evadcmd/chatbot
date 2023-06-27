import glob
from os.path import basename, dirname, isfile, join


# https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder
def test_import():
    modules = glob.glob(join(dirname(__file__), "*.py"))
    files = [
        basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")
    ]
    for file in files:
        print(file)


if __name__ == "__main__":
    test_import()
