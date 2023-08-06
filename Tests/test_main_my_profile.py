import locators as l
import pages as p


def test_main_my_profile(user, authorization):
    user.push_the_button(l.user_account_button)
    assert user.check_url() == p.profile_page
