from pprint import pprint


class ContactList(list['Contact']):

    def search(self, name):
        matching_contacts = []
        for c in self:
            if name in c.name:
                matching_contacts.append(c)
        return matching_contacts


class LongestKeyDisct(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f'{self.name!r}, {self.email!r}'


class Suplier(Contact):

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


class Friend(Suplier, Contact):

    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

    # przy wielodziedziczeniu, mozna wskazac z której klasy ma byc uzyta metoda
    # def order(self, order):
    #     super(Suplier, self).order()

    def __repr__(self):
        return f'{self.name!r}, {self.email!r}, +48 {self.phone!r}'


c1 = Contact("Adam", "adam@wp.pl")
print(c1)
print(c1.all_contacts)
s = Suplier("Radek", "radek@wp.pl")
print(s.all_contacts)
s.order("kawa")
pprint(c1.all_contacts)
# (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
print(Friend.__mro__)
f = Friend("JArek", "jarek@wp.pl", "567456789")
print(c1.all_contacts)
f.order("ciatko")

art = LongestKeyDisct()
art['tomasz'] = 12
art['Abraham'] = 122
art['zen'] = 1
# Abraham
print(art.longest_key())
print(art)
