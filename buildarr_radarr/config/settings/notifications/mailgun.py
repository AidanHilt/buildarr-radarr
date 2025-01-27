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
Mailgun notification connection configuration.
"""


from __future__ import annotations

from typing import ClassVar, List, Literal

from buildarr.config import RemoteMapEntry
from buildarr.types import NonEmptyStr, Password
from pydantic import Field, NameEmail
from typing_extensions import Annotated

from .base import Notification


class MailgunNotification(Notification):
    """
    Send media update and health alert emails via the Mailgun delivery service.
    """

    type: Literal["mailgun"] = "mailgun"
    """
    Type value associated with this kind of connection.
    """

    api_key: Password
    """
    API key to use to authenticate with Mailgun.
    """

    use_eu_endpoint: bool = False
    """
    Send mail via the EU endpoint instead of the US one.
    """

    from_address: NameEmail
    """
    Email address to send the mail as.

    RFC-5322 formatted mailbox addresses are also supported,
    e.g. `Radarr <radarr@example.com>`.
    """

    sender_domain: NonEmptyStr
    """
    The domain from which the mail will be sent.
    """

    recipient_addresses: Annotated[
        List[NameEmail],
        Field(min_items=1, json_schema_extra={"uniqueItems": True}),
    ]
    """
    The recipient email addresses of the notification mail.

    At least one recipient address is required.
    """

    _implementation: ClassVar[str] = "MailGun"
    _remote_map: ClassVar[List[RemoteMapEntry]] = [
        ("api_key", "apiKey", {"is_field": True}),
        ("use_eu_endpoint", "useEuEndpoint", {"is_field": True}),
        ("from_address", "from", {"is_field": True}),
        ("sender_domain", "senderDomain", {"is_field": True}),
        ("recipient_addresses", "recipients", {"is_field": True}),
    ]
