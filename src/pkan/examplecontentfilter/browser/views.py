# -*- coding: utf-8 -*-
"""Example views."""

from Products.Five import BrowserView
from plone.autoform.form import AutoExtensibleForm
from z3c.form import button
from z3c.form import form
from zope.annotation.interfaces import IAnnotations
from zope.traversing.browser.absoluteurl import absoluteURL


class SourceForm(AutoExtensibleForm, form.Form):
    """Form to show/edit the source data."""

    label = u'Source Data'
    description = u'Edit the source data for this item'
    ignoreRequiredOnExtract = True

    @property
    def schema(self):
        return self.context.schema

    def getContent(self):
        return self.context.source_data

    @button.buttonAndHandler(u'Save')
    def handle_save(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        annotations = IAnnotations(self.context)
        annotations['pkan.examplecontentfilter.source_data'] = data
        self.request.response.redirect(absoluteURL(self.context, self.request))

    @button.buttonAndHandler(u'Cancel')
    def handle_cancel(self, action):
        self.request.response.redirect(absoluteURL(self.context, self.request))


class FilterForm(AutoExtensibleForm, form.Form):
    """Form to show/edit the filter data."""

    label = u'Filter Data'
    description = u'Edit the filter data for this item'
    ignoreRequiredOnExtract = True

    @property
    def schema(self):
        return self.context.schema

    def getContent(self):
        return self.context.filter_data

    @button.buttonAndHandler(u'Save')
    def handle_save(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        annotations = IAnnotations(self.context)
        annotations['pkan.examplecontentfilter.filter_data'] = data
        self.request.response.redirect(absoluteURL(self.context, self.request))

    @button.buttonAndHandler(u'Cancel')
    def handle_cancel(self, action):
        self.request.response.redirect(absoluteURL(self.context, self.request))


class CustomForm(AutoExtensibleForm, form.Form):
    """Form to show/edit the custom data."""

    label = u'Custom Data'
    description = u'Edit the custom data for this item'
    ignoreRequiredOnExtract = True

    @property
    def schema(self):
        return self.context.schema

    def getContent(self):
        return self.context.custom_data

    @button.buttonAndHandler(u'Save')
    def handle_save(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        annotations = IAnnotations(self.context)
        annotations['pkan.examplecontentfilter.custom_data'] = data
        self.request.response.redirect(absoluteURL(self.context, self.request))

    @button.buttonAndHandler(u'Cancel')
    def handle_cancel(self, action):
        self.request.response.redirect(absoluteURL(self.context, self.request))


class ItemView(BrowserView):
    """Default View for the item."""
