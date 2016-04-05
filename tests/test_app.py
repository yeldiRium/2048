import unittest
from unittest.mock import MagicMock
from app import App


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.input = MagicMock()
        # swipe somewhere (south):
        self.input.getline = MagicMock(return_value='s')

        self.output = MagicMock()
        self.output.write = MagicMock()

        self.app = App(self.input, self.output)

    def test_runZeroTimesRendersOnce(self):
        self.app.run(max_prompts=0)
        self.output.write.assert_any_call('rendering...')
