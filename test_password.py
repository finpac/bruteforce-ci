from unittest import TestCase


class TestPassword(TestCase):
    def test_check1(selfself):
        pwd = Password("abc")
        self.assertEqual(True, pwd.check("abc"))

    def test_check2(self):
        pwd = Password("bca")
        self.assertEqual(False, pwd.check("abc"))


