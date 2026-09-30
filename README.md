# Assos

Assos provides higher-level imaging workflows and catalog overlays. Its reusable Gaussian point-spread-function image model is owned by PCAT as ``pcat.image.forward_model_image``; ``assos.forward_model_image`` remains an import-compatible alias.

## Purpose

The package retains its imaging workflows and catalog-level overlays. For deterministic Gaussian-PSF scene modeling, use PCAT's image module; the Assos import path delegates to the same implementation.

## Image forward modeling

``forward_model_image`` accepts a two-dimensional source image, Gaussian PSF width in pixels, and an optional uniform background. It returns the intrinsic scene, normalized PSF kernel, and predicted detector image. It is deterministic and does not sample parameters or add Poisson noise.

## Installation

```bash
cd assos
python -m pip install -e .
export ASSOS_PATH=/path/to/assos
```

Assos depends on PCAT. For a local workspace checkout, install the PCAT source
before installing Assos in the same environment.

`ASSOS_PATH` identifies the repository root. Keep runtime inputs in `data/` and generated pipeline outputs in `visuals/`; both directories are ignored by Git.

## Minimal workflow

The runnable forward-modeling example constructs an explicitly simulated two-source scene and passes it through Assos's normalized Gaussian point-spread function convolution:

```bash
python examples/psf_forward_model.py --typefileplot png
```

![Assos simulated PSF forward model](examples/psf_forward_model.png)

The panels expose the intrinsic source scene, the normalized point-spread function kernel, and the final detector image after convolution and addition of a uniform background. The two sources, their flux rates, the 1.5-pixel point-spread width, and the background rate are explicit simulation assumptions. The figure contains no observed data.

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
- `pcat`

## Output behavior

Assos saves the intrinsic source scene, point-spread function, predicted detector image, and residual diagnostics needed to inspect the image-formation model.

