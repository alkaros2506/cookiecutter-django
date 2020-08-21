from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "{{ cookiecutter.project_slug }}.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import lean_django_drf_app.users.signals  # type: ignore # noqa F401 # pylint: disable=W0611,C0415
        except ImportError:
            pass
