from django.test import TestCase
from django.core.urlresolvers import reverse


class PlogTestCase(TestCase):
    def assertAdminViewLoads(self, app, model, view, args=()):
        name = 'admin:%s_%s_%s' % (app, model, view)
        url = reverse(name, args=args)
        response = self.client.get(url)

        assert response.status_code == 200, \
            "The %s.%s admin %s view should return 200." % (app, model, view)

        return response

