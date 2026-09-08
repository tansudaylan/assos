# Assos

Assos is a forward-modeling package for imaging data in the active astrophysics ecosystem. It is designed to synthesize observational imaging products, apply model-driven diagnostics, and provide a reproducible path from input image assumptions to transformed, diagnostic, and summary outputs.

## Scientific purpose

The package supports imaging-domain forward modeling for astrophysical scenes and catalog-level overlays. The core workflow is to construct a synthetic image or parameterized field, model the relevant structure, and visualize the result alongside diagnostic annotations or residual diagnostics.

## Current ecosystem role

Assos sits in the imaging and forward-modeling layer of the active stack. It builds on the shared numerical utilities in `tdpy`, overlaps conceptually with the lensing and image-simulation work in `chalcedon`, and contributes to the broader time-domain and imaging workflow around the active scientific repositories.

## Installation

```bash
cd assos
python -m pip install -e .
```

## Minimal workflow

The project is organized around reusable functions rather than long standalone scripts. The most important package entry points are accessed through the library interface and the core modeling routines in `assos/main.py`.

A lightweight smoke check is intended to confirm that the library loads and exposes its main entry points without requiring a full imaging dataset:

```python
import assos
from assos.main import plot_imag

print(hasattr(assos, '__file__'))
print(callable(plot_imag))
```

## Main modules

- `assos/main.py`: imaging forward-modeling routines, plotting diagnostics, and workflow initialization.
- `tests/`: lightweight import and compatibility checks.

## Dependencies

The package depends on the standard scientific stack and imaging utilities, including:

- `numpy`
- `scipy`
- `matplotlib`
- `astropy`
- `h5py`
- `tdpy`
- `chalcedon`
- `nicomedia`
- `aspendos`

## Output behavior

Assos is intended to make imaging transformations and model assumptions visible through saved diagnostic figures. The main scientific emphasis is on keeping the model-data relationship inspectable rather than hiding it inside opaque processing steps.

## Development status

This repository is maintained as a focused imaging and forward-modeling workflow rather than a general-purpose analysis dump. It remains useful when used with the appropriate data products and parameter conventions, and its reusable functions should remain library-first rather than being spread across ad hoc scripts.

