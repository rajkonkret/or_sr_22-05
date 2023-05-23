from pprint import pprint


class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f'{self.name!r}, {self.email!r}'


# Suplier dziedziczy po Contact
class Suplier(Contact):
    """
    Dziedziczy po klasie Contact
    """

    # pass
    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


# z !r
# 'Adam', 'admin@wp.pl'

c1 = Contact("Adam", "admin@wp.pl")
c2 = Contact("Radek", "admin@wp.pl")
c3 = Contact("Krzys", "admin@wp.pl")
c4 = Contact("Arek", "admin@wp.pl")
print(c1)
s = Suplier("Tomasz", "tomasz@wp")
print(s)
s.order("kawa")
print(s.all_contacts)
print(c1.all_contacts)

# pprint do ładniejszego wyswietlania obiektów
pprint(c1.all_contacts)