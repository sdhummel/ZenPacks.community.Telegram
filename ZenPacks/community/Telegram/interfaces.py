from zope.interface import Interface
from Products.Zuul.interfaces.actions import IActionContentInfo
from Products.Zuul.interfaces import IFacade
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t
import textwrap

class ITelegramActionContentInfo(IActionContentInfo):
    token = schema.TextLine(
        title = _t(u'Telegram Bot Token'),
        order=90,
    )
    chat_id = schema.TextLine(
        title = _t(u'Telegram Chat ID'),
        order=100,
    )

    message_body = schema.Text(
        title = _t(u'Message Body'),
        description = _t(u'The content of the Telegram message'),
        order = 110,
        default = textwrap.dedent(text = u'''
            Device: ${evt/device}
            Component: ${evt/component}
            Severity: ${evt/severity}
            Time: ${evt/lastTime}
            Message:
            ${evt/message}
            ''')
    )

    message_clear = schema.Text(
        title = _t(u'Clear Message Body'),
        description = _t(u'The content of the Telegram Clear message'),
        order = 120,
        default = textwrap.dedent(text = u'''
            Event: ${evt/summary}
            Cleared by: ${evt/clearid}
            At: ${evt/stateChange}
            Component: ${evt/component}
            Severity: ${evt/severity}
            Device: ${evt/device}
            Message:
            ${evt/message}
            ''')    
    )