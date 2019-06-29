from django.core.urlresolvers import reverse
from divar.models import UserProfile
from django.test import TestCase
from django.contrib.auth.models import User
from divar import views
from django.contrib.auth import login, authenticate
class UserProfileViewTest(TestCase):
    def setUp(self):
        # Create two users
        test_user1 = User.objects.create_user(username='testuser1@gmail.com', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2@gmail.com', password='2HJ1vRV0Z&3iD')
        user1p=UserProfile.objects.create(user=test_user1, phone_number="12345678")
        user2p = UserProfile.objects.create(user=test_user2, phone_number="12345679")
        test_user1.save()
        test_user2.save()
        user1p.save()
        user2p.save()

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1@gmail.com', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('user_profile'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1@gmail.com')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'user_profile.html')
    # def test_view_url_exists_at_desired_location(self):
    #     response = self.client.get('/divar/user_profile/')
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_view_url_accessible_by_name(self):
    #     response = self.client.get(reverse('user_profile'))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_view_uses_correct_template(self):
    #     response = self.client.get(reverse('user_profile'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'user_profile.html')
    #
    # def test_show_userProfile(self):
    #     user = User.objects.create_user(username="mahsa@gmail.com")
    #     user_profile=UserProfile.objects.create(user=user, phone_number="12345678")
    #     url = reverse('user_profile', args=(user_profile.id,))
    #     response = self.client.get(url)
    #     self.assertContains(response, user_profile.user.mail)
    #     self.assertContains(response, user_profile.user.password)
    #

    # def test_detail_view_with_a_userprofile(self):
    #     """
    #     The detail view of a question with a pub_date in the past should
    #     display the question's text.
    #     """
    #     user = User.objects.create_user(username="mahsa@gmail.com")
    #     user_p=UserProfile.objects.create(user=user, phone_number="12345678")
    #     url = reverse('user_profile')
    #     response = self.client.get(url)
    #     self.assertContains(response, user_p.user.username)

# class ShowStuff(generic.ListView):
#     template_name = 'showStuffByTime.html'
#     context_object_name = 'stuffList'
#
#     def get_queryset(self):
#         return Stuff.objects.order_by('id')[:20]
# def create_stuff(, days):
#     """
#     Creates a question with the given `question_text` and published the
#     given number of `days` offset to now (negative for questions published
#     in the past, positive for questions that have yet to be published).
#     # """
    # time = timezone.now() + datetime.timedelta(days=days)
    # return Question.objects.create(question_text=question_text, pub_date=time)

class ShowStuffViewTest(TestCase):
    # @classmethod
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/divar/home/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('showStuff'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('showStuff'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'showStuffByTime.html')

