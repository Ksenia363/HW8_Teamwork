import view, model

while True:
    view.menu()
    key = int(input())
    if key == 1:
        model.add_contact()
    elif key == 2:
        model.show_contact()
    elif key == 3:
        model.find_contact()
    else:
        break