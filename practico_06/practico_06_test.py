# Implementar los casos de prueba descriptos.

import unittest

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_1(valido))

        self.ns.alta(valido)
        repetido = Socio(dni=12345678, nombre='Carlos', apellido='Lopez')
        self.assertRaises(DniRepetido, self.ns.regla_1, repetido)

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        invalido = Socio(dni=12345678, nombre='J' * 16, apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Pe')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        invalido = Socio(dni=12345678, nombre='Juan', apellido='P' * 16)
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        self.ns.MAX_SOCIOS = 1
        self.ns.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3)

    def test_baja(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        self.assertEqual(len(self.ns.todos()), 1)

        exito = self.ns.baja(socio.id)
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 0)

    def test_buscar(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        encontrado = self.ns.buscar(socio.id)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.id, socio.id)

    def test_buscar_dni(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        encontrado = self.ns.buscar_dni(socio.dni)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.dni, socio.dni)

    def test_todos(self):
        self.assertEqual(len(self.ns.todos()), 0)

        self.ns.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
        self.ns.alta(Socio(dni=87654321, nombre='Ana', apellido='Gomez'))

        self.assertEqual(len(self.ns.todos()), 2)

    def test_modificacion(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        socio.nombre = 'Carlos'
        socio.apellido = 'Gimenez'
        exito = self.ns.modificacion(socio)

        self.assertTrue(exito)
        actualizado = self.ns.buscar(socio.id)
        self.assertEqual(actualizado.nombre, 'Carlos')
        self.assertEqual(actualizado.apellido, 'Gimenez')
