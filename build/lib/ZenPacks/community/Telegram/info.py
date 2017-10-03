from zope.interface import implements

from Products.Zuul.infos.actions import ActionContentInfo
from Products.Zuul.infos.actions import ActionFieldProperty

from ZenPacks.community.Telegram.interfaces import ITelegramActionContentInfo


class TelegramActionContentInfo(ActionContentInfo):
    implements(ITelegramActionContentInfo)

    token = ActionFieldProperty(ITelegramActionContentInfo, 'token')
    chat_id = ActionFieldProperty(ITelegramActionContentInfo, 'chat_id')
    message_body = ActionFieldProperty(ITelegramActionContentInfo, 'message_body')
    message_clear = ActionFieldProperty(ITelegramActionContentInfo, 'message_clear')
