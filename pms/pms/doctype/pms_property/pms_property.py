# Copyright (c) 2026, lloyd and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PMS_Property(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		property_address: DF.SmallText
		property_name: DF.Data
		property_owner: DF.Link
		property_type: DF.Literal["", "Apartment", "House", "Commercial"]
	# end: auto-generated types

	pass
