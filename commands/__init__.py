"""Command auto-discovery.

Each module in this package is a self-contained subcommand that exposes a
``register(subparsers)`` function. Commands are discovered at runtime, so adding
a new subcommand means adding one new file here — no edits to any shared file.
"""
import importlib
import pkgutil


def iter_command_modules():
    for info in sorted(pkgutil.iter_modules(__path__), key=lambda i: i.name):
        yield importlib.import_module(f"{__name__}.{info.name}")


def register_all(subparsers):
    for mod in iter_command_modules():
        register = getattr(mod, "register", None)
        if register is not None:
            register(subparsers)
