# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer

from z3c.relationfield.schema import RelationList, RelationChoice

from bgetem.gefahrstoffgemische import _

from bgetem.gefahrstoffgemische.vocabularies import klasse, ausgangsmaterial


class IDruckbestaeubungspuder(model.Schema):
    """
    Description of the Example Type
    """

#    hersteller = RelationChoice(title=_(u"Hersteller"),
#            description=_(u"Bitte wählen Sie hier den Hersteller des Druckbestäubungspuders aus."),
#            source=ObjPathSourceBinder(object_provides=IHersteller.__identifier__),
#            required=True,)

    produktklasse = schema.Choice(title=_(u"Produktklasse"),
            description=_(u"Bitte wählen Sie eine Produktklasse für das Druckbestäubungspuder aus."),
            vocabulary = klasse,
            required=True,)

    ausgangsmaterial = schema.Choice(title=_(u"Ausgangsmaterial"),
            description=_(u"Bitte wählen Sie das Ausgangsmaterial für das Druckbestäubungspuder aus."),
            vocabulary=ausgangsmaterial,
            required=True,)

    medianwert = schema.Float(title=_(u"Medianwert in µm"),
            description=_(u"Bitte geben Sie hier den Medianwert in Micrometer als Gleitkommawert an."),
            required=True,)

    volumenanteil = schema.Float(title=_(u"Volumenanteil < 10 µm"),
            description=_(u"Prozentuale Angabe des Volumenanteils der Partikel mit Korngrößen unterhalb\
                              10 µm am Gesamtvolumen der Puderprobe"),
            required=True,)

    maschinen = schema.List(title=_(u"Maschinen mit Ausschlußkriterien"),
            description=_(u"Bitte geben Sie hier Maschinen an, bei denen dieses Druckbestäubungspuder\
                              explizit nicht verwendet werden darf (ein Eintrag pro Zeile)"),
            value_type = schema.TextLine(title=_(u"Druckbestäubungspuder")),
            required=False,)

    emissionsgeprueft = schema.Bool(title=_(u"Emissionsarmes Produkt"),
            description=_(u"Bitte markieren Sie hier, wenn für das Produkt die Kriterien des Gütesiegels\
                              erfüllt sind."),
            default=True,
            required=False,)

    pruefdateum = schema.Date(title=_(u"Prüfdatum"),
            required=False,)

@implementer(IDruckbestaeubungspuder)
class Druckbestaeubungspuder(Container):
    """
    """
