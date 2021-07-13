from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Snack
from django.urls import reverse

class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='ebrahimayyad11',
            email='ayyad_ebrahim@hotmail.com',
            password='En_215111'
        )
        self.post = Snack.objects.create(
            title='potato',
            purchaser=self.user,
            description='nice taste'
        )
    def test_string_representation(self):
        post = Snack(title='title')
        self.assertEqual(str(post), post.title)
    def test_all_fields(self):
        self.assertEqual(str(self.post.title), 'potato')
        self.assertEqual(f'{self.post.purchaser}', 'ebrahimayyad11')
        self.assertEqual(self.post.description, 'nice taste')
    def test_snack_list_view(self):
        response = self.client.get(reverse('snacklist'))
        self.assertEqual(response.status_code, 200)
    def test_snack_details_view(self):
        response = self.client.get(reverse('snackdetail', args='1'))
        self.assertEqual(response.status_code, 200)
    def test_snack_update_view(self):
        response = self.client.post(reverse('snackupdate', args='1'), {
            'title': 'potato',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'potato')


    def test_home_status(self):
        expected = 200
        url = reverse('snacklist')
        response = self.client.get(url)
        actual = response.status_code
        self.assertEquals(expected, actual)

        
    def test_home_template(self):
        url = reverse('snacklist')
        response = self.client.get(url)
        actual = 'snacklist.html'
        self.assertTemplateUsed(response, actual)


    def test_create_view(self):
        response = self.client.post(reverse('snackcreate'), {
            'title': 'potato',
            'purchaser': self.user,
            'description': 'nice taste',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'potato')
        self.assertContains(response, 'nice taste')
        self.assertContains(response, 'ebrahimayyad11')
    def test_delete_view(self):
        response = self.client.get(reverse('snackdelete', args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Delete Snack')
        post_response = self.client.post(reverse('snackdelete', args='1'))
        self.assertRedirects(post_response, reverse(
            'snacklist'), status_code=302)