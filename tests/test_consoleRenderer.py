import unittest
from unittest.mock import MagicMock

from console.console_renderer import ConsoleRenderer


class ConsoleRendererTestCase(unittest.TestCase):
    def setUp(self):
        self.output = MagicMock()
        self.output.write = MagicMock()
        self.console_renderer = ConsoleRenderer(self.output)

    def test_rendering(self):
        """
        Tests that the Renderer renders the GameField correctly.
        """
        self.fail()
