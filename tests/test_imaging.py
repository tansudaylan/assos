from assos.imaging import forward_model_image as assos_forward_model_image
from pcat.image import forward_model_image


def test_assos_reexports_pcat_image_forward_model():
    assert assos_forward_model_image is forward_model_image