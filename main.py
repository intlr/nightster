"""
Basic proof of concept, we demonstrate it is possible to move a file
using Python and Docker volumes.

To keep it simple, we hard coded the file to be moved as well as the
directory where the file will be moved. We also don't test if a file at
the location already exists.

Read the README.md documentation to learn more about how to build and
run the Docker image.
"""

from os.path import exists
from pathlib import PurePath
from shutil import move

if __name__ == '__main__':
	_FILE = 'foo.txt'
	_DIR_ARCHIVE = './archive'

	if not exists(_DIR_ARCHIVE):
		print(f'Archive directory {_DIR_ARCHIVE} missing')
		exit(1)

	if exists(_FILE):
		new_path = PurePath(f'{_DIR_ARCHIVE}/{_FILE}')
		move(_FILE, new_path)
		print(f'File {_FILE} moved to {new_path}')
	else:
		print(f'File {_FILE} missing')
		exit(1)
