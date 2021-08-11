from datetime import datetime


def birthday100(name, age):
    last = 100 - age
    if last < 0:
        print(f"Hey {name}, you are already older than 100 years")
    else:
        year = datetime.now().year
        print(f"Hey {name}, your 100th birthday will be in {year + last}")


if __name__ == "__main__":
    birthday100('Alice', 100)
    birthday100('Bob', 45)
    birthday100('Cooper', 102)
