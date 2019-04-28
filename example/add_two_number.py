from lazy.ef_app import EfApp
from lazy.effect import composer, lazy
from lazy.utils import input, int, print


@composer
def sum(a, b):
    if a.left != None and b.left != None:
        return 0
    return a.left + b.left

@EfApp
def app():
    number_a = (input("input number 1 : ") << int).attempt()
    number_b = (input("input number 2 : ") << int).attempt()
    app_effect = sum(number_a, number_b) << print
    return app_effect
