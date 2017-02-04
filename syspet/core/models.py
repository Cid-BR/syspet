from django.db import models


class Person(models.Model):
    '''
        Person
    '''
    company_name = models.CharField('razão social', max_length=255)
    fantasy_name = models.CharField('nome fantasia', max_length=255)
    TYPE_J = "Pessoa Jurídica"
    TYPE_F = "Pessoa Fisíca"
    TYPE_PERSON = (
        ("F", TYPE_F),
        ("J", TYPE_J),
    )
    person_type = models.CharField('tipo pessoa', max_length=1, choices=TYPE_PERSON)
    cpnj_cpf = models.CharField('CNPJ/CPF', max_length=20)
    address = models.CharField('logradouro', max_length=255, blank=True)
    number_address = models.CharField('N.', max_length=60, blank=True)
    neighborhood = models.CharField('bairro', max_length=255, blank=True)
    zip_code = models.CharField('CEP', max_length=15, blank=True)
    city = models.CharField('cidade', max_length=255, blank=True)
    state = models.CharField('uf', max_length=2, blank=True)
    phone = models.CharField('telefone', max_length=20, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.company_name
