class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers are allowed")
        if integer % 2:
            raise Exception("Trying general exception instead of value error")
        super().append(integer)


def create_exception():
    print("create exception is about to do its job")
    raise AttributeError("Random exception")
    print("will not take place cause of exceptions")


def call_create_exception():
    print('Calling create exception')
    create_exception()
    print("man this wo't run")


def try_funny_division(anumber):
    try:
        if anumber == 13:
            raise ValueError("Unlucky number")
        print(100 / anumber)

    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError as e:
        print("Can't velieve you entered 13", e.args)
        # raise
    else:
        print("No exceptions")
    finally:
        print("Always run no matter if there's an exception")


class InvalidDemandError(Exception):
    def __init__(self, demand, availability):
        super().__init__("Cannot satisfy {} demand".format(demand))
        self.demand = demand
        self.availability = availability

    def availability_deficit(self):
        return self.demand - self.availability


def compute_availability_surplus(demand, availability):
    if demand < availability:
        return availability - demand
    else:
        raise InvalidDemandError(demand, availability)


if __name__ == "__main__":
    a = EvenOnly()
    print(a)
    a = EvenOnly([])
    print(a)
    a.append(2)
    print(a)
    try:
        a.append(3)
        print(a)

    except Exception:
        pass

    try:
        call_create_exception()
    except (ValueError, AttributeError):
        print("didn't let exception stop this from running")
    print("executed after exception")

    try_funny_division(1)
    try_funny_division(0)
    try_funny_division("hello")
    try_funny_division(13)

    demand, availability = 4, 1
    try:
        compute_availability_surplus(demand, availability)
    except InvalidDemandError as e:
        print(e.args[0])
        print(e.availability_deficit())
