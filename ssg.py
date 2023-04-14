import ssg.parsers
import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    """Captures command line arguments: Kwargs:
        source: default is 'content'
        dest: default is 'dist' """
    config = {
        "source": source, "dest": dest,
        "parsers": [ssg.parsers.ResourceParser()]
    }
    Site(**config).build()


typer.run(main)
