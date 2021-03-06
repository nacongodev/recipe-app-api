from django.test import TestCase
from django.contrib.auth import  get_user_model


class  ModelTests(TestCase):

      def test_create_user_with_email_successful(self):
            """ Test creating a new user with email is successful"""
            email = 'test@devapp.com'
            password='avlnvwkv;w kdvml;dvll'
            user= get_user_model().objects.create_user(
            email=email,
            password=password
            )
            self.assertEqual(user.email,email)
            self.assertTrue(user.check_password(password))

      def test_new_user_email_normalized(self):
            """Test the email for a new user is normalized"""
            email = "test@DEVAPP.com"
            user = get_user_model().objects.create_user(email, 'test2155')

            self.assertEqual(user.email, email.lower())

      def test_new_user_invalid_email(self):
            """Test creating user with no email should raise an error"""
            with self.assertRaises(ValueError):
                  get_user_model().objects.create_user(None,'test2155')

      def test_new_superuser(self):
            """Test creating a new superuser"""
            user = get_user_model().objects.create_superuser(
                  'test@devapp.com',
                  'test2155'
            )
            self.assertTrue(user.is_superuser)
            self.assertTrue(user.is_staff)



