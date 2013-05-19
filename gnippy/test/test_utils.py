# -*- coding: utf-8 -*-

import ConfigParser
import os
import pwd

test_config_path = "/tmp/.gnippy"
test_username = "TestUserName"
test_password = "testP@ssw0rd"
test_powertrack_url = "https://stream.gnip.com:443/accounts/Organization/publishers/twitter/streams/track/Production.json"
test_rules_url = "https://api.gnip.com:443/accounts/Organization/publishers/twitter/streams/track/Production/rules.json"


def _add_credentials(parser):
    """ Add the Credentials section to a ConfigParser. """
    parser.add_section("Credentials")
    parser.set("Credentials", "username", test_username)
    parser.set("Credentials", "password", test_password)


def _add_power_track_url(parser):
    """ Add the PowerTrack section to a ConfigParser. """
    parser.add_section("PowerTrack")
    parser.set("PowerTrack", "url", test_powertrack_url)


def _write_config_file(parser):
    with open(test_config_path, 'wb') as configfile:
        parser.write(configfile)


def delete_test_config():
    """ Delete the test config if it exists. """
    if os.path.isfile(test_config_path):
        try:
            os.remove(test_config_path)
        except:
            pass


def generate_test_config_file():
    """ Generate a test config file at test_config_path """
    try:
        parser = ConfigParser.SafeConfigParser()
        _add_credentials(parser)
        _add_power_track_url(parser)
        _write_config_file(parser)
    except:
        pass


def generate_test_config_file_with_only_auth():
    """ Generate a test config file at test_config_path """
    try:
        parser = ConfigParser.SafeConfigParser()
        _add_credentials(parser)
        _write_config_file(parser)
    except:
        pass


def generate_test_config_file_with_only_powertrack():
    """ Generate a test config file at test_config_path """
    try:
        parser = ConfigParser.SafeConfigParser()
        _add_power_track_url(parser)
        _write_config_file(parser)
    except:
        pass


def get_current_username():
    return pwd.getpwuid(os.getuid())[0]


def get_possible_home_dirs():
    username = get_current_username()
    return [i % username for i in ["/Users/%s", "/home/%s"]]


def get_possible_config_locations():
    return [os.path.join(i, ".gnippy") for i in get_possible_home_dirs()]

def os_file_exists_false(path):
    """ Used to patch the os.path.isfile method in tests. """
    return False

class Response():
    """ Various sub-classes of Response are used by Mocks throughout tests. """
    status_code = None
    text = None

    def __init__(self, response_code, text):
        self.status_code = response_code
        self.text = text

class BadResponse(Response):
    def __init__(self):
        Response.__init__(self, 500, "Internal Server Error")

class GoodResponse(Response):
    def __init__(self):
        Response.__init__(self, 200, "All OK")