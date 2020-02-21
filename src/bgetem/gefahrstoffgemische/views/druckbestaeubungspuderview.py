# -*- coding: utf-8 -*-

from bgetem.gefahrstoffgemische import _
from Products.Five.browser import BrowserView

from bgetem.gefahrstoffgemische.vocabularies import ausgangsmaterialien

class Druckbestaeubungspuderview(BrowserView):

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        return self.index()

    def get_ausgangsmaterial(self):
        if self.context.ausgangsmaterial:
            return ausgangsmaterialien.getTerm(self.context.ausgangsmaterial).title
        return ''

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


    def emissionsgeprueft(self):
        emissionsgeprueft = self.context.emissionsgeprueft
        if emissionsgeprueft:
            emissionsgeprueft = "Ja"
        else:
            emissionsgeprueft = "Nein"

        return emissionsgeprueft

