import unittest
from unittest.mock import MagicMock, call
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

    def test_runOneTimeSwipingSouthRendersTwice(self):
        self.app.run(max_prompts=1)
        count = self.output.write.mock_calls.count(call.write('rendering...'))
        self.assertEqual(
            2,
            count,
            '\'rendering...\' should be printed two times.'
        )
