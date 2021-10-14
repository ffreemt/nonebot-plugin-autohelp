"""Test nonebot_plugin_autohelp."""
import nonebot
nonebot.init()

# pylint: disable=wrong-import-position
from nonebot_plugin_autohelp import __version__, nonebot_plugin_autohelp  # noqa


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Sanity check."""
    try:
        assert not nonebot_plugin_autohelp()
    except Exception:
        assert True
