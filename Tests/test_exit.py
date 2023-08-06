import locators as l
import pages as p

def test_exit_profile(user, authorization):
    user.push_the_button(l.user_account_button)
    user.push_the_button(l.exit_button)
    user.push_the_button(l.user_account_button)
    assert user.check_url() == p.login_page
