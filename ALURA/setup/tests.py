import time

from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        # no nitro , colocar link  do local do aquivo
        self.browser = webdriver.Chrome(executable_path='/home/eduardo/Área de Trabalho/chromedriver')

   # def test_para_verificar_se_a_janela_esta_ok(self):
        #self.browser.get('https://chromedriver.chromium.org/getting-started')

    #time.sleep(20)

    #def test_fail(self):
        #self.fail('Teste esta falhando')

    # vini deseja encontrar um novo animal
    def test_buscando_um_novo_animal(self):
        """
        Teste se um usuario encontra um animal na pesquisa
        """
    # Ele encontra o Busca Animal e decide usar o site
        home_page = self.browser.get(self.live_server_url + '/')

    # porque ele ve no menu do site escrito Busca Animal
        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

    # Ele vê um campo para pesquisar animais pelo nome

        buscar_animal_input = self.browser.find_element_by_css_selector('input#buscar-animal')

        self.assertEqual(buscar_animal_input.get_attribute('placeholder'),'Exemplo: Leão')

    # Ele pesquisa por Leão e clica no botão pesquisar
        buscar_animal_input.send_keys('leão')
        self.browser.find_element_by_css_selector('form button').click()

    # O site exibe 4 caracteristicas do animal pesquisado
        caracteristicas = self.browser.find_elements_by_css_selector('.results-description')
        self.assertGreater(len(caracteristicas), 3)


    def tearDown(self):
        self.browser.quit()