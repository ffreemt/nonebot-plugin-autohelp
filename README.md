# nonebot_plugin_autohelp
[![tests](https://github.com/ffreemt/nonebot-plugin-autohelp/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/nonebot-plugin-autohelp/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/nonebot_plugin_autohelp.svg)](https://badge.fury.io/py/nonebot_plugin_autohelp)

Show a summary of names, aliases and usages for plugins loaded

## Dependent adapter
`cqhttp`

## Install it

```shell
pip install nonebot_plugin_autohelp
# or poetry add nonebot_plugin_autohelp
# pip install git+htts://github.com/ffreemt/nonebot_plugin_autohelp
# poetry add git+htts://github.com/ffreemt/nonebot_plugin_autohelp

# To upgrade
pip install nonebot_plugin_autohelp -U
# or poetry add nonebot_plugin_autohelp@latest
```

## Use it
```python
# bot.py
import nonebot
...
nonebot.init()

driver = nonebot.get_driver()

driver.register_adapter("cqhttp", CQHTTPBot)

nonebot.load_from_toml("pyproject.toml")
nonebot.load_plugin("nonebot_plugin_guess")

nonebot.load_plugin("nonebot_plugin_autohelp")

# plugin loaded after autohelp will not be taken care of by autohelp
nonebot.load_plugin("nonebot_plugin_fancy")

```
