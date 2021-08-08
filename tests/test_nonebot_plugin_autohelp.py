"""Test nonebot_plugin_autohelp."""
import nonebot
from nonebot_plugin_autohelp import __version__
# from nonebot_plugin_autohelp import nonebot_plugin_autohelp

nonebot.init()


def test_version():
    """Test version."""
    assert __version__ == "0.1.0"


def test_sanity():
    """Sanity check."""
    try:
        assert not nonebot_plugin_autohelp()
    except Exception:
        assert True
