import locators as l
import pages as p
import time


def test_switch_ingredients_bread(user):
    user.open_site(p.main_page)
    assert 'current' in user.switch_ingredients('Булки')


def test_switch_ingredients_sauses(user):
    user.open_site(p.main_page)
    assert 'current' in user.switch_ingredients('Соусы')


def test_switch_ingredients_filling(user):
    user.open_site(p.main_page)
    assert 'current' in user.switch_ingredients('Начинки')
