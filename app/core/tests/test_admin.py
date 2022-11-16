from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AdminSiteTest(TestCase):
    """Tests for Django admin."""

    def setUp(self) -> None:
        """Create user and client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@exameple.com',
            password='testpass123'
        )
        self.user = get_user_model().objects.create(
            email='test@example.com',
            password='testpass123',
            name='Test User'
        )

    def test_users_lists(self):
        """Test that users are listed on page."""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
