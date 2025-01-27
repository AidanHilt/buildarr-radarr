# Copyright (C) 2023 Callum Dickinson
#
# Buildarr is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
#
# Buildarr is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Buildarr.
# If not, see <https://www.gnu.org/licenses/>.


"""
WDTV metadata configuration.
"""


from __future__ import annotations

from typing import ClassVar, List

from buildarr.config import RemoteMapEntry

from .base import Metadata


class WdtvMetadata(Metadata):
    # Output metadata files in a format suitable for WDTV.

    movie_metadata: bool = True
    """
    Create metadata file.
    """

    movie_images: bool = True
    """
    Save movie images.
    """

    _implementation: ClassVar[str] = "WdtvMetadata"
    _remote_map: ClassVar[List[RemoteMapEntry]] = [
        ("movie_metadata", "movieMetadata", {"is_field": True}),
        ("movie_images", "movieImages", {"is_field": True}),
    ]
