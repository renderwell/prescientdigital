from zope.interface import Interface
from zope import schema

class IThemeSpecific(Interface):
    """A layer specific to my product        """

class ITwitterPortletFixLayer(Interface):
    """Marker interface that defines a Zope 3 browser layer."""


class ITwitterSettings(Interface):
    """Twitter settings."""

    consumer_key = schema.TextLine(
        title=u'Consumer key',
    )

    consumer_secret = schema.TextLine(
        title=u'Consumer secret'
    )

    access_token = schema.TextLine(
        title=u'Access token'
    )

    access_token_secret = schema.TextLine(
        title=u'Access token secret'
    )
