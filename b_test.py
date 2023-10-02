# class Employee:
#
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = "{}.{}@email.com".format(self.first, self.last)
#
#     def fullname(self):
#         return "{} {}".format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)
#
#     def __repr__(self):
#         return "Employee('{}', '{}', '{}')".format(self.first,
#                                                    self.last, self.pay)
#
#     def __str__(self):
#         return "{} - {}".format(self.fullname(), self.email)
#
#     def __add__(self, other):
#         return "{}".format(format((self.pay + other.pay), ','))
#
#     def __len__(self):
#         return len(self.fullname())
#
#
# def main():
#
#     emp_1 = Employee('Test', 'User', 55000)
#     emp_2 = Employee('Joe', 'Wambua', 45000)
#
#     # print(emp_1)
#     print(emp_1 + emp_2)
#
#
# main()


# def dec_funct(origin_funct):
#     def wrap_funct(*args, **kwargs):
#         print("Wrapper exec'd this before {}()".format(origin_funct.__name__))
#         return origin_funct(*args, **kwargs)
#     return wrap_funct


# @dec_funct
# def display():
#     print("Display function OK")
from functools import wraps


def my_log(orig_funct):
    import logging
    logging.basicConfig(filename="{}.log"
                        .format(orig_funct.__name__), level=logging.INFO)

    @wraps(orig_funct)
    def wrapper(*args, **kwargs):
        logging.info(
            "Ran with args: {}, & kwargs: {}".format(args, kwargs))
        return orig_funct(*args, **kwargs)

    return wrapper


def my_timer(orig_funct):
    import time

    @wraps(orig_funct)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_funct(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in {:.8f} sec".format(orig_funct.__name__, t2))
        return result

    return wrapper()


@my_log
# @my_timer
def info_displ(name):
    import time

    time.sleep(1)
    print("info_displ ran with args ({})".format(name))


info_displ('Milan')
