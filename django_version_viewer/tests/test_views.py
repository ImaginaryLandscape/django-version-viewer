import mock
from django.test import TestCase
import json
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import Client


class TestVersionViewer(TestCase):

    url_django_version_viewer = reverse('django_version_viewer')
    url_django_version_viewer_csv = reverse('django_version_viewer_csv')
    url_django_version_viewer_toolbar = reverse('django_version_viewer_toolbar')

    mock_data = [
        {"key": "appdirs", "version": "1.4.3"},
        {"key": "django", "version": "1.8.18"},
        {"key": "six", "version": "1.10.0"}
    ]

    def mocked_working_set(self, *args, **kwargs):
        class MockPackageObject:
            def __init__(self, key, version):
                self.key = key
                self.version = version

        class MockResponse:
            def __init__(self, data):
                self.packages = []
                for _dict in data:
                    mocked_obj = MockPackageObject(_dict['key'], _dict['version'])
                    self.packages.append(mocked_obj)

            def working_set(self):
                return self.packages

        return MockResponse(self.mock_data).working_set()

    def setUp(self):
        self.admin = User.objects.create_superuser(
            email="adminmail@mail.com",
            username="admin_user",
            password="password",
        )
        self.user = User.objects.create(
            email="user@usermail.com",
            username="regular_user",
            password="password"
        )

    def tearDown(self):
        self.admin.delete()
        self.user.delete()

    def test_django_version_viewer_view__admin(self):
        client = Client()
        client.login(username=self.admin.username, password="password")

        with mock.patch('pkg_resources.WorkingSet',
                        return_value=self.mocked_working_set()):
            response = client.get(self.url_django_version_viewer)
            json_response = json.loads(response.content.decode("utf-8"))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(json_response), 3)

    def test_django_version_viewer_view__user(self):
        client = Client()
        client.login(username=self.user.username, password="password")
        response = client.get(self.url_django_version_viewer)
        self.assertEqual(response.status_code, 403)

    def test_django_version_viewer_csv_view__admin(self):
        client = Client()
        client.login(username=self.admin.username, password="password")
        with mock.patch('pkg_resources.WorkingSet',
                        side_effect=self.mocked_working_set):
            response = client.get(self.url_django_version_viewer_csv)
            self.assertEqual(
                response.content,
                b'Package Name,Package Version\r\nappdirs,1.4.3\r\ndjango,1.8.18\r\nsix,1.10.0\r\n'
            )
        self.assertEqual(response.status_code, 200)

    def test_django_version_viewer_csv_view__user(self):
        client = Client()
        client.login(username=self.user.username, password="password")
        response = client.get(self.url_django_version_viewer_csv)
        self.assertEqual(response.status_code, 403)

    def test_django_version_viewer_toolbar_view__admin(self):
        client = Client()
        client.login(username=self.admin.username, password="password")
        with mock.patch('pkg_resources.WorkingSet',
                        side_effect=self.mocked_working_set):
            response = client.get(self.url_django_version_viewer_toolbar)
            context_pakcages = response.context['packages']
            for i in list(range(0, 3)):
                self.assertEqual(self.mock_data[i]['key'], context_pakcages[i]['package_name'])
                self.assertEqual(
                    self.mock_data[i]['version'], context_pakcages[i]['package_version'])

        self.assertEqual(response.status_code, 200)

    def test_django_version_viewer_toolbar_view__user(self):
        client = Client()
        client.login(username=self.user.username, password="password")
        response = client.get(self.url_django_version_viewer_toolbar)
        self.assertEqual(response.status_code, 403)
