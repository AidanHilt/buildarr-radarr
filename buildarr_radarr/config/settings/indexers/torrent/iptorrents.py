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
IP Torrents native API indexer configuration.
"""


from __future__ import annotations

from typing import ClassVar, List, Literal

from buildarr.config import RemoteMapEntry
from buildarr.types import RssUrl

from .base import TorrentIndexer


class IptorrentsIndexer(TorrentIndexer):
    # Monitor for releases using the IP Torrents native API.

    type: Literal["iptorrents"] = "iptorrents"
    """
    Type value associated with this kind of indexer.
    """

    feed_url: RssUrl
    """
    The full RSS feed url generated by IPTorrents, using only the categories
    you selected (HD, SD, x264, etc ...).
    """

    _implementation: ClassVar[str] = "IPTorrents"
    _remote_map: ClassVar[List[RemoteMapEntry]] = [("feed_url", "baseUrl", {"is_field": True})]
