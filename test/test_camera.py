import os
import pytest
from hadrian.connections.camera import Camera

@pytest.fixture
def camera(tmp_path):
    image_path = tmp_path / "test_image.jpg"
    return Camera(str(image_path))

def test_camera_take_image(camera):
    camera.take_image()
    assert os.path.exists(camera.save_path), "Image was not saved at the specified path"
