# -*- coding: utf-8 -*-
from bgetem.gefahrstoffgemische.content.druckbestaeubungspuder import IDruckbestaeubungspuder  # NOQA E501
from bgetem.gefahrstoffgemische.testing import BGETEM_GEFAHRSTOFFGEMISCHE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class DruckbestaeubungspuderIntegrationTest(unittest.TestCase):

    layer = BGETEM_GEFAHRSTOFFGEMISCHE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_druckbestaeubungspuder_schema(self):
        fti = queryUtility(IDexterityFTI, name='Druckbestaeubungspuder')
        schema = fti.lookupSchema()
        self.assertEqual(IDruckbestaeubungspuder, schema)

    def test_ct_druckbestaeubungspuder_fti(self):
        fti = queryUtility(IDexterityFTI, name='Druckbestaeubungspuder')
        self.assertTrue(fti)

    def test_ct_druckbestaeubungspuder_factory(self):
        fti = queryUtility(IDexterityFTI, name='Druckbestaeubungspuder')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IDruckbestaeubungspuder.providedBy(obj),
            u'IDruckbestaeubungspuder not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_druckbestaeubungspuder_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Druckbestaeubungspuder',
            id='druckbestaeubungspuder',
        )

        self.assertTrue(
            IDruckbestaeubungspuder.providedBy(obj),
            u'IDruckbestaeubungspuder not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('druckbestaeubungspuder', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('druckbestaeubungspuder', parent.objectIds())

    def test_ct_druckbestaeubungspuder_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Druckbestaeubungspuder')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_druckbestaeubungspuder_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Druckbestaeubungspuder')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'druckbestaeubungspuder_id',
            title='Druckbestaeubungspuder container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
