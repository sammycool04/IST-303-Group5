from django.urls import reverse, resolve
from Worksample import views

class TestUrls:

    def test_detail_url(self):
        path = reverse('homepg')
        assert resolve(path).view_name == 'homepg'
