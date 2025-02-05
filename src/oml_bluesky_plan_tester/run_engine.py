import time

from bluesky.run_engine import RunEngine


def get_run_engine() -> RunEngine:
    """Instantiates RunEngine and check its running.

    Returns:
        A running RunEngine"""
    RE = RunEngine()
    # As in dodal conftest
    timeout = time.monotonic()
    while not RE.loop.is_running():
        time.sleep(0)
        if time.monotonic() > timeout:
            raise TimeoutError("This really shouldn't happen but just in case")

    return RE
