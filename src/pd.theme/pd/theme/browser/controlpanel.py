from plone.app.registry.browser import controlpanel

from pd.theme.browser.interfaces import ITwitterSettings

class TwitterSettingsEditForm(controlpanel.RegistryEditForm):

    schema = ITwitterSettings
    label = (u'Twitter settings')
    description = u'Lets you configure your Twitter settings.'


class TwitterControlPanel(controlpanel.ControlPanelFormWrapper):
    """Twitter control panel view"""

    form = TwitterSettingsEditForm
