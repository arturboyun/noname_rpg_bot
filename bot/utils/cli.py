import asyncio
import logging
import os
import sys

import aiogram
import click
from bot.misc import start_pooling

logger = logging.getLogger("bot.utils.cli")


@click.group()
def cli():
    from bot import misc

    # from bot.utils import logging
    # logging.setup()
    asyncio.run(misc.setup())


@cli.command()
def version():
    """
    Get application version
    """
    click.echo(f'AIOGram: {aiogram.__version__}')
    click.echo(f'Bot API: {aiogram.__api_version__}')
    click.echo(f'Python: {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}')


@cli.command()
@click.option('--skip-updates', '-S', is_flag=True, default=False, help="Skip pending updates")
def start(skip_updates: bool):
    try:
        asyncio.run(start_pooling(skip_updates))
    except KeyboardInterrupt:
        logger.info("Bot stopped")
