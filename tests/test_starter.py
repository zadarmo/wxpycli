import unittest
import os
import shutil


class TestStarter(unittest.TestCase):
    def test_scrapy(self):
        STARTER_NAME = "scrapy_starter"

        os.chdir("../")
        os.system("python main.py scrapy_starter")
        self.assertTrue(os.path.exists(STARTER_NAME))
        shutil.rmtree(STARTER_NAME)


if __name__ == '__main__':
    unittest.main()
