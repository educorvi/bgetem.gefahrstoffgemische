# -*- coding: utf-8 -*-
from bgetem.gefahrstoffgemische.content.heatsetwaschmittel import IHeatsetwaschmittel  # NOQA E501
from bgetem.gefahrstoffgemische.testing import BGETEM_GEFAHRSTOFFGEMISCHE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class HeatsetwaschmittelIntegrationTest(unittest.TestCase):

    layer = BGETEM_GEFAHRSTOFFGEMISCHE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_heatsetwaschmittel_schema(self):
        fti = queryUtility(IDexterityFTI, name='Heatsetwaschmittel')
        schema = fti.lookupSchema()
        self.assertEqual(IHeatsetwaschmittel, schema)

    def test_ct_heatsetwaschmittel_fti(self):
        fti = queryUtility(IDexterityFTI, name='Heatsetwaschmittel')
        self.assertTrue(fti)

    def test_ct_heatsetwaschmittel_factory(self):
        fti = queryUtility(IDexterityFTI, name='Heatsetwaschmittel')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IHeatsetwaschmittel.providedBy(obj),
            u'IHeatsetwaschmittel not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_heatsetwaschmittel_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Heatsetwaschmittel',
            id='heatsetwaschmittel',
        )

        self.assertTrue(
            IHeatsetwaschmittel.providedBy(obj),
            u'IHeatsetwaschmittel not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('heatsetwaschmittel', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('heatsetwaschmittel', parent.objectIds())

    def test_ct_heatsetwaschmittel_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Heatsetwaschmittel')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_heatsetwaschmittel_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Heatsetwaschmittel')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'heatsetwaschmittel_id',
            title='Heatsetwaschmittel container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
