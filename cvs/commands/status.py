from cvs import Command
from pathlib import Path
import logging
import os


class Status(Command):
    """
    Shows the current status of repository
    """
    def run(self) -> None:
        branch = self.get_branch()
        logging.info(f'Current branch: {branch.name}')
        for directory, _, files in os.walk(self.system.directory):
            for file in files:
                full_path = Path(directory) / file
                relative_path = full_path.relative_to(self.system.directory)
                if str(relative_path) not in branch.source.keys():
                    if not self.system.is_in_cvsignore(relative_path):
                        logging.info(f'New file: {relative_path}')
                elif self.is_file_modified(branch, full_path):
                    logging.info(f'File {relative_path} was modified')

    def set_parser(self, subparsers_list) -> None:
        parser = subparsers_list.add_parser('status')
        parser.set_defaults(command=Status)
        parser.add_argument('-b', '--branch', help='Branch name')
