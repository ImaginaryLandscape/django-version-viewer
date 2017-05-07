import mock
from django.test import TestCase
from django.test.client import RequestFactory
from django_version_viewer.mixins import SuperuserAccessor


class TestGetAccessorClass(TestCase):

    @mock.patch('django.contrib.auth.models.User')
    def test__SuperuserAccessor__user_is_superuser(self, mock_user):
        request = RequestFactory().get("/")
        mock_user.is_superuser = True
        request.user = mock_user
        self.assertTrue(SuperuserAccessor().allow_access(request))

    @mock.patch('django.contrib.auth.models.User')
    def test__SuperuserAccessor__user_not_superuser(self, mock_user):
        request = RequestFactory().get("/")
        mock_user.is_superuser = False
        request.user = mock_user
        self.assertFalse(SuperuserAccessor().allow_access(request))
