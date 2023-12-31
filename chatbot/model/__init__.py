import glob
from os.path import basename, dirname, isfile, join

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

# https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [
    basename(f)[:-3]
    for f in modules
    if isfile(f) and not f.endswith("__init__.py")  # pyright: ignore
]


class BaseSchema(DeclarativeBase, MappedAsDataclass, AsyncAttrs):
    pass
