# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer


from bgetem.gefahrstoffgemische import _

#from bgetem.gefahrstoffgemische.vocabularies import hskategorieVocabulary

# from collective.z3cform.datagridfield import DictRow, DataGridFieldFactory



class IHeatsetwaschmittel(model.Schema):
    """
    Description of the Example Type
    """

#    directives.widget('verdampfung', DataGridFieldFactory)

#    hersteller = RelationChoice(title=_(u"Hersteller"),
#            description=_(u"Bitte wählen Sie hier den Hersteller des Reinigungsmittels aus."),
#            source=ObjPathSourceBinder(object_provides=IHersteller.__identifier__),
#            required = True,)

#    verdampfung = schema.List(title=_(u"Verdampungsfaktoren"),
#            description=_(u"Bitte tragen Sie hier die Verdampfungsfaktoren fuer die entsprechenden Bahntemperaturen ein"),
#            value_type=DictRow(title=u"Verdampfungsfaktoren", schema=IVerdampfung),
#            required = False,)

    emissionsgeprueft=schema.Bool(title=_(u"Emissionsarmes Produkt"),
            description=_(u"Bitte markieren Sie hier, wenn für das Produkt die Kriterien des Gütesiegels\
                              erfüllt sind."),
            required=False,)

    ueg = schema.TextLine(title=_(u"UEG in g/m3"), required=False)

    response = schema.TextLine(title=_(u"Responsefaktor"), required=False)

    #hskategorie = schema.Choice(title=_(u"Hautschutzmittelgruppe"),
    #        vocabulary=hskategorieVocabulary,
    #        required=False)

    pruefdateum = schema.Date(title=_(u"Prüfdatum"),
            required = False,)


@implementer(IHeatsetwaschmittel)
class Heatsetwaschmittel(Container):
    """
    """
