from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal


class IndexViewTestCase(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory
        self.animal = Animal.objects.create(
            nome_animal='calopsita',
            predador='Não',
            venenoso='Não',
            domestico='Sim'
        )

    def test_index_view_retorna_caracteriscias_do_animal(self):
        """Test que verifica se a index retornas as caracteristicas do anima"""

        response = self.client.get('/', {'buscar':'calopsita'})

        caracteristica_animal = response.context['caracteristicas']

        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(caracteristica_animal[0].nome_animal, 'calopsita')

