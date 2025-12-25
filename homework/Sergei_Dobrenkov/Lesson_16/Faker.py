from faker import Faker

fake = Faker(locale='ru_RU')

for _ in range(50):
    print(fake.name())
    print(fake.job())
    print(fake.address())
