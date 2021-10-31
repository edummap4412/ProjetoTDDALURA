from animais.models import Animal
from django.test import TestCase, RequestFactory


class AnimalModelTestCase(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome_animal='Leão',
            predador='Sim',
            venenoso='Não',
            domestico='Não'
        )


    def test_animal_casdastrado_com_caracteriscitas(self):
        """Teste que verifica se o animl esta cadastrado com suas respectivas caracteristicas"""

        self.assertEqual(self.animal.nome_animal, 'Leão')
