from django.test import Client, TestCase
from django.urls import reverse

from posts.forms import CreationForm
from posts.models import Post, User


class PostCreateFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.form = CreationForm()

    def setUp(self):
        # Создаем авторизованный клиент
        self.user = User.objects.create_user(username='StasBasov')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_create_post(self):
        """Валидная форма не создает запись в Post."""
        # Подсчитаем количество записей в Task
        post_count = Post.objects.count()

        form_data = {
            'text': 'Крутой текст',

        }
        response = self.authorized_client.post(
            reverse('new_post'),
            data=form_data,
            follow=True)

        self.assertRedirects(response, reverse('index'))
        self.assertEqual(Post.objects.count(), post_count + 1)
        # Проверяем, что создалась запись с нашим слагом
        self.assertTrue(
            Post.objects.filter(
                text='Крутой текст',
            ).exists()
        )

    def test_create_pure_post(self):
        """Валидная форма создает запись в Task."""
        # Подсчитаем количество записей в Task
        post_count = Post.objects.count()

        form_data = {
            'text': '',

        }
        response = self.authorized_client.post(
            reverse('new_post'),
            data=form_data,
            follow=True)

        self.assertEqual(Post.objects.count(), post_count)

        self.assertFormError(
            response,
            'form',
            'text',
            'Обязательное поле.'
        )
        # Проверим, что ничего не упало и страница отдаёт код 200
        self.assertEqual(response.status_code, 200)
