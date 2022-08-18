import pytest
from django.contrib.auth.models import User
from website.models import House, UserProfile

# from faker import Faker
# fake = Faker()



@pytest.fixture
def new_house(db) -> House:
    return House.objects.create(
        name='Serin Residence, Cyberjaya', 
        room = 'Master Bedroom',
        description = 'TV, Car park, Washing machine, Water heater, Wifi, Gym',
        price = 500.00,
        accommodationtype = 'Entire House',
        image = 'uploads/serin.jpg',
        thumbnail = 'uploads/uploads/serin.jpg'
        )

@pytest.fixture
def new_housemate(db) -> UserProfile:
    return UserProfile.objects.create(
        fullname='Shafiq Aiman', 
        username = 'shafiqaiman',
        phonenumber = '0123456789',
        dateofbirth='2000-06-20',
        gender = 'Male',
        orientation = 'Straight',
        religion = 'Muslim',
        occupation = 'Student',
        bio = 'Hi! Im Shafiq, 23 y/o and I work in a startup (very creative) so hit me up!',
        HasRoom = 'Needs A Room',
        pet = 'Yes'
        
        )



