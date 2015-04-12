from unittest import TestCase
import uuid

from staticargs import staticargs

@staticargs
def append_something(foo=[]):
    foo.append("something")
    return foo

@staticargs
def set_something(foo={}):
    foo_key = uuid.uuid4()
    foo[foo_key] = "something"
    return foo

class TestStaticArgs(TestCase):
    def test_list_not_provided(self):
        for x in range(5):
            assert len(append_something()) == 1
    
    def test_list_provided(self):
        for x in range(5):
            test_uuid = uuid.uuid4()
            list_result = append_something(foo=[test_uuid])
            assert list_result == [test_uuid, "something"]

    def test_dict_not_provided(self):
        for x in range(5):
            assert(len(set_something().keys())) == 1

    def test_dict_provided(self):
        for x in range(5):
            test_uuid = uuid.uuid4()
            dict_result = set_something(foo={test_uuid:"test value"})
            assert dict_result[test_uuid] == "test value"
            assert len(dict_result) == 2
