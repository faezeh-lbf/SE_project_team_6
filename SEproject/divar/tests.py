from django.test import TestCase
from django.core.urlresolvers import reverse


# Create your tests here.
from divar.models import Stuff


def create_stuff(name, price, description, city, location):
    """
    Creates a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """

    return Stuff.objects.create(name= name, price= price, description= description, city= city, location= location)


class StuffViewTests(TestCase):
    def test_index_view_with_no_stuffs(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('showStuff'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "")
        self.assertQuerysetEqual(response.context['latest_stuff_list'], [])
