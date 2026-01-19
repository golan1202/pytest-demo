import math
from source import shapes
import logging
logger = logging.getLogger(__name__)


class TestCircle:

    def setup_method(self, method):
        logger.info(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        logger.info(f"Tearing down {method}")
        del self.circle

    def test_radius(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius