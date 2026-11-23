# mensajes/tests.py
from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from zoneinfo import ZoneInfo

from .models import Mensaje


class PruebasMensaje(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mensaje = Mensaje.objects.create(texto="Esta es una prueba.")

    def test_contenido_modelo(self):
        self.assertEqual(self.mensaje.texto, "Esta es una prueba.")

    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)

    def test_pagina_inicio(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "inicio.html")
        self.assertContains(respuesta, "Esta es una prueba.")

    def test_str_modelo(self):  # nuevo
        self.assertEqual(str(self.mensaje), "Esta es una prueba.")


class PruebasSinMensajes(TestCase):
    def test_pagina_vacia(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Todavía no hay mensajes.")


class PruebasFechaMensaje(TestCase):
    def test_fecha_en_pagina(self):
        mensaje = Mensaje.objects.create(texto="Mensaje con fecha")
        fecha = datetime(2026, 10, 10, 17, 55, tzinfo=ZoneInfo("America/Mexico_City"))
        Mensaje.objects.filter(pk=mensaje.pk).update(fecha=fecha)
        respuesta = self.client.get(reverse("inicio"))
        self.assertRegex(respuesta.content.decode(), r"10 de \w+, 17:55")


class PruebasContenidoPagina(TestCase):
    def test_autor_y_contador(self):
        Mensaje.objects.create(texto="Hola", autor="Leo")
        respuesta = self.client.get(reverse("inicio"))
        self.assertContains(respuesta, "Leo")
        self.assertContains(respuesta, "Hay 1 mensaje.")
