from django.urls import reverse, resolve
from Worksample import views

class TestUrls:

    def test_homepg_url(self):
        path = reverse('homepg')
        assert resolve(path).view_name == 'homepg'

    def test_signup_url(self):
        path = reverse('signup')
        assert resolve(path).view_name == 'signup'

    def test_searchByAdd_url(self):
        path = reverse('searchByAdd')
        assert resolve(path).view_name == 'searchByAdd'

    def test_sbAdd_url(self):
        path = reverse('sbAdd')
        assert resolve(path).view_name == 'sbAdd'

    def test_searchByPre_url(self):
        path = reverse('searchByPre')
        assert resolve(path).view_name == 'searchByPre'

    def test_sbPre_url(self):
        path = reverse('sbPre')
        assert resolve(path).view_name == 'sbPre'
