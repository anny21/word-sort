import unittest

import sort


class TestSort(unittest.TestCase):

    def test_inValid_paths(self):
        result = sort.check_file("wordss.txt", "paragraphs.txt")
        self.assertEqual(result, "Invalid file")

    def test_return_val_is_dict(self):
        result = sort.find("words.txt", "paragraph.txt")
        self.assertTrue(isinstance(result, dict))


