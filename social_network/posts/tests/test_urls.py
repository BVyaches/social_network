from django.test import TestCase, Client
from posts.models import Group, User


class TaskURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(
            username='Чел'
        )

        Group.objects.create(
            title='Крутое название',
            slug='cool_address',
            description='Крутое описание',
            author=cls.user
        )

    def setUp(self):
        # Создаем неавторизованный клиент
        self.guest_client = Client()
        # Создаем авторизованый клиент
        self.user = User.objects.create_user(username='Крутой чел')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_homepage_template(self):
        '''Тест работы стартовой страницы'''
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_group_template(self):
        '''Group page works'''
        response = self.guest_client.get('/group/cool_address/')
        self.assertEqual(response.status_code, 200)

    def test_new_unauthorized(self):
        '''New is unavailable for anonymous users'''
        response = self.guest_client.get('/new')
        self.assertEqual(response.status_code, 302)

    def test_new_authorized(self):
        '''New is available for authorized users'''
        response = self.authorized_client.get('/new')
        self.assertEqual(response.status_code, 200)

    def test_templates(self):
        '''templates work fine'''
        templates = {
            '/': 'index.html',
            '/new': 'new.html',
            '/group/cool_address/': 'group.html'
        }
        for value, expected in templates.items():
            with self.subTest(value=value):
                self.assertTemplateUsed(
                    self.authorized_client.get(value), expected)
