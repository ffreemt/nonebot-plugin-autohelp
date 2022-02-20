# nonebot-plugin-autohelp
[![nonebot2beta](https://img.shields.io/static/v1?label=nonebot&message=v2b2&color=green)](https://v2.nonebot.dev/)[![onebot](https://img.shields.io/static/v1?label=driver&message=onebot&color=green)](https://adapter-onebot.netlify.app/)[![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/nonebot_plugin_autohelp.svg)](https://badge.fury.io/py/nonebot_plugin_autohelp)

Show a summary of commands, aliases and usages for plugins loaded

## Dependent adapter
`onebotv11`

## Install it

```shell
pip install nonebot-plugin-autohelp
# or poetry add nonebot-plugin-autohelp
# pip install git+htts://github.com/ffreemt/nonebot-plugin-autohelp
# poetry add git+htts://github.com/ffreemt/nonebot-plugin-autohelp

# To upgrade
pip install nonebot-plugin-autohelp -U
# or poetry add nonebot-plugin-autohelp@latest
```

## Use it
```python
# bot.py
import nonebot
from nonebot.adapters.onebot.v11 import Adapter
...
nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(Adapter)

nonebot.load_from_toml("pyproject.toml")
nonebot.load_builtin_plugin("echo")
nonebot.load_plugin("nonebot_plugin_guess")

nonebot.load_plugin("nonebot_plugin_autohelp")

# plugin loaded after autohelp will not be taken care of by autohelp
nonebot.load_plugin("nonebot_plugin_fancy")

```

Sample session in a qq group
```bash
mu (μ)(41947782)  11:23:34 AM
help
mubot(2129462094)  11:23:36 AM
nickname:
command_start: /
command_sep: .

command: say
command: mecho
	aliases: ping, ryt, 在不, p

command: news
	aliases: xinwen, 新闻, 无聊

command: debug test: %s
	aliases: 爬, fetch, crawl

command: guess
	aliases: cai, 猜猜看, 猜

(help -d will display detailed docs for all plugins loaded before nonebot_plugin_autohelp)

mu (μ)(41947782)  11:53:25 AM
help -h
mubot(2129462094)  11:53:27 AM
usage: help [-h] [-d] [params [params ...]]

positional arguments:
  params         list of parameters of type str (default: None)

optional arguments:
  -h, --help     show this help message and exit
  -d, --details  show __doc__ for each plugin (default: False)
---

mu (μ)(41947782)  11:23:34 AM
help --details  # or help details
...(attach __doc___ for each plugin, ommitted)
```

