import importlib.util
from pathlib import Path

import matplotlib.image as mpimg
import numpy as np


EXAMPLE_PATH = Path(__file__).resolve().parents[1] / "examples" / "psf_forward_model.py"
SPECIFICATION = importlib.util.spec_from_file_location(
    "assos_psf_forward_model_example", EXAMPLE_PATH
)
example = importlib.util.module_from_spec(SPECIFICATION)
SPECIFICATION.loader.exec_module(example)


def test_simulated_scene_has_declared_total_flux():
    source_image = example.create_simulated_scene()

    assert source_image.shape == (51, 51)
    np.testing.assert_allclose(source_image.sum(), 1650.0)


def test_psf_forward_model_example_writes_nonblank_png(tmp_path, capsys):
    output_path = tmp_path / "psf_forward_model.png"

    products = example.run_example(output_path)

    image = mpimg.imread(output_path)
    assert image.shape[0] > 100
    assert image.shape[1] > 100
    assert image[..., :3].min() < 0.8
    assert products["observed_image"].max() < products["source_image"].max()
    assert f"Writing to {output_path}..." in capsys.readouterr().out