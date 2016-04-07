import unittest
from unittest.mock import MagicMock, create_autospec
from app import App
from renderer.renderer import Renderer


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.input = MagicMock()
        # swipe somewhere (south):
        self.input.getline = MagicMock(return_value='s')

        self.output = MagicMock()
        self.output.write = MagicMock()

        self.app = App(self.input, self.output)
        self.app.renderer = create_autospec(Renderer)  # type: MagicMock

    def test_runZeroTimesRendersOnce(self):
        self.app.run(max_prompts=0)
        count = len(self.app.renderer.mock_calls)
        self.assertEqual(
            1,
            count,
            "Method render on Renderer should be called one time."
        )

    def test_runOneTimeSwipingSouthRendersTwice(self):
        self.app.run(max_prompts=1)
        count = len(self.app.renderer.mock_calls)
        self.assertEqual(
            2,
            count,
            "Method render on Renderer should be called two times."
        )
