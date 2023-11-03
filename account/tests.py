from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.test import TestCase


class SigninTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='test_password')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='test_password')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='test_password')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


class SignInViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test',
                                                         password='test_password')

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        response = self.client.post('/login/', {'username': 'test', 'password': 'test_password'})

        # Check for the redirect status code (302)
        self.assertEqual(response.status_code, 302)

        # After a successful login, the user will be redirect to home page.
        self.assertIn('Location', response)
        redirect_location = response['Location']

        # Check if the redirect location is the expected value
        self.assertEqual(redirect_location, '/home/')

        # Check if the final status code is 200
        response = self.client.get(redirect_location)
        self.assertEqual(response.status_code, 200)

    def test_wrong_username(self):
        response = self.client.post('/login/', {'username': 'wrong', 'password': 'test_password'})
        self.assertEqual(response.status_code, 200)  # Check for a failed login

    def test_wrong_pssword(self):
        response = self.client.post('/login/', {'username': 'test', 'password': 'wrong'})
        self.assertEqual(response.status_code, 200)  # Check for a failed login


class LogoutViewTest(TestCase):

    def test_logout(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)  # Check for a redirect to login page.

        self.assertIn('Location', response)
        redirect_location = response['Location']

        # Check if the redirect location is the expected value
        self.assertEqual(redirect_location, '/login/')

        # Check if the final status code is 200
        response = self.client.get(redirect_location)
        self.assertEqual(response.status_code, 200)


class RegisterViewTest(TestCase):

    def test_register_with_strong_password(self):
        response = self.client.post('/register/', {'username': 'abc', 'password1': 'dfhj4321', 'password2': 'dfhj4321'})
        self.assertEqual(response.status_code, 302)  # Check for a redirect

        # Check if the user was created
        self.assertTrue(get_user_model().objects.filter(username='abc').exists())

        # After a successful registration, the user will be redirect to login page.
        self.assertIn('Location', response)
        redirect_location = response['Location']

        # Check if the redirect location is the expected value
        self.assertEqual(redirect_location, '/home')

    def test_register_with_small_password(self):
        response = self.client.post('/register/', {'username': 'def', 'password1': 'hjk321', 'password2': 'hjk321'})
        self.assertEqual(response.status_code, 200)

        # Check if the user was not created
        self.assertFalse(get_user_model().objects.filter(username='def').exists())

    def test_register_with_common_password(self):
        response = self.client.post('/register/', {'username': 'xyz', 'password1': 'abcd1234', 'password2': 'abcd1234'})
        self.assertEqual(response.status_code, 200)

        # Check if the user was not created
        self.assertFalse(get_user_model().objects.filter(username='xyz').exists())


class PasswordChangeViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='test_password')
        self.client.login(username='test', password='test_password')

    def tearDown(self):
        self.user.delete()

    def test_password_change(self):
        response = self.client.post('/change_password/', {'new_password1': 'new_password',
                                                          'new_password2': 'new_password'})
        self.assertEqual(response.status_code, 302)  # Check for a redirect to login page.

        self.assertIn('Location', response)
        redirect_location = response['Location']

        # Check if the redirect location is the expected value
        self.assertEqual(redirect_location, '/login')
