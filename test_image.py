from image_editor.test import test

try:
    test.test_downscale()
except Exception as e:
    print(e)
