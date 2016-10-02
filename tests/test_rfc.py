#!/usr/bin/python
# -*- coding: utf-8 -*-
from rfcmx.rfc import RFCValidator, RFCGeneratorFisicas
import unittest
import datetime


class test_RFCValidator(unittest.TestCase):
    def test_ValidRFC(self):
        rfc = [
            ('MANO610814JL5', True),
            ('MME941130K54', True),
            ('BACL891217NJ8', False),
            ('NIR6812205X9', True),
            ('BNM840515VB1', True),
        ]

        for elem, result in rfc:
            # print elem, result
            self.assertEqual(RFCValidator(elem).validate(), result)


class test_RFCPersonasFisicas(unittest.TestCase):
    def test_generaLetras(self):
        tests = [
            ('Juan', 'Barrios', 'Fernández', 'BAFJ'),
            ('Eva', 'Iriarte', 'Méndez', 'IIME'),
            ('Manuel', 'Chávez', 'González', 'CAGM'),
            ('Felipe', 'Camargo', 'Lleras', 'CALF'),
            ('Charles', 'Kennedy', 'Truman', 'KETC'),
            ('Alvaro', 'De la O', 'Lozano', 'OLAL'),
            ('Ernesto', 'Ek', 'Rivera', 'ERER'),
            ('Julio', 'Ek', '', 'EKJU'),
            ('Julio', 'Ek', None, 'EKJU'),
            ('Luis', 'Bárcenas', '', 'BALU'),
            ('Dolores', 'San Martín', 'Dávalos', 'SADD'),
            ('Mario', 'Sánchez de la Barquera', 'Gómez', 'SAGM'),
            ('Antonio', 'Jiménez', 'Ponce de León', 'JIPA'),
            ('Luz María', 'Fernández', 'Juárez', 'FEJL'),
            ('José Antonio', 'Camargo', 'Hernández', 'CAHA'),
            ('María de Guadalupe', 'Hernández', 'von Räutlingen', 'HERG'),
            ('María Luisa', 'Ramírez', 'Sánchez', 'RASL'),
            ('Ernesto', 'Martínez', 'Mejía', 'MAMX'),
            ('Fernando', 'Ñemez', 'Ñoz', 'ÑEÑF'),
            ('泽东', '毛', '', 'MAZE'),  # Mao Zedong
            ('中山', '孙', '', 'SUZH'),  # Sun Zhongshan
            ('中山', '孙', None, 'SUZH')
        ]

        for elem in tests:
            r = RFCGeneratorFisicas(nombre=elem[0], paterno=elem[1], materno=elem[2], fecha=datetime.date(2000, 1, 1))
            self.assertEqual(r.generate_letters(), elem[3])
