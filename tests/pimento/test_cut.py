from io import BytesIO

from PIL import Image

from pimento.cut import cut_out


class TestCutout:

    DEBUG = False

    def test_cut_out_one_polygon_no_fill_color(self, resources):
        expected_result = resources / "pimento" / "cut" / "expected" / "cut_out_one_polygon_no_fill_color.jpg"
        polygon = [(15, 8), (368, 78), (325, 161), (14, 71)]
        with Image.open(resources / "some_text.jpg") as image:
            cut_out(image, polygon)
            if self.DEBUG:
                image.show()
                if not expected_result.exists():
                    image.save(expected_result)
            image_bytes = BytesIO()
            image.save(image_bytes, format="jpeg")
        image_bytes.seek(0)
        assert image_bytes.read() == expected_result.read_bytes()

    def test_cut_out_no_polygon(self, resources):
        expected_result = resources / "pimento" / "cut" / "expected" / "cut_out_no_polygon.jpg"
        with Image.open(resources / "some_text.jpg") as image:
            cut_out(image)
            if self.DEBUG:
                image.show()
                if not expected_result.exists():
                    image.save(expected_result)
            image_bytes = BytesIO()
            image.save(image_bytes, format="jpeg")
        image_bytes.seek(0)
        assert image_bytes.read() == expected_result.read_bytes()

    def test_cut_out_multi_polygon_and_color(self, resources):
        expected_result = resources / "pimento" / "cut" / "expected" / "cut_out_muti_polygon_and_color.jpg"
        polygons = (
            [(15, 8), (368, 78), (325, 161), (14, 71)],
            [(100, 0), (150, 0), (125, 20)],
            [(0, 150), (200, 150), (200, 178), (0, 178)],
        )
        with Image.open(resources / "some_text.jpg") as image:
            cut_out(image, *polygons, fillcolor=(255, 0, 255))
            if self.DEBUG:
                image.show()
                if not expected_result.exists():
                    image.save(expected_result)
            image_bytes = BytesIO()
            image.save(image_bytes, format="jpeg")
        image_bytes.seek(0)
        assert image_bytes.read() == expected_result.read_bytes()
