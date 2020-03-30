# -*- coding: UTF-8 -*-

import os
from abc import ABC
from argparse import ArgumentParser


class BaseCommand(ABC):
    def __init__(self):
        self.base_dir = os.getcwd()
        self.core_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def create_parser(self, prog_name, subcommand, **kwargs):
        pass
