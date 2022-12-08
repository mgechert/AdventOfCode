from typing import List, Tuple

# Advent of Code Day 7 solution code


class FileSystem:
    def __init__(self) -> None:
        self.root = {'.': '/'}
        self.current_directory = self.root

    def mkdir(self, dir_name: str) -> None:
        """
        Create new directory inside the current one with
        a link to its parent.
        """
        if dir_name not in self.current_directory:
            self.current_directory[dir_name] = {
                '.': dir_name,
                '..': self.current_directory
            }
        else:
            raise FileExistsError(f"Directory {dir_name} already exists.")

    def cd(self, dir_name: str) -> None:
        """
        Change the current directory to dir_name
        """
        if dir_name in self.current_directory:
            self.current_directory = self.current_directory[dir_name]
        elif dir_name == '/':
            self.current_directory = self.root
        else:
            raise FileNotFoundError(f"Directory {dir_name} does not exist.")

    def touch(self, file_name: str, file_size: int) -> None:
        """
        Creates a file entry in cwd with the specified size
        """
        if file_name not in self.current_directory:
            self.current_directory[file_name] = file_size
        else:
            raise FileExistsError(f"File {file_name} already exists.")

    def get_dir_catalog(self, dir=None) -> List[Tuple[str, int]]:
        """
        Recursively builds a catalog of every directory and its size.
        Returns a list of tuples of (name, size)
        """
        # If no object to size, size from the root
        if not dir:
            dir = self.root

        this_dir_name = dir['.']
        this_dir_size = 0
        subdir_catalog = []

        for obj_name, data in dir.items():
            if type(data) is int:
                # item is a file
                this_dir_size += data
            elif not obj_name.startswith('.'):
                # item is a dir, skipping . and ..
                subdir = self.get_dir_catalog(dir=data)
                subdir_catalog += subdir

                # Only add the child's size to not double-count nested subdirs
                this_dir_size += subdir[0][1]

        return [(this_dir_name, this_dir_size)] + subdir_catalog


def build_fs_from_terminal(inputs: List[str]) -> None:
    """
    Driver function to create a FileSystem object based on terminal session
    (ie, parses the puzzle input)
    """
    fs = FileSystem()

    line = 0

    while line < len(inputs):
        if inputs[line].startswith('$ cd'):
            # Change into directory, create if it doesn't exist
            dir_name = inputs[line][4:].strip()
            fs.cd(dir_name)
            line += 1
        elif inputs[line].startswith('$ ls'):
            # Read the output of ls until we hit the next command
            # and insert those files in the cwd
            line += 1
            while line < len(inputs) and not inputs[line].startswith('$'):
                metadata, obj_name = inputs[line].split()
                if metadata != 'dir':
                    fs.touch(file_name=obj_name, file_size=int(metadata))
                else:
                    fs.mkdir(dir_name=obj_name)
                line += 1

    fs.cd('/')

    return fs
