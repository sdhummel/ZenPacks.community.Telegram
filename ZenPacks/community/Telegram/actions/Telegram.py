from zope.interface import implements
from Products.ZenModel.actions import IActionBase, TargetableAction
from Products.ZenModel.interfaces import IAction
from Products.ZenUtils.guid.guid import GUIDManager
from Products.ZenModel.actions import processTalSource, _signalToContextDict
from ZenPacks.community.Telegram.interfaces import ITelegramActionContentInfo
from ZenPacks.community.Telegram.lib.botapi import TelegramBot

import logging
log = logging.getLogger("zen.useraction.actions")


class TelegramAction(IActionBase, TargetableAction):
    implements(IAction)

    id = 'Telegram'
    name = 'Telegram'
    actionContentInfo = ITelegramActionContentInfo

    def __init__(self):
        super(TelegramAction, self).__init__()

    def setupAction(self, dmd):
        self.guidManager = GUIDManager(dmd)

    def execute(self, notification, signal):
        log.debug("Executing %s action", self.name)
        self.setupAction(notification.dmd)

        data = _signalToContextDict(
            signal,
            self.options.get('zopeurl'),
            notification,
            self.guidManager
        )

        bot = TelegramBot(notification.content['token'])
        bot.update_bot_info().wait()

        if signal.clear:
            text = processTalSource(notification.content['message_clear'], **data)

        else:
            text = processTalSource(notification.content['message_body'], **data)

        bot.send_message(notification.content['chat_id'], text, parse_mode="Markdown").wait()
        print
