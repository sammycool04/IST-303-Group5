from mixer.backend.django import mixer
import pytest
pytestmark = pytest.mark.django_db



@pytest.mark.django_db
class TestModels:

    def test_house_is_valid(self):
        house = mixer.blend('house.HouseInfo', price = 100)
        assert house.is_valid == True

    def test_house_is_not_valid(self):
        house = mixer.blend('house.HouseInfo', price = 0)
        assert house.is_valid == False

class TestProductModel:

    def test_save():
        house = House.objects.create(
            summary="Sample house",
            price=500
        )
        assert house.name == "Sample house"
        assert house.price == 500
