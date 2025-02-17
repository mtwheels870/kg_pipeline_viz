from spacy.cli.project.run import project_run
from spacy.cli.project.assets import project_assets
from pathlib import Path


def test_rel_project():
    root = Path(__file__).parent
    project_assets(root)
    print(f"project_run(), ...")
    project_run(root, "all", capture=True)
