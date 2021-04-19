from io import BytesIO

import cv2
from PIL import Image

from imforge.color import remove_color_cv2, keep_color_cv2


class TestColorCv2:

    DEBUG = False

    def test_remove_red_default_background(self, resources):
        expected_result = resources / "imforge" / "color" / "expected" / "cv2" / "remove_red_default_background.png"
        image = cv2.imread(str(resources / "some_text.jpg"), cv2.IMREAD_UNCHANGED)
        remove_color_cv2(image, min_color=(0, 128, 128), max_color=(0, 255, 255))
        # Use PIL image for saving and comparison of result
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), "RGB")
        if self.DEBUG:
            image.show()
            if not expected_result.exists():
                image.save(expected_result, optimize=True)
        image_bytes = BytesIO()
        image.save(image_bytes, format="png", optimize=True)
        image_bytes.seek(0)
        assert image_bytes.read() == expected_result.read_bytes()

    def test_remove_red_blue_background(self, resources):
        expected_result = resources / "imforge" / "color" / "expected" / "cv2" / "remove_red_blue_background.png"
        image = cv2.imread(str(resources / "some_text.jpg"), cv2.IMREAD_UNCHANGED)
        remove_color_cv2(image, min_color=(0, 128, 128), max_color=(0, 255, 255), fillcolor=(255, 0, 0))
        # Use PIL image for saving and comparison of result
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), "RGB")
        if self.DEBUG:
            image.show()
            if not expected_result.exists():
                image.save(expected_result, optimize=True)
        image_bytes = BytesIO()
        image.save(image_bytes, format="png", optimize=True)
        image_bytes.seek(0)
        assert image_bytes.read() == expected_result.read_bytes()

    def test_keep_red_default_background(self, resources):
        expected_result = resources / "imforge" / "color" / "expected" / "cv2" / "keep_red_default_background.png"
        image = cv2.imread(str(resources / "some_text.jpg"), cv2.IMREAD_UNCHANGED)
        keep_color_cv2(image, min_color=(0, 128, 128), max_color=(0, 255, 255))
        # Use PIL image for saving and comparison of result
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), "RGB")
        if self.DEBUG:
            image.show()
            if not expected_result.exists():
                image.save(expected_result, optimize=True)
        image_bytes = BytesIO()
        image.save(image_bytes, format="png", optimize=True)
        image_bytes.seek(0)
        assert image_bytes.read() == expected_result.read_bytes()

    def test_keep_red_blue_background(self, resources):
        expected_result = resources / "imforge" / "color" / "expected" / "cv2" / "keep_red_blue_background.png"
        image = cv2.imread(str(resources / "some_text.jpg"), cv2.IMREAD_UNCHANGED)
        keep_color_cv2(image, min_color=(0, 128, 128), max_color=(0, 255, 255), fillcolor=(255, 0, 0))
        # Use PIL image for saving and comparison of result
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), "RGB")
        if self.DEBUG:
            image.show()
            if not expected_result.exists():
                image.save(expected_result, optimize=True)
        image_bytes = BytesIO()
        image.save(image_bytes, format="png", optimize=True)
        image_bytes.seek(0)
        assert image_bytes.read() == expected_result.read_bytes()
