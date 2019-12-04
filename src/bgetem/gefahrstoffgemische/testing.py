# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import bgetem.gefahrstoffgemische


class BgetemGefahrstoffgemischeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=bgetem.gefahrstoffgemische)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'bgetem.gefahrstoffgemische:default')


BGETEM_GEFAHRSTOFFGEMISCHE_FIXTURE = BgetemGefahrstoffgemischeLayer()


BGETEM_GEFAHRSTOFFGEMISCHE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(BGETEM_GEFAHRSTOFFGEMISCHE_FIXTURE,),
    name='BgetemGefahrstoffgemischeLayer:IntegrationTesting',
)


BGETEM_GEFAHRSTOFFGEMISCHE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(BGETEM_GEFAHRSTOFFGEMISCHE_FIXTURE,),
    name='BgetemGefahrstoffgemischeLayer:FunctionalTesting',
)


BGETEM_GEFAHRSTOFFGEMISCHE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        BGETEM_GEFAHRSTOFFGEMISCHE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='BgetemGefahrstoffgemischeLayer:AcceptanceTesting',
)
