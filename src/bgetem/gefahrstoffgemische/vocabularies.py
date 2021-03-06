# -*- coding:utf-8 -*-
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from bgetem.gefahrstoffgemische import _

klasse = SimpleVocabulary([
     SimpleTerm(u'fein', u'fein'),
     SimpleTerm(u'mittel', u'mittel'),
     SimpleTerm(u'grob', u'grob'),
     ])

ausgangsmaterialien = SimpleVocabulary([
     SimpleTerm(value=u'Staerke', title=_(u'Stärke')),
     SimpleTerm(value=u'Calciumcarbonat', title=_(u'Calciumcarbonat')),
     SimpleTerm(value=u'Zucker', title=_(u'Zucker'))]
    )

#hskategorieVocabulary = SimpleVocabulary((
#    SimpleTerm(u"id_wasserloeslich", u"wasserloeslich", u"gegen wasserlösliche Arbeitsstoffe"),
#    SimpleTerm(u"id_nichtwasserloeslich", u"nichtwasserloeslich", u"gegen wasserunlösliche Arbeitsstoffe"),
#    SimpleTerm(u"id_wechselnd", u"wechselnd", u"gegen wechselnde Arbeitsstoffe")
#    ))

#wmklasse = SimpleVocabulary(
#     SimpleTerm(value=u'Reinigungsoele auf Pflanzenoelbasis', title=_(u'Waschmittel auf Pflanzenölbasis')),
#     SimpleTerm(value=u'UV-Waschmittel', title=_(u'UV-Waschmittel')),
#     SimpleTerm(value=u'Waschmittel auf Kohlenwasserstoffbasis', title=_(u'Waschmittel auf Kohlenwasserstoffbasis')),
#     SimpleTerm(value=u'Waschmittel auf Basis Testbenzin', title=_(u'Waschmittel auf Basis Testbenzin')),
#     SimpleTerm(value=u'Wasch- und Reinigungsmittel auf waessriger Basis/Emulsionen',
#                title=_(u'Waschmittel auf wässriger Basis/Emulsionen')),
#     )

#wmkategorie = SimpleVocabulary(
#    [SimpleTerm(value=u"UV-Druck", title=_(u'UV-Druck')),
#     SimpleTerm(value=u'Konventioneller Druck', title=_(u'Konventioneller Druck')),]
#    )

institute = SimpleVocabulary((
     SimpleTerm(value=u'FOGRA', title=_(u'FOGRA')),
     SimpleTerm(value=u'nicht getestet', title=_(u'nicht auf Materialverträglichkeit getestet.')),
    ))


    # SimpleTerm(value=u'Zucker', title=_(u'Zucker'))
    #])

hskategorieVocabulary = SimpleVocabulary((
    SimpleTerm(value=u"id_wasserloeslich", token=u"id_wasserloeslich", title=_(u"gegen wasserlösliche Arbeitsstoffe")),
    SimpleTerm(value=u"id_nichtwasserloeslich", token=u"id_nichtwasserloeslich", title=_(u"gegen wasserunlösliche Arbeitsstoffe")),
    SimpleTerm(value=u"id_wechselnd", token=u"id_wechselnd", title=_(u"gegen wechselnde Arbeitsstoffe")),
    ))

wmklasse = SimpleVocabulary((
     SimpleTerm(value=u'Reinigungsoele auf Pflanzenoelbasis', title=_(u'Waschmittel auf Pflanzenölbasis')),
     SimpleTerm(value=u'UV-Waschmittel', title=_(u'UV-Waschmittel')),
     SimpleTerm(value=u'Waschmittel auf Kohlenwasserstoffbasis', title=_(u'Waschmittel auf Kohlenwasserstoffbasis')),
     SimpleTerm(value=u'Waschmittel auf Basis Testbenzin', title=_(u'Waschmittel auf Basis Testbenzin')),
     SimpleTerm(value=u'Wasch- und Reinigungsmittel auf waessriger Basis/Emulsionen',
           title=_(u'Waschmittel auf wässriger Basis/Emulsionen')),
     ))

wmkategorie = SimpleVocabulary((
    SimpleTerm(value=u"UV-Druck", title=_(u'UV-Druck')),
    SimpleTerm(value=u'Konventioneller Druck', title=_(u'Konventioneller Druck')),
    ))

#institute = SimpleVocabulary(
#    [SimpleTerm(value=u'FOGRA', title=_(u'FOGRA')),
#     SimpleTerm(value=u'nicht getestet', title=_(u'nicht auf Materialverträglichkeit getestet.')),]
#    )
