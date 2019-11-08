from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestModels:

    def test_house_is_valid(self):
        house = mixer.blend('house.HouseInfo', price = 100)
        assert house.is_valid == True

    def test_house_is_not_valid(self):
        house = mixer.blend('house.HouseInfo', price = 0)
        assert house.is_valid == False
