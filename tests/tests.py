import unittest

import json_sort.sorter
jsn = {
            "glossary": {
                "title": "example glossary",
                "GlossDiv": {
                    "title": "S",
                    "GlossList": {
                        "GlossEntry": {
                            "ID": "SGML",
                            "SortAs": "SGML",
                            "GlossTerm": "Standard Generalized Markup Language",
                            "Acronym": "SGML",
                            "Abbrev": "ISO 8879:1986",
                            "GlossDef": {
                                "para": "A meta-markup language, used to create markup languages such as DocBook.",
                                "GlossSeeAlso": ["GML", "XML"]
                            },
                            "GlossSee": "markup"
                        }
                    }
                }
            }
        }

class TestSortOrder(unittest.TestCase):

    def test_sort_order(self):
        jsn2 = {"name": "jason", "bane": "cosmos", "thing": ["world", "hello"], "my_thing": [2, 35, 5, 6, 7, 8]}
        sorted_jsn = json_sort.sorter.sort_from_dict(jsn2)
        keys = sorted_jsn.keys()
        keys = list(keys)
        self.assertEqual(keys[0], "bane")
        self.assertEqual(jsn2["my_thing"][0], 2)

    def test_larger_json(self):
        sorted_jsn = json_sort.sorter.sort_from_dict(jsn)
        jsns = sorted_jsn["glossary"]
        keys = jsns.keys()
        keys = list(keys)
        self.assertEqual(keys[0], "GlossDiv")

    def test_custom_sort(self):
        def predicate(a, b):
            if type(a) is dict or type(b) is dict:
                return True
            else:
                return a > b

        sorted_jsn = json_sort.sorter.sort_from_dict(jsn, predicate=predicate)
        jsns = sorted_jsn["glossary"]
        keys = jsns.keys()
        keys = list(keys)
        self.assertEqual(keys[0], "title")

