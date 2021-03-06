from .i18n import MessageFactory as _
from .interfaces import IGlobalSettings
from plone.app.registry.browser import controlpanel
from plone.z3cform import layout
from z3c.form import field


class ControlPanelEditForm(controlpanel.RegistryEditForm):
    schema = IGlobalSettings
    fields = field.Fields(IGlobalSettings)

    label = _(u"Configure panels")
    description = _(
        u"This form lets you configure the panel add-on product."
    )


ControlPanel = layout.wrap_form(
    ControlPanelEditForm,
    controlpanel.ControlPanelFormWrapper
)
