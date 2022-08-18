# Pattern for writing tests
# 1. Arrange (fixture)
# 2. Act
# 3. Assert

import os
import pytest
from website.models import House, UserProfile
import datetime

@pytest.mark.skipif(os.system("service postgresql status") == 768,
                    reason="PostgreSQL service is not running")
def test_house(new_house):
    # print(os.system("service postgresql status"))
    print("House Name: "+ new_house.name)
    print("Room Type: "+ new_house.room)
    print("Description: "+new_house.description)
    print(f"Price: RM {new_house.price}")
    print("Accommodation Type: "+new_house.accommodationtype)
    print("Image: "+ str(new_house.image))
    print("Thumbnail: "+ str(new_house.thumbnail))

    assert House.objects.count() == 1
    assert new_house.name == 'Serin Residence, Cyberjaya'
    assert new_house.room == 'Master Bedroom'
    assert new_house.description == 'TV, Car park, Washing machine, Water heater, Wifi, Gym'
    assert new_house.price == 500.00
    assert new_house.accommodationtype == 'Entire House'
    assert new_house.image == 'uploads/serin.jpg'
    assert new_house.thumbnail == 'uploads/uploads/serin.jpg'

@pytest.mark.skipif(os.system("service postgresql status") == 768,
                    reason="PostgreSQL service is not running")
def test_update_house(new_house):
    new_house.name = 'Cyberia, Cyberjaya'
    new_house.price = 200.00
    new_house.save()
    updated_house = House.objects.get(name='Cyberia, Cyberjaya')
    print("Updated House Name: "+ updated_house.name)
    print(f"Updated Price: RM {updated_house.price}")
    assert updated_house.name == 'Cyberia, Cyberjaya'
    assert updated_house.price == 200.00
    
@pytest.mark.skipif(os.system("service postgresql status") == 768,
                    reason="PostgreSQL service is not running")
def test_housemate(new_housemate):
    print("Full Name: "+ new_housemate.fullname)
    print("Username: "+ new_housemate.username)
    print("Phone Number: "+ new_housemate.phonenumber)
    print("Date of Birth: "+ new_housemate.dateofbirth)
    print("Gender: "+ new_housemate.gender)
    print("Orientation: "+ new_housemate.orientation)
    print("Religion "+ new_housemate.religion)
    print("Occupation "+ new_housemate.occupation)
    print("Bio: "+ new_housemate.bio)
    print("HasRoom: "+ new_housemate.HasRoom)
    print("Pet: "+ new_housemate.pet)
    
    assert UserProfile.objects.count() == 1
    assert new_housemate.fullname == 'Shafiq Aiman'
    assert new_housemate.username == 'shafiqaiman'
    assert new_housemate.phonenumber == '0123456789'
    assert new_housemate.dateofbirth == '2000-06-20'
    assert new_housemate.gender == 'Male'
    assert new_housemate.orientation == 'Straight'
    assert new_housemate.religion == 'Muslim'
    assert new_housemate.occupation == 'Student'
    assert new_housemate.bio == 'Hi! Im Shafiq, 23 y/o and I work in a startup (very creative) so hit me up!'
    assert new_housemate.HasRoom == 'Needs A Room'
    assert new_housemate.pet == 'Yes'

@pytest.mark.skipif(os.system("service postgresql status") == 768,
                    reason="PostgreSQL service is not running")
def test_update_housemate(new_housemate):
    new_housemate.fullname = 'Wayne Rooney'
    new_housemate.dateofbirth = '2000-01-10'
    new_housemate.save()
    updated_housemate = UserProfile.objects.get(fullname='Wayne Rooney')
    print("Updated Full Name: "+ updated_housemate.fullname)
    print("Updated Date of Birth: "+ str(updated_housemate.dateofbirth))
    assert updated_housemate.fullname == 'Wayne Rooney'
    assert updated_housemate.dateofbirth == datetime.date(2000, 1, 10)


