from faker import Faker

class Helpers:
    preset_name = 'Viky'
    preset_email = ''
    preset_password = ''

    @staticmethod
    def generate_email():
        fake = Faker()
        fake.name()

        return f"victoria_kharnovets_9_{fake.random_number(digits=3)}@{fake.domain_name()}"

    @staticmethod
    def generate_password():
        fake = Faker()
        fake.name()

        return fake.password(length=14, special_chars=True, digits=True, upper_case=True, lower_case=True)