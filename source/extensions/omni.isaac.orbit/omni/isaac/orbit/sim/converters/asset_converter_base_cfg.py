# Copyright [2023] Boston Dynamics AI Institute, Inc.
# Copyright (c) 2022, NVIDIA CORPORATION & AFFILIATES, ETH Zurich, and University of Toronto
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from dataclasses import MISSING

from omni.isaac.orbit.utils import configclass


@configclass
class AssetConverterBaseCfg:
    """The base configuration class for asset converters."""

    asset_path: str = MISSING
    """The absolute path to the asset file to convert into USD."""

    usd_dir: str | None = None
    """The output directory path to store the generated USD file. Defaults to :obj:`None`.

    If set to :obj:`None`, it is resolved as ``/tmp/Orbit/usd_{date}_{time}_{random}``, where
    the parameters in braces are runtime generated.
    """

    usd_file_name: str | None = None
    """The name of the generated usd file. Defaults to :obj:`None`.

    If set to :obj:`None`, it is resolved from the asset file name. The extension of the asset file
    is replaced with ``.usd``.
    """

    force_usd_conversion: bool = False
    """Force the conversion of the asset file to usd. Defaults to False.

    If True, then the USD file is always generated. It will overwrite the existing USD file if it exists.
    """

    make_instanceable: bool = True
    """Make the generated USD file instanceable. Defaults to True.

    Note:
        Instancing helps reduce the memory footprint of the asset when multiple copies of the asset are
        used in the scene. For more information, please check the USD documentation on
        `scene-graph instancing <https://openusd.org/dev/api/_usd__page__scenegraph_instancing.html>`_.
    """