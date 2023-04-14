from pathlib import Path  # subclass of Pure Path: concrete Path; are some methods like running commands in cmd


class Site:

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        # second part of path is relative to self.source so pass in self.source to a Path method
        # relative_to: PASS IN a path and hcecl if that path is PART OF the path that CALLED the method
        directory = self.dest / path.relative_to(self.source)
        # creating directory at given path; how does directory reference to a path object?
        # What are parents? What does it mean "missing parents"? What are default permissions?
        # What is the last path compenent? Last of the path? It still creates the directory if the error is ignored?
        # Why would it not be ignored if the component is an existing non-direcotry file?
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        # will self.source also be a directory?
        self.dest.mkdir(parents=True, exist_ok=True)
        # r stands for recursive? it finds the pattern in the directory and subdirectories too;is it a form of regex?
        for path in self.source.rglob("*"):
            # if the path points to a directory or if is a symbolic link pointing to a directory
            if path.is_dir():
                self.create_dir(path)
