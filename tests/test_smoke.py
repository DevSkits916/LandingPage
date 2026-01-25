import pathlib
import unittest


class LandingPageSmokeTest(unittest.TestCase):
    def test_index_has_title(self):
        content = pathlib.Path('index.html').read_text(encoding='utf-8')
        self.assertIn('Travis Ramsey', content)


if __name__ == '__main__':
    unittest.main()
