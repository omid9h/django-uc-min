import os
import sys

from django.conf import settings
from django.urls import path
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from django.template import RequestContext, Template

settings.configure(
    DEBUG=False,
    ALLOWED_HOSTS=["*"],
    ROOT_URLCONF=__name__,
    SECRET_KEY=os.environ.get("SECRET_KEY", "chnagethissecret"),
    TEMPLATES=[{"BACKEND": "django.template.backends.django.DjangoTemplates"}],
    MIDDLEWARE_CLASSES=(
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ),
)


def home(request):
    context = RequestContext(
        request, {"content": "Optional Content"}
    )
    return HttpResponse(MAIN_HTML.render(context))


urlpatterns = [
    path("", home),
]

app = get_wsgi_application()


MAIN_HTML = Template(
    """ """
)


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
