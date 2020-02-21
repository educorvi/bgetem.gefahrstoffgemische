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

from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield import DictRow


from bgetem.gefahrstoffgemische import _

from bgetem.gefahrstoffgemische.vocabularies import wmkategorie, wmklasse, institute, hskategorieVocabulary

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.app.vocabularies.catalog import CatalogSource

class IGefahrstoffgemisch(model.Schema):
    """
    Datenblatt eines Produkts
    """

    hersteller = RelationChoice(
        title=_(u"Hersteller oder Lieferant"),
        source=CatalogSource(portal_type=["Folder", "Hersteller"]),
        required=False)

    produktkategorie = schema.List(title=_(u"Produktkategorie"),
            description=_(u"Bitte wählen Sie eine Produktkategorie für das Wasch- und Reinigungsmittel aus."),
            value_type=schema.Choice(vocabulary=wmkategorie),
            required = True,)

    produktklasse = schema.Choice(title=_(u"Produktklasse"),
            description=_(u"Bitte wählen Sie eine Produktklasse für das Waschn- und Reinigungsmittel aus."),
            vocabulary = wmklasse,
            required=True,)

    flammpunkt = schema.Int(title=_(u"Flammpunkt"),
            description = _(u"Bitte geben Sie hier den Wert des Flammpunktes in Grad Celsius an."),
            required=False,)

    # HINWEIS: schema=IChemikalien?

    #directives.widget(chemikalienliste=DataGridFieldFactory)
    #chemikalienliste = schema.List(title=u'EG Sicherheitsdatenblatt',
    #                    description=u'Zusammensetzung/Angaben zu Bestandteilen',
    #                    value_type=DictRow(title=u"Chemikalien", schema=IChemikalien),
    #                    required=False,)

    wertebereich = schema.Bool(title=_(u"Wertebereich für den Flammpunkt"),
            description=_(u"Bitte treffen Sie hier eine Auswahl wenn der Wertebereich für den\
                              Flammpunkt größer als der angegebene Zahlenwert ist."),
            required=False,)

    emissionsgeprueft = schema.Bool(title=_(u"Emissionsarmes Produkt"),
            description=_(u"Bitte markieren Sie hier, wenn für das Produkt die Kriterien des Gütesiegels\
                              erfüllt sind."),
            required=False,)

    # HINWEIS: dmvocab?

    #maschinen = schema.List(title=_(u"Druckmaschinen und automatische Waschanlagen"),
    #        description=_(u"Bitte geben Sie hier die Druckmaschinen und automatischen Waschanlagen an,\
    #                          für das dieses Wasch- und Reinigungsmittel zugelassen wurde."),
    #        value_type=schema.Choice(source=dmvocab),
    #        required=True,)

    materialvertraeglichkeit = schema.Choice(title=_(u"Materialverträglichkeit"),
            description = _(u"Bitte wählen Sie hier die Institute aus, von denen die Materialverträglichkeit getestet wurde."),
            vocabulary=institute,
            required=True,)

    hskategorie = schema.Choice(title=_(u"Hautschutzmittelgruppe"),
            vocabulary=hskategorieVocabulary,
            required=False)

    bemerkungen = RichText(title=_(u"Bemerkungen"),
                  description=_(u"Hier können zusätliche Bemerkungen zum Produktdatenblatt eingefügt werden."),
                  required=False,)


@implementer(IGefahrstoffgemisch)
class Gefahrstoffgemisch(Container):
    """
    """
