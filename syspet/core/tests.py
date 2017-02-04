from django.test import TestCase

from syspet.core.models import Person


class PersonModelTest(TestCase):
    def setUp(self):
        self.company_name = 'Razão1'
        self.person = Person.objects.create(
            company_name=self.company_name,
            fantasy_name='Fantasia1',
            person_type=Person.TYPE_F,
            cpnj_cpf='000.000.000-00'
        )

    def test_create(self):
        self.assertTrue(Person.objects.exists())

    def test_str(self):
        self.assertEqual(self.company_name, str(self.person))