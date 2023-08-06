import locators as l
import pages as p


def test_my_profile_constructor(user, authorization):
    user.push_the_button(l.user_account_button)
    user.push_the_button(l.constuctor_button)
    assert user.check_url() == p.main_page


def test_my_profile_main_icon(user, authorization):
    user.push_the_button(l.user_account_button)
    user.push_the_button(l.main_icon)
    assert user.check_url() == p.main_page
