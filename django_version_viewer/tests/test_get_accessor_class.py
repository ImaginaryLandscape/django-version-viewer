import mock
from django.test import TestCase, override_settings
from django.test.client import RequestFactory
from django_version_viewer.utils import get_accessor_class
from django.core import exceptions


class FakeAccessorClassTrue(object):

    def allow_access(self, request):
        return True


class FakeAccessorClassFalse(object):

    def allow_access(self, request):
        return False


class TestGetAccessorClass(TestCase):

    @mock.patch('django.contrib.auth.models.User')
    def test__get_accessor_class__default(self, mock_user):
        from django_version_viewer.mixins import SuperuserAccessor
        self.assertTrue(isinstance(get_accessor_class(), SuperuserAccessor))

    @override_settings(
        ACCESSOR_CLASS_PATH='django_version_viewer.tests.test_get_accessor_class.FakeAccessorClassTrue') # noqa
    def test__get_accessor_class__override_allow_all(self):
        request = RequestFactory().get("/")
        self.assertTrue(get_accessor_class().allow_access(request))

    @override_settings(
        ACCESSOR_CLASS_PATH='django_version_viewer.tests.test_get_accessor_class.FakeAccessorClassFalse') # noqa
    def test__get_accessor_class__override_deny_all(self):
        request = RequestFactory().get("/")
        self.assertFalse(get_accessor_class().allow_access(request))

    @override_settings(ACCESSOR_CLASS_PATH='')
    def test__get_accessor_class__empty_path(self):
        request = RequestFactory().get("/")
        with self.assertRaises(exceptions.ImproperlyConfigured):
            get_accessor_class().allow_access(request)

    @override_settings(ACCESSOR_CLASS_PATH='Foo')
    def test__get_accessor_class__invalid_class(self):
        request = RequestFactory().get("/")
        with self.assertRaises(exceptions.ImproperlyConfigured):
            get_accessor_class().allow_access(request)
