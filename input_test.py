import pytest

def enter_meals():
    breakfast_input = input("Enter breakfast:")
    lunch_input = input("Enter lunch:")
    dinner_input = input("Enter dinner:")
    breakfast_input = input("Enter snack:")
    print("Hello " + name + " " + name2)
    return "Hello " + name + " " + name2

if __name__ == "__main__":
    say_hello()

""" TEST """
def test_say_hello(monkeypatch):
    inputs = iter(['Pavol', 'Kutaj'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = say_hello()
    assert result == "Hello Pavol Kutaj"