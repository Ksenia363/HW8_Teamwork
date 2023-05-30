def add_contact() -> None:
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')

def show_contact() -> None:
    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())

def find_contact() -> None:
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)

def search(book: str, info: str) -> list[str]:
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))