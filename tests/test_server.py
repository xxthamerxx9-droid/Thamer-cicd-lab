import unittest
from app.server import get_version, get_status
class TestPulse(unittest.TestCase):
def test_version(self):
self.assertEqual(get_version(), "1.0")
def test_health(self):
self.assertEqual(get_status(), 200)
if __name__ == "__main__":
unittest.main()
