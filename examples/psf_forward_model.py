#!/usr/bin/env python3
"""Demonstrate Assos image formation with a labeled two-source simulation."""

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("agg")

import matplotlib.pyplot as plt
import numpy as np

import assos


IMAGE_SIZE_PIXELS = 51
PSF_SIGMA_PIXELS = 1.5  # [pixel]
BACKGROUND_RATE = 5.0  # [electron s^-1 pixel^-1]


def create_simulated_scene() -> np.ndarray:
    """Return two compact Gaussian sources under explicit assumptions."""

    coordinate_pixels = np.arange(IMAGE_SIZE_PIXELS)  # [pixel]
    x_grid, y_grid = np.meshgrid(coordinate_pixels, coordinate_pixels)
    source_image = np.zeros((IMAGE_SIZE_PIXELS, IMAGE_SIZE_PIXELS))
    source_parameters = [
        (24.0, 25.0, 1000.0),
        (28.0, 25.0, 650.0),
    ]  # [pixel, pixel, electron s^-1]
    intrinsic_sigma_pixels = 0.35  # [pixel]
    for x_position, y_position, flux_rate in source_parameters:
        profile = np.exp(
            -0.5
            * (
                (x_grid - x_position) ** 2
                + (y_grid - y_position) ** 2
            )
            / intrinsic_sigma_pixels**2
        )
        source_image += flux_rate * profile / profile.sum()
    return source_image


def run_example(output_path: Path) -> dict[str, np.ndarray]:
    """Run and plot the simulated Assos image-formation pipeline."""

    source_image = create_simulated_scene()
    products = assos.forward_model_image(
        source_image,
        psf_sigma_pixels=PSF_SIGMA_PIXELS,
        background=BACKGROUND_RATE,
    )

    figure, axes = plt.subplots(
        1,
        3,
        figsize=(12.5, 4.2),
        facecolor="white",
        constrained_layout=True,
    )
    scene_slice = slice(17, 35)
    scene_extent = (16.5, 34.5, 16.5, 34.5)  # [pixel]
    kernel_half_width = products["psf_kernel"].shape[0] / 2.0  # [pixel]
    kernel_extent = (
        -kernel_half_width,
        kernel_half_width,
        -kernel_half_width,
        kernel_half_width,
    )  # [pixel]
    panels = [
        (
            products["source_image"][scene_slice, scene_slice],
            "Intrinsic two-source scene",
            r"Flux rate [electron s$^{-1}$ pixel$^{-1}$]",
            scene_extent,
            "Detector",
        ),
        (
            products["psf_kernel"],
            "Normalized Gaussian PSF",
            "Kernel weight",
            kernel_extent,
            "PSF",
        ),
        (
            products["observed_image"][scene_slice, scene_slice],
            "PSF-convolved detector image",
            r"Flux rate [electron s$^{-1}$ pixel$^{-1}$]",
            scene_extent,
            "Detector",
        ),
    ]
    for axis, (image, title, colorbar_label, extent, coordinate_name) in zip(
        axes, panels
    ):
        image_artist = axis.imshow(
            image,
            origin="lower",
            cmap="magma",
            extent=extent,
        )
        figure.colorbar(image_artist, ax=axis, label=colorbar_label)
        axis.set_xlabel(f"{coordinate_name} x pixel")
        axis.set_ylabel(f"{coordinate_name} y pixel")
        axis.set_title(title)
        axis.grid(False)
    figure.suptitle(
        "Simulated image formation with "
        rf"$\sigma_{{PSF}}={PSF_SIGMA_PIXELS:.1f}$ pixel",
        fontweight="bold",
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Writing to {output_path}...")
    figure.savefig(
        output_path,
        dpi=300 if output_path.suffix == ".png" else None,
        bbox_inches="tight",
        facecolor="white",
    )
    plt.close(figure)
    return products


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Plot Assos's simulated PSF image-formation pipeline."
    )
    parser.add_argument(
        "--typefileplot",
        choices=("png", "pdf"),
        default="png",
    )
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    output_path = Path(__file__).with_name(
        f"psf_forward_model.{arguments.typefileplot}"
    )
    run_example(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())