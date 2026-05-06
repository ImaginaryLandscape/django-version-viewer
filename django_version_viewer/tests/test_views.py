import json
from unittest import mock

from django.contrib.auth.models import User
from django.test import Client, TestCase

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class MockDistribution:
    def __init__(self, name, version, home_page=""):
        self.metadata = {
            "Name": name,
            "Home-page": home_page,
        }
        self.version = version


class TestVersionViewer(TestCase):

    url_django_version_viewer = reverse("django_version_viewer")
    url_django_version_viewer_csv = reverse("django_version_viewer_csv")
    url_django_version_viewer_toolbar = reverse("django_version_viewer_toolbar")

    mock_data = [
        {"name": "appdirs", "version": "1.4.3"},
        {"name": "django", "version": "1.8.18"},
        {"name": "six", "version": "1.10.0"},
    ]

    def mocked_distributions(self):
        return [
            MockDistribution(d["name"], d["version"])
            for d in self.mock_data
        ]

    def setUp(self):
        self.admin = User.objects.create_superuser(
            email="adminmail@mail.com",
            username="admin_user",
            password="password",
        )
        self.user = User.objects.create(
            email="user@usermail.com",
            username="regular_user",
            password="password",
        )

    def tearDown(self):
        self.admin.delete()
        self.user.delete()

    def test_django_version_viewer_view__admin(self):
        client = Client()
        client.login(username=self.admin.username, password="password")

        with mock.patch(
            "django_version_viewer.pip_viewer.metadata.distributions",
            return_value=self.mocked_distributions(),
        ):
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

        with mock.patch(
            "django_version_viewer.pip_viewer.metadata.distributions",
            return_value=self.mocked_distributions(),
        ):
            response = client.get(self.url_django_version_viewer_csv)
            self.assertEqual(
                response.content,
                b"Package Name,Package Version\r\n"
                b"appdirs,1.4.3\r\n"
                b"django,1.8.18\r\n"
                b"six,1.10.0\r\n",
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

        with mock.patch(
            "django_version_viewer.pip_viewer.metadata.distributions",
            return_value=self.mocked_distributions(),
        ):
            response = client.get(self.url_django_version_viewer_toolbar)
            context_packages = response.context["packages"]

            for i in range(3):
                self.assertEqual(
                    self.mock_data[i]["name"],
                    context_packages[i]["package_name"],
                )
                self.assertEqual(
                    self.mock_data[i]["version"],
                    context_packages[i]["package_version"],
                )

        self.assertEqual(response.status_code, 200)

    def test_django_version_viewer_toolbar_view__user(self):
        client = Client()
        client.login(username=self.user.username, password="password")
        response = client.get(self.url_django_version_viewer_toolbar)
        self.assertEqual(response.status_code, 403)
