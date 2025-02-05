import subprocess
import sys

from oml_bluesky_plan_tester import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "oml_bluesky_plan_tester", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
