# -*- coding: utf-8 -*-
"""PKAN Item Sample Content Type."""

# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Item
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.annotation.interfaces import IAnnotations
from zope.interface import implementer
# from pkan.examplecontentfilter import _


def prepare_data(data):
    """Prepare data dicts."""
    result = {}

    for item in data:
        # Remove all None-Type values.
        if data[item] is not None:
            value = data[item]
            if isinstance(value, unicode):
                value = value.encode('utf-8')
            result[item] = value
    return result


class IPkanItem(model.Schema):
    """Marker interface and Dexterity Python Schema for PkanItem."""

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


class IExampleSchema(model.Schema):
    """Example schema."""

    field_1 = schema.TextLine(
        title=u'Field 1',
    )

    field_2 = schema.Int(
        title=u'Field 2',
    )

    field_3 = schema.Text(
        title=u'Field 3',
    )


@implementer(IPkanItem)
class PkanItem(Item):
    """PKAN Item"""

    @property
    def schema(self):
        """Return the schema based on the selected sub type."""
        return IExampleSchema

    @property
    def source_data(self):
        annotations = IAnnotations(self)
        return annotations.get(
            'pkan.examplecontentfilter.source_data',
            annotations.setdefault('pkan.examplecontentfilter.source_data', {})
        )

    @property
    def filter_data(self):
        annotations = IAnnotations(self)
        return annotations.get(
            'pkan.examplecontentfilter.filter_data',
            annotations.setdefault('pkan.examplecontentfilter.filter_data', {})
        )

    @property
    def custom_data(self):
        annotations = IAnnotations(self)
        return annotations.get(
            'pkan.examplecontentfilter.custom_data',
            annotations.setdefault('pkan.examplecontentfilter.custom_data', {})
        )

    @property
    def result_data(self):
        result = {}
        result.update(prepare_data(self.source_data))
        result.update(prepare_data(self.filter_data))
        result.update(prepare_data(self.custom_data))
        return result
