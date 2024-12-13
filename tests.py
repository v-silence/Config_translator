import unittest
from Config_Translator import ConfigTranslator

class TestConfigTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = ConfigTranslator()

    def test_simple_values(self):
        self.assertEqual(self.translator.format_value(42), "42")
        self.assertEqual(self.translator.format_value("test"), "'test'")
        self.assertEqual(self.translator.format_value(3.14), "3.14")

    def test_arrays(self):
        self.assertEqual(self.translator.format_value([1, 2, 3]), "#(1, 2, 3)")
        self.assertEqual(
            self.translator.format_value(["a", "b"]),
            "#('a', 'b')"
        )

    def test_dictionaries(self):
        self.assertEqual(
            self.translator.format_value({"a": 1, "b": 2}),
            "{a => 1, b => 2}"
        )

    def test_nested_structures(self):
        nested = {
            "arr": [1, {"x": 10}],
            "dict": {"y": [1, 2, 3]}
        }
        expected = "{arr => #(1, {x => 10}), dict => {y => #(1, 2, 3)}}"
        self.assertEqual(self.translator.format_value(nested), expected)

    def test_constants(self):
        data = {
            "_constants": {
                "MAX": 100,
                "NAMES": ["a", "b"]
            },
            "value": "[MAX]",
            "list": "[NAMES]"
        }
        result = self.translator.process_constants(data)
        expected = "MAX: 100\nNAMES: #('a', 'b')\n{value => '[MAX]', list => '[NAMES]'}"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
