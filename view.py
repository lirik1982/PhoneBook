from db import Session
from models import Contact, PhoneNumber
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

from faker import Faker
from random import randint


def create_contact():
    name = input('Веедите имя: ')
    session = Session()
    contact = Contact(name)
    session.add(contact)
    while True:
        ch = input('Добавить номер (Y/N) ')
        if ch == 'Y' or ch == 'y':
            number = input()
            phone = PhoneNumber(number)
            contact.phones.append(phone)
        else:
            break
    session.commit()
    session.close()


def add_to_contact(name):
    session = Session()
    try:
        contact = session.query(Contact).filter(
            Contact.name.like(f'%{name}%')).one()
    except MultipleResultsFound:
        print('Уточните имя, несколько результатов')
    except NoResultFound:
        print('Записей с таким именем не найдено')

    while True:
        ch = input('Добавить номер (Y/N): ')
        if ch == 'Y' or ch == 'y':
            number = input()
            phone = PhoneNumber(number)
            contact.phones.append(phone)
        else:
            break
    session.commit()
    session.close()


def seach_by_number(number):
    session = Session()
    try:
        phone = session.query(PhoneNumber).filter(
            PhoneNumber.phone == number
        ).one()
        print(phone)
        contact = session.query(Contact).filter(
            Contact.id == phone.contact_id
        ).one()
        print(contact)
    except MultipleResultsFound:
        print('Уточните имя, несколько результатов')
    except NoResultFound:
        print('Записей с таким номером не найдено')
    else:
        print(f"Номер '{phone}' принадлежит '{contact}'")
        session.close()


def seach_by_name(name):
    session = Session()
    try:
        contact = session.query(Contact).filter(
            Contact.name.like(f'%{name}%')).one()
        phones = session.query(PhoneNumber).filter(
            PhoneNumber.contact_id == contact.id
        ).all()
        print(f'К контакту {contact} привязаны номера:')
        for phone in phones:
            print(phone)
    except MultipleResultsFound:
        print('Уточните имя, несколько результатов')
    except NoResultFound:
        print('Записей с таким номером не найдено')
    else:
        session.close()


def del_by_name(name):
    session = Session()
    try:
        contact = session.query(Contact).filter(
            Contact.name.like(f'%{name}%')
        ).one()

        phones = session.query(PhoneNumber).filter(
            PhoneNumber.contact_id == contact.id
        ).all()

        session.delete(contact)
        print(f'Удален контакт {contact}')
        for phone in phones:
            session.delete(phone)
            print(f'Удален привязанный номер {phone}')
    except MultipleResultsFound:
        print('Уточните имя, несколько результатов')
    except NoResultFound:
        print('Записей с таким номером не найдено')
    else:
        session.commit()
        session.close()


def del_phone(number):
    session = Session()
    try:
        phone = session.query(PhoneNumber).filter(
            PhoneNumber.phone == number
        ).one()
        session.delete(phone)
        print(f'Удален номер {phone}')
    except MultipleResultsFound:
        print('Уточните номер, несколько результатов')
    except NoResultFound:
        print('Записей с таким номером не найдено')
    else:
        session.commit()
        session.close()


def show_all():
    session = Session()
    try:
        contacts = session.query(Contact).all()
        for contact in contacts:
            phones = session.query(PhoneNumber).filter(
                PhoneNumber.contact_id == contact.id
            ).all()
            print('-=' * 30)
            print(f'У контакта "{contact}" имеются номера:')
            for phone in phones:
                print(phone)

    except MultipleResultsFound:
        print('Уточните имя, несколько результатов')
    except NoResultFound:
        print('Записей с таким номером не найдено')
    else:
        session.close()


def seed_base(number):
    fake = Faker()
    fake = Faker(locale="ru_RU")
    try:
        session = Session()

        for _ in range(number):
            contact = Contact(fake.name())
            session.add(contact)

            for _ in range(randint(1, 3)):
                phone = PhoneNumber(f'+91{fake.msisdn()[3:]}')
                contact.phones.append(phone)
            session.commit()
    except Exception as e:
        print('error', e)
    else:
        session.close()
