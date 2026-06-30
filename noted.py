#!/usr/bin/env python3
"""noted: a tiny notes CLI.

Subcommands live in the ``commands`` package and are auto-discovered, so each
command owns its own file. Shared note persistence lives in ``storage``.
"""
import argparse

from commands import register_all


def build_parser():
    parser = argparse.ArgumentParser(prog="noted", description="A tiny notes CLI.")
    sub = parser.add_subparsers(dest="command", required=True)
    register_all(sub)
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
