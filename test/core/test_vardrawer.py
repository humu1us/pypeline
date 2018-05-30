from unittest import TestCase
from pypeline.core.vardrawer import VarDrawer


class TestVarDrawer(TestCase):
    def test_var_drawer(self):
        test_value = {
            "name": "var_name",
            "value": 1234
        }

        drawer = VarDrawer()
        drawer.set_var(test_value["name"], test_value["value"])
        self.assertEqual(drawer.get_var(test_value["name"]),
                         test_value["value"])

        drawer.delete_var(test_value["name"])
        self.assertIsNone(drawer.get_var(test_value["name"]))

    def test_multiple_var_drawer(self):
        test_values = [
            {
                "name": "string",
                "value": "var string"
            },
            {
                "name": "list",
                "value": [1, 2, 3, 4, 5]
            },
            {
                "name": "dict",
                "value": {
                    "list": [10, 10000, 50],
                    "tuple": (1, 2, 3, 4, 5),
                    "dict": {"a": 1, "b": 2},
                    "int": 1234
                }
            }
        ]

        drawer = VarDrawer()
        for d in test_values:
            drawer.set_var(d["name"], d["value"])

        for d in test_values:
            self.assertEqual(drawer.get_var(d["name"]), d["value"])

        for d in test_values:
            drawer.delete_var(d["name"])
            self.assertIsNone(drawer.get_var(d["name"]))
