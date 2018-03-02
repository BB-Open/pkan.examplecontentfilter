# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import pkan.examplecontentfilter


class PkanExamplecontentfilterLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=pkan.examplecontentfilter)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'pkan.examplecontentfilter:default')


PKAN_EXAMPLECONTENTFILTER_FIXTURE = PkanExamplecontentfilterLayer()


PKAN_EXAMPLECONTENTFILTER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PKAN_EXAMPLECONTENTFILTER_FIXTURE,),
    name='PkanExamplecontentfilterLayer:IntegrationTesting'
)


PKAN_EXAMPLECONTENTFILTER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PKAN_EXAMPLECONTENTFILTER_FIXTURE,),
    name='PkanExamplecontentfilterLayer:FunctionalTesting'
)


PKAN_EXAMPLECONTENTFILTER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PKAN_EXAMPLECONTENTFILTER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PkanExamplecontentfilterLayer:AcceptanceTesting'
)
