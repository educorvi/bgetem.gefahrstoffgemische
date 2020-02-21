# -*- coding: utf-8 -*-

from bgetem.gefahrstoffgemische import _
from Products.Five.browser import BrowserView
from bgetem.gefahrstoffgemische.vocabularies import hskategorieVocabulary

class GefahrstoffgemischView(BrowserView):

    def __call__(self):
        self.msg = _(u'A small message')
        return self.index()


    def get_herstellerdaten(self):
        herstellerdaten = {}
        if self.context.hersteller:
            hersteller = self.context.hersteller.to_object
            herstellerdaten['name'] = hersteller.title
            herstellerdaten['anschrift1'] = hersteller.anschrift1
            herstellerdaten['anschrift2'] = hersteller.anschrift2
            herstellerdaten['anschrift3'] = hersteller.anschrift3
            herstellerdaten['telefon'] = hersteller.telefon
            herstellerdaten['email'] = hersteller.email
            herstellerdaten['homepage'] = hersteller.homepage
        return herstellerdaten

    def wertebereich(self):
        wertebereich = self.context.wertebereich
        if wertebereich:
            wertebereich = "Ja"
        else:
            wertebereich = "Nein"

        return wertebereich


    def emissionsgeprueft(self):
        emissionsgeprueft = self.context.emissionsgeprueft
        if emissionsgeprueft:
            emissionsgeprueft = "Ja"
        else:
            emissionsgeprueft = "Nein"

        return emissionsgeprueft


    def get_hskategorie(self):
        hskategorien = []
        import pdb; pdb.set_trace()
        for i in self.context.hskategorie:
            hskategorien.append(hskategorieVocabulary.getTerm(i).title)
            import pdb; pdb.set_trace()
        return hskategorien

    def bemerkungen(self):
        if self.context.bemerkungen:
            bemerkungen = self.context.bemerkungen
            bemerkungen = bemerkungen.output
            return bemerkungen
